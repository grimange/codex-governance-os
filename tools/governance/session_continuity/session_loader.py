from __future__ import annotations

import re
from pathlib import Path

from .models import ScenarioDefinition

SCENARIO_FILE_PATTERN = "[0-9][0-9]-*.md"


def load_scenarios(scenario_dir: Path) -> list[ScenarioDefinition]:
    scenario_paths = sorted(
        path
        for path in scenario_dir.glob(SCENARIO_FILE_PATTERN)
        if path.name not in {"01-problem-statement.md", "02-scenario-model-definition.md", "07-final-verdict.md"}
    )
    return [load_scenario(path) for path in scenario_paths]


def load_scenario(path: Path) -> ScenarioDefinition:
    text = path.read_text(encoding="utf-8")
    title = _extract_heading(text)
    scenario_id = _extract_inline_code_value(text, "scenario_id")
    sessions = tuple(_extract_bullets(text, "Participating sessions"))
    evidence = tuple(_normalize_optional_bullets(_extract_bullets(text, "Admissible evidence")))
    expected_classification = _extract_optional_bullet_value(text, "Expected classification")
    expected_failure_classification = _extract_optional_bullet_value(text, "Expected failure classification")
    boundary_conditions = tuple(_extract_bullets(text, "Boundary validation"))
    invalid_reasoning_patterns = tuple(
        _extract_bullets(text, "Prohibited reasoning patterns")
        or _extract_bullets(text, "Invalid reasoning being exercised")
    )
    return ScenarioDefinition(
        title=title,
        scenario_id=scenario_id,
        sessions=sessions,
        evidence=evidence,
        expected_classification=expected_classification,
        expected_failure_classification=expected_failure_classification,
        boundary_conditions=boundary_conditions,
        invalid_reasoning_patterns=invalid_reasoning_patterns,
        source_path=str(path),
    )


def _extract_heading(text: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if not match:
        raise ValueError("scenario file missing top-level heading")
    return match.group(1).strip()


def _extract_inline_code_value(text: str, field_name: str) -> str:
    pattern = rf"`{re.escape(field_name)}`:\s*`([^`]+)`"
    match = re.search(pattern, text)
    if not match:
        raise ValueError(f"scenario file missing `{field_name}`")
    return _strip_code_ticks(match.group(1).strip())


def _extract_optional_bullet_value(text: str, heading: str) -> str | None:
    bullets = _extract_bullets(text, heading)
    return _strip_code_ticks(bullets[0]) if bullets else None


def _extract_bullets(text: str, heading: str) -> list[str]:
    lines = text.splitlines()
    bullets: list[str] = []
    capture = False
    current: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped == f"{heading}:":
            capture = True
            current = []
            continue
        if not capture:
            continue
        if stripped.startswith("#"):
            break
        if stripped.endswith(":") and not stripped.startswith("- "):
            break
        if stripped.startswith("- "):
            if current:
                bullets.append(" ".join(current).strip())
            current = [_strip_code_ticks(stripped[2:].strip())]
            continue
        if current and stripped:
            current.append(_strip_code_ticks(stripped))
            continue
        if current and not stripped:
            bullets.append(" ".join(current).strip())
            current = []
    if current:
        bullets.append(" ".join(current).strip())
    return bullets


def _normalize_optional_bullets(bullets: list[str]) -> list[str]:
    if not bullets:
        return []
    if len(bullets) == 1 and bullets[0].lower().startswith("none"):
        return []
    return bullets


def _strip_code_ticks(value: str) -> str:
    if value.startswith("`") and value.endswith("`") and len(value) >= 2:
        return value[1:-1]
    return value
