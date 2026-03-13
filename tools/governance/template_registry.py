from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


DEFAULT_REGISTRY_PATH = (
    Path(__file__).resolve().parents[2]
    / "docs"
    / "governance"
    / "templates"
    / "template-registry.yaml"
)


class RegistryError(ValueError):
    """Raised when the template registry is malformed."""


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
class TemplateRegistry:
    schema_version: str
    governance_mode: str
    execution_mode: str
    universal_core: dict
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


def _read_json_compatible_yaml(path: Path) -> dict:
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


def _validate_overlay_definitions(raw_overlays: list[dict]) -> dict[str, OverlayDefinition]:
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
    raw_templates: list[dict], overlays: dict[str, OverlayDefinition]
) -> dict[str, TemplateFamily]:
    templates: dict[str, TemplateFamily] = {}
    alias_targets: dict[str, str] = {}
    for raw in raw_templates:
        family_name = raw.get("family")
        if not isinstance(family_name, str) or not family_name:
            raise RegistryError("Template definitions require a non-empty family")
        if family_name in templates:
            raise RegistryError(f"Duplicate template family: {family_name}")
        aliases = {}
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
            version=raw.get("version", ""),
            required_sections=_tupled_strings(
                raw.get("required_sections", []), f"{family_name}.required_sections"
            ),
            optional_sections=_tupled_strings(
                raw.get("optional_sections", []), f"{family_name}.optional_sections"
            ),
            required_frontmatter=_tupled_strings(
                raw.get("required_frontmatter", []),
                f"{family_name}.required_frontmatter",
            ),
            normalization_aliases=aliases,
            output_path_pattern=raw.get("output_path_pattern", ""),
            validator=raw.get("validator", ""),
            scaffold=raw.get("scaffold", ""),
            compatible_overlays=compatible_overlays,
        )
    return templates


def load_registry(path: Path | None = None) -> TemplateRegistry:
    registry_path = path or DEFAULT_REGISTRY_PATH
    raw = _read_json_compatible_yaml(registry_path)
    overlays = _validate_overlay_definitions(raw.get("overlays", []))
    templates = _validate_template_definitions(raw.get("templates", []), overlays)
    return TemplateRegistry(
        schema_version=raw.get("schema_version", ""),
        governance_mode=raw.get("governance_mode", ""),
        execution_mode=raw.get("execution_mode", ""),
        universal_core=raw.get("universal_core", {}),
        templates=templates,
        overlays=overlays,
    )
