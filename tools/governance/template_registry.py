from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

DEFAULT_FAMILY_REGISTRY_PATH = (
    REPO_ROOT / "docs" / "governance" / "templates" / "template-registry.yaml"
)
DEFAULT_ADMISSION_ROOT = (
    REPO_ROOT / "docs" / "governance" / "registries" / "templates"
)
DEFAULT_ENTRY_DIRECTORY = DEFAULT_ADMISSION_ROOT / "entries"
DEFAULT_COMPILED_INDEX_PATH = DEFAULT_ADMISSION_ROOT / "index.yaml"

ALLOWED_TEMPLATE_FAMILIES = frozenset(
    {
        "pipeline",
        "verification",
        "rule",
        "skill",
        "sub_agent",
        "instruction",
        "report",
        "policy",
        "artifact",
        "evidence-pack",
        "decision",
        "remediation",
    }
)
ALLOWED_TEMPLATE_KINDS = frozenset(
    {
        "base",
        "verification",
        "safety",
        "discovery",
        "architecture-specialist",
        "governance-summary",
        "instruction",
        "policy",
        "artifact",
        "decision",
        "remediation",
    }
)
ALLOWED_STATUSES = frozenset({"draft", "active", "deprecated", "restricted", "archived"})
ALLOWED_AUTHORITY_LEVELS = frozenset({"canonical", "advisory", "experimental", "local"})
ALLOWED_STACKS = frozenset(
    {
        "agnostic",
        "laravel",
        "django",
        "php",
        "python",
        "node",
        "docs-only",
        "mcp-tools",
        "infrastructure",
    }
)
ALLOWED_MODES = frozenset(
    {"analysis", "implementation", "verification", "reporting", "design"}
)


class RegistryError(ValueError):
    """Raised when a registry surface is malformed or policy-blocked."""


@dataclass(frozen=True)
class OverlayDefinition:
    name: str
    layer: str
    compatible_families: tuple[str, ...]
    additional_sections: tuple[str, ...]
    weakens_core: bool


@dataclass(frozen=True)
class TemplateFamily:
    family: str
    version: str
    required_sections: tuple[str, ...]
    optional_sections: tuple[str, ...]
    required_frontmatter: tuple[str, ...]
    normalization_aliases: dict[str, tuple[str, ...]]
    output_path_pattern: str
    validator: str
    scaffold: str
    compatible_overlays: tuple[str, ...]


@dataclass(frozen=True)
class TemplateFamilyRegistry:
    schema_version: str
    governance_mode: str
    execution_mode: str
    universal_core: dict[str, Any]
    templates: dict[str, TemplateFamily]
    overlays: dict[str, OverlayDefinition]

    def get_family(self, family: str) -> TemplateFamily:
        try:
            return self.templates[family]
        except KeyError as exc:
            raise RegistryError(f"Unknown template family: {family}") from exc

    def get_overlay(self, overlay_name: str) -> OverlayDefinition:
        try:
            return self.overlays[overlay_name]
        except KeyError as exc:
            raise RegistryError(f"Unknown overlay: {overlay_name}") from exc


TemplateRegistry = TemplateFamilyRegistry


@dataclass(frozen=True)
class TemplateEntry:
    template_id: str
    template_name: str
    template_family: str
    template_kind: str
    version: str
    status: str
    authority_level: str
    description: str
    inputs_contract: dict[str, Any]
    outputs_contract: dict[str, Any]
    compatible_stacks: tuple[str, ...]
    compatible_modes: tuple[str, ...]
    constraints: tuple[str, ...]
    resolution_tags: tuple[str, ...]
    file_path: str
    checksum_sha256: str
    admitted_at: str
    admitted_by: str
    supersedes: tuple[str, ...]

    @property
    def absolute_file_path(self) -> Path:
        return REPO_ROOT / self.file_path

    @property
    def resolution_key_parts(self) -> list[tuple[str, str, str, str]]:
        return [
            (self.template_family, self.template_kind, stack, mode)
            for stack in self.compatible_stacks
            for mode in self.compatible_modes
        ]


@dataclass(frozen=True)
class ResolutionOutcome:
    status: str
    reason: str
    selected_template_id: str | None
    selected_file_path: str | None
    trace: tuple[dict[str, Any], ...]
    warnings: tuple[str, ...] = ()


def _read_json_compatible_yaml(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise RegistryError(
            f"Registry at {path} is not valid JSON-compatible YAML: {exc}"
        ) from exc


def _tupled_strings(values: list[str], field_name: str) -> tuple[str, ...]:
    if not isinstance(values, list) or not all(isinstance(item, str) for item in values):
        raise RegistryError(f"{field_name} must be a list of strings")
    return tuple(values)


def _ensure_mapping(value: Any, field_name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise RegistryError(f"{field_name} must be a mapping")
    return value


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _validate_overlay_definitions(raw_overlays: list[dict[str, Any]]) -> dict[str, OverlayDefinition]:
    overlays: dict[str, OverlayDefinition] = {}
    for raw in raw_overlays:
        name = raw.get("name")
        if not isinstance(name, str) or not name:
            raise RegistryError("Overlay definitions require a non-empty name")
        if name in overlays:
            raise RegistryError(f"Duplicate overlay name: {name}")
        overlay = OverlayDefinition(
            name=name,
            layer=raw.get("layer", ""),
            compatible_families=_tupled_strings(
                raw.get("compatible_families", []), f"{name}.compatible_families"
            ),
            additional_sections=_tupled_strings(
                raw.get("additional_sections", []), f"{name}.additional_sections"
            ),
            weakens_core=bool(raw.get("weakens_core", False)),
        )
        if overlay.weakens_core:
            raise RegistryError(f"Overlay {name} weakens the universal core")
        overlays[name] = overlay
    return overlays


def _validate_template_definitions(
    raw_templates: list[dict[str, Any]], overlays: dict[str, OverlayDefinition]
) -> dict[str, TemplateFamily]:
    templates: dict[str, TemplateFamily] = {}
    alias_targets: dict[str, str] = {}
    for raw in raw_templates:
        family_name = raw.get("family")
        if not isinstance(family_name, str) or not family_name:
            raise RegistryError("Template definitions require a non-empty family")
        if family_name in templates:
            raise RegistryError(f"Duplicate template family: {family_name}")
        aliases: dict[str, tuple[str, ...]] = {}
        raw_aliases = raw.get("normalization_aliases", {})
        if not isinstance(raw_aliases, dict):
            raise RegistryError(f"{family_name}.normalization_aliases must be a mapping")
        for canonical, values in raw_aliases.items():
            aliases[canonical] = _tupled_strings(values, f"{family_name}.{canonical}")
            for alias in aliases[canonical]:
                if alias in alias_targets:
                    raise RegistryError(
                        f"Alias collision: {alias} already used by {alias_targets[alias]}"
                    )
                alias_targets[alias] = family_name
        compatible_overlays = _tupled_strings(
            raw.get("compatible_overlays", []), f"{family_name}.compatible_overlays"
        )
        for overlay_name in compatible_overlays:
            if overlay_name not in overlays:
                raise RegistryError(
                    f"{family_name} references unknown overlay {overlay_name}"
                )
        templates[family_name] = TemplateFamily(
            family=family_name,
            version=str(raw.get("version", "")),
            required_sections=_tupled_strings(
                raw.get("required_sections", []), f"{family_name}.required_sections"
            ),
            optional_sections=_tupled_strings(
                raw.get("optional_sections", []), f"{family_name}.optional_sections"
            ),
            required_frontmatter=_tupled_strings(
                raw.get("required_frontmatter", []), f"{family_name}.required_frontmatter"
            ),
            normalization_aliases=aliases,
            output_path_pattern=str(raw.get("output_path_pattern", "")),
            validator=str(raw.get("validator", "")),
            scaffold=str(raw.get("scaffold", "")),
            compatible_overlays=compatible_overlays,
        )
    return templates


def load_registry(path: Path | None = None) -> TemplateFamilyRegistry:
    registry_path = path or DEFAULT_FAMILY_REGISTRY_PATH
    raw = _read_json_compatible_yaml(registry_path)
    overlays = _validate_overlay_definitions(raw.get("overlays", []))
    templates = _validate_template_definitions(raw.get("templates", []), overlays)
    return TemplateFamilyRegistry(
        schema_version=str(raw.get("schema_version", "")),
        governance_mode=str(raw.get("governance_mode", "")),
        execution_mode=str(raw.get("execution_mode", "")),
        universal_core=_ensure_mapping(raw.get("universal_core", {}), "universal_core"),
        templates=templates,
        overlays=overlays,
    )


def _validate_stack_list(values: tuple[str, ...], field_name: str) -> None:
    unknown = sorted(set(values) - ALLOWED_STACKS)
    if unknown:
        raise RegistryError(f"{field_name} contains unknown stacks: {', '.join(unknown)}")


def _validate_mode_list(values: tuple[str, ...], field_name: str) -> None:
    unknown = sorted(set(values) - ALLOWED_MODES)
    if unknown:
        raise RegistryError(f"{field_name} contains unknown modes: {', '.join(unknown)}")


def _validate_family_and_kind(family: str, kind: str, family_registry: TemplateFamilyRegistry) -> None:
    if family not in ALLOWED_TEMPLATE_FAMILIES:
        raise RegistryError(f"Unknown template family enumeration: {family}")
    if family not in family_registry.templates:
        raise RegistryError(f"Family {family} is not defined in the canonical family registry")
    if kind not in ALLOWED_TEMPLATE_KINDS:
        raise RegistryError(f"Unknown template kind enumeration: {kind}")


def _lint_entry_body(entry: TemplateEntry, family_registry: TemplateFamilyRegistry) -> None:
    from tools.governance.template_lint import lint_template

    result = lint_template(
        entry.absolute_file_path, family=entry.template_family, registry=family_registry
    )
    if result.decision == "BLOCKED":
        raise RegistryError(
            "Template body "
            f"{entry.file_path} failed lint: "
            + "; ".join(issue.message for issue in result.issues if issue.severity == "error")
        )


def _load_entry(path: Path, family_registry: TemplateFamilyRegistry) -> TemplateEntry:
    raw = _read_json_compatible_yaml(path)
    required_fields = [
        "template_id",
        "template_name",
        "template_family",
        "template_kind",
        "version",
        "status",
        "authority_level",
        "description",
        "inputs_contract",
        "outputs_contract",
        "compatible_stacks",
        "compatible_modes",
        "constraints",
        "resolution_tags",
        "file_path",
        "checksum_sha256",
        "admitted_at",
        "admitted_by",
        "supersedes",
    ]
    missing = [field for field in required_fields if field not in raw]
    if missing:
        raise RegistryError(f"{path.name} missing required fields: {', '.join(missing)}")
    template_family = str(raw["template_family"])
    template_kind = str(raw["template_kind"])
    _validate_family_and_kind(template_family, template_kind, family_registry)
    status = str(raw["status"])
    if status not in ALLOWED_STATUSES:
        raise RegistryError(f"{path.name} has invalid lifecycle status {status}")
    authority_level = str(raw["authority_level"])
    if authority_level not in ALLOWED_AUTHORITY_LEVELS:
        raise RegistryError(f"{path.name} has invalid authority level {authority_level}")
    entry = TemplateEntry(
        template_id=str(raw["template_id"]),
        template_name=str(raw["template_name"]),
        template_family=template_family,
        template_kind=template_kind,
        version=str(raw["version"]),
        status=status,
        authority_level=authority_level,
        description=str(raw["description"]),
        inputs_contract=_ensure_mapping(raw["inputs_contract"], f"{path.name}.inputs_contract"),
        outputs_contract=_ensure_mapping(raw["outputs_contract"], f"{path.name}.outputs_contract"),
        compatible_stacks=_tupled_strings(
            raw["compatible_stacks"], f"{path.name}.compatible_stacks"
        ),
        compatible_modes=_tupled_strings(
            raw["compatible_modes"], f"{path.name}.compatible_modes"
        ),
        constraints=_tupled_strings(raw["constraints"], f"{path.name}.constraints"),
        resolution_tags=_tupled_strings(
            raw["resolution_tags"], f"{path.name}.resolution_tags"
        ),
        file_path=str(raw["file_path"]),
        checksum_sha256=str(raw["checksum_sha256"]),
        admitted_at=str(raw["admitted_at"]),
        admitted_by=str(raw["admitted_by"]),
        supersedes=_tupled_strings(raw["supersedes"], f"{path.name}.supersedes"),
    )
    _validate_stack_list(entry.compatible_stacks, f"{path.name}.compatible_stacks")
    _validate_mode_list(entry.compatible_modes, f"{path.name}.compatible_modes")
    if not entry.absolute_file_path.exists():
        raise RegistryError(f"{path.name} references missing template body {entry.file_path}")
    actual_checksum = _sha256(entry.absolute_file_path)
    if entry.checksum_sha256 != actual_checksum:
        raise RegistryError(
            f"{path.name} checksum mismatch for {entry.file_path}: expected {entry.checksum_sha256}, got {actual_checksum}"
        )
    _lint_entry_body(entry, family_registry)
    return entry


def load_template_entries(
    entry_directory: Path | None = None,
    family_registry: TemplateFamilyRegistry | None = None,
) -> dict[str, TemplateEntry]:
    family_registry = family_registry or load_registry()
    directory = entry_directory or DEFAULT_ENTRY_DIRECTORY
    if not directory.exists():
        raise RegistryError(f"Template entry directory does not exist: {directory}")
    entries: dict[str, TemplateEntry] = {}
    for path in sorted(directory.glob("*.yaml")):
        entry = _load_entry(path, family_registry)
        if entry.template_id in entries:
            raise RegistryError(f"Duplicate template_id: {entry.template_id}")
        entries[entry.template_id] = entry
    _validate_unique_resolution_keys(entries.values())
    _validate_supersession(entries)
    return entries


def _validate_unique_resolution_keys(entries: Any) -> None:
    keys: dict[tuple[str, str, str, str], str] = {}
    for entry in entries:
        if entry.status != "active":
            continue
        for key in entry.resolution_key_parts:
            if key in keys:
                raise RegistryError(
                    "Duplicate active resolution key "
                    f"{key} for {entry.template_id} and {keys[key]}"
                )
            keys[key] = entry.template_id


def _validate_supersession(entries: dict[str, TemplateEntry]) -> None:
    for entry in entries.values():
        if entry.template_id in entry.supersedes:
            raise RegistryError(f"{entry.template_id} may not supersede itself")
        for superseded in entry.supersedes:
            if superseded not in entries:
                raise RegistryError(
                    f"{entry.template_id} supersedes unknown template_id {superseded}"
                )


def build_compiled_index(
    entry_directory: Path | None = None,
    output_path: Path | None = None,
    family_registry_path: Path | None = None,
) -> dict[str, Any]:
    family_registry = load_registry(family_registry_path)
    entries = load_template_entries(entry_directory, family_registry)
    compiled = {
        "schema_version": "1.0.0",
        "registry_version": "1.0.0",
        "entries": [asdict(entries[key]) for key in sorted(entries)],
    }
    compiled_path = output_path or DEFAULT_COMPILED_INDEX_PATH
    compiled_path.parent.mkdir(parents=True, exist_ok=True)
    compiled_path.write_text(json.dumps(compiled, indent=2, sort_keys=True) + "\n")
    return compiled


def _load_compiled_or_build(entry_directory: Path | None = None) -> dict[str, Any]:
    if DEFAULT_COMPILED_INDEX_PATH.exists():
        compiled = _read_json_compatible_yaml(DEFAULT_COMPILED_INDEX_PATH)
        if compiled.get("entries"):
            return compiled
    return build_compiled_index(entry_directory)


def _filter_entries_for_resolution(
    entries: list[TemplateEntry],
    *,
    family: str | None,
    kind: str | None,
    stack: str | None,
    mode: str | None,
    tags: tuple[str, ...],
) -> list[TemplateEntry]:
    filtered = []
    for entry in entries:
        if family and entry.template_family != family:
            continue
        if kind and entry.template_kind != kind:
            continue
        if stack and stack not in entry.compatible_stacks:
            continue
        if mode and mode not in entry.compatible_modes:
            continue
        if tags and not set(tags).issubset(set(entry.resolution_tags)):
            continue
        filtered.append(entry)
    return filtered


def _gate_status(
    entry: TemplateEntry,
    *,
    allow_restricted: bool,
    allow_deprecated: bool,
) -> tuple[bool, str | None]:
    if entry.status == "archived":
        return False, "archived templates are evidence-only"
    if entry.status == "draft":
        return False, "draft templates are not eligible for governed execution"
    if entry.status == "restricted" and not allow_restricted:
        return False, "restricted template requires explicit policy authorization"
    if entry.status == "deprecated" and not allow_deprecated:
        return False, "deprecated template requires explicit legacy allowance"
    return True, None


def resolve_template(
    *,
    template_id: str | None = None,
    family: str | None = None,
    kind: str | None = None,
    stack: str | None = None,
    mode: str | None = None,
    tags: tuple[str, ...] = (),
    strict_stack_match: bool = False,
    allow_agnostic_fallback: bool = False,
    allow_restricted: bool = False,
    allow_deprecated: bool = False,
    entry_directory: Path | None = None,
) -> ResolutionOutcome:
    entries = list(load_template_entries(entry_directory).values())
    trace: list[dict[str, Any]] = []

    if template_id:
        matches = [entry for entry in entries if entry.template_id == template_id]
        trace.append({"step": "template_id", "matches": [entry.template_id for entry in matches]})
        if not matches:
            return ResolutionOutcome("blocked", "missing template_id", None, None, tuple(trace))
        entry = matches[0]
        allowed, blocked_reason = _gate_status(
            entry,
            allow_restricted=allow_restricted,
            allow_deprecated=allow_deprecated,
        )
        if not allowed:
            return ResolutionOutcome(
                "blocked",
                blocked_reason or "policy conflict",
                None,
                None,
                tuple(trace),
            )
        warnings = ("deprecated template allowed",) if entry.status == "deprecated" else ()
        return ResolutionOutcome(
            "resolved",
            "exact template_id match",
            entry.template_id,
            entry.file_path,
            tuple(trace),
            warnings=warnings,
        )

    if not family or not kind:
        return ResolutionOutcome(
            "blocked",
            "family and kind are required when template_id is not provided",
            None,
            None,
            tuple(trace),
        )

    exact_matches = _filter_entries_for_resolution(
        entries, family=family, kind=kind, stack=stack, mode=mode, tags=()
    )
    trace.append({"step": "family-kind-stack-mode", "matches": [entry.template_id for entry in exact_matches]})
    allowed_exact = []
    for entry in exact_matches:
        allowed, _ = _gate_status(
            entry,
            allow_restricted=allow_restricted,
            allow_deprecated=allow_deprecated,
        )
        if allowed and (stack is None or stack in entry.compatible_stacks) and stack != "agnostic":
            if stack is None or stack in entry.compatible_stacks and "agnostic" not in entry.compatible_stacks:
                allowed_exact.append(entry)
    if len(allowed_exact) == 1:
        entry = allowed_exact[0]
        warnings = ("deprecated template allowed",) if entry.status == "deprecated" else ()
        return ResolutionOutcome(
            "resolved",
            "exact family-kind-stack-mode match",
            entry.template_id,
            entry.file_path,
            tuple(trace),
            warnings=warnings,
        )
    if len(allowed_exact) > 1:
        return ResolutionOutcome("blocked", "ambiguous exact resolution", None, None, tuple(trace))

    if allow_agnostic_fallback and not strict_stack_match:
        agnostic_matches = _filter_entries_for_resolution(
            entries, family=family, kind=kind, stack="agnostic", mode=mode, tags=()
        )
        trace.append({"step": "agnostic-fallback", "matches": [entry.template_id for entry in agnostic_matches]})
        allowed_agnostic = []
        for entry in agnostic_matches:
            allowed, _ = _gate_status(
                entry,
                allow_restricted=allow_restricted,
                allow_deprecated=allow_deprecated,
            )
            if allowed:
                allowed_agnostic.append(entry)
        if len(allowed_agnostic) == 1:
            entry = allowed_agnostic[0]
            warnings = ("deprecated template allowed",) if entry.status == "deprecated" else ()
            return ResolutionOutcome(
                "resolved",
                "agnostic fallback match",
                entry.template_id,
                entry.file_path,
                tuple(trace),
                warnings=warnings,
            )
        if len(allowed_agnostic) > 1:
            return ResolutionOutcome("blocked", "ambiguous agnostic fallback", None, None, tuple(trace))

    if tags:
        tag_matches = _filter_entries_for_resolution(
            entries, family=family, kind=None, stack=stack, mode=mode, tags=tags
        )
        trace.append({"step": "family-tags-stack", "matches": [entry.template_id for entry in tag_matches]})
        allowed_tags = []
        for entry in tag_matches:
            allowed, _ = _gate_status(
                entry,
                allow_restricted=allow_restricted,
                allow_deprecated=allow_deprecated,
            )
            if allowed:
                allowed_tags.append(entry)
        if len(allowed_tags) == 1:
            entry = allowed_tags[0]
            warnings = ("deprecated template allowed",) if entry.status == "deprecated" else ()
            return ResolutionOutcome(
                "resolved",
                "tag-based stack match",
                entry.template_id,
                entry.file_path,
                tuple(trace),
                warnings=warnings,
            )
        if len(allowed_tags) > 1:
            return ResolutionOutcome("blocked", "ambiguous tag-based resolution", None, None, tuple(trace))

    return ResolutionOutcome("blocked", "no admissible template match", None, None, tuple(trace))


def list_templates(
    *,
    status: str | None = None,
    family: str | None = None,
    entry_directory: Path | None = None,
) -> list[dict[str, Any]]:
    entries = load_template_entries(entry_directory)
    result = []
    for template_id in sorted(entries):
        entry = entries[template_id]
        if status and entry.status != status:
            continue
        if family and entry.template_family != family:
            continue
        result.append(asdict(entry))
    return result


def _command_validate(args: argparse.Namespace) -> int:
    try:
        entries = load_template_entries(args.entry_directory)
        output = {
            "valid": True,
            "entry_count": len(entries),
            "errors": [],
        }
        print(json.dumps(output, indent=2, sort_keys=True))
        return 0
    except RegistryError as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, indent=2, sort_keys=True))
        return 1


def _command_build_index(args: argparse.Namespace) -> int:
    compiled = build_compiled_index(args.entry_directory, args.output)
    print(json.dumps(compiled, indent=2, sort_keys=True))
    return 0


def _command_resolve(args: argparse.Namespace) -> int:
    outcome = resolve_template(
        template_id=args.template_id,
        family=args.family,
        kind=args.kind,
        stack=args.stack,
        mode=args.mode,
        tags=tuple(args.tag or []),
        strict_stack_match=args.strict_stack_match,
        allow_agnostic_fallback=args.allow_agnostic_fallback,
        allow_restricted=args.allow_restricted,
        allow_deprecated=args.allow_deprecated,
        entry_directory=args.entry_directory,
    )
    print(json.dumps(asdict(outcome), indent=2, sort_keys=True))
    return 0 if outcome.status == "resolved" else 1


def _command_list(args: argparse.Namespace) -> int:
    print(json.dumps(list_templates(status=args.status, family=args.family), indent=2, sort_keys=True))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Governed universal template registry commands.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--entry-directory", type=Path, default=None)
    validate_parser.set_defaults(func=_command_validate)

    build_parser = subparsers.add_parser("build-index")
    build_parser.add_argument("--entry-directory", type=Path, default=None)
    build_parser.add_argument("--output", type=Path, default=None)
    build_parser.set_defaults(func=_command_build_index)

    resolve_parser = subparsers.add_parser("resolve")
    resolve_parser.add_argument("--template-id", default=None)
    resolve_parser.add_argument("--family", default=None)
    resolve_parser.add_argument("--kind", default=None)
    resolve_parser.add_argument("--stack", default=None)
    resolve_parser.add_argument("--mode", default=None)
    resolve_parser.add_argument("--tag", action="append", default=[])
    resolve_parser.add_argument("--strict-stack-match", action="store_true")
    resolve_parser.add_argument("--allow-agnostic-fallback", action="store_true")
    resolve_parser.add_argument("--allow-restricted", action="store_true")
    resolve_parser.add_argument("--allow-deprecated", action="store_true")
    resolve_parser.add_argument("--entry-directory", type=Path, default=None)
    resolve_parser.set_defaults(func=_command_resolve)

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--status", default=None)
    list_parser.add_argument("--family", default=None)
    list_parser.add_argument("--entry-directory", type=Path, default=None)
    list_parser.set_defaults(func=_command_list)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
