# 179 --- Verify Remediation of Canonical Input Authority Gaps in Governance System Next-Action Selector

``` yaml
pipeline_id: 179
registry_id: governance.system.verify-remediation-canonical-input-authority-gaps-next-action-selector
title: Verify Remediation of Canonical Input Authority Gaps in Governance System Next-Action Selector
stage: verification
governance_layer: Autonomous Governance Loop
classification: GOVERNANCE_VERIFICATION
status: IMPLEMENTATION_REQUIRED
created_by: codex-governance-os
objective: >
  Verify that the remediation implemented in Pipeline 178 correctly closes
  the canonical input authority gaps discovered in Pipeline 177 by enforcing
  cross-surface target consensus and rejecting ambiguous governance surface
  candidates during next-action selector execution.
```

------------------------------------------------------------------------

# 01 --- Problem Statement

Pipeline **177** exposed two canonical input authority defects in the
governance next-action selector:

1.  Cross-surface governance target disagreement was accepted when the
    roadmap target changed to another internally known domain.
2.  Alternate-named duplicate governance surfaces were not rejected.

Pipeline **178** implemented remediation for these issues.

Governance safety doctrine requires remediation to be **verified with
evidence** before the system is considered secure.

Pipeline **179** verifies that the previously failing scenarios now
correctly trigger fail-closed behavior.

------------------------------------------------------------------------

# 02 --- Verification Scope

The verification targets the selector logic in:

    tools/governance/inspect_governance_state.py

Validation routines:

    validate_governance_target_consensus()
    detect_ambiguous_governance_surface_candidates()
    validate_canonical_input_authority()

------------------------------------------------------------------------

# 03 --- Canonical Governance Surfaces

Canonical surfaces:

    governance-system-state.json
    governance-roadmap.json
    governance-gap-analysis.json
    governance-maturity-scoring.json
    governance-remediation-plan.json

Selector output:

    governance-system-next-action.json

------------------------------------------------------------------------

# 04 --- Verification Scenario Matrix

## Scenario 1 --- Valid Canonical Governance State

Expected:

    selector exits 0
    next-action surface generated
    output deterministic

Verification:

    run selector twice
    hash governance-system-next-action.json
    hashes must match

------------------------------------------------------------------------

## Scenario 2 --- Cross-Surface Target Consensus Violation

Example change:

    governance-roadmap.json
    recommended_next_target = architecture_advisor

Expected:

    exit code != 0
    error_code: GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION

Selector must abort and not rewrite output.

------------------------------------------------------------------------

## Scenario 3 --- Alternate-Named Governance Surface Candidate

Inject:

    governance-roadmap-copy.json

Expected:

    exit code != 0
    error_code: AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED

------------------------------------------------------------------------

## Scenario 4 --- Alternate Pattern Variants

Inject:

    governance-roadmap-backup.json
    governance-roadmap-old.json
    governance-roadmap-draft.json

Expected:

    exit code != 0
    error_code: AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED

------------------------------------------------------------------------

# 05 --- Output Protection Verification

Procedure:

    record hash of governance-system-next-action.json
    trigger failure scenario
    recompute hash

Expected:

    hash_before == hash_after

------------------------------------------------------------------------

# 06 --- Deterministic Behavior Verification

Run selector twice:

    python tools/governance/inspect_governance_state.py

Hash output:

    sha256 governance-system-next-action.json

Expected:

    hash1 == hash2

------------------------------------------------------------------------

# 07 --- Regression Test Execution

Run tests:

    python -m unittest discover -s tests/governance -p "test_*.py"

Expected:

    All tests pass

------------------------------------------------------------------------

# 08 --- Evidence Artifact Bundle

Directory:

    docs/pipelines/governance/
    verify-remediation-canonical-input-authority-gaps-next-action-selector/

Artifacts:

    01-problem-statement.md
    02-verification-scope.md
    03-scenario-matrix.md
    04-execution-log.md
    05-consensus-verification.md
    06-duplicate-surface-detection.md
    07-regression-test-results.md
    08-output-protection-check.md
    09-final-verdict.md

------------------------------------------------------------------------

# 09 --- Acceptance Criteria

Pipeline 179 completes when:

-   cross-surface disagreement fails closed
-   duplicate governance surfaces fail closed
-   correct machine-readable errors emitted
-   selector output deterministic under valid state
-   next-action output protected during failure
-   governance regression suite passes

------------------------------------------------------------------------

# 10 --- Expected Final Verdict

    CANONICAL_INPUT_AUTHORITY_REMEDIATION_VERIFIED_FOR_GOVERNANCE_NEXT_ACTION_SELECTOR

------------------------------------------------------------------------

# 11 --- Next Recommended Pipeline

    180 — Establish Governance State Snapshot Integrity Verification
