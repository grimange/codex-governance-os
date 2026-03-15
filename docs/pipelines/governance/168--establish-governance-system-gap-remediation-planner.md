# 168 --- Establish Governance System Gap Remediation Planner

``` yaml
---
pipeline_id: 168
registry_id: governance.system.establish-governance-gap-remediation-planner
stage: establish

title: Establish Governance System Gap Remediation Planner

summary: >
  Create a canonical remediation planning surface that converts
  governance-system-gaps.json into an ordered, evidence-scoped
  remediation plan describing how each governance gap can be
  resolved and what capability or pipeline would close it.

capability_type: governance_system_introspection

inputs:
  - governance-system-gaps.json
  - governance-system-maturity.json

outputs:
  - governance-system-gap-remediation-plan.json

invariants:
  - remediation plan must remain evidence-scoped
  - remediation must not infer unsupported capabilities
  - remediation ordering must respect dependency relationships
  - planner must fail closed if gap surface is inconsistent

execution:
  - generate remediation plan from gap surface
  - classify each gap by remediation strategy
  - assign dependency ordering
  - assign remediation priority
  - record evidence scope

verification:
  - remediation plan schema valid
  - every gap mapped to remediation strategy
  - deterministic output across runs

final_verdict: GOVERNANCE_SYSTEM_GAP_REMEDIATION_PLANNER_ESTABLISHED
---
```

------------------------------------------------------------------------

# 01 --- Problem Statement

Pipeline **166--167** established and verified the **Governance System
Gap Analyzer**.

The analyzer produces:

`governance-system-gaps.json`

which lists governance domains that are not fully verified.

However, the system currently lacks a canonical way to answer:

-   Which gap should be fixed first
-   What evidence would close the gap
-   What capability is missing
-   What pipeline or governance action could resolve it

Without this layer, the system detects problems but does not provide a
**governed remediation strategy**.

Pipeline **168** establishes the **Gap Remediation Planner** to convert
gap detection into actionable governance planning.

------------------------------------------------------------------------

# 02 --- Gap Surface Input

The planner consumes the canonical gap surface:

`governance-system-gaps.json`

Example structure:

``` json
{
  "gaps": [
    {
      "domain": "autonomous_governance_loop",
      "status": "UNVERIFIED"
    },
    {
      "domain": "multi_agent_governance",
      "status": "INVALID_STATE"
    },
    {
      "domain": "architecture_advisor",
      "status": "UNVERIFIED"
    }
  ]
}
```

------------------------------------------------------------------------

# 03 --- Remediation Planning Model

The remediation planner converts each gap into a **remediation entry**.

Each entry describes:

  Field                  Meaning
  ---------------------- ---------------------------------------
  domain                 governance domain
  current_status         UNVERIFIED / INVALID_STATE
  remediation_strategy   how to resolve the gap
  required_evidence      evidence needed to promote the domain
  recommended_action     governance action
  suggested_pipeline     possible pipeline class
  priority               remediation importance
  dependency_order       sequencing requirement
  promotion_target       expected maturity upgrade

------------------------------------------------------------------------

# 04 --- Remediation Plan Output

The planner generates:

`governance-system-gap-remediation-plan.json`

Example structure:

``` json
{
  "generated_by": "inspect_governance_state.py",
  "planner_version": "1.0",
  "remediation_plan": [
    {
      "domain": "multi_agent_governance",
      "current_status": "INVALID_STATE",
      "remediation_strategy": "state_normalization",
      "required_evidence": [
        "governed multi-agent orchestration surface",
        "agent role specialization evidence"
      ],
      "recommended_action": "normalize multi-agent governance state",
      "suggested_pipeline": "establish-multi-agent-governance-orchestrator",
      "priority": "CRITICAL",
      "dependency_order": 1,
      "promotion_target": "VERIFIED"
    },
    {
      "domain": "autonomous_governance_loop",
      "current_status": "UNVERIFIED",
      "remediation_strategy": "capability_completion",
      "required_evidence": [
        "closed-loop governance execution",
        "governance decision-to-action cycle"
      ],
      "recommended_action": "implement autonomous governance loop",
      "suggested_pipeline": "establish-autonomous-governance-loop",
      "priority": "HIGH",
      "dependency_order": 2,
      "promotion_target": "VERIFIED"
    },
    {
      "domain": "architecture_advisor",
      "current_status": "UNVERIFIED",
      "remediation_strategy": "advisor_capability",
      "required_evidence": [
        "architecture evaluation surface",
        "governance architecture recommendation capability"
      ],
      "recommended_action": "establish architecture advisor capability",
      "suggested_pipeline": "establish-architecture-advisor",
      "priority": "MEDIUM",
      "dependency_order": 3,
      "promotion_target": "VERIFIED"
    }
  ]
}
```

------------------------------------------------------------------------

# 05 --- Remediation Strategy Classification

The planner must classify gaps into one of the following strategies:

  Strategy                Meaning
  ----------------------- ------------------------------------------
  state_normalization     system state inconsistent
  capability_completion   capability partially implemented
  capability_missing      capability not implemented
  verification_missing    capability exists but lacks verification
  evidence_gap            insufficient evidence for promotion

------------------------------------------------------------------------

# 06 --- Remediation Ordering

The planner must assign **dependency ordering**.

Example ordering rule:

INVALID_STATE gaps → must be resolved before UNVERIFIED domains.

Typical ordering:

1.  State normalization
2.  Missing orchestration capabilities
3.  Advisory and analysis capabilities
4.  Optional optimization capabilities

------------------------------------------------------------------------

# 07 --- Planner Determinism

The remediation planner must produce **deterministic output**.

Requirements:

-   identical input → identical remediation plan
-   stable ordering
-   no randomness
-   evidence-scoped reasoning only

Determinism ensures the planner can safely participate in **governed
automation loops**.

------------------------------------------------------------------------

# 08 --- Verification Requirements

Verification must confirm:

1.  planner successfully consumes `governance-system-gaps.json`
2.  remediation plan is generated
3.  schema validity confirmed
4.  every gap has a remediation entry
5.  output deterministic across two executions

Example verification commands:

    python inspect_governance_state.py remediation-plan
    python inspect_governance_state.py remediation-plan

Hashes of output must match.

------------------------------------------------------------------------

# 09 --- Final Verdict

**GOVERNANCE_SYSTEM_GAP_REMEDIATION_PLANNER_ESTABLISHED**

The governance system now supports:

-   maturity scoring
-   gap detection
-   remediation planning

forming the **full governance diagnostic cycle**.
