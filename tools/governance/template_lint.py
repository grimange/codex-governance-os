from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from tools.governance.template_registry import RegistryError, TemplateRegistry, load_registry


FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
HEADING_PATTERN = re.compile(r"^##\s+(.*)$", re.MULTILINE)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        raise RegistryError("Document is missing frontmatter")
    block = match.group(1)
    frontmatter = {}
    for line in block.splitlines():
        if not line.strip():
            continue
        key, _, raw_value = line.partition(":")
        if not _:
            raise RegistryError(f"Malformed frontmatter line: {line}")
        key = key.strip()
        value = raw_value.strip()
        if value.startswith("[") or value.startswith("{") or value.startswith('"'):
            frontmatter[key] = json.loads(value)
        else:
            frontmatter[key] = value.strip('"')
    return frontmatter, text[match.end() :]


def parse_sections(body: str) -> list[str]:
    return HEADING_PATTERN.findall(body)


def _frontmatter_has_key(frontmatter: dict, key: str, aliases: tuple[str, ...]) -> bool:
    return key in frontmatter or any(alias in frontmatter for alias in aliases)


def validate_document(
    path: Path, family: str, registry: TemplateRegistry | None = None
) -> list[str]:
    registry = registry or load_registry()
    template_family = registry.get_family(family)
    issues: list[str] = []
    frontmatter, body = parse_frontmatter(path.read_text())
    overlays = frontmatter.get("overlays", [])
    if overlays and not isinstance(overlays, list):
        issues.append("Frontmatter key overlays must be a list")
        overlays = []

    for required_key in template_family.required_frontmatter:
        aliases = template_family.normalization_aliases.get(required_key, ())
        if not _frontmatter_has_key(frontmatter, required_key, aliases):
            issues.append(f"Missing required frontmatter key: {required_key}")

    sections = parse_sections(body)
    expected_sections = list(template_family.required_sections)
    seen_indices: list[int] = []
    for section in expected_sections:
        if section not in sections:
            issues.append(f"Missing required section: {section}")
            continue
        seen_indices.append(sections.index(section))
    if seen_indices != sorted(seen_indices):
        issues.append("Required sections are not in canonical order")

    stack_layers = []
    for overlay_name in sorted(overlays):
        try:
            overlay = registry.get_overlay(overlay_name)
        except RegistryError as exc:
            issues.append(str(exc))
            continue
        if family not in overlay.compatible_families:
            issues.append(f"Overlay {overlay_name} is not compatible with family {family}")
        if overlay.weakens_core:
            issues.append(f"Overlay {overlay_name} weakens the universal core")
        if overlay.layer == "stack":
            stack_layers.append(overlay_name)
        for section in overlay.additional_sections:
            if section not in sections:
                issues.append(f"Missing overlay-required section: {section}")
    if len(stack_layers) > 1:
        issues.append("Only one stack overlay may be applied at a time")
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint governed artifacts against the template registry.")
    parser.add_argument("family")
    parser.add_argument("path", type=Path)
    parser.add_argument("--registry", type=Path, default=None)
    args = parser.parse_args(argv)
    registry = load_registry(args.registry)
    issues = validate_document(args.path, args.family, registry)
    if issues:
        for issue in issues:
            print(issue)
        return 1
    print(f"{args.path} conforms to template family {args.family}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
