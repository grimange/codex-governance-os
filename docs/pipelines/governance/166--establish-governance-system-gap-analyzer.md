# 166 --- Establish Governance System Gap Analyzer

``` yaml
pipeline_id: 166
registry_id: governance.system.establish-governance-system-gap-analyzer
title: Establish Governance System Gap Analyzer
stage: implementation
lane: governance
status: proposed
created: 2026-03-15
author: codex
governance_layer: Governance System Introspection
capability_type: gap-analysis
depends_on:
  - 162
  - 164
  - 165
```

# 1. Problem Statement

The governance system now exposes:

-   governance-system-state.json
-   governance-system-maturity.json

These surfaces describe governance **state** and **maturity**, but the
system cannot yet produce a canonical inventory of **governance gaps**.

The system can reveal that a domain is incomplete, invalid, or
unverified, but it cannot yet answer:

-   what exact governance gaps exist
-   why they exist
-   what evidence supports them
-   which remediation class or pipeline may address them

This pipeline establishes a deterministic **Governance System Gap
Analyzer**.

# 2. Objectives

The gap analyzer must:

1.  read canonical governance surfaces
2.  detect missing or invalid governance domains
3.  classify gaps using evidence-only rules
4.  emit a canonical machine-readable gap surface
5.  prepare the system for automatic next-pipeline inference

# 3. Canonical Inputs

The analyzer must derive only from canonical surfaces such as:

-   governance-system-state.json
-   governance-system-maturity.json
-   capability registry
-   pipeline registry

If canonical inputs are inconsistent, the analyzer must fail closed.

# 4. Canonical Output

The pipeline introduces:

governance-system-gaps.json

Example:

``` json
{
  "overall_gap_state": "GAPS_PRESENT",
  "detected_gaps": [
    {
      "gap_id": "multi-agent-governance-missing-registry-coverage",
      "domain": "multi_agent_governance",
      "classification": "INVALID_STATE",
      "severity": "high",
      "reason": "Domain expected by maturity model but absent from capability registry",
      "evidence_sources": [
        "governance-system-maturity.json",
        "capability-registry"
      ],
      "blocking_effect": "prevents full governance-system maturity",
      "recommended_remediation_type": "registry-and-capability-establishment",
      "recommended_pipeline_candidates": [
        "establish-role-scoped-codex-sub-agent-specialization-layer"
      ]
    }
  ]
}
```

# 5. Gap Classifications

The analyzer supports:

-   INVALID_STATE
-   MISSING_CAPABILITY
-   UNVERIFIED_CAPABILITY
-   UNDECLARED_DOMAIN
-   PARTIAL_COVERAGE
-   BLOCKED_BY_DRIFT
-   EVIDENCE_INSUFFICIENT

Each classification must be derived strictly from canonical evidence.

# 6. Severity Model

Severity levels:

-   critical
-   high
-   medium
-   low

Severity reflects governance-system impact, not subjective urgency.

# 7. CLI Surface

Example command:

``` bash
python tools/governance/inspect_governance_state.py gaps
```

Expected behavior:

-   read canonical governance surfaces
-   derive gaps
-   emit governance-system-gaps.json
-   remain deterministic

# 8. Fail‑Closed Rules

The analyzer must not:

-   fabricate capabilities
-   normalize invalid state
-   modify registry truth
-   invent pipelines

If remediation is unknown, the analyzer must explicitly record that
fact.

# 9. Artifact Bundle

Create artifacts under:

docs/pipelines/governance/establish-governance-system-gap-analyzer/

Required artifacts:

-   01-problem-statement.md
-   02-gap-analysis-scope.md
-   03-gap-model-and-classification-rules.md
-   04-severity-and-blocking-rules.md
-   05-gap-output-schema.md
-   06-cli-extension-design.md
-   07-remediation-linkage-boundary.md
-   08-verification-plan.md
-   09-final-verdict.md

# 10. Verification Plan

Verification must confirm:

-   CLI executes successfully
-   governance-system-gaps.json is produced
-   output is deterministic
-   classifications are evidence-scoped
-   invalid upstream domains remain flagged

Example:

``` bash
python tools/governance/inspect_governance_state.py gaps
sha256sum governance-system-gaps.json

python tools/governance/inspect_governance_state.py gaps
sha256sum governance-system-gaps.json
```

Hashes must match.

# 11. Expected Outcome

The governance system can now answer:

"What governance gaps currently exist?"

with a deterministic machine-readable surface.

# 12. Final Verdict

Expected verdict:

GOVERNANCE_SYSTEM_GAP_ANALYZER_ESTABLISHED
