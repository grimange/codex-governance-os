from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


CONTRACT_PATH = "docs/contracts/universal-template-composition-contract.md"
BASE_TEMPLATE_NAME = "universal-base"

CERTIFIED_MULTI_OVERLAY_COMPOSITIONS = frozenset(
    {
        ("cli-worker", "monorepo"),
        ("cli-worker", "node-typescript-service"),
        ("cli-worker", "php-package"),
        ("cli-worker", "python-package"),
        ("django", "monorepo"),
        ("laravel", "monorepo"),
        ("monorepo", "service"),
        ("monorepo", "node-typescript-service"),
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


@dataclass(frozen=True)
class ContractDocumentMatrix:
    admitted_non_composite: tuple[str, ...]
    certified_multi_overlay: tuple[tuple[str, ...], ...]
    certified_fail_closed: tuple[tuple[str, ...], ...]


@dataclass(frozen=True)
class ContractDriftReport:
    valid: bool
    errors: tuple[str, ...]


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
        return CompositionValidationResult(
            False,
            normalized,
            EXPLICITLY_REJECTED_COMPOSITIONS[normalized],
            "explicitly-rejected",
        )
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


def _closest_supported_compositions(normalized: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    scored = []
    requested = set(normalized)
    for candidate in sorted(CERTIFIED_MULTI_OVERLAY_COMPOSITIONS):
        overlap = len(requested & set(candidate))
        scored.append((overlap, candidate))
    scored.sort(key=lambda item: (-item[0], item[1]))
    filtered = [candidate for score, candidate in scored if score > 0]
    return tuple(filtered[:4])


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
        f"{f' ({result.rejection_reason})' if result.rejection_reason else ''}\n"
        f"allowed: see {CONTRACT_PATH}\n"
        f"Run: {doctor_command_hint(explanation.requested_overlays or result.normalized_overlays)}"
    )


def validate_manifest_inventory(manifests: Iterable[object]) -> InventoryValidationResult:
    manifest_map = {}
    errors: list[str] = []
    for manifest in manifests:
        name = getattr(manifest, "template_name", None)
        if not isinstance(name, str) or not name:
            errors.append("manifest inventory contains an entry without template_name")
            continue
        manifest_map[name] = manifest

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
            result = validate_template_composition([overlay_name, other_overlay])
            if not result.supported:
                errors.append(
                    f"{overlay_name} declares unsupported composition {result.composition_label}; "
                    f"run: {doctor_command_hint(result.normalized_overlays)}"
                )

    for composition in sorted(CERTIFIED_MULTI_OVERLAY_COMPOSITIONS):
        left, right = composition
        left_manifest = manifest_map.get(left)
        right_manifest = manifest_map.get(right)
        if left_manifest is None or right_manifest is None:
            errors.append(f"certified composition missing manifest: {' + '.join(composition)}")
            continue
        if right not in getattr(left_manifest, "compatible_overlays", ()):
            errors.append(f"{left} is missing certified compatibility with {right}")
        if left not in getattr(right_manifest, "compatible_overlays", ()):
            errors.append(f"{right} is missing certified compatibility with {left}")

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
