# 172 --- Establish Governance System Next-Action Selector

``` yaml
---
pipeline_id: 172
registry_id: governance.system.establish-governance-next-action-selector
stage: establish

title: Establish Governance System Next-Action Selector

summary: >
  Create a canonical next-action decision surface that converts the
  governance-system-advancement-roadmap.json into a single governed
  recommendation describing the highest-priority action the governance
  system should execute next.

capability_type: governance_system_introspection

inputs:
  - governance-system-advancement-roadmap.json
  - governance-system-gap-remediation-plan.json
  - governance-system-gaps.json
  - governance-system-maturity.json

outputs:
  - governance-system-next-action.json

invariants:
  - selector must remain evidence-scoped
  - selected action must correspond to roadmap priority
  - selector must not invent unsupported capabilities
  - selector must fail closed if roadmap surface inconsistent

execution:
  - load advancement roadmap
  - derive highest-priority actionable domain
  - determine action classification
  - map action to governance target domain
  - emit canonical next-action surface

verification:
  - next-action schema valid
  - selected domain matches roadmap recommended_next_target
  - deterministic output across runs

final_verdict: GOVERNANCE_SYSTEM_NEXT_ACTION_SELECTOR_ESTABLISHED
---
```

------------------------------------------------------------------------

# 01 --- Problem Statement

Pipelines **164--171** established a full governance diagnostic and
planning system:

-   maturity scoring
-   gap detection
-   remediation planning
-   advancement roadmap

However, the system still lacks a **decision surface** that converts
planning into a single governed action.

The roadmap explains *what should happen over time*, but governance
execution requires a canonical answer to:

**What is the single best governed action to execute next?**

Pipeline **172** establishes this next-action selector.

------------------------------------------------------------------------

# 02 --- Inputs

The selector derives its decision from the following canonical
artifacts:

-   `governance-system-advancement-roadmap.json`
-   `governance-system-gap-remediation-plan.json`
-   `governance-system-gaps.json`
-   `governance-system-maturity.json`

These surfaces together describe:

-   the current governance maturity
-   detected gaps
-   remediation strategy
-   ordered advancement roadmap

------------------------------------------------------------------------

# 03 --- Output Surface

Pipeline 172 generates:

`governance-system-next-action.json`

This file represents the **governance system's current recommended
action**.

------------------------------------------------------------------------

# 04 --- Next Action Structure

Example structure:

``` json
{
  "generated_by": "inspect_governance_state.py",
  "selector_version": "1.0",
  "recommended_action_type": "governance_capability_establishment",
  "target_domain": "multi_agent_governance",
  "reason": "INVALID_STATE governance domain must be normalized before other capabilities",
  "derived_from": "governance-system-advancement-roadmap.json"
}
```

------------------------------------------------------------------------

# 05 --- Action Classification

The selector must classify the action type.

Possible types:

  -----------------------------------------------------------------------
  Action Type                         Meaning
  ----------------------------------- -----------------------------------
  state_normalization                 resolving invalid governance state

  capability_establishment            implementing missing governance
                                      capability

  capability_completion               finishing partially implemented
                                      capability

  verification_required               capability exists but requires
                                      verification

  advisory_capability                 enabling governance advisory
                                      surfaces
  -----------------------------------------------------------------------

The classification must match the roadmap stage and remediation
strategy.

------------------------------------------------------------------------

# 06 --- Selection Rules

The next-action selector must follow deterministic rules:

1.  Prefer **INVALID_STATE** domains.
2.  Otherwise select the first **UNVERIFIED** remediation entry.
3.  Follow the ordering defined in the advancement roadmap.
4.  Never select a domain already marked **VERIFIED**.

------------------------------------------------------------------------

# 07 --- Deterministic Selection

The selector must produce deterministic output.

Requirements:

-   identical inputs → identical next-action output
-   no random prioritization
-   roadmap ordering preserved
-   evidence boundaries respected

------------------------------------------------------------------------

# 08 --- Evidence-Scoped Decision

The selector must not invent unsupported governance capabilities.

If the remediation plan indicates:

    "suggested_pipeline": "unknown"

the selector must preserve that uncertainty rather than inventing
pipeline recommendations.

------------------------------------------------------------------------

# 09 --- Fail-Closed Safety

The selector must fail if:

-   roadmap surface missing
-   roadmap inconsistent with remediation plan
-   recommended_next_target cannot be resolved
-   governance surfaces internally inconsistent

The system must never silently select an action when governance state is
invalid.

------------------------------------------------------------------------

# 10 --- Verification Requirements

Verification confirms:

-   selector successfully produces next-action surface
-   recommended domain matches roadmap target
-   schema validity confirmed
-   deterministic output across runs

Example commands:

    python inspect_governance_state.py next-action
    python inspect_governance_state.py next-action

Hashes must match.

------------------------------------------------------------------------

# 11 --- Final Verdict

If execution succeeds, record:

**GOVERNANCE_SYSTEM_NEXT_ACTION_SELECTOR_ESTABLISHED**

This confirms the governance system can now convert governance
diagnostics and planning into a **governed next action decision**.
