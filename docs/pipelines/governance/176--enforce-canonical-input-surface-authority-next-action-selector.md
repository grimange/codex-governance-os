# 176 --- Enforce Canonical Input Surface Authority for Governance System Next-Action Selection

``` yaml
pipeline_id: 176
registry_id: governance.system.enforce-canonical-input-surface-authority-next-action-selector
title: Enforce Canonical Input Surface Authority for Governance System Next-Action Selection
stage: hardening
governance_layer: Autonomous Governance Loop
classification: SAFETY_ENFORCEMENT
status: IMPLEMENTATION_REQUIRED
created_by: codex-governance-os
objective: >
  Ensure the governance system next-action selector resolves exclusively from
  declared canonical governance surfaces and fails closed when non-canonical,
  shadow, stale, or inconsistent input sources are detected.
```

------------------------------------------------------------------------

# 01 --- Problem Statement

Pipeline **174--175** established and verified **fail-closed roadmap
resolution** for the governance system next-action selector.

However, a remaining risk exists:

The selector could potentially resolve governance decisions from
**non-canonical or stale inputs**.

Examples include:

-   shadow copies of governance state
-   stale artifacts
-   partially updated governance surfaces
-   duplicated governance files in alternative locations
-   mixed-source state resolution

If allowed, these situations could lead to **incorrect governance
decisions** despite the selector itself behaving correctly.

Therefore the system must enforce **canonical input authority**.

The next-action selector must only trust the **approved canonical
governance surfaces**.

Any deviation must trigger a **fail-closed error**.

------------------------------------------------------------------------

# 02 --- Canonical Governance Surfaces

The next-action selector is allowed to resolve state **only from these
canonical surfaces**:

### Governance State

    governance-system-state.json

### Governance Roadmap

    governance-roadmap.json

### Governance Gap Analysis

    governance-gap-analysis.json

### Governance Maturity Surface

    governance-maturity-scoring.json

### Governance Remediation Plan

    governance-remediation-plan.json

### Selector Output

    governance-system-next-action.json

These files together represent the **canonical governance state
surfaces**.

------------------------------------------------------------------------

# 03 --- Canonical Input Authority Contract

The next-action selector must enforce the following rules.

### Rule 1 --- Canonical Path Enforcement

Only the canonical paths defined in Section 02 may be read.

Any attempt to resolve state from:

    /tmp
    build/
    artifacts/
    old/
    backup/
    shadow copies

must fail closed.

------------------------------------------------------------------------

### Rule 2 --- No Shadow Surfaces

If duplicate governance state files exist outside the canonical paths,
the selector must **ignore them completely**.

If a shadow file attempts to override canonical state, the selector must
fail closed.

------------------------------------------------------------------------

### Rule 3 --- Cross-Surface Consistency

The selector must verify that:

    roadmap
    gap analysis
    maturity scoring
    remediation plan

describe **consistent governance targets**.

If cross-surface mismatch occurs:

    FAIL CLOSED

------------------------------------------------------------------------

### Rule 4 --- Atomic State Requirement

All canonical surfaces must exist and be readable.

If any required surface is missing:

    FAIL CLOSED

------------------------------------------------------------------------

### Rule 5 --- Deterministic Input Resolution

The selector must read **only one authoritative version** of each
canonical surface.

Multiple candidate sources must not be merged or inferred.

------------------------------------------------------------------------

### Rule 6 --- No Silent State Mutation

The selector must not modify canonical governance surfaces during input
validation.

It may only write:

    governance-system-next-action.json

and only when validation passes.

------------------------------------------------------------------------

# 04 --- Fail-Closed Conditions

The selector must exit non-zero when any authority violation occurs.

Examples:

### Missing Canonical Surface

    error_code: MISSING_CANONICAL_GOVERNANCE_SURFACE

### Shadow State Detected

    error_code: SHADOW_GOVERNANCE_SURFACE_DETECTED

### Non-Canonical Path Access

    error_code: NON_CANONICAL_GOVERNANCE_INPUT_SOURCE

### Cross-Surface Mismatch

    error_code: GOVERNANCE_STATE_SURFACE_INCONSISTENCY

### Multiple Candidate Inputs

    error_code: MULTIPLE_GOVERNANCE_SURFACE_CANDIDATES

------------------------------------------------------------------------

# 05 --- Required Implementation

The following component must be updated:

    tools/governance/inspect_governance_state.py

Add a new validation function:

    validate_canonical_input_authority()

Responsibilities:

-   enforce canonical path allowlist
-   verify required surfaces exist
-   detect shadow surfaces
-   verify cross-surface consistency
-   block selector output when validation fails

------------------------------------------------------------------------

# 06 --- Output Protection Rule

When canonical input authority validation fails:

    governance-system-next-action.json

must **NOT be written or modified**.

The selector must terminate before resolution.

------------------------------------------------------------------------

# 07 --- Machine-Readable Error Payload

Errors must be emitted in structured format.

Example:

``` json
{
  "status": "error",
  "error_code": "NON_CANONICAL_GOVERNANCE_INPUT_SOURCE",
  "message": "Next-action selector attempted to resolve governance state from non-canonical path.",
  "allowed_surfaces": [
    "governance-system-state.json",
    "governance-roadmap.json",
    "governance-gap-analysis.json",
    "governance-maturity-scoring.json",
    "governance-remediation-plan.json"
  ]
}
```

------------------------------------------------------------------------

# 08 --- Governance Evidence Requirements

The artifact bundle must include:

    docs/pipelines/governance/
    enforce-canonical-input-surface-authority-next-action-selector/

Required artifacts:

    01-problem-statement.md
    02-canonical-surface-definition.md
    03-authority-contract.md
    04-fail-closed-error-cases.md
    05-implementation-summary.md
    06-verification-plan.md
    07-final-verdict.md

------------------------------------------------------------------------

# 09 --- Acceptance Criteria

Pipeline 176 is complete when:

-   selector reads only canonical governance surfaces
-   shadow or duplicate surfaces cannot influence resolution
-   cross-surface inconsistencies fail closed
-   missing canonical surfaces fail closed
-   selector emits machine-readable errors
-   selector does not write output on authority failure
-   governance regression suite passes

------------------------------------------------------------------------

# 10 --- Expected Final Verdict

    CANONICAL_INPUT_SURFACE_AUTHORITY_ENFORCED_FOR_GOVERNANCE_NEXT_ACTION_SELECTOR

------------------------------------------------------------------------

# 11 --- Next Recommended Pipeline

After implementing Pipeline 176, run verification:

**Pipeline 177**

    Verify Canonical Input Surface Authority for Governance System Next-Action Selection

This verification must demonstrate:

-   fail-closed behavior on shadow inputs
-   fail-closed behavior on missing canonical surfaces
-   deterministic selector output under valid canonical state.
