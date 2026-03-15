# 164 --- Establish Governance System Maturity Scoring Surface

``` yaml
pipeline_id: 164
registry_id: governance.system.establish-governance-system-maturity-scoring-surface
title: Establish Governance System Maturity Scoring Surface
stage: implementation
lane: governance
status: proposed
created: 2026-03-15
author: codex
governance_layer: Governance System Introspection
capability_type: maturity-analysis
```

# 1. Problem Statement

The governance system now exposes a **machine-readable state surface**
through:

`governance-system-state.json`

and this surface has been verified as:

-   deterministic
-   drift-detecting
-   self-consistent

However, the current system **does not provide an interpretable maturity
signal** describing:

-   how complete the governance system is
-   which governance domains are fully established
-   what gaps prevent reaching full maturity
-   what pipelines should logically come next

Without a deterministic scoring surface, the system can only answer
**state**, not **maturity**.

This pipeline establishes a **Governance System Maturity Scoring
Surface** that derives maturity scores directly from canonical
governance evidence.

# 2. Objectives

This pipeline introduces a **deterministic governance maturity model**
that:

1.  Calculates maturity scores across governance domains.
2.  Produces a canonical machine-readable output.
3.  Identifies blockers preventing full maturity.
4.  Recommends next governance actions.

Outputs must be derived strictly from canonical governance evidence:

-   governance-system-state.json
-   capability registry
-   pipeline registry
-   execution evidence surfaces

No subjective scoring is allowed.

# 3. Governance Maturity Domains

## 3.1 Codex Governance Layer

Evaluates whether the repository enforces:

-   governed pipeline routing
-   admission gates
-   canonical instruction entry
-   codex collaboration structure

## 3.2 Pipeline Governance

Evaluates the maturity of the pipeline system itself:

-   pipeline registry integrity
-   lane routing
-   admission gates
-   registry synchronization

## 3.3 Passive Observation

Evaluates whether the system can observe itself without intervention.

Capabilities include:

-   lifecycle observation
-   pipeline execution recording
-   centralized run ledger
-   evidence generation

## 3.4 Autonomous Governance Loop

Evaluates whether the system can:

-   detect governance drift
-   identify missing pipelines
-   recommend remediation
-   maintain state integrity

## 3.5 Multi-Agent Governance

Evaluates whether multiple specialized agents can collaborate safely.

Capabilities include:

-   role-scoped sub-agents
-   session orchestration
-   collaboration discipline
-   shared governance state

## 3.6 Architecture Advisor

Evaluates whether the system can provide architecture-level guidance.

Capabilities include:

-   architecture drift detection
-   governance-aware architecture analysis
-   pipeline recommendation

# 4. Scoring Model

Each governance domain receives a score from **0--100**.

    domain_score = (verified_capabilities / declared_capabilities) * 100

Where:

-   **declared_capabilities** are defined in the capability registry
-   **verified_capabilities** have passed verification pipelines

# 5. Fail-Closed Scoring Rules

### Rule 1 --- Unknown Capability

If a capability appears in the state surface but not in the registry:

    score = 0
    classification = INVALID_STATE

### Rule 2 --- Missing Evidence

If a capability exists but has no verification evidence:

    score = 0
    classification = UNVERIFIED

### Rule 3 --- Drift Detection Failure

If the self-inspection CLI detects drift:

    global_maturity = BLOCKED

### Rule 4 --- Partial Domains

Domains with incomplete capability coverage are scored proportionally.

# 6. Canonical Output Surface

This pipeline introduces:

`governance-system-maturity.json`

Example:

``` json
{
  "overall_maturity": 72,
  "domains": {
    "codex_governance_layer": 85,
    "pipeline_governance": 90,
    "passive_observation": 65,
    "autonomous_governance_loop": 55,
    "multi_agent_governance": 60,
    "architecture_advisor": 40
  },
  "blockers": [
    "architecture_advisor_missing_verification",
    "autonomous_governance_loop_partial"
  ],
  "recommended_next_pipelines": [
    165,
    166,
    167
  ]
}
```

# 7. CLI Extension

Extend the CLI:

    python tools/governance/inspect_governance_state.py maturity

The CLI must:

1.  Load canonical governance surfaces
2.  Evaluate maturity scores
3.  Produce `governance-system-maturity.json`

The output must remain deterministic.

# 8. Artifact Bundle

Create bundle:

`docs/pipelines/governance/establish-governance-system-maturity-scoring-surface/`

Required artifacts:

-   01-problem-statement.md
-   02-governance-maturity-domain-model.md
-   03-capability-scoring-model.md
-   04-fail-closed-scoring-rules.md
-   05-maturity-output-schema.md
-   06-cli-extension-design.md
-   07-verification-plan.md
-   08-final-verdict.md

# 9. Verification Plan

### Deterministic scoring

Run twice:

    python inspect_governance_state.py maturity
    python inspect_governance_state.py maturity

Hashes must match.

### Domain completeness

Each maturity domain must have a defined scoring rule.

### Evidence-only scoring

Scores must derive only from canonical evidence surfaces.

# 10. Expected Outcome

The governance system can answer:

**"How mature is the governance system?"**

Outputs include:

-   maturity by governance domain
-   blockers preventing full maturity
-   recommended next pipelines

# 11. Final Verdict

Expected verdict:

    GOVERNANCE_SYSTEM_MATURITY_SCORING_SURFACE_ESTABLISHED
