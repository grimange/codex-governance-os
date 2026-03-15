from __future__ import annotations

from .models import ContinuityChain, EvaluationResult


def classify_chain(chain: ContinuityChain) -> EvaluationResult:
    scenario = chain.scenario
    classification: str | None = None
    failure_classification: str | None = None
    verdict = "AMBIGUOUS_CONTINUITY_STATE"

    if chain.has_boundary_violation and not scenario.evidence:
        failure_classification = "SESSION_BOUNDARY_VIOLATION"
        verdict = "SESSION_ISOLATION_VIOLATION"
    elif not scenario.evidence:
        classification = "NO_CONTINUITY"
        verdict = "MISSING_BRIDGE_EVIDENCE"
    elif chain.is_incomplete:
        verdict = "INCOMPLETE_SESSION_RECONSTRUCTION"
    elif chain.is_ambiguous:
        failure_classification = "AMBIGUOUS_SESSION_CONTINUITY"
        verdict = "AMBIGUOUS_CONTINUITY_STATE"
    elif _is_verified_chain(chain):
        classification = "VERIFIED_CONTINUITY"
        verdict = "VALID_CONTINUITY_CHAIN"
    elif chain.explicit_evidence_count >= 1:
        classification = "WEAK_CONTINUITY"
        verdict = "INCOMPLETE_SESSION_RECONSTRUCTION"
    else:
        failure_classification = "CONTINUITY_CLAIM_WITHOUT_EVIDENCE"
        verdict = "MISSING_BRIDGE_EVIDENCE"

    matched_expectation = (
        classification == scenario.expected_classification
        and failure_classification == scenario.expected_failure_classification
    )
    return EvaluationResult(
        scenario_id=scenario.scenario_id,
        source_path=scenario.source_path,
        sessions=scenario.sessions,
        evidence=scenario.evidence,
        evidence_types=chain.evidence_types,
        classification=classification,
        failure_classification=failure_classification,
        verdict=verdict,
        expected_classification=scenario.expected_classification,
        expected_failure_classification=scenario.expected_failure_classification,
        matched_expectation=matched_expectation,
    )


def _is_verified_chain(chain: ContinuityChain) -> bool:
    evidence_types = set(chain.evidence_types)
    return (
        "explicit_session_predecessor_reference" in evidence_types
        and "governance_artifact_continuation" in evidence_types
        and len(chain.scenario.sessions) >= 2
    )
