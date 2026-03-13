from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from tools.governance.template_lint import validate_document
from tools.governance.template_registry import RegistryError, load_registry


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


if __name__ == "__main__":
    sys.exit(main())
