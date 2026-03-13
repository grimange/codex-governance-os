from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.governance.template_registry import RegistryError, TemplateRegistry, load_registry


FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
HEADING_PATTERN = re.compile(r"^##\s+(.*)$", re.MULTILINE)
TOP_HEADING_PATTERN = re.compile(r"^#\s+(.+)$", re.MULTILINE)
PLACEHOLDER_PATTERN = re.compile(r"{{[^}]+}}|__[^_]+__|\b(?:TODO|TBD|FIXME)\b")
ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
PIPELINE_ID_PATTERN = re.compile(r"^[0-9]{3,}|^[a-z0-9][a-z0-9._-]*$")


RULE_CATALOG = {
    "UTL-001": {
        "severity": "error",
        "message": "Every governed template must declare a recognized template class.",
        "remediation": "Add or correct the canonical template family classification.",
    },
    "UTL-002": {
        "severity": "error",
        "message": "Every governed template must contain canonical frontmatter keys required by its class.",
        "remediation": "Add the missing required frontmatter keys for the classified template family.",
    },
    "UTL-003": {
        "severity": "error",
        "message": "Titles, identifiers, and slugs must match canonical naming conventions.",
        "remediation": "Normalize the title, id, pipeline_id, and heading naming to the canonical pattern.",
    },
    "UTL-004": {
        "severity": "error",
        "message": "Required sections must appear exactly once unless repetition is explicitly allowed.",
        "remediation": "Add missing required sections, remove duplicates, and restore canonical section ordering.",
    },
    "UTL-005": {
        "severity": "error",
        "message": "Templates must not contain unresolved placeholder tokens unless explicitly allowed.",
        "remediation": "Replace unresolved placeholder tokens or use the allowed REQUIRED/OPTIONAL/GENERATED/PROJECT_DEFINED markers only.",
    },
    "UTL-006": {
        "severity": "error",
        "message": "Universal templates must not hard-code repo-specific assumptions.",
        "remediation": "Remove repository-local names, paths, or assumptions from universal templates.",
    },
    "UTL-007": {
        "severity": "error",
        "message": "Templates must not contain contradictory status metadata or mixed draft/final semantics.",
        "remediation": "Make status language and template semantics consistent across frontmatter and body.",
    },
    "UTL-008": {
        "severity": "warning",
        "message": "Only approved safe normalizations may be applied automatically.",
        "remediation": "Accept the recorded normalization or update the source template manually if the change is not desired.",
    },
    "UTL-009": {
        "severity": "error",
        "message": "The linter must return deterministic results for identical file content.",
        "remediation": "Stabilize rule ordering and output formatting.",
    },
    "UTL-010": {
        "severity": "error",
        "message": "Every lint failure must include actionable remediation text.",
        "remediation": "Add remediation guidance for each emitted rule violation.",
    },
}

UNIVERSAL_LEAKAGE_PATTERNS = [
    ("codex-governance-os", "Remove repository-specific project naming from universal templates."),
    ("/home/ramjf", "Remove workstation-specific filesystem paths from universal templates."),
    ("python-projects/codex-governance-os", "Remove repository-local root paths from universal templates."),
    (".idea/", "Remove editor-specific repository assumptions from universal templates."),
]
ALLOWED_PLACEHOLDER_PREFIXES = ("REQUIRED:", "OPTIONAL:", "GENERATED:", "PROJECT_DEFINED:")
DEFAULT_TEMPLATE_ROOTS = (
    REPO_ROOT / "docs" / "governance" / "templates",
    REPO_ROOT / "docs" / "codex" / "templates",
)


@dataclass(frozen=True)
class LintIssue:
    rule_id: str
    severity: str
    path: str
    message: str
    remediation: str


@dataclass(frozen=True)
class LintResult:
    path: str
    template_class: str
    decision: str
    issues: tuple[LintIssue, ...]
    normalizations: tuple[str, ...]
    normalized_content: str | None


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


def _top_heading(body: str) -> str | None:
    match = TOP_HEADING_PATTERN.search(body)
    return match.group(1).strip() if match else None


def _add_issue(issues: list[LintIssue], rule_id: str, path: Path, detail: str | None = None) -> None:
    rule = RULE_CATALOG[rule_id]
    message = rule["message"] if detail is None else f"{rule['message']} {detail}"
    issues.append(
        LintIssue(
            rule_id=rule_id,
            severity=rule["severity"],
            path=str(path),
            message=message,
            remediation=rule["remediation"],
        )
    )


def _normalize_content(text: str) -> tuple[str, list[str]]:
    normalizations: list[str] = []
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    if normalized != text:
        normalizations.append("normalized line endings")
    lines = normalized.split("\n")
    trimmed_lines = [line.rstrip() for line in lines]
    if trimmed_lines != lines:
        normalizations.append("trimmed trailing whitespace")
    normalized = "\n".join(trimmed_lines)
    if not normalized.endswith("\n"):
        normalized += "\n"
    return normalized, normalizations


def classify_template(path: Path, frontmatter: dict, body: str, registry: TemplateRegistry | None = None) -> str:
    registry = registry or load_registry()
    explicit_family = frontmatter.get("category")
    if isinstance(explicit_family, str) and explicit_family in registry.templates:
        return explicit_family
    stem = path.stem.lower()
    family_hints = (
        ("pipeline", "pipeline"),
        ("verification", "verification"),
        ("rule", "rule"),
        ("skill", "skill"),
        ("sub-agent", "sub_agent"),
        ("subagent", "sub_agent"),
        ("report", "report"),
        ("instruction", "instruction"),
        ("prompt", "instruction"),
        ("remediation", "remediation"),
        ("decision", "decision"),
        ("evidence-pack", "evidence-pack"),
        ("evidence", "evidence-pack"),
    )
    for token, family_name in family_hints:
        if token in stem and family_name in registry.templates:
            return family_name
    if "pipeline_id" in frontmatter:
        return "pipeline"
    if "id" in frontmatter:
        candidates = []
        sections = set(parse_sections(body))
        for family_name, family in registry.templates.items():
            required = set(family.required_sections)
            if required.issubset(sections):
                candidates.append((len(required), family_name))
        if candidates:
            candidates.sort(reverse=True)
            return candidates[0][1]
    raise RegistryError("Unable to classify template family")


def lint_template(
    path: Path,
    *,
    family: str | None = None,
    registry: TemplateRegistry | None = None,
    apply_normalization: bool = False,
) -> LintResult:
    registry = registry or load_registry()
    original_text = path.read_text()
    normalized_text, normalizations = _normalize_content(original_text)
    working_text = normalized_text
    issues: list[LintIssue] = []

    try:
        frontmatter, body = parse_frontmatter(working_text)
    except RegistryError:
        _add_issue(issues, "UTL-002", path, "Document frontmatter is missing or malformed.")
        return LintResult(str(path), family or "unknown", "BLOCKED", tuple(sorted(issues, key=lambda i: (i.rule_id, i.message))), tuple(normalizations), None)

    if _top_heading(body) is None and isinstance(frontmatter.get("title"), str):
        title = frontmatter["title"]
        insertion = f"# {title}\n\n"
        working_text = FRONTMATTER_PATTERN.sub(lambda match: match.group(0) + insertion, working_text, count=1)
        normalizations.append("inserted canonical top heading from title")
        frontmatter, body = parse_frontmatter(working_text)

    try:
        template_class = family or classify_template(path, frontmatter, body, registry)
    except RegistryError:
        _add_issue(issues, "UTL-001", path)
        template_class = family or "unknown"
        return LintResult(str(path), template_class, "BLOCKED", tuple(sorted(issues, key=lambda i: (i.rule_id, i.message))), tuple(normalizations), None)

    template_family = registry.get_family(template_class)

    for required_key in template_family.required_frontmatter:
        aliases = template_family.normalization_aliases.get(required_key, ())
        if not _frontmatter_has_key(frontmatter, required_key, aliases):
            _add_issue(issues, "UTL-002", path, f"Missing required frontmatter key `{required_key}`.")

    id_value = frontmatter.get("pipeline_id") or frontmatter.get("id")
    if not isinstance(id_value, str) or not (
        PIPELINE_ID_PATTERN.match(id_value) if template_class == "pipeline" else ID_PATTERN.match(id_value)
    ):
        _add_issue(issues, "UTL-003", path, "Identifier is missing or not canonically formatted.")

    title = frontmatter.get("title")
    if not isinstance(title, str) or not title.strip():
        _add_issue(issues, "UTL-003", path, "Title is missing or empty.")
    top_heading = _top_heading(body)
    if isinstance(title, str) and top_heading is not None and top_heading != title:
        _add_issue(issues, "UTL-003", path, "Top heading does not match the frontmatter title.")

    sections = parse_sections(body)
    indices: list[int] = []
    for section in template_family.required_sections:
        count = sections.count(section)
        if count == 0:
            _add_issue(issues, "UTL-004", path, f"Missing required section `{section}`.")
        elif count > 1:
            _add_issue(issues, "UTL-004", path, f"Required section `{section}` appears more than once.")
        else:
            indices.append(sections.index(section))
    if indices != sorted(indices):
        _add_issue(issues, "UTL-004", path, "Required sections are not in canonical order.")

    overlays = frontmatter.get("overlays", [])
    if overlays and not isinstance(overlays, list):
        _add_issue(issues, "UTL-002", path, "Frontmatter key `overlays` must be a list.")
        overlays = []
    stack_layers = []
    for overlay_name in sorted(overlays):
        try:
            overlay = registry.get_overlay(overlay_name)
        except RegistryError:
            _add_issue(issues, "UTL-001", path, f"Unknown overlay `{overlay_name}`.")
            continue
        if template_class not in overlay.compatible_families:
            _add_issue(issues, "UTL-004", path, f"Overlay `{overlay_name}` is not compatible with family `{template_class}`.")
        if overlay.weakens_core:
            _add_issue(issues, "UTL-006", path, f"Overlay `{overlay_name}` weakens the universal core.")
        if overlay.layer == "stack":
            stack_layers.append(overlay_name)
        for section in overlay.additional_sections:
            if sections.count(section) != 1:
                _add_issue(issues, "UTL-004", path, f"Overlay-required section `{section}` is missing or duplicated.")
    if len(stack_layers) > 1:
        _add_issue(issues, "UTL-004", path, "Only one stack overlay may be applied at a time.")

    for match in PLACEHOLDER_PATTERN.finditer(working_text):
        line = match.group(0)
        if any(prefix in working_text[max(0, match.start() - 32): match.end() + 32] for prefix in ALLOWED_PLACEHOLDER_PREFIXES):
            continue
        _add_issue(issues, "UTL-005", path, f"Found unresolved placeholder token `{line}`.")

    universal_mode = (
        "universal" in path.as_posix()
        or (isinstance(title, str) and "universal" in title.lower())
        or (isinstance(id_value, str) and ".universal." in id_value)
    )
    if universal_mode:
        for token, remediation in UNIVERSAL_LEAKAGE_PATTERNS:
            if token in working_text:
                issues.append(
                    LintIssue(
                        rule_id="UTL-006",
                        severity="error",
                        path=str(path),
                        message=f"{RULE_CATALOG['UTL-006']['message']} Found `{token}`.",
                        remediation=remediation,
                    )
                )

    status = frontmatter.get("status")
    if isinstance(status, str):
        lowered = working_text.lower()
        if status in {"active", "complete", "accepted"} and "draft" in lowered:
            _add_issue(issues, "UTL-007", path, "Body text contains draft semantics while status is final or active.")
        if status == "draft" and "final verdict" in lowered and "active" in lowered:
            _add_issue(issues, "UTL-007", path, "Draft template mixes final/active semantics.")

    if any(not issue.remediation for issue in issues):
        _add_issue(issues, "UTL-010", path)

    if normalizations:
        issues.append(
            LintIssue(
                rule_id="UTL-008",
                severity="warning",
                path=str(path),
                message=f"{RULE_CATALOG['UTL-008']['message']} Applied: {', '.join(normalizations)}.",
                remediation=RULE_CATALOG["UTL-008"]["remediation"],
            )
        )

    ordered_issues = tuple(sorted(issues, key=lambda item: (item.rule_id, item.message, item.path)))
    blocking = any(issue.severity == "error" for issue in ordered_issues)
    if blocking:
        decision = "BLOCKED"
    elif normalizations:
        decision = "NORMALIZED_AND_VALID"
    else:
        decision = "VALID_AS_IS"

    if apply_normalization and normalizations and not blocking:
        path.write_text(working_text)

    return LintResult(
        path=str(path),
        template_class=template_class,
        decision=decision,
        issues=ordered_issues,
        normalizations=tuple(normalizations),
        normalized_content=working_text if normalizations else None,
    )


def validate_document(
    path: Path, family: str, registry: TemplateRegistry | None = None
) -> list[str]:
    result = lint_template(path, family=family, registry=registry)
    return [f"{issue.rule_id}: {issue.message}" for issue in result.issues if issue.severity == "error"]


def lint_templates(
    *,
    roots: tuple[Path, ...] = DEFAULT_TEMPLATE_ROOTS,
    registry: TemplateRegistry | None = None,
    apply_normalization: bool = False,
) -> list[LintResult]:
    registry = registry or load_registry()
    results: list[LintResult] = []
    files: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        files.extend(sorted(path for path in root.rglob("*.md") if path.name != "README.md"))
    for path in sorted(files):
        results.append(lint_template(path, registry=registry, apply_normalization=apply_normalization))
    return results


def _result_to_json(result: LintResult) -> dict:
    return {
        "path": result.path,
        "template_class": result.template_class,
        "decision": result.decision,
        "normalizations": list(result.normalizations),
        "issues": [asdict(issue) for issue in result.issues],
    }


def format_result_text(result: LintResult) -> str:
    lines = [f"{result.path}: {result.decision} [{result.template_class}]"]
    for issue in result.issues:
        lines.append(f"  {issue.rule_id} {issue.severity}: {issue.message}")
        lines.append(f"    remediation: {issue.remediation}")
    return "\n".join(lines)


def _command_lint_template(args: argparse.Namespace) -> int:
    registry = load_registry(args.registry)
    result = lint_template(
        args.path,
        family=args.family,
        registry=registry,
        apply_normalization=args.apply_normalization,
    )
    if args.output == "json":
        print(json.dumps(_result_to_json(result), indent=2, sort_keys=True))
    else:
        print(format_result_text(result))
    return 0 if result.decision != "BLOCKED" else 1


def _command_lint_templates(args: argparse.Namespace) -> int:
    registry = load_registry(args.registry)
    roots = tuple(Path(root) for root in args.root) if args.root else DEFAULT_TEMPLATE_ROOTS
    results = lint_templates(roots=roots, registry=registry, apply_normalization=args.apply_normalization)
    if args.output == "json":
        print(json.dumps([_result_to_json(result) for result in results], indent=2, sort_keys=True))
    else:
        print("\n\n".join(format_result_text(result) for result in results))
    return 0 if all(result.decision != "BLOCKED" for result in results) else 1


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if argv and not argv[0].startswith("-") and argv[0] not in {"lint-template", "lint-templates"}:
        registry = load_registry()
        if len(argv) >= 2 and argv[0] in registry.templates and Path(argv[1]).exists():
            family, path = argv[0], Path(argv[1])
            result = lint_template(path, family=family, registry=registry)
            print(format_result_text(result))
            return 0 if result.decision != "BLOCKED" else 1

    parser = argparse.ArgumentParser(description="Lint governed templates against the universal canonical contract.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    lint_template_parser = subparsers.add_parser("lint-template")
    lint_template_parser.add_argument("path", type=Path)
    lint_template_parser.add_argument("--family", default=None)
    lint_template_parser.add_argument("--registry", type=Path, default=None)
    lint_template_parser.add_argument("--apply-normalization", action="store_true")
    lint_template_parser.add_argument("--output", choices=("text", "json"), default="text")
    lint_template_parser.set_defaults(func=_command_lint_template)

    lint_templates_parser = subparsers.add_parser("lint-templates")
    lint_templates_parser.add_argument("--root", action="append", default=[])
    lint_templates_parser.add_argument("--registry", type=Path, default=None)
    lint_templates_parser.add_argument("--apply-normalization", action="store_true")
    lint_templates_parser.add_argument("--output", choices=("text", "json"), default="text")
    lint_templates_parser.set_defaults(func=_command_lint_templates)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
