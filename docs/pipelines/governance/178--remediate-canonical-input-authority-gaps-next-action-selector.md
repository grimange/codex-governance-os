# 178 --- Remediate Remaining Canonical Input Authority Gaps in Governance System Next-Action Selector

``` yaml
pipeline_id: 178
registry_id: governance.system.remediate-canonical-input-authority-gaps-next-action-selector
title: Remediate Remaining Canonical Input Authority Gaps in Governance System Next-Action Selector
stage: remediation
governance_layer: Autonomous Governance Loop
classification: GOVERNANCE_REMEDIATION
status: IMPLEMENTATION_REQUIRED
created_by: codex-governance-os
objective: >
  Remediate the remaining canonical input authority enforcement gaps discovered
  in Pipeline 177 by enforcing cross-surface target consensus and rejecting
  ambiguous or alternate-named governance surface candidates during
  next-action selector execution.
```

------------------------------------------------------------------------

# 01 --- Problem Statement

Pipeline **177** verified canonical input authority enforcement for the
governance next-action selector.

Two critical authority gaps were discovered:

1.  Cross-surface inconsistency was still accepted when the roadmap
    target was changed to another internally known but lower-priority
    domain.
2.  Alternate-named duplicate candidate governance surfaces were not
    rejected.

These gaps allow ambiguous or inconsistent governance state to influence
selector decisions.

------------------------------------------------------------------------

# 02 --- Remediation Scope

Remediation targets the selector implementation in:

    tools/governance/inspect_governance_state.py

Functions to add or harden:

    validate_canonical_input_authority()
    validate_governance_target_consensus()
    detect_ambiguous_governance_surface_candidates()

------------------------------------------------------------------------

# 03 --- Cross-Surface Target Consensus Enforcement

The selector must require **exact consensus** across the following
canonical governance surfaces:

    governance-roadmap.json
    governance-remediation-plan.json
    governance-gap-analysis.json
    governance-maturity-scoring.json

If any surface contains a different target, the selector must fail
closed.

Required error:

    error_code: GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION

------------------------------------------------------------------------

# 04 --- Ambiguous Governance Surface Candidate Detection

The selector must reject alternate-named governance surfaces such as:

    *-copy.json
    *-backup.json
    *-old.json
    *-temp.json
    *-draft.json

Example:

    governance-system-advancement-roadmap-copy.json

Required error:

    error_code: AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED

------------------------------------------------------------------------

# 05 --- Duplicate Surface Detection Scope

Canonical surfaces:

    governance-system-state.json
    governance-roadmap.json
    governance-gap-analysis.json
    governance-maturity-scoring.json
    governance-remediation-plan.json

Detection patterns:

    governance-roadmap*.json
    governance-gap-analysis*.json
    governance-remediation-plan*.json

If more than one candidate exists → FAIL CLOSED.

------------------------------------------------------------------------

# 06 --- Selector Execution Safeguards

When violations occur:

    GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION
    AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED

The selector must:

    exit non-zero
    emit machine-readable error
    abort resolution

It must **not modify**:

    governance-system-next-action.json

------------------------------------------------------------------------

# 07 --- Machine-Readable Error Payload

Example:

``` json
{
  "status": "error",
  "error_code": "GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION",
  "message": "Canonical governance surfaces disagree on recommended next target."
}
```

------------------------------------------------------------------------

# 08 --- Regression Coverage

Extend tests in:

    tests/governance/test_governance_system_next_action.py

Test cases:

A --- Target consensus violation

    roadmap target != remediation target

Expected:

    exit non-zero
    error_code: GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION

B --- Ambiguous surface candidate

Inject:

    governance-roadmap-copy.json

Expected:

    exit non-zero
    error_code: AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED

------------------------------------------------------------------------

# 09 --- Evidence Artifact Bundle

Create:

    docs/pipelines/governance/
    remediate-canonical-input-authority-gaps-next-action-selector/

Required artifacts:

    01-problem-statement.md
    02-authority-gap-analysis.md
    03-remediation-design.md
    04-implementation-summary.md
    05-regression-test-additions.md
    06-verification-plan.md
    07-final-verdict.md

------------------------------------------------------------------------

# 10 --- Acceptance Criteria

Pipeline 178 is complete when:

-   selector fails closed on cross-surface target disagreement
-   selector rejects alternate-named candidate governance surfaces
-   selector emits structured machine-readable error payloads
-   selector preserves deterministic behavior under valid state
-   selector does not rewrite next-action output when authority
    validation fails
-   regression tests covering both failure cases pass

------------------------------------------------------------------------

# 11 --- Expected Final Verdict

    CANONICAL_INPUT_AUTHORITY_GAPS_REMEDIATED_FOR_GOVERNANCE_NEXT_ACTION_SELECTOR

------------------------------------------------------------------------

# 12 --- Next Recommended Pipeline

    179 — Verify Remediation of Canonical Input Authority Gaps in Governance System Next-Action Selector
