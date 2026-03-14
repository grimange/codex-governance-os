from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


CONTRACT_PATH = "docs/contracts/universal-template-composition-contract.md"
MATRIX_SNAPSHOT_PATH = "tools/governance/template_composition_matrix.json"
CAPABILITY_REGISTRY_PATH = "tools/governance/template_capability_registry.json"
BASE_TEMPLATE_NAME = "universal-base"

CERTIFIED_MULTI_OVERLAY_COMPOSITIONS = frozenset(
    {
        ("cli-worker", "monorepo"),
        ("cli-worker", "monorepo", "python-package"),
        ("cli-worker", "monorepo", "scheduler"),
        ("cli-worker", "node-typescript-service"),
        ("cli-worker", "php-package"),
        ("cli-worker", "python-package"),
        ("cli-worker", "python-package", "scheduler"),
        ("cli-worker", "scheduler"),
        ("django", "scheduler"),
        ("laravel", "scheduler"),
        ("django", "monorepo"),
        ("laravel", "monorepo"),
        ("monorepo", "service"),
        ("monorepo", "node-typescript-service"),
        ("monorepo", "scheduler"),
        ("python-package", "scheduler"),
    }
)

EXPLICITLY_REJECTED_COMPOSITIONS = {
    ("cli-worker", "laravel"): "missing Laravel worker composition contract",
    ("django", "laravel"): "cross-framework application collision",
}


@dataclass(frozen=True)
class CompositionValidationResult:
    supported: bool
    normalized_overlays: tuple[str, ...]
    rejection_reason: str | None
    reason_code: str
    conflict_code: str | None = None

    @property
    def composition_label(self) -> str:
        if not self.normalized_overlays:
            return "base-only"
        return " + ".join(self.normalized_overlays)


@dataclass(frozen=True)
class InventoryValidationResult:
    valid: bool
    errors: tuple[str, ...]


@dataclass(frozen=True)
class CompositionExplanation:
    requested_overlays: tuple[str, ...]
    normalized_overlays: tuple[str, ...]
    supported: bool
    decision_source: str
    rejection_reason: str | None
    closest_supported: tuple[tuple[str, ...], ...]
    reason_code: str
    conflict_code: str | None


@dataclass(frozen=True)
class ContractDocumentMatrix:
    admitted_non_composite: tuple[str, ...]
    certified_multi_overlay: tuple[tuple[str, ...], ...]
    certified_fail_closed: tuple[tuple[str, ...], ...]


@dataclass(frozen=True)
class ContractDriftReport:
    valid: bool
    errors: tuple[str, ...]


@dataclass(frozen=True)
class CompositionMatrixSnapshot:
    supported: tuple[tuple[str, ...], ...]
    explicitly_rejected: tuple[tuple[tuple[str, ...], str], ...]


@dataclass(frozen=True)
class CompositionMatrixVerificationReport:
    valid: bool
    errors: tuple[str, ...]


@dataclass(frozen=True)
class TemplateCapabilityRegistry:
    capabilities: frozenset[str]
    roles: dict[str, frozenset[str]]
    conflict_taxonomy: dict[str, str]
    explicit_boundary_codes: dict[tuple[str, ...], str]
    role_collision_codes: dict[tuple[str, str], str]
    capability_collision_codes: dict[str, str]


@dataclass(frozen=True)
class CapabilityCompositionReport:
    valid: bool
    errors: tuple[str, ...]


def _manifest_capability_values(manifest: object) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], str | None]:
    provides = getattr(manifest, "provides", None)
    requires = getattr(manifest, "requires", None)
    conflicts = getattr(manifest, "conflicts", None)
    role = getattr(manifest, "composition_role", None)
    if provides is not None and requires is not None and conflicts is not None and role is not None:
        return tuple(provides), tuple(requires), tuple(conflicts), role

    raw = getattr(manifest, "capabilities", None)
    if isinstance(raw, dict):
        provides_raw = raw.get("provides", ())
        requires_raw = raw.get("requires", ())
        conflicts_raw = raw.get("conflicts", ())
        role_raw = raw.get("composition_role")
        return tuple(provides_raw), tuple(requires_raw), tuple(conflicts_raw), role_raw
    return (), (), (), None


def normalize_overlays(overlays: Iterable[str]) -> tuple[str, ...]:
    normalized = []
    for overlay in overlays:
        if not isinstance(overlay, str) or not overlay.strip():
            raise ValueError("overlays must be non-empty strings")
        normalized.append(overlay.strip())
    return tuple(sorted(set(normalized)))


def validate_template_composition(overlays: Iterable[str]) -> CompositionValidationResult:
    normalized = normalize_overlays(overlays)
    if not normalized:
        return CompositionValidationResult(True, normalized, None, "base-only")
    if len(normalized) == 1:
        return CompositionValidationResult(True, normalized, None, "single-overlay")
    if normalized in CERTIFIED_MULTI_OVERLAY_COMPOSITIONS:
        return CompositionValidationResult(True, normalized, None, "certified-multi-overlay")
    if normalized in EXPLICITLY_REJECTED_COMPOSITIONS:
        conflict_code = _explicit_conflict_code(normalized)
        return CompositionValidationResult(
            False,
            normalized,
            EXPLICITLY_REJECTED_COMPOSITIONS[normalized],
            "explicitly-rejected",
            conflict_code,
        )
    return CompositionValidationResult(
        False,
        normalized,
        "not present in certified composition matrix",
        "unsupported",
    )


def validate_capability_composition(
    manifests: Iterable[object],
    overlays: Iterable[str],
    *,
    registry_path: str | Path | None = None,
) -> CompositionValidationResult:
    normalized = normalize_overlays(overlays)
    registry = load_template_capability_registry(registry_path)
    if not normalized:
        return CompositionValidationResult(True, normalized, None, "base-only")
    if len(normalized) == 1:
        return CompositionValidationResult(True, normalized, None, "single-overlay")
    if normalized in EXPLICITLY_REJECTED_COMPOSITIONS:
        return CompositionValidationResult(
            False,
            normalized,
            EXPLICITLY_REJECTED_COMPOSITIONS[normalized],
            "explicitly-rejected",
            registry.explicit_boundary_codes.get(normalized),
        )
    manifest_map = {
        getattr(manifest, "template_name", None): manifest
        for manifest in manifests
        if isinstance(getattr(manifest, "template_name", None), str)
    }
    base_manifest = manifest_map.get(BASE_TEMPLATE_NAME)
    if base_manifest is None:
        raise ValueError(f"missing base scaffold manifest {BASE_TEMPLATE_NAME}")

    selected = []
    for overlay in normalized:
        manifest = manifest_map.get(overlay)
        if manifest is None:
            raise ValueError(f"missing overlay manifest {overlay}")
        selected.append(manifest)

    manifests_in_scope = [base_manifest, *selected]
    aggregate_provides = {
        capability
        for manifest in manifests_in_scope
        for capability in _manifest_capability_values(manifest)[0]
    }
    selected_capability_counts: dict[str, int] = {}
    for manifest in selected:
        for capability in _manifest_capability_values(manifest)[0]:
            selected_capability_counts[capability] = selected_capability_counts.get(capability, 0) + 1

    for manifest in manifests_in_scope:
        provides, requires, conflicts, role = _manifest_capability_values(manifest)
        if role not in registry.roles:
            raise ValueError(f"{manifest.template_name} declares unknown composition role {role}")
        for field_name, values in (
            ("provides", provides),
            ("requires", requires),
            ("conflicts", conflicts),
        ):
            for capability in values:
                if capability not in registry.capabilities:
                    raise ValueError(
                        f"{manifest.template_name} declares unknown capability {capability} in {field_name}"
                    )

    for manifest in selected:
        missing = sorted(set(_manifest_capability_values(manifest)[1]) - aggregate_provides)
        if missing:
            return CompositionValidationResult(
                False,
                normalized,
                f"{manifest.template_name} is missing required capabilities: {', '.join(missing)}",
                "missing-required-capability",
            )

    duplicated_runtime_capabilities = sorted(
        capability
        for capability, count in selected_capability_counts.items()
        if count > 1 and capability in registry.capability_collision_codes
    )
    if duplicated_runtime_capabilities:
        return CompositionValidationResult(
            False,
            normalized,
            "multiple overlays claim the same governed runtime capability: "
            + ", ".join(duplicated_runtime_capabilities),
            "capability-conflict",
            _capability_conflict_code(duplicated_runtime_capabilities, registry),
        )

    for manifest in selected:
        other_capabilities = set()
        for other in manifests_in_scope:
            if other.template_name == manifest.template_name:
                continue
            other_capabilities.update(_manifest_capability_values(other)[0])
        conflicting = sorted(set(_manifest_capability_values(manifest)[2]) & other_capabilities)
        if conflicting:
            return CompositionValidationResult(
                False,
                normalized,
                f"{manifest.template_name} conflicts with capabilities: {', '.join(conflicting)}",
                "capability-conflict",
                _capability_conflict_code(conflicting, registry),
            )

    selected_names = [manifest.template_name for manifest in selected]
    selected_roles = {
        manifest.template_name: _manifest_capability_values(manifest)[3]
        for manifest in selected
    }
    for left_index, left_name in enumerate(selected_names):
        for right_name in selected_names[left_index + 1 :]:
            left_role = selected_roles[left_name]
            right_role = selected_roles[right_name]
            if right_role not in registry.roles[left_role] or left_role not in registry.roles[right_role]:
                return CompositionValidationResult(
                    False,
                    normalized,
                    f"composition roles collide: {left_role} vs {right_role}",
                    "capability-role-conflict",
                    _role_conflict_code(left_role, right_role, registry),
                )

    if normalized in CERTIFIED_MULTI_OVERLAY_COMPOSITIONS:
        return CompositionValidationResult(True, normalized, None, "certified-multi-overlay")
    return CompositionValidationResult(
        False,
        normalized,
        "not present in certified composition matrix",
        "unsupported",
    )


def _contract_document_path(contract_path: str | Path | None = None) -> Path:
    if contract_path is None:
        return Path(__file__).resolve().parents[2] / CONTRACT_PATH
    path = Path(contract_path)
    if path.is_absolute():
        return path
    return Path(__file__).resolve().parents[2] / path


def _matrix_snapshot_path(snapshot_path: str | Path | None = None) -> Path:
    if snapshot_path is None:
        return Path(__file__).resolve().parents[2] / MATRIX_SNAPSHOT_PATH
    path = Path(snapshot_path)
    if path.is_absolute():
        return path
    return Path(__file__).resolve().parents[2] / path


def _capability_registry_path(registry_path: str | Path | None = None) -> Path:
    if registry_path is None:
        return Path(__file__).resolve().parents[2] / CAPABILITY_REGISTRY_PATH
    path = Path(registry_path)
    if path.is_absolute():
        return path
    return Path(__file__).resolve().parents[2] / path


def load_template_capability_registry(
    registry_path: str | Path | None = None,
) -> TemplateCapabilityRegistry:
    payload = json.loads(_capability_registry_path(registry_path).read_text())
    capabilities_raw = payload.get("capabilities")
    roles_raw = payload.get("composition_roles")
    taxonomy_raw = payload.get("conflict_taxonomy")
    explicit_raw = payload.get("explicit_boundary_codes", {})
    role_codes_raw = payload.get("role_collision_codes", {})
    capability_codes_raw = payload.get("capability_collision_codes", {})
    if not isinstance(capabilities_raw, list):
        raise ValueError("capabilities must be a list")
    if not isinstance(roles_raw, dict):
        raise ValueError("composition_roles must be a mapping")
    if not isinstance(taxonomy_raw, dict):
        raise ValueError("conflict_taxonomy must be a mapping")
    if not isinstance(explicit_raw, dict):
        raise ValueError("explicit_boundary_codes must be a mapping")
    if not isinstance(role_codes_raw, dict):
        raise ValueError("role_collision_codes must be a mapping")
    if not isinstance(capability_codes_raw, dict):
        raise ValueError("capability_collision_codes must be a mapping")

    capabilities = frozenset(
        item for item in capabilities_raw if isinstance(item, str) and item.strip()
    )
    if len(capabilities) != len(capabilities_raw):
        raise ValueError("capabilities must contain only non-empty strings")

    roles: dict[str, frozenset[str]] = {}
    for role, raw in roles_raw.items():
        if not isinstance(role, str) or not role:
            raise ValueError("composition_roles keys must be non-empty strings")
        if not isinstance(raw, dict):
            raise ValueError(f"composition_roles.{role} must be an object")
        compatible_with = raw.get("compatible_with")
        if not isinstance(compatible_with, list):
            raise ValueError(f"composition_roles.{role}.compatible_with must be a list")
        normalized = frozenset(
            item for item in compatible_with if isinstance(item, str) and item.strip()
        )
        if len(normalized) != len(compatible_with):
            raise ValueError(
                f"composition_roles.{role}.compatible_with must contain only non-empty strings"
        )
        roles[role] = normalized
    taxonomy = {
        key: value
        for key, value in taxonomy_raw.items()
        if isinstance(key, str) and key and isinstance(value, str) and value
    }
    if len(taxonomy) != len(taxonomy_raw):
        raise ValueError("conflict_taxonomy entries must be non-empty string pairs")
    explicit_boundary_codes: dict[tuple[str, ...], str] = {}
    for key, value in explicit_raw.items():
        if not isinstance(key, str) or not key or not isinstance(value, str) or not value:
            raise ValueError("explicit_boundary_codes entries must be non-empty string pairs")
        explicit_boundary_codes[normalize_overlays(key.split("+"))] = value
    role_collision_codes: dict[tuple[str, str], str] = {}
    for key, value in role_codes_raw.items():
        if not isinstance(key, str) or not key or not isinstance(value, str) or not value:
            raise ValueError("role_collision_codes entries must be non-empty string pairs")
        pair = tuple(sorted(part.strip() for part in key.split("+")))
        if len(pair) != 2 or not all(pair):
            raise ValueError("role_collision_codes keys must be role_a+role_b")
        role_collision_codes[pair] = value
    capability_collision_codes: dict[str, str] = {}
    for key, value in capability_codes_raw.items():
        if not isinstance(key, str) or not key or not isinstance(value, str) or not value:
            raise ValueError("capability_collision_codes entries must be non-empty string pairs")
        capability_collision_codes[key] = value
    return TemplateCapabilityRegistry(
        capabilities=capabilities,
        roles=roles,
        conflict_taxonomy=taxonomy,
        explicit_boundary_codes=explicit_boundary_codes,
        role_collision_codes=role_collision_codes,
        capability_collision_codes=capability_collision_codes,
    )


def _extract_section(text: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    if not match:
        raise ValueError(f"Missing contract section: {heading}")
    return match.group("body")


def _extract_bullets(section_text: str) -> tuple[str, ...]:
    bullets = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(stripped[2:].strip())
    return tuple(bullets)


def _parse_composition_bullet(bullet: str) -> tuple[str, ...]:
    normalized = bullet.replace("`", "").strip()
    if normalized == "base-only":
        return ()
    if " + " in normalized:
        return normalize_overlays(normalized.split(" + "))
    return (normalized,)


def load_contract_document_matrix(
    contract_path: str | Path | None = None,
) -> ContractDocumentMatrix:
    text = _contract_document_path(contract_path).read_text()
    non_composite = _extract_bullets(_extract_section(text, "Admitted Non-Composite Realizations"))
    supported = _extract_bullets(_extract_section(text, "Certified Supported Multi-Overlay Matrix"))
    rejected = _extract_bullets(_extract_section(text, "Certified Fail-Closed Boundary"))
    return ContractDocumentMatrix(
        admitted_non_composite=non_composite,
        certified_multi_overlay=tuple(
            composition
            for composition in (_parse_composition_bullet(item) for item in supported)
            if composition
        ),
        certified_fail_closed=tuple(
            composition
            for composition in (_parse_composition_bullet(item) for item in rejected)
            if composition
        ),
    )


def load_composition_matrix_snapshot(
    snapshot_path: str | Path | None = None,
) -> CompositionMatrixSnapshot:
    payload = json.loads(_matrix_snapshot_path(snapshot_path).read_text())
    supported_raw = payload.get("supported", [])
    rejected_raw = payload.get("explicitly_rejected", [])
    if not isinstance(supported_raw, list):
        raise ValueError("supported must be a list")
    if not isinstance(rejected_raw, list):
        raise ValueError("explicitly_rejected must be a list")

    supported: list[tuple[str, ...]] = []
    for pair in supported_raw:
        if not isinstance(pair, list):
            raise ValueError("supported entries must be lists")
        supported.append(normalize_overlays(pair))

    explicitly_rejected: list[tuple[tuple[str, ...], str]] = []
    for entry in rejected_raw:
        if not isinstance(entry, dict):
            raise ValueError("explicitly_rejected entries must be objects")
        pair = entry.get("pair")
        reason = entry.get("reason")
        if not isinstance(pair, list):
            raise ValueError("explicitly_rejected.pair must be a list")
        if not isinstance(reason, str) or not reason:
            raise ValueError("explicitly_rejected.reason must be a non-empty string")
        explicitly_rejected.append((normalize_overlays(pair), reason))

    return CompositionMatrixSnapshot(
        supported=tuple(sorted(set(supported))),
        explicitly_rejected=tuple(sorted(set(explicitly_rejected))),
    )


def _closest_supported_compositions(normalized: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    scored = []
    requested = set(normalized)
    for candidate in sorted(CERTIFIED_MULTI_OVERLAY_COMPOSITIONS):
        overlap = len(requested & set(candidate))
        size_distance = abs(len(candidate) - len(normalized))
        scored.append((overlap, size_distance, candidate))
    scored.sort(key=lambda item: (-item[0], item[1], item[2]))
    filtered = [candidate for score, _, candidate in scored if score > 0]
    return tuple(filtered[:4])


def _explicit_conflict_code(
    normalized: tuple[str, ...],
    registry: TemplateCapabilityRegistry | None = None,
) -> str | None:
    if registry is None:
        registry = load_template_capability_registry()
    return registry.explicit_boundary_codes.get(normalized)


def _role_conflict_code(
    left_role: str,
    right_role: str,
    registry: TemplateCapabilityRegistry,
) -> str:
    return registry.role_collision_codes.get(
        tuple(sorted((left_role, right_role))),
        "entrypoint-surface-collision",
    )


def _capability_conflict_code(
    conflicting: list[str],
    registry: TemplateCapabilityRegistry,
) -> str:
    for capability in conflicting:
        code = registry.capability_collision_codes.get(capability)
        if code:
            return code
    return "runtime-ownership-collision"


def explain_template_composition(overlays: Iterable[str]) -> CompositionExplanation:
    requested = tuple(overlays)
    result = validate_template_composition(requested)
    closest_supported: tuple[tuple[str, ...], ...] = ()
    if not result.supported:
        closest_supported = _closest_supported_compositions(result.normalized_overlays)
    return CompositionExplanation(
        requested_overlays=requested,
        normalized_overlays=result.normalized_overlays,
        supported=result.supported,
        decision_source=CONTRACT_PATH,
        rejection_reason=result.rejection_reason,
        closest_supported=closest_supported,
        reason_code=result.reason_code,
        conflict_code=result.conflict_code,
    )


def doctor_command_hint(overlays: Iterable[str]) -> str:
    requested = tuple(overlays)
    if not requested:
        return "python tools/governance/template_scaffold.py doctor-composition"
    joined = " ".join(requested)
    return f"python tools/governance/template_scaffold.py doctor-composition --overlays {joined}"


def render_explanation_summary(explanation: CompositionExplanation) -> str:
    lines = [
        f"requested: {' + '.join(explanation.normalized_overlays) if explanation.normalized_overlays else 'base-only'}",
        f"supported: {'true' if explanation.supported else 'false'}",
        f"decision_source: {explanation.decision_source}",
    ]
    if explanation.conflict_code:
        lines.append(f"conflict_code: {explanation.conflict_code}")
    if explanation.rejection_reason:
        lines.append(f"reason: {explanation.rejection_reason}")
    if explanation.closest_supported:
        suggestions = ", ".join(" + ".join(item) for item in explanation.closest_supported)
        lines.append(f"closest_supported: {suggestions}")
    return "\n".join(lines)


def format_rejection_message(
    result: CompositionValidationResult,
    requested_overlays: Iterable[str] | None = None,
) -> str:
    explanation = explain_template_composition(requested_overlays or result.normalized_overlays)
    return (
        "unsupported template composition\n"
        f"requested: {result.composition_label}\n"
        f"reason: {result.reason_code}"
        f"{f' [{result.conflict_code}]' if result.conflict_code else ''}"
        f"{f' ({result.rejection_reason})' if result.rejection_reason else ''}\n"
        f"allowed: see {CONTRACT_PATH}\n"
        f"Run: {doctor_command_hint(explanation.requested_overlays or result.normalized_overlays)}"
    )


def validate_manifest_inventory(manifests: Iterable[object]) -> InventoryValidationResult:
    manifest_map = {}
    errors: list[str] = []
    try:
        capability_registry = load_template_capability_registry()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return InventoryValidationResult(False, (f"invalid capability registry: {exc}",))
    for manifest in manifests:
        name = getattr(manifest, "template_name", None)
        if not isinstance(name, str) or not name:
            errors.append("manifest inventory contains an entry without template_name")
            continue
        manifest_map[name] = manifest
        provides, requires, conflicts, role = _manifest_capability_values(manifest)
        if role not in capability_registry.roles:
            errors.append(f"{name} declares unknown composition role {role}")
        for field_name, values in (
            ("provides", provides),
            ("requires", requires),
            ("conflicts", conflicts),
        ):
            for capability in values:
                if capability not in capability_registry.capabilities:
                    errors.append(
                        f"{name} declares unknown capability {capability} in {field_name}"
                    )

    base_manifest = manifest_map.get(BASE_TEMPLATE_NAME)
    if base_manifest is None:
        errors.append(f"missing base scaffold manifest {BASE_TEMPLATE_NAME}")
        return InventoryValidationResult(False, tuple(errors))

    overlay_names = {
        name
        for name, manifest in manifest_map.items()
        if getattr(manifest, "template_type", None) == "overlay"
    }
    base_compatible = set(getattr(base_manifest, "compatible_overlays", ()))
    missing_from_base = sorted(overlay_names - base_compatible)
    if missing_from_base:
        errors.append(
            "base scaffold is missing admitted overlays: " + ", ".join(missing_from_base)
        )
    unknown_from_base = sorted(base_compatible - overlay_names)
    if unknown_from_base:
        errors.append(
            "base scaffold declares overlays without manifests: " + ", ".join(unknown_from_base)
        )

    for overlay_name in sorted(overlay_names):
        manifest = manifest_map[overlay_name]
        declared = tuple(sorted(set(getattr(manifest, "compatible_overlays", ()))))
        for other_overlay in declared:
            if other_overlay not in overlay_names:
                errors.append(
                    f"{overlay_name} declares unknown overlay compatibility with {other_overlay}"
                )
                continue
            result = validate_capability_composition(
                manifest_map.values(),
                [overlay_name, other_overlay],
            )
            if not result.supported:
                errors.append(
                    f"{overlay_name} declares unsupported composition {result.composition_label}; "
                    f"run: {doctor_command_hint(result.normalized_overlays)}"
                )

    for composition in sorted(CERTIFIED_MULTI_OVERLAY_COMPOSITIONS):
        component_manifests = [manifest_map.get(name) for name in composition]
        if any(manifest is None for manifest in component_manifests):
            errors.append(f"certified composition missing manifest: {' + '.join(composition)}")
            continue
        if len(composition) == 2:
            left, right = composition
            left_manifest = manifest_map[left]
            right_manifest = manifest_map[right]
            if right not in getattr(left_manifest, "compatible_overlays", ()):
                errors.append(f"{left} is missing certified compatibility with {right}")
            if left not in getattr(right_manifest, "compatible_overlays", ()):
                errors.append(f"{right} is missing certified compatibility with {left}")

    preservation_report = verify_capability_matrix_preservation(manifest_map.values())
    if not preservation_report.valid:
        errors.extend(preservation_report.errors)

    return InventoryValidationResult(not errors, tuple(errors))


def detect_contract_drift(
    manifests: Iterable[object],
    *,
    contract_path: str | Path | None = None,
) -> ContractDriftReport:
    errors: list[str] = []
    document = load_contract_document_matrix(contract_path)
    runtime_supported = set(CERTIFIED_MULTI_OVERLAY_COMPOSITIONS)
    document_supported = set(document.certified_multi_overlay)
    runtime_rejected = set(EXPLICITLY_REJECTED_COMPOSITIONS)
    document_rejected = set(document.certified_fail_closed)

    if "base-only" not in document.admitted_non_composite:
        errors.append("contract document is missing admitted non-composite entry base-only")
    if "a single admitted overlay applied to `universal-base`" not in document.admitted_non_composite:
        errors.append("contract document is missing admitted single-overlay realization rule")

    missing_supported = sorted(document_supported - runtime_supported)
    for composition in missing_supported:
        errors.append(
            "CONTRACT_DRIFT_DETECTED: contract documents unsupported runtime support for "
            + " + ".join(composition)
        )

    undocumented_supported = sorted(runtime_supported - document_supported)
    for composition in undocumented_supported:
        errors.append(
            "CONTRACT_DRIFT_DETECTED: runtime supports undocumented composition "
            + " + ".join(composition)
        )

    missing_rejected = sorted(document_rejected - runtime_rejected)
    for composition in missing_rejected:
        errors.append(
            "CONTRACT_DRIFT_DETECTED: contract documents rejection missing from runtime "
            + " + ".join(composition)
        )

    undocumented_rejected = sorted(runtime_rejected - document_rejected)
    for composition in undocumented_rejected:
        errors.append(
            "CONTRACT_DRIFT_DETECTED: runtime rejects undocumented composition "
            + " + ".join(composition)
        )

    manifest_validation = validate_manifest_inventory(manifests)
    if not manifest_validation.valid:
        errors.extend(
            f"CONTRACT_DRIFT_DETECTED: {message}" for message in manifest_validation.errors
        )

    return ContractDriftReport(not errors, tuple(errors))


def verify_capability_matrix_preservation(
    manifests: Iterable[object],
    *,
    registry_path: str | Path | None = None,
) -> CapabilityCompositionReport:
    manifest_list = list(manifests)
    for composition in sorted(CERTIFIED_MULTI_OVERLAY_COMPOSITIONS):
        baseline = validate_template_composition(composition)
        capability = validate_capability_composition(
            manifest_list,
            composition,
            registry_path=registry_path,
        )
        if not capability.supported or capability.reason_code != baseline.reason_code:
            return CapabilityCompositionReport(
                False,
                (
                    "capability resolution diverges from certified matrix for "
                    f"{baseline.composition_label} (baseline={baseline.reason_code}, capability={capability.reason_code})",
                ),
            )

    overlay_names = sorted(
        getattr(manifest, "template_name", "")
        for manifest in manifest_list
        if getattr(manifest, "template_type", None) == "overlay"
    )
    errors: list[str] = []
    for left_index, left in enumerate(overlay_names):
        for right in overlay_names[left_index + 1 :]:
            baseline = validate_template_composition([left, right])
            capability = validate_capability_composition(
                manifest_list,
                [left, right],
                registry_path=registry_path,
            )
            if baseline.supported != capability.supported:
                errors.append(
                    "capability resolution diverges from certified matrix for "
                    f"{baseline.composition_label} (baseline={baseline.reason_code}, capability={capability.reason_code})"
                )
                continue
            if baseline.reason_code == "explicitly-rejected":
                if capability.reason_code != baseline.reason_code:
                    errors.append(
                        "capability resolution lost explicit rejection classification for "
                        + baseline.composition_label
                    )
                if capability.rejection_reason != baseline.rejection_reason:
                    errors.append(
                        "capability resolution changed explicit rejection reason for "
                        + baseline.composition_label
                    )
            elif baseline.supported and capability.reason_code != baseline.reason_code:
                errors.append(
                    "capability resolution changed certified classification for "
                    + baseline.composition_label
                )
            elif not baseline.supported and baseline.reason_code == "unsupported":
                if capability.reason_code not in {
                    "unsupported",
                    "capability-conflict",
                    "capability-role-conflict",
                    "missing-required-capability",
                }:
                    errors.append(
                        "capability resolution returned unexpected unsupported classification for "
                        + baseline.composition_label
                    )
    return CapabilityCompositionReport(not errors, tuple(errors))


def verify_composition_matrix(
    manifests: Iterable[object],
    *,
    snapshot_path: str | Path | None = None,
    contract_path: str | Path | None = None,
) -> CompositionMatrixVerificationReport:
    errors: list[str] = []
    snapshot = load_composition_matrix_snapshot(snapshot_path)
    contract_report = detect_contract_drift(manifests, contract_path=contract_path)
    if not contract_report.valid:
        errors.extend(contract_report.errors)

    snapshot_supported = set(snapshot.supported)
    runtime_supported = set(CERTIFIED_MULTI_OVERLAY_COMPOSITIONS)
    snapshot_rejected = {pair: reason for pair, reason in snapshot.explicitly_rejected}
    runtime_rejected = dict(EXPLICITLY_REJECTED_COMPOSITIONS)

    missing_supported = sorted(snapshot_supported - runtime_supported)
    for composition in missing_supported:
        errors.append(
            "COMPOSITION_MATRIX_DRIFT: snapshot declares unsupported runtime support for "
            + " + ".join(composition)
        )

    undocumented_supported = sorted(runtime_supported - snapshot_supported)
    for composition in undocumented_supported:
        errors.append(
            "COMPOSITION_MATRIX_DRIFT: runtime supports pair missing from snapshot "
            + " + ".join(composition)
        )

    missing_rejected = sorted(set(snapshot_rejected) - set(runtime_rejected))
    for composition in missing_rejected:
        errors.append(
            "COMPOSITION_MATRIX_DRIFT: snapshot declares explicit rejection missing from runtime "
            + " + ".join(composition)
        )

    undocumented_rejected = sorted(set(runtime_rejected) - set(snapshot_rejected))
    for composition in undocumented_rejected:
        errors.append(
            "COMPOSITION_MATRIX_DRIFT: runtime explicit rejection missing from snapshot "
            + " + ".join(composition)
        )

    for composition, reason in snapshot_rejected.items():
        runtime_reason = runtime_rejected.get(composition)
        if runtime_reason is not None and runtime_reason != reason:
            errors.append(
                "COMPOSITION_MATRIX_DRIFT: rejection reason mismatch for "
                + " + ".join(composition)
                + f" (snapshot={reason!r}, runtime={runtime_reason!r})"
            )

    for composition in snapshot_supported:
        explanation = explain_template_composition(composition)
        if not explanation.supported or explanation.reason_code != "certified-multi-overlay":
            errors.append(
                "COMPOSITION_MATRIX_DRIFT: supported snapshot pair does not resolve as certified-multi-overlay "
                + " + ".join(composition)
            )
        capability = validate_capability_composition(manifests, composition)
        if not capability.supported or capability.reason_code != "certified-multi-overlay":
            errors.append(
                "COMPOSITION_MATRIX_DRIFT: supported snapshot composition is not admitted by capability resolution "
                + " + ".join(composition)
            )

    for composition, reason in snapshot_rejected.items():
        explanation = explain_template_composition(composition)
        if explanation.supported:
            errors.append(
                "COMPOSITION_MATRIX_DRIFT: explicitly rejected snapshot pair resolves as supported "
                + " + ".join(composition)
            )
            continue
        if explanation.reason_code != "explicitly-rejected":
            errors.append(
                "COMPOSITION_MATRIX_DRIFT: explicitly rejected snapshot pair lost explicit classification "
                + " + ".join(composition)
            )
        if explanation.rejection_reason != reason:
            errors.append(
                "COMPOSITION_MATRIX_DRIFT: explicitly rejected snapshot pair has mismatched reason "
                + " + ".join(composition)
                + f" (snapshot={reason!r}, runtime={explanation.rejection_reason!r})"
            )

    return CompositionMatrixVerificationReport(not errors, tuple(errors))
