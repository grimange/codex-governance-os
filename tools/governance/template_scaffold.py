from __future__ import annotations

import argparse
import dataclasses
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.governance.template_lint import validate_document
from tools.governance.template_registry import RegistryError, load_registry
from tools.templates.composition_contract import (
    explain_template_composition,
    format_rejection_message,
    render_explanation_summary,
    validate_manifest_inventory,
    validate_template_composition,
)

DEFAULT_SCAFFOLD_MANIFEST_DIRECTORY = REPO_ROOT / "docs" / "codex" / "templates" / "manifests"
DEFAULT_SCAFFOLD_SELECTION_PATH = Path("docs/governance/scaffold-selection.json")
REQUIRED_MANIFEST_KEYS = (
    "template_name",
    "template_type",
    "base_template",
    "compatible_overlays",
    "required_surfaces",
    "optional_surfaces",
    "governance_compatibility",
    "maturity",
    "supported_runtime_shapes",
)


DEFAULT_VALUES = {
    "status": "proposed",
    "category": "governance",
    "stage": "design",
    "objective": "REQUIRED: project-defined objective",
    "depends_on": [],
    "outputs": [],
    "success_criteria": [],
    "governance_mode": "fail-closed",
    "execution_mode": "advisory-then-enforcing",
    "restrictions": [],
    "non_claims": [],
}


@dataclasses.dataclass(frozen=True)
class ScaffoldManifest:
    template_name: str
    template_type: str
    base_template: str | None
    compatible_overlays: tuple[str, ...]
    required_surfaces: tuple[str, ...]
    optional_surfaces: tuple[str, ...]
    governance_compatibility: str
    maturity: str
    supported_runtime_shapes: tuple[str, ...]
    template_root: str
    description: str = ""
    composition_overrides: dict[str, dict[str, object]] = dataclasses.field(default_factory=dict)


def _load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise RegistryError(f"Invalid scaffold manifest at {path}: {exc}") from exc


def _tuple_of_strings(value: object, field_name: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        raise RegistryError(f"{field_name} must be a non-empty list of strings")
    return tuple(value)


def _mapping_of_overrides(value: object, field_name: str) -> dict[str, dict[str, object]]:
    if value in (None, {}):
        return {}
    if not isinstance(value, dict):
        raise RegistryError(f"{field_name} must be a mapping")
    normalized: dict[str, dict[str, object]] = {}
    for key, raw in value.items():
        if not isinstance(key, str) or not key:
            raise RegistryError(f"{field_name} contains invalid override key")
        if not isinstance(raw, dict):
            raise RegistryError(f"{field_name}.{key} must be a mapping")
        normalized[key] = raw
    return normalized


def load_scaffold_manifest(
    template_name: str,
    manifest_dir: Path | None = None,
) -> ScaffoldManifest:
    manifest_dir = manifest_dir or DEFAULT_SCAFFOLD_MANIFEST_DIRECTORY
    path = manifest_dir / f"{template_name}.json"
    if not path.exists():
        raise RegistryError(f"Unknown scaffold manifest: {template_name}")
    raw = _load_json(path)
    for key in REQUIRED_MANIFEST_KEYS:
        if key not in raw:
            raise RegistryError(f"Scaffold manifest {template_name} missing key `{key}`")
    template_type = raw["template_type"]
    if template_type not in {"base", "overlay"}:
        raise RegistryError(f"Unsupported scaffold template_type `{template_type}`")
    base_template = raw["base_template"]
    if base_template is not None and not isinstance(base_template, str):
        raise RegistryError("base_template must be a string or null")
    governance_compatibility = raw["governance_compatibility"]
    maturity = raw["maturity"]
    template_root = raw.get("template_root")
    if not isinstance(template_root, str) or not template_root:
        raise RegistryError("template_root must be a non-empty string")
    return ScaffoldManifest(
        template_name=raw["template_name"],
        template_type=template_type,
        base_template=base_template,
        compatible_overlays=_tuple_of_strings(raw["compatible_overlays"], "compatible_overlays"),
        required_surfaces=_tuple_of_strings(raw["required_surfaces"], "required_surfaces"),
        optional_surfaces=_tuple_of_strings(raw["optional_surfaces"], "optional_surfaces"),
        governance_compatibility=str(governance_compatibility),
        maturity=str(maturity),
        supported_runtime_shapes=_tuple_of_strings(
            raw["supported_runtime_shapes"], "supported_runtime_shapes"
        ),
        template_root=template_root,
        description=str(raw.get("description", "")),
        composition_overrides=_mapping_of_overrides(
            raw.get("composition_overrides", {}),
            f"{template_name}.composition_overrides",
        ),
    )


def _resolve_overlay_surfaces(
    overlay_manifest: ScaffoldManifest,
    selected_overlays: list[str],
    *,
    include_optional: bool,
) -> tuple[list[str], dict[str, object] | None]:
    for other_overlay in selected_overlays:
        if other_overlay == overlay_manifest.template_name:
            continue
        override = overlay_manifest.composition_overrides.get(other_overlay)
        if override:
            required = list(_tuple_of_strings(override.get("required_surfaces", []), "required_surfaces"))
            optional = list(_tuple_of_strings(override.get("optional_surfaces", []), "optional_surfaces"))
            surfaces = required + (optional if include_optional else [])
            return surfaces, override
    surfaces = list(overlay_manifest.required_surfaces)
    if include_optional:
        surfaces.extend(overlay_manifest.optional_surfaces)
    return surfaces, None


def list_scaffold_manifests(
    manifest_dir: Path | None = None,
) -> list[ScaffoldManifest]:
    manifest_dir = manifest_dir or DEFAULT_SCAFFOLD_MANIFEST_DIRECTORY
    if not manifest_dir.exists():
        return []
    manifests: list[ScaffoldManifest] = []
    for path in sorted(manifest_dir.glob("*.json")):
        manifests.append(load_scaffold_manifest(path.stem, manifest_dir=manifest_dir))
    validation = validate_manifest_inventory(manifests)
    if not validation.valid:
        raise RegistryError("; ".join(validation.errors))
    return manifests


def realize_repository_scaffold(
    template_name: str,
    output_root: Path,
    *,
    overlays: list[str] | None = None,
    include_optional: bool = False,
    manifest_dir: Path | None = None,
) -> Path:
    manifest_dir = manifest_dir or DEFAULT_SCAFFOLD_MANIFEST_DIRECTORY
    composition = validate_template_composition(overlays or [])
    if not composition.supported:
        raise RegistryError(format_rejection_message(composition, overlays or []))
    base_manifest = load_scaffold_manifest(template_name, manifest_dir=manifest_dir)
    if base_manifest.template_type != "base":
        raise RegistryError(f"{template_name} is not a base scaffold manifest")

    selected_overlays = sorted(overlays or [])
    overlay_manifests: list[ScaffoldManifest] = []
    for overlay_name in selected_overlays:
        if overlay_name not in base_manifest.compatible_overlays:
            raise RegistryError(f"Overlay {overlay_name} is not compatible with base template {template_name}")
        overlay_manifest = load_scaffold_manifest(overlay_name, manifest_dir=manifest_dir)
        if overlay_manifest.template_type != "overlay":
            raise RegistryError(f"{overlay_name} is not an overlay manifest")
        if overlay_manifest.base_template != template_name:
            raise RegistryError(
                f"Overlay {overlay_name} expects base template {overlay_manifest.base_template}, not {template_name}"
            )
        overlay_manifests.append(overlay_manifest)

    for overlay_manifest in overlay_manifests:
        for other_overlay in selected_overlays:
            if other_overlay == overlay_manifest.template_name:
                continue
            if other_overlay not in overlay_manifest.compatible_overlays:
                raise RegistryError(
                    f"Overlay {overlay_manifest.template_name} is not compatible with overlay {other_overlay}"
                )

    surfaces = list(base_manifest.required_surfaces)
    composition_metadata: dict[str, dict[str, object]] = {}
    if include_optional:
        surfaces.extend(base_manifest.optional_surfaces)
    for overlay_manifest in overlay_manifests:
        overlay_surfaces, override = _resolve_overlay_surfaces(
            overlay_manifest,
            selected_overlays,
            include_optional=include_optional,
        )
        surfaces.extend(overlay_surfaces)
        if override:
            composition_metadata[overlay_manifest.template_name] = {
                key: value
                for key, value in override.items()
                if key not in {"required_surfaces", "optional_surfaces"}
            }

    created_paths: list[str] = []
    for surface in sorted(set(surfaces)):
        target = output_root / surface
        if target.suffix:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(f"// scaffold placeholder for {surface}\n")
        else:
            target.mkdir(parents=True, exist_ok=True)
        created_paths.append(surface)

    selection_path = output_root / DEFAULT_SCAFFOLD_SELECTION_PATH
    selection_path.parent.mkdir(parents=True, exist_ok=True)
    selection = {
        "base_template": base_manifest.template_name,
        "overlays": selected_overlays,
        "include_optional": include_optional,
        "required_surfaces": list(base_manifest.required_surfaces),
        "created_surfaces": created_paths,
    }
    if composition_metadata:
        selection["composition_metadata"] = composition_metadata
    selection_path.write_text(json.dumps(selection, indent=2, sort_keys=True) + "\n")
    return selection_path


def _slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _serialize_frontmatter_value(value) -> str:
    if isinstance(value, (list, dict)):
        return json.dumps(value)
    return json.dumps(value) if " " in str(value) or ":" in str(value) else str(value)


def scaffold_document(
    family: str,
    artifact_id: str,
    title: str,
    output_path: Path | None = None,
    overlays: list[str] | None = None,
    registry_path: Path | None = None,
) -> Path:
    registry = load_registry(registry_path)
    template_family = registry.get_family(family)
    overlays = sorted(overlays or [])
    stack_layers = []
    for overlay_name in overlays:
        overlay = registry.get_overlay(overlay_name)
        if family not in overlay.compatible_families:
            raise RegistryError(f"Overlay {overlay_name} is not compatible with family {family}")
        if overlay.layer == "stack":
            stack_layers.append(overlay_name)
    if len(stack_layers) > 1:
        raise RegistryError("Only one stack overlay may be applied at a time")

    frontmatter = {}
    for key in template_family.required_frontmatter:
        frontmatter[key] = DEFAULT_VALUES.get(key, "")
    id_key = "pipeline_id" if "pipeline_id" in template_family.required_frontmatter else "id"
    frontmatter[id_key] = artifact_id
    frontmatter["title"] = title
    if overlays:
        frontmatter["overlays"] = overlays

    lines = ["---"]
    for key in template_family.required_frontmatter:
        lines.append(f"{key}: {_serialize_frontmatter_value(frontmatter[key])}")
    if overlays:
        lines.append(f"overlays: {_serialize_frontmatter_value(overlays)}")
    lines.append("---")
    lines.append("")
    lines.append(f"# {title}")
    lines.append("")
    for section in template_family.required_sections:
        lines.append(f"## {section}")
        lines.append("")
        lines.append(f"REQUIRED: project-defined content for {section.lower()}.")
        lines.append("")
    for overlay_name in overlays:
        overlay = registry.get_overlay(overlay_name)
        for section in overlay.additional_sections:
            lines.append(f"## {section}")
            lines.append("")
            lines.append(f"PROJECT_DEFINED: overlay-specific content for {overlay_name}.")
            lines.append("")

    if output_path is None:
        output_path = Path(template_family.output_path_pattern.format(id=_slugify(artifact_id)))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).rstrip() + "\n")

    issues = validate_document(output_path, family, registry)
    if issues:
        raise RegistryError(f"Scaffolded output failed lint: {'; '.join(issues)}")
    return output_path


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if argv and argv[0] not in {"scaffold-document", "list-manifests", "realize-repository", "doctor-composition"}:
        parser = argparse.ArgumentParser(description="Scaffold governed artifacts from the universal template system.")
        parser.add_argument("family")
        parser.add_argument("artifact_id")
        parser.add_argument("title")
        parser.add_argument("--output", type=Path, default=None)
        parser.add_argument("--overlay", action="append", default=[])
        parser.add_argument("--registry", type=Path, default=None)
        args = parser.parse_args(argv)
        path = scaffold_document(
            family=args.family,
            artifact_id=args.artifact_id,
            title=args.title,
            output_path=args.output,
            overlays=args.overlay,
            registry_path=args.registry,
        )
        print(path)
        return 0

    parser = argparse.ArgumentParser(description="Scaffold governed artifacts from the universal template system.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    document_parser = subparsers.add_parser("scaffold-document")
    document_parser.add_argument("family")
    document_parser.add_argument("artifact_id")
    document_parser.add_argument("title")
    document_parser.add_argument("--output", type=Path, default=None)
    document_parser.add_argument("--overlay", action="append", default=[])
    document_parser.add_argument("--registry", type=Path, default=None)

    list_parser = subparsers.add_parser("list-manifests")
    list_parser.add_argument("--manifest-dir", type=Path, default=None)
    list_parser.add_argument("--output", choices=("text", "json"), default="text")

    realize_parser = subparsers.add_parser("realize-repository")
    realize_parser.add_argument("template_name")
    realize_parser.add_argument("output_root", type=Path)
    realize_parser.add_argument("--overlay", action="append", default=[])
    realize_parser.add_argument("--include-optional", action="store_true")
    realize_parser.add_argument("--manifest-dir", type=Path, default=None)

    doctor_parser = subparsers.add_parser("doctor-composition")
    doctor_parser.add_argument("--overlays", nargs="*", default=[])
    doctor_parser.add_argument("--output", choices=("text", "json"), default="text")

    args = parser.parse_args(argv)
    if args.command == "scaffold-document":
        path = scaffold_document(
            family=args.family,
            artifact_id=args.artifact_id,
            title=args.title,
            output_path=args.output,
            overlays=args.overlay,
            registry_path=args.registry,
        )
        print(path)
        return 0
    if args.command == "list-manifests":
        try:
            manifests = [dataclasses.asdict(manifest) for manifest in list_scaffold_manifests(args.manifest_dir)]
            if args.output == "json":
                print(json.dumps(manifests, indent=2, sort_keys=True))
            else:
                for manifest in manifests:
                    print(
                        f"{manifest['template_name']} [{manifest['template_type']}] "
                        f"overlays={','.join(manifest['compatible_overlays']) or '-'}"
                    )
            return 0
        except RegistryError as exc:
            if args.output == "json":
                print(json.dumps({"valid": False, "errors": [str(exc)]}, indent=2, sort_keys=True))
            else:
                print(f"ERROR: {exc}")
            return 1
    if args.command == "doctor-composition":
        explanation = explain_template_composition(args.overlays)
        if args.output == "json":
            print(
                json.dumps(
                    {
                        "requested_overlays": list(explanation.requested_overlays),
                        "normalized_overlays": list(explanation.normalized_overlays),
                        "supported": explanation.supported,
                        "decision_source": explanation.decision_source,
                        "rejection_reason": explanation.rejection_reason,
                        "closest_supported": [list(item) for item in explanation.closest_supported],
                        "reason_code": explanation.reason_code,
                    },
                    indent=2,
                    sort_keys=True,
                )
            )
        else:
            print(render_explanation_summary(explanation))
        return 0 if explanation.supported else 1

    try:
        selection_path = realize_repository_scaffold(
            args.template_name,
            args.output_root,
            overlays=args.overlay,
            include_optional=args.include_optional,
            manifest_dir=args.manifest_dir,
        )
        print(selection_path)
        return 0
    except RegistryError as exc:
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
