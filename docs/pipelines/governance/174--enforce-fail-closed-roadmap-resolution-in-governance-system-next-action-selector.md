---
classification: governance-system
inputs:
- governance-system-roadmap.json
- governance-system-gaps.json
- governance-system-maturity.json
- tools/governance/inspect_governance_state.py
layer: Layer 8 --- Governance System Self-Inspection & Autonomous
  Guidance
objective: Repair the next-action selector so unresolved roadmap targets
  fail closed, emit machine-readable failure, and never write a
  misleading canonical next-action surface.
outputs:
- tools/governance/inspect_governance_state.py
- tests/governance/test_governance_system_next_action.py
- governance-system-next-action.json
- docs/pipelines/governance/enforce-fail-closed-roadmap-resolution-in-governance-system-next-action-selector/
owner: codex-governance-os
pipeline_id: 174
predecessors:
- 172
- 173
stage: implementation
status: proposed
successor_hint: 175 --- Verify Fail-Closed Roadmap Resolution in
  Governance System Next Action Selector
tags:
- governance
- fail-closed
- selector
- roadmap
- autonomous-guidance
title: Enforce Fail-Closed Roadmap Resolution in Governance System Next
  Action Selector
---

# 174 --- Enforce Fail-Closed Roadmap Resolution in Governance System Next Action Selector

## Purpose

Pipeline 173 verified that the Governance System Next Action Selector is
deterministic on canonical state, but it also proved a control-plane
defect: when `recommended_next_target` is invalid, the selector still
exits successfully and regenerates `governance-system-next-action.json`.

That behavior is unsafe. This pipeline enforces fail-closed behavior for
unresolved roadmap targets.

## Goals

-   Fail closed when `recommended_next_target` cannot be resolved
-   Exit non-zero on invalid roadmap resolution
-   Do not write `governance-system-next-action.json` on invalid
    resolution
-   Emit machine-readable failure reason
-   Preserve deterministic behavior on valid canonical state

## Required Implementation Changes

### Repair roadmap target resolution

Update `tools/governance/inspect_governance_state.py` so `next-action`
mode validates `recommended_next_target` before emitting output.

Validation must confirm:

-   the field exists when required
-   the target maps to a recognized governance domain
-   the target exists in the ordered remediation plan
-   the target aligns with current maturity / gap state

If any check fails, the selector must terminate as invalid state.

### Enforce fail-closed termination

When roadmap resolution fails:

-   exit non-zero
-   emit machine-readable failure
-   do not generate a canonical next-action surface

Example failure:

``` json
{
  "status": "ERROR",
  "error_code": "UNRESOLVED_ROADMAP_RECOMMENDED_NEXT_TARGET",
  "message": "recommended_next_target could not be resolved against the remediation plan"
}
```

### Prevent misleading canonical output

`governance-system-next-action.json` must not be written when resolution
fails.

### Preserve valid-state determinism

On valid state the selector must remain deterministic and continue to
emit the expected canonical result:

-   target: `multi_agent_governance`
-   action_type: `state_normalization`
-   suggested_pipeline:
    `establish-role-scoped-codex-sub-agent-specialization`

## Required Tests

Add tests in:

`tests/governance/test_governance_system_next_action.py`

Test cases:

1.  Valid canonical roadmap target → exit 0 and deterministic output.
2.  Invalid `recommended_next_target` → non-zero exit and failure
    output.
3.  Missing `recommended_next_target` → fail closed.
4.  Target absent from remediation plan → fail closed.
5.  Gap / roadmap mismatch → fail closed.

## Artifact Bundle

Create bundle:

`docs/pipelines/governance/enforce-fail-closed-roadmap-resolution-in-governance-system-next-action-selector/`

Required files:

-   01-problem-statement.md
-   02-defect-summary.md
-   03-implementation-delta.md
-   04-fail-closed-behavior-contract.md
-   05-test-and-verification-log.md
-   06-output-surface-impact.md
-   07-final-verdict.md

## Acceptance Criteria

-   selector exits non-zero on unresolved roadmap targets
-   selector emits stable machine-readable failure
-   canonical next-action surface is not written on invalid resolution
-   deterministic behavior preserved for valid state
-   regression tests cover the defect path
-   artifact bundle complete

## Expected Final Verdict

`GOVERNANCE_SYSTEM_NEXT_ACTION_SELECTOR_FAIL_CLOSED_RESOLUTION_ENFORCED`

## Next Pipeline

175 --- Verify Fail-Closed Roadmap Resolution in Governance System Next
Action Selector
