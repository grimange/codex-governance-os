#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import hashlib
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DOCS = REPO_ROOT / "docs" / "governance"
STATE_MD = DOCS / "governance-system-state.md"
STATE_JSON = DOCS / "governance-system-state.json"
EVIDENCE_INVENTORY = DOCS / "governance-evidence-inventory.md"
SYSTEM_MATURITY_JSON = DOCS / "governance-system-maturity.json"
SYSTEM_GAPS_JSON = DOCS / "governance-system-gaps.json"
SYSTEM_GAP_REMEDIATION_PLAN_JSON = DOCS / "governance-system-gap-remediation-plan.json"
SYSTEM_ADVANCEMENT_ROADMAP_JSON = DOCS / "governance-system-advancement-roadmap.json"
SYSTEM_NEXT_ACTION_JSON = DOCS / "governance-system-next-action.json"
AUTHORITATIVE_STATE_ANSWER_JSON = DOCS / "governance-authoritative-state-answer.json"
STATE_SNAPSHOT_JSON = DOCS / "governance-state-snapshot.json"
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

DOMAIN_REMEDIATION_MAP = {
    "codex_governance_layer": {
        "type": "governance-surface-verification",
        "pipelines": [],
    },
    "pipeline_governance": {
        "type": "pipeline-governance-normalization",
        "pipelines": [],
    },
    "passive_observation": {
        "type": "observability-expansion",
        "pipelines": [],
    },
    "autonomous_governance_loop": {
        "type": "autonomous-governance-establishment",
        "pipelines": [],
    },
    "multi_agent_governance": {
        "type": "registry-and-capability-establishment",
        "pipelines": ["establish-role-scoped-codex-sub-agent-specialization"],
    },
    "architecture_advisor": {
        "type": "advisory-capability-establishment",
        "pipelines": [],
    },
}

REMEDIATION_STRATEGY_MAP = {
    "INVALID_STATE": "state_normalization",
    "UNVERIFIED": "capability_completion",
    "PARTIAL": "verification_missing",
    "BLOCKED_BY_DRIFT": "evidence_gap",
}

REMEDIATION_PRIORITY_MAP = {
    "INVALID_STATE": "CRITICAL",
    "UNVERIFIED": "HIGH",
    "PARTIAL": "MEDIUM",
    "BLOCKED_BY_DRIFT": "CRITICAL",
}

ROADMAP_FOCUS_MAP = {
    "state_normalization": "state_normalization",
    "capability_completion": "capability_expansion",
    "verification_missing": "capability_expansion",
    "evidence_gap": "evidence_gap_resolution",
}

ACTION_TYPE_MAP = {
    "state_normalization": "state_normalization",
    "capability_completion": "capability_completion",
    "verification_missing": "verification_required",
    "evidence_gap": "verification_required",
}

AMBIGUOUS_SUFFIXES = ("-copy", "-backup", "-old", "-temp", "-draft")


class GovernanceInputError(ValueError):
    def __init__(self, error_code: str, message: str, allowed_surfaces: list[str]):
        super().__init__(message)
        self.error_code = error_code
        self.message = message
        self.allowed_surfaces = allowed_surfaces

    def to_payload(self) -> dict[str, object]:
        return {
            "status": "error",
            "error_code": self.error_code,
            "message": self.message,
            "allowed_surfaces": self.allowed_surfaces,
        }


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def allowed_next_action_surfaces() -> list[Path]:
    return [
        STATE_SNAPSHOT_JSON,
        STATE_JSON,
        SYSTEM_MATURITY_JSON,
        SYSTEM_GAPS_JSON,
        SYSTEM_GAP_REMEDIATION_PLAN_JSON,
        SYSTEM_ADVANCEMENT_ROADMAP_JSON,
    ]


def allowed_next_action_surface_strings() -> list[str]:
    return [str(path.relative_to(REPO_ROOT)) for path in allowed_next_action_surfaces()]


def snapshot_surface_paths() -> list[Path]:
    return [
        STATE_JSON,
        SYSTEM_ADVANCEMENT_ROADMAP_JSON,
        SYSTEM_GAPS_JSON,
        SYSTEM_MATURITY_JSON,
        SYSTEM_GAP_REMEDIATION_PLAN_JSON,
    ]


def build_governance_state_snapshot_payload(
    previous_snapshot: dict[str, object] | None = None,
) -> dict[str, object]:
    surfaces = {
        str(path.name): sha256_text(read_text(path))
        for path in snapshot_surface_paths()
    }
    snapshot_id = sha256_text("\n".join(surfaces[name] for name in surfaces))
    previous_snapshot_id = None
    if previous_snapshot is not None:
        previous_snapshot_id = previous_snapshot.get("snapshot_id")

    return {
        "generated_by": "inspect_governance_state.py",
        "snapshot_version": "1.0",
        "snapshot_id": snapshot_id,
        "previous_snapshot_id": previous_snapshot_id,
        "drift_detected": previous_snapshot_id not in {None, snapshot_id},
        "surfaces": surfaces,
    }


def validate_required_governance_snapshot(
    snapshot_payload: dict[str, object],
    allowed_surfaces: list[str],
) -> None:
    required_fields = {"snapshot_id", "drift_detected", "surfaces"}
    missing_fields = sorted(field for field in required_fields if field not in snapshot_payload)
    if missing_fields:
        raise GovernanceInputError(
            "INVALID_GOVERNANCE_STATE_SNAPSHOT",
            f"Governance state snapshot is missing required fields: {', '.join(missing_fields)}",
            allowed_surfaces,
        )

    if not isinstance(snapshot_payload["surfaces"], dict) or not snapshot_payload["surfaces"]:
        raise GovernanceInputError(
            "INVALID_GOVERNANCE_STATE_SNAPSHOT",
            "Governance state snapshot surfaces payload is missing or invalid",
            allowed_surfaces,
        )

    expected_snapshot = build_governance_state_snapshot_payload(None)
    if snapshot_payload["surfaces"] != expected_snapshot["surfaces"] or snapshot_payload["snapshot_id"] != expected_snapshot["snapshot_id"]:
        raise GovernanceInputError(
            "GOVERNANCE_STATE_SNAPSHOT_MISMATCH",
            "Governance state snapshot does not match current canonical governance surfaces",
            allowed_surfaces,
        )

    if snapshot_payload["drift_detected"]:
        raise GovernanceInputError(
            "GOVERNANCE_STATE_SNAPSHOT_DRIFT_DETECTED",
            "Governance state snapshot is marked drifted and cannot authorize current-state answers",
            allowed_surfaces,
        )


def detect_ambiguous_governance_surface_candidates() -> list[Path]:
    candidates: list[Path] = []
    for canonical_path in allowed_next_action_surfaces():
        stem = canonical_path.stem
        for suffix in AMBIGUOUS_SUFFIXES:
            pattern = f"{stem}{suffix}.json"
            for candidate in REPO_ROOT.rglob(pattern):
                if candidate != canonical_path and ".git" not in candidate.parts and "__pycache__" not in candidate.parts:
                    candidates.append(candidate)
    return sorted(candidates)


def validate_governance_target_consensus(
    roadmap_payload: dict[str, object],
    remediation_payload: dict[str, object],
    gap_payload: dict[str, object],
    maturity_payload: dict[str, object],
    allowed_surfaces: list[str],
) -> None:
    target = roadmap_payload.get("recommended_next_target")
    if not target:
        raise GovernanceInputError(
            "UNRESOLVED_ROADMAP_RECOMMENDED_NEXT_TARGET",
            "recommended_next_target could not be resolved against the remediation plan",
            allowed_surfaces,
        )

    remediation_plan = remediation_payload.get("remediation_plan", [])
    if not remediation_plan:
        raise GovernanceInputError(
            "GOVERNANCE_STATE_SURFACE_INCONSISTENCY",
            "Canonical remediation plan is empty and cannot resolve recommended next target",
            allowed_surfaces,
        )

    first_remediation_domain = remediation_plan[0].get("domain")
    first_blocker_domain = None
    blockers = roadmap_payload.get("blockers_to_full_maturity", [])
    if blockers:
        first_blocker_domain = blockers[0]

    if target != first_remediation_domain or (first_blocker_domain is not None and target != first_blocker_domain):
        raise GovernanceInputError(
            "GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION",
            "Canonical governance surfaces disagree on recommended next target.",
            allowed_surfaces,
        )

    remediation_entry = next((entry for entry in remediation_plan if entry.get("domain") == target), None)
    gap_entry = next((entry for entry in gap_payload.get("detected_gaps", []) if entry.get("domain") == target), None)
    maturity_classification = maturity_payload.get("domain_classifications", {}).get(target)

    if remediation_entry is None or gap_entry is None or maturity_classification is None:
        raise GovernanceInputError(
            "GOVERNANCE_STATE_SURFACE_INCONSISTENCY",
            "Canonical governance surfaces are inconsistent for the roadmap recommended_next_target",
            allowed_surfaces,
        )

    if target in roadmap_payload.get("current_maturity_snapshot", {}).get("verified_domains", []):
        raise GovernanceInputError(
            "GOVERNANCE_STATE_SURFACE_INCONSISTENCY",
            "recommended_next_target is already marked VERIFIED in the roadmap snapshot",
            allowed_surfaces,
        )

    if remediation_entry.get("current_status") != maturity_classification:
        raise GovernanceInputError(
            "GOVERNANCE_STATE_SURFACE_INCONSISTENCY",
            "Canonical governance surfaces are inconsistent for the roadmap recommended_next_target",
            allowed_surfaces,
        )

    if gap_entry.get("classification") != maturity_classification:
        raise GovernanceInputError(
            "GOVERNANCE_STATE_SURFACE_INCONSISTENCY",
            "Canonical governance surfaces are inconsistent for the roadmap recommended_next_target",
            allowed_surfaces,
        )


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


def build_gap_payload() -> dict[str, object]:
    state_payload, issues = build_state_payload()
    if issues:
        return {
            "overall_gap_state": "BLOCKED_BY_DRIFT",
            "detected_gaps": [
                {
                    "gap_id": "governance-state-drift-detected",
                    "domain": "governance_system_state",
                    "classification": "BLOCKED_BY_DRIFT",
                    "severity": "critical",
                    "reason": "Self-inspection detected inconsistencies across canonical governance surfaces",
                    "evidence_sources": [
                        "docs/governance/governance-system-state.json",
                        "docs/governance/governance-capability-registry.md",
                        "docs/governance/governance-capability-progress.md",
                        "docs/governance/governance-capability-execution-map.md",
                    ],
                    "blocking_effect": "prevents trustworthy governance-system gap analysis",
                    "recommended_remediation_type": "state-alignment-verification",
                    "recommended_pipeline_candidates": [],
                }
            ],
            "sources": [
                "docs/governance/governance-system-state.json",
                "docs/governance/governance-system-maturity.json",
                "docs/governance/governance-capability-registry.md",
                "docs/pipelines/registry/pipeline-registry.md",
            ],
        }

    maturity_payload = build_maturity_payload()
    detected_gaps: list[dict[str, object]] = []
    severity_by_classification = {
        "INVALID_STATE": "high",
        "UNVERIFIED": "medium",
        "PARTIAL": "medium",
    }

    for domain, classification in maturity_payload["domain_classifications"].items():
        if classification == "VERIFIED":
            continue

        remediation = DOMAIN_REMEDIATION_MAP.get(domain, {"type": "unknown", "pipelines": []})
        if classification == "INVALID_STATE":
            reason = "Domain expected by maturity model but absent from capability registry"
        elif classification == "UNVERIFIED":
            reason = "Domain capability is declared but not yet complete in canonical governance state"
        else:
            reason = "Domain capability coverage is only partially complete in canonical governance state"

        detected_gaps.append(
            {
                "gap_id": f"{domain}-{classification.lower().replace('_', '-')}",
                "domain": domain,
                "classification": classification,
                "severity": severity_by_classification.get(classification, "low"),
                "reason": reason,
                "evidence_sources": [
                    "docs/governance/governance-system-maturity.json",
                    "docs/governance/governance-system-state.json",
                    "docs/governance/governance-capability-registry.md",
                ],
                "blocking_effect": "prevents full governance-system maturity",
                "recommended_remediation_type": remediation["type"],
                "recommended_pipeline_candidates": remediation["pipelines"],
            }
        )

    return {
        "overall_gap_state": "GAPS_PRESENT" if detected_gaps else "NO_GAPS_DETECTED",
        "detected_gaps": detected_gaps,
        "sources": [
            "docs/governance/governance-system-state.json",
            "docs/governance/governance-system-maturity.json",
            "docs/governance/governance-capability-registry.md",
            "docs/pipelines/registry/pipeline-registry.md",
        ],
        "current_governance_maturity_reference": state_payload["governance_maturity_estimate"],
        "overall_system_maturity": maturity_payload["overall_maturity"],
    }


def build_remediation_plan_payload() -> dict[str, object]:
    gap_payload = build_gap_payload()
    if gap_payload["overall_gap_state"] == "BLOCKED_BY_DRIFT":
        raise ValueError("Cannot build remediation plan from inconsistent governance state")

    entries: list[dict[str, object]] = []
    sort_order = {"INVALID_STATE": 0, "BLOCKED_BY_DRIFT": 1, "UNVERIFIED": 2, "PARTIAL": 3}

    sorted_gaps = sorted(
        gap_payload["detected_gaps"],
        key=lambda gap: (
            sort_order.get(gap["classification"], 9),
            gap["domain"],
        ),
    )

    for index, gap in enumerate(sorted_gaps, start=1):
        classification = gap["classification"]
        domain = gap["domain"]
        remediation = DOMAIN_REMEDIATION_MAP.get(domain, {"type": "unknown", "pipelines": []})

        if classification == "INVALID_STATE":
            required_evidence = [
                "capability registry declaration aligned to the maturity domain",
                "canonical capability tracking evidence",
            ]
            recommended_action = f"normalize {domain} registry and capability state"
        elif classification == "UNVERIFIED":
            required_evidence = [
                "established governance capability surface",
                "verification evidence proving completed capability coverage",
            ]
            recommended_action = f"complete and verify {domain}"
        else:
            required_evidence = [
                "additional verification evidence",
                "canonical completion signals for partially covered domain capabilities",
            ]
            recommended_action = f"close remaining verification gaps for {domain}"

        suggested_pipeline = remediation["pipelines"][0] if remediation["pipelines"] else "unknown"
        entries.append(
            {
                "domain": domain,
                "current_status": classification,
                "remediation_strategy": REMEDIATION_STRATEGY_MAP.get(classification, "evidence_gap"),
                "required_evidence": required_evidence,
                "recommended_action": recommended_action,
                "suggested_pipeline": suggested_pipeline,
                "priority": REMEDIATION_PRIORITY_MAP.get(classification, "LOW"),
                "dependency_order": index,
                "promotion_target": "VERIFIED",
            }
        )

    return {
        "generated_by": "inspect_governance_state.py",
        "planner_version": "1.0",
        "remediation_plan": entries,
        "sources": [
            "docs/governance/governance-system-gaps.json",
            "docs/governance/governance-system-maturity.json",
        ],
    }


def build_advancement_roadmap_payload() -> dict[str, object]:
    maturity_payload = build_maturity_payload()
    remediation_payload = build_remediation_plan_payload()

    classifications = maturity_payload["domain_classifications"]
    verified_domains = sorted([domain for domain, status in classifications.items() if status == "VERIFIED"])
    unverified_domains = sorted([domain for domain, status in classifications.items() if status == "UNVERIFIED"])
    invalid_domains = sorted([domain for domain, status in classifications.items() if status == "INVALID_STATE"])

    stages: list[dict[str, object]] = []
    current_focus: str | None = None
    current_targets: list[str] = []
    stage_number = 0

    for entry in remediation_payload["remediation_plan"]:
        focus = ROADMAP_FOCUS_MAP.get(entry["remediation_strategy"], "capability_expansion")
        if focus != current_focus:
            if current_focus is not None:
                stages.append(
                    {
                        "stage": stage_number,
                        "focus": current_focus,
                        "targets": current_targets,
                    }
                )
            stage_number += 1
            current_focus = focus
            current_targets = []
        current_targets.append(entry["domain"])

    if current_focus is not None:
        stages.append(
            {
                "stage": stage_number,
                "focus": current_focus,
                "targets": current_targets,
            }
        )

    blockers = [entry["domain"] for entry in remediation_payload["remediation_plan"]]
    recommended_next_target = blockers[0] if blockers else None

    return {
        "generated_by": "inspect_governance_state.py",
        "roadmap_version": "1.0",
        "current_maturity_snapshot": {
            "verified_domains": verified_domains,
            "unverified_domains": unverified_domains,
            "invalid_domains": invalid_domains,
        },
        "advancement_stages": stages,
        "blockers_to_full_maturity": blockers,
        "recommended_next_target": recommended_next_target,
        "sources": [
            "docs/governance/governance-system-maturity.json",
            "docs/governance/governance-system-gaps.json",
            "docs/governance/governance-system-gap-remediation-plan.json",
        ],
    }


def build_next_action_payload() -> dict[str, object]:
    validate_canonical_input_authority()

    snapshot_payload = read_json(STATE_SNAPSHOT_JSON)
    roadmap_payload = read_json(SYSTEM_ADVANCEMENT_ROADMAP_JSON)
    remediation_payload = read_json(SYSTEM_GAP_REMEDIATION_PLAN_JSON)
    gap_payload = read_json(SYSTEM_GAPS_JSON)
    maturity_payload = read_json(SYSTEM_MATURITY_JSON)

    target = roadmap_payload["recommended_next_target"]
    if not target:
        raise ValueError("No recommended next target available from advancement roadmap")

    if target not in DOMAIN_CAPABILITY_MAP:
        raise ValueError("recommended_next_target is not a recognized governance domain")

    remediation_entry = next(
        (entry for entry in remediation_payload["remediation_plan"] if entry["domain"] == target),
        None,
    )
    if remediation_entry is None:
        raise ValueError("Roadmap recommended_next_target is not present in remediation plan")

    gap_entry = next((entry for entry in gap_payload["detected_gaps"] if entry["domain"] == target), None)
    if gap_entry is None:
        raise ValueError("Roadmap recommended_next_target is not present in detected gaps")

    maturity_classification = maturity_payload["domain_classifications"].get(target)
    if maturity_classification is None:
        raise ValueError("recommended_next_target has no maturity classification")
    if maturity_classification == "VERIFIED":
        raise ValueError("recommended_next_target is already VERIFIED")
    if remediation_entry["current_status"] != maturity_classification:
        raise ValueError("recommended_next_target classification does not match remediation plan")
    if gap_entry["classification"] != maturity_classification:
        raise ValueError("recommended_next_target classification does not match detected gaps")

    status = remediation_entry["current_status"]
    if status == "INVALID_STATE":
        reason = "INVALID_STATE governance domain must be normalized before other capability advancement"
    elif status == "UNVERIFIED":
        reason = "first unresolved UNVERIFIED domain in the ordered remediation plan"
    else:
        reason = "first unresolved domain in the ordered remediation plan"

    return {
        "generated_by": "inspect_governance_state.py",
        "selector_version": "1.0",
        "required_snapshot_input": "docs/governance/governance-state-snapshot.json",
        "snapshot_id": snapshot_payload["snapshot_id"],
        "snapshot_drift_detected": snapshot_payload["drift_detected"],
        "governance_state_consensus": True,
        "recommended_action_type": ACTION_TYPE_MAP.get(
            remediation_entry["remediation_strategy"],
            "capability_establishment",
        ),
        "target_domain": target,
        "reason": reason,
        "derived_from": "docs/governance/governance-system-advancement-roadmap.json",
        "current_status": remediation_entry["current_status"],
        "suggested_pipeline": remediation_entry["suggested_pipeline"],
    }


def build_authoritative_governance_state_answer_payload() -> dict[str, object]:
    validate_canonical_input_authority()

    snapshot_payload = read_json(STATE_SNAPSHOT_JSON)
    state_payload = read_json(STATE_JSON)
    maturity_payload = read_json(SYSTEM_MATURITY_JSON)
    gap_payload = read_json(SYSTEM_GAPS_JSON)
    roadmap_payload = read_json(SYSTEM_ADVANCEMENT_ROADMAP_JSON)
    next_action_payload = build_next_action_payload()

    active_stage = None
    advancement_stages = roadmap_payload.get("advancement_stages", [])
    if advancement_stages:
        active_stage = advancement_stages[0]

    return {
        "generated_by": "inspect_governance_state.py",
        "answer_version": "1.0",
        "control_plane_version": "1.0",
        "control_plane_surface_role": "canonical_governance_control_plane",
        "required_snapshot_input": "docs/governance/governance-state-snapshot.json",
        "snapshot_id": snapshot_payload["snapshot_id"],
        "snapshot_drift_detected": snapshot_payload["drift_detected"],
        "governance_state_consensus": True,
        "governance_maturity": {
            "overall_system_maturity": maturity_payload["overall_maturity"],
            "governance_maturity_reference": maturity_payload["current_governance_maturity_reference"],
        },
        "governance_blockers": roadmap_payload["blockers_to_full_maturity"],
        "governance_progression_stage": active_stage,
        "governance_gap_state": gap_payload["overall_gap_state"],
        "governance_trend_classification": state_payload["trend_classification"],
        "authoritative_next_action": next_action_payload,
        "recommended_next_action": next_action_payload,
        "sources": [
            "docs/governance/governance-state-snapshot.json",
            "docs/governance/governance-system-state.json",
            "docs/governance/governance-system-maturity.json",
            "docs/governance/governance-system-gaps.json",
            "docs/governance/governance-system-advancement-roadmap.json",
            "docs/governance/governance-system-next-action.json",
        ],
    }


def validate_canonical_input_authority() -> None:
    allowed_surfaces = allowed_next_action_surface_strings()

    ambiguous_candidates = detect_ambiguous_governance_surface_candidates()
    if ambiguous_candidates:
        raise GovernanceInputError(
            "AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED",
            f"Ambiguous governance surface candidate detected: {ambiguous_candidates[0].relative_to(REPO_ROOT)}",
            allowed_surfaces,
        )

    for path in allowed_next_action_surfaces():
        if not path.exists():
            raise GovernanceInputError(
                "MISSING_CANONICAL_GOVERNANCE_SURFACE",
                f"Required canonical governance surface is missing: {path.relative_to(REPO_ROOT)}",
                allowed_surfaces,
            )
        if path.parent != DOCS:
            raise GovernanceInputError(
                "NON_CANONICAL_GOVERNANCE_INPUT_SOURCE",
                f"Non-canonical governance input source configured: {path}",
                allowed_surfaces,
            )

        shadow_candidates = [
            candidate
            for candidate in REPO_ROOT.rglob(path.name)
            if candidate != path and ".git" not in candidate.parts and "__pycache__" not in candidate.parts
        ]
        if shadow_candidates:
            raise GovernanceInputError(
                "SHADOW_GOVERNANCE_SURFACE_DETECTED",
                f"Shadow governance surface detected for {path.name}: {shadow_candidates[0].relative_to(REPO_ROOT)}",
                allowed_surfaces,
            )

    snapshot_payload = read_json(STATE_SNAPSHOT_JSON)
    validate_required_governance_snapshot(snapshot_payload, allowed_surfaces)

    roadmap_payload = read_json(SYSTEM_ADVANCEMENT_ROADMAP_JSON)
    remediation_payload = read_json(SYSTEM_GAP_REMEDIATION_PLAN_JSON)
    gap_payload = read_json(SYSTEM_GAPS_JSON)
    maturity_payload = read_json(SYSTEM_MATURITY_JSON)
    validate_governance_target_consensus(
        roadmap_payload,
        remediation_payload,
        gap_payload,
        maturity_payload,
        allowed_surfaces,
    )


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


def run_gap_analysis() -> int:
    payload = build_gap_payload()
    SYSTEM_GAPS_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Regenerated {SYSTEM_GAPS_JSON.relative_to(REPO_ROOT)}")
    return 0


def run_remediation_plan() -> int:
    payload = build_remediation_plan_payload()
    SYSTEM_GAP_REMEDIATION_PLAN_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Regenerated {SYSTEM_GAP_REMEDIATION_PLAN_JSON.relative_to(REPO_ROOT)}")
    return 0


def run_advancement_roadmap() -> int:
    payload = build_advancement_roadmap_payload()
    SYSTEM_ADVANCEMENT_ROADMAP_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Regenerated {SYSTEM_ADVANCEMENT_ROADMAP_JSON.relative_to(REPO_ROOT)}")
    return 0


def run_next_action_selector() -> int:
    try:
        payload = build_next_action_payload()
    except GovernanceInputError as exc:
        print(json.dumps(exc.to_payload(), indent=2), file=sys.stderr)
        return 1
    except ValueError:
        error_payload = {
            "status": "error",
            "error_code": "UNRESOLVED_ROADMAP_RECOMMENDED_NEXT_TARGET",
            "message": "recommended_next_target could not be resolved against the remediation plan",
            "allowed_surfaces": allowed_next_action_surface_strings(),
        }
        print(json.dumps(error_payload, indent=2), file=sys.stderr)
        return 1

    SYSTEM_NEXT_ACTION_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Regenerated {SYSTEM_NEXT_ACTION_JSON.relative_to(REPO_ROOT)}")
    return 0


def run_authoritative_state_answer() -> int:
    try:
        payload = build_authoritative_governance_state_answer_payload()
    except GovernanceInputError as exc:
        print(json.dumps(exc.to_payload(), indent=2), file=sys.stderr)
        return 1
    except ValueError:
        error_payload = {
            "status": "error",
            "error_code": "UNRESOLVED_AUTHORITATIVE_GOVERNANCE_STATE",
            "message": "authoritative governance state answer could not be resolved from the required snapshot-backed inputs",
            "allowed_surfaces": allowed_next_action_surface_strings(),
        }
        print(json.dumps(error_payload, indent=2), file=sys.stderr)
        return 1

    AUTHORITATIVE_STATE_ANSWER_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Regenerated {AUTHORITATIVE_STATE_ANSWER_JSON.relative_to(REPO_ROOT)}")
    return 0


def run_snapshot_generation() -> int:
    previous_snapshot = read_json(STATE_SNAPSHOT_JSON) if STATE_SNAPSHOT_JSON.exists() else None
    payload = build_governance_state_snapshot_payload(previous_snapshot)
    STATE_SNAPSHOT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Regenerated {STATE_SNAPSHOT_JSON.relative_to(REPO_ROOT)}")
    return 0


def main() -> int:
    if len(sys.argv) == 1:
        return run_state_inspection()

    if len(sys.argv) == 2 and sys.argv[1] == "maturity":
        return run_maturity_scoring()

    if len(sys.argv) == 2 and sys.argv[1] == "gaps":
        return run_gap_analysis()

    if len(sys.argv) == 2 and sys.argv[1] == "remediation-plan":
        return run_remediation_plan()

    if len(sys.argv) == 2 and sys.argv[1] == "advancement-roadmap":
        return run_advancement_roadmap()

    if len(sys.argv) == 2 and sys.argv[1] == "snapshot":
        return run_snapshot_generation()

    if len(sys.argv) == 2 and sys.argv[1] == "next-action":
        return run_next_action_selector()

    if len(sys.argv) == 2 and sys.argv[1] == "authoritative-state":
        return run_authoritative_state_answer()

    print(
        "Usage: python tools/governance/inspect_governance_state.py [maturity|gaps|remediation-plan|advancement-roadmap|snapshot|next-action|authoritative-state]",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
