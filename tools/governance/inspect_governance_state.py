#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS = REPO_ROOT / "docs" / "governance"
STATE_MD = DOCS / "governance-system-state.md"
STATE_JSON = DOCS / "governance-system-state.json"
EVIDENCE_INVENTORY = DOCS / "governance-evidence-inventory.md"
SYSTEM_MATURITY_JSON = DOCS / "governance-system-maturity.json"
REGISTRY_MD = DOCS / "governance-capability-registry.md"
EXECUTION_MAP_MD = DOCS / "governance-capability-execution-map.md"
PROGRESS_MD = DOCS / "governance-capability-progress.md"
SCORECARD_MD = DOCS / "governance-maturity-scorecard.md"
HISTORY_MD = DOCS / "governance-maturity-history.md"
GAP_ANALYSIS_MD = DOCS / "governance-maturity-gap-analysis.md"
ADVANCEMENT_PLAN_MD = DOCS / "governance-capability-advancement-plan.md"

DOMAIN_CAPABILITY_MAP = {
    "codex_governance_layer": ["Governance Doctrine", "Execution Governance"],
    "pipeline_governance": ["Pipeline Governance"],
    "passive_observation": ["Observability"],
    "autonomous_governance_loop": ["Autonomous Governance Loop"],
    "multi_agent_governance": ["Multi-Agent Governance"],
    "architecture_advisor": ["Architecture Advisor"],
}


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_state_layers(text: str) -> dict[str, str]:
    layers: dict[str, str] = {}
    pattern = re.compile(r"^(Layer \d+ --- .+?)\\\nStatus: ([A-Z ]+)$", re.MULTILINE)
    for label, status in pattern.findall(text):
        name = label.split("---", 1)[1].strip()
        layers[slugify(name)] = status.lower().replace(" ", "_")
    return layers


def parse_constraints(text: str) -> dict[str, int]:
    constraints = {}
    patterns = {
        "unresolved_historical_gaps": r"`(\d+)` unresolved historical governance gaps",
        "bounded_verdict_family_runs": r"`(\d+)` bounded verdict-family runs",
        "analytics_other_verdicts": r"`(\d+)` analytics `OTHER` verdicts",
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if not match:
            raise ValueError(f"Missing constraint for {key} in governance system state")
        constraints[key] = int(match.group(1))
    return constraints


def parse_maturity_score(text: str) -> int:
    match = re.search(r"maturity score: `(\d+)%`", text)
    if not match:
        raise ValueError("Missing maturity score in governance system state")
    return int(match.group(1))


def parse_trend_classification(text: str) -> str:
    match = re.search(r"trend classification: `([^`]+)`", text)
    if not match:
        raise ValueError("Missing trend classification in governance system state")
    return slugify(match.group(1))


def parse_progress_sections(text: str) -> dict[str, list[str]]:
    result = {"completed": [], "in_progress": [], "planned": []}
    current: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line == "Completed capabilities:":
            current = "completed"
            continue
        if line == "Capabilities in progress:":
            current = "in_progress"
            continue
        if line == "Planned capabilities:":
            current = "planned"
            continue
        if current and line.startswith("- "):
            result[current].append(line[2:].strip())
            continue
        if current and line and not line.startswith("- "):
            current = None
    return result


def parse_registry_capabilities(text: str) -> dict[str, str]:
    capabilities: dict[str, str] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or stripped.startswith("|---") or "Capability | Status" in stripped:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 2:
            continue
        capability = cells[0]
        status = cells[1]
        capabilities[capability] = slugify(status)
    return capabilities


def parse_execution_map_headings(text: str) -> set[str]:
    headings = set()
    for line in text.splitlines():
        if line.startswith("## "):
            headings.add(line[3:].strip())
    return headings


def validate_alignment(
    registry: dict[str, str],
    progress: dict[str, list[str]],
    execution_headings: set[str],
) -> list[str]:
    issues: list[str] = []

    progress_status_map: dict[str, str] = {}
    for status, items in progress.items():
        mapped = {"completed": "complete", "in_progress": "in_progress", "planned": "planned"}[status]
        for item in items:
            progress_status_map[item] = mapped

    for capability, registry_status in registry.items():
        progress_status = progress_status_map.get(capability)
        if progress_status and progress_status != registry_status:
            issues.append(
                f"Capability status mismatch for '{capability}': registry={registry_status}, progress={progress_status}"
            )
        if capability not in execution_headings and capability not in {"Governance State Introspection automation"}:
            issues.append(f"Capability missing from execution map: '{capability}'")

    return issues


def build_state_payload() -> tuple[dict[str, object], list[str]]:
    state_text = read_text(STATE_MD)
    progress_text = read_text(PROGRESS_MD)
    registry_text = read_text(REGISTRY_MD)
    execution_map_text = read_text(EXECUTION_MAP_MD)

    layers = parse_state_layers(state_text)
    progress = parse_progress_sections(progress_text)
    registry = parse_registry_capabilities(registry_text)
    execution_headings = parse_execution_map_headings(execution_map_text)
    issues = validate_alignment(registry, progress, execution_headings)

    payload = {
        "governance_maturity_estimate": parse_maturity_score(state_text),
        "trend_classification": parse_trend_classification(state_text),
        "layers": layers,
        "capabilities": registry,
        "capability_snapshot": progress,
        "bounded_constraints": parse_constraints(state_text),
        "capability_sources": [
            "docs/governance/governance-capability-registry.md",
            "docs/governance/governance-capability-execution-map.md",
            "docs/governance/governance-capability-progress.md",
        ],
        "maturity_sources": [
            "docs/governance/governance-maturity-scorecard.md",
            "docs/governance/governance-maturity-history.md",
            "docs/governance/governance-maturity-gap-analysis.md",
            "docs/governance/governance-capability-advancement-plan.md",
        ],
        "evidence_inventory": "docs/governance/governance-evidence-inventory.md",
    }
    return payload, issues


def classify_domain(registry: dict[str, str], capabilities: list[str]) -> tuple[int, str]:
    missing = [capability for capability in capabilities if capability not in registry]
    if missing:
        return 0, "INVALID_STATE"

    statuses = [registry[capability] for capability in capabilities]
    verified = sum(1 for status in statuses if status == "complete")
    total = len(statuses)
    score = round((verified / total) * 100) if total else 0

    if verified == total:
        return score, "VERIFIED"
    if verified == 0:
        return 0, "UNVERIFIED"
    return score, "PARTIAL"


def build_maturity_payload() -> dict[str, object]:
    state_payload, issues = build_state_payload()
    if issues:
        raise ValueError("Cannot compute maturity from inconsistent governance state")

    registry = parse_registry_capabilities(read_text(REGISTRY_MD))
    domains: dict[str, int] = {}
    classifications: dict[str, str] = {}
    blockers: list[str] = []

    for domain, capabilities in DOMAIN_CAPABILITY_MAP.items():
        score, classification = classify_domain(registry, capabilities)
        domains[domain] = score
        classifications[domain] = classification
        if classification == "INVALID_STATE":
            blockers.append(f"{domain}_missing_registry")
        elif classification == "UNVERIFIED":
            blockers.append(f"{domain}_unverified")

    overall_maturity = round(sum(domains.values()) / len(domains)) if domains else 0

    return {
        "overall_maturity": overall_maturity,
        "current_governance_maturity_reference": state_payload["governance_maturity_estimate"],
        "domains": domains,
        "domain_classifications": classifications,
        "blockers": blockers,
        "recommended_next_pipelines": [165, 166, 167],
        "sources": [
            "docs/governance/governance-system-state.json",
            "docs/governance/governance-capability-registry.md",
            "docs/pipelines/registry/pipeline-registry.md",
        ],
    }


def run_state_inspection() -> int:
    payload, issues = build_state_payload()
    STATE_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    print(f"Regenerated {STATE_JSON.relative_to(REPO_ROOT)}")
    if issues:
        print("Detected governance artifact inconsistencies:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("No governance artifact inconsistencies detected.")
    return 0


def run_maturity_scoring() -> int:
    payload = build_maturity_payload()
    SYSTEM_MATURITY_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Regenerated {SYSTEM_MATURITY_JSON.relative_to(REPO_ROOT)}")
    return 0


def main() -> int:
    if len(sys.argv) == 1:
        return run_state_inspection()

    if len(sys.argv) == 2 and sys.argv[1] == "maturity":
        return run_maturity_scoring()

    print("Usage: python tools/governance/inspect_governance_state.py [maturity]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
