from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]

FORBIDDEN_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("POSIX_HOME", re.compile(r"/home/")),
    ("MAC_USERS", re.compile(r"/Users/")),
    ("WINDOWS_DRIVE", re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:\\")),
    ("FILE_URI", re.compile(r"file://")),
    ("HOME_SHORTCUT", re.compile(r"~/")),
)

HISTORICAL_EVIDENCE_ROOTS = (
    Path("docs/pipelines/governance/remediate-non-portable-filesystem-links-in-canonical-governance-surfaces"),
    Path("docs/pipelines/governance/enforce-repository-portability-link-invariants-across-governance-surfaces"),
    Path("docs/pipelines/governance/verify-non-portable-filesystem-references-were-remediated-and-no-longer-exist-in-governed-repository-surfaces"),
)


@dataclass(frozen=True)
class ScanMatch:
    path: str
    line: int
    column: int
    pattern: str
    classification: str
    excerpt: str


@dataclass(frozen=True)
class ScanResult:
    scope: str
    scanned_files: tuple[str, ...]
    violations: tuple[ScanMatch, ...]
    exceptions: tuple[ScanMatch, ...]


def active_governed_surface_paths(repo_root: Path = REPO_ROOT) -> list[Path]:
    paths: set[Path] = set()
    for root in (
        repo_root / "docs" / "governance",
        repo_root / "docs" / "contracts",
    ):
        if root.exists():
            paths.update(path for path in root.rglob("*.md") if path.is_file())

    for direct_path in (
        repo_root / "README.md",
        repo_root / ".codex" / "AGENTS.md",
        repo_root / "docs" / "pipelines" / "registry" / "pipeline-registry.md",
    ):
        if direct_path.exists():
            paths.add(direct_path)

    pipeline_root = repo_root / "docs" / "pipelines" / "governance"
    if pipeline_root.exists():
        paths.update(path for path in pipeline_root.glob("*--*.md") if path.is_file())

    return sorted(paths)


def is_historical_evidence(path: Path, repo_root: Path = REPO_ROOT) -> bool:
    try:
        relative_path = path.relative_to(repo_root)
    except ValueError:
        return False
    return any(relative_path.is_relative_to(root) for root in HISTORICAL_EVIDENCE_ROOTS)


def _is_link_target(line: str, start: int) -> bool:
    prefix = line[:start]
    return "](" in prefix and prefix.rfind("](") > prefix.rfind(")")


def _is_inside_inline_code(line: str, start: int) -> bool:
    backticks_before = line[:start].count("`")
    backticks_after = line[start:].count("`")
    return backticks_before % 2 == 1 and backticks_after >= 1


def _classify_match(
    path: Path,
    line: str,
    start: int,
    in_fence: bool,
    repo_root: Path,
) -> str:
    if is_historical_evidence(path, repo_root):
        return "historical_evidence"
    if _is_link_target(line, start):
        return "violation"
    if in_fence:
        return "scan_definition"
    if line.startswith("    "):
        return "scan_definition"
    if _is_inside_inline_code(line, start):
        return "rule_example"
    return "violation"


def scan_files(
    paths: list[Path],
    *,
    scope: str,
    repo_root: Path = REPO_ROOT,
) -> ScanResult:
    violations: list[ScanMatch] = []
    exceptions: list[ScanMatch] = []

    for path in sorted(paths):
        if not path.exists() or not path.is_file():
            continue
        in_fence = False
        for line_number, raw_line in enumerate(path.read_text().splitlines(), start=1):
            stripped = raw_line.lstrip()
            if stripped.startswith("```"):
                in_fence = not in_fence
            for pattern_name, pattern in FORBIDDEN_PATTERNS:
                for match in pattern.finditer(raw_line):
                    classification = _classify_match(path, raw_line, match.start(), in_fence, repo_root)
                    record = ScanMatch(
                        path=str(path.relative_to(repo_root)),
                        line=line_number,
                        column=match.start() + 1,
                        pattern=pattern_name,
                        classification=classification,
                        excerpt=raw_line.strip(),
                    )
                    if classification == "violation":
                        violations.append(record)
                    else:
                        exceptions.append(record)

    return ScanResult(
        scope=scope,
        scanned_files=tuple(str(path.relative_to(repo_root)) for path in sorted(paths) if path.exists()),
        violations=tuple(sorted(violations, key=lambda item: (item.path, item.line, item.column, item.pattern))),
        exceptions=tuple(sorted(exceptions, key=lambda item: (item.path, item.line, item.column, item.pattern))),
    )


def scan_active_governed_surfaces(repo_root: Path = REPO_ROOT) -> ScanResult:
    return scan_files(
        active_governed_surface_paths(repo_root),
        scope="active_governed_surfaces",
        repo_root=repo_root,
    )


def _result_to_json(result: ScanResult) -> dict:
    return {
        "scope": result.scope,
        "scanned_files": list(result.scanned_files),
        "violations": [asdict(item) for item in result.violations],
        "exceptions": [asdict(item) for item in result.exceptions],
    }


def format_result_text(result: ScanResult) -> str:
    lines = [
        f"scope: {result.scope}",
        f"scanned_files: {len(result.scanned_files)}",
        f"violations: {len(result.violations)}",
        f"exceptions: {len(result.exceptions)}",
    ]
    if result.violations:
        lines.append("violation_details:")
        for violation in result.violations:
            lines.append(
                f"  - {violation.path}:{violation.line}:{violation.column} "
                f"[{violation.pattern}] {violation.excerpt}"
            )
    return "\n".join(lines)


def _command_scan_active(args: argparse.Namespace) -> int:
    result = scan_active_governed_surfaces(args.repo_root)
    if args.output == "json":
        print(json.dumps(_result_to_json(result), indent=2, sort_keys=True))
    else:
        print(format_result_text(result))
    return 0 if not result.violations else 1


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description="Scan governed repository surfaces for non-portable machine-local filesystem references."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_active_parser = subparsers.add_parser("scan-active")
    scan_active_parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    scan_active_parser.add_argument("--output", choices=("text", "json"), default="text")
    scan_active_parser.set_defaults(func=_command_scan_active)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
