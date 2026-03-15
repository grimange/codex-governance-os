from __future__ import annotations

from .models import ContinuityChain, ScenarioDefinition


def build_chain(scenario: ScenarioDefinition) -> ContinuityChain:
    evidence_types = tuple(_classify_evidence_type(item) for item in scenario.evidence)
    explicit_evidence_count = sum(1 for item in evidence_types if item != "unknown")
    invalid_patterns = " ".join(scenario.invalid_reasoning_patterns).lower()
    has_boundary_violation = any(
        phrase in invalid_patterns
        for phrase in (
            "event merging",
            "cross-session event merging",
            "attempted cross-session event merging",
            "illegal bleed across boundaries",
        )
    )
    is_ambiguous = any("ambiguous" in item.lower() for item in scenario.boundary_conditions + scenario.invalid_reasoning_patterns)
    is_incomplete = len(scenario.sessions) < 2 or (
        bool(scenario.evidence) and explicit_evidence_count == 0
    )
    return ContinuityChain(
        scenario=scenario,
        evidence_types=evidence_types,
        explicit_evidence_count=explicit_evidence_count,
        has_boundary_violation=has_boundary_violation,
        is_ambiguous=is_ambiguous,
        is_incomplete=is_incomplete,
    )


def _classify_evidence_type(evidence: str) -> str:
    normalized = evidence.lower()
    if "predecessor-successor" in normalized or "predecessor" in normalized:
        return "explicit_session_predecessor_reference"
    if "artifact continuation" in normalized or "governed artifact continuation" in normalized:
        return "governance_artifact_continuation"
    if "artifact chain" in normalized:
        return "artifact_chain_evidence"
    if "continuation_of_session" in normalized or "continuation marker" in normalized:
        return "canonical_continuation_marker"
    return "unknown"
