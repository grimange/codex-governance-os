---
pipeline_id: 147
title: Normalize Governance Run Analytics Surface Against Verdict Family Canon
registry_id: governance.pipeline.normalize-run-analytics-against-verdict-family-canon
status: active
stage: normalization
owner: codex
classification:
  domain: governance
  layer: 5
  type: normalization
  safety_criticality: medium
preconditions:
  - Pipeline 145 established the verdict family classification canon.
  - Pipeline 146 verified the canon across all ledger verdicts.
  - docs/governance/pipeline-run-ledger.md exists as canonical governance memory.
  - docs/governance/pipeline-run-analytics.md exists as a derived analytics surface.
triggers:
  - Verification revealed analytics distribution drift from canon-derived classification.
  - Governance analytics must align strictly with the verdict classification canon.
inputs:
  - docs/governance/pipeline-run-ledger.md
  - docs/governance/pipeline-run-analytics.md
  - docs/governance/verdict-family-classification-canon.md
  - docs/pipelines/governance/
outputs:
  - updated docs/governance/pipeline-run-analytics.md
  - docs/pipelines/governance/normalize-governance-run-analytics-surface-against-verdict-family-canon/
success_criteria:
  - Analytics verdict-family counts match canon-derived recomputation from the ledger.
  - Analytics explicitly includes the OTHER family for legacy verdicts.
  - No ledger entries or historical verdict strings are modified.
failure_conditions:
  - Analytics values remain inconsistent with canon-derived classification.
  - Ledger entries are modified instead of analytics normalization.
---

# 147 — Normalize Governance Run Analytics Surface Against Verdict Family Canon

## 1. Purpose

Normalize the governance run analytics surface so that all verdict-family metrics are derived strictly from the canonical verdict-family classification rules established in Pipeline 145.

Pipeline 146 verified that the canon correctly classifies all ledger verdicts but revealed that the analytics surface still uses a legacy grouping model. This pipeline updates the analytics document so its distributions match canonical recomputation.

---

# 2. Problem Statement

Verification results from Pipeline 146 identified bounded inconsistencies between:

- canon-derived classification counts
- analytics-reported counts

Example discrepancy:

Canonical recomputation:
VERIFIED 16 / ESTABLISHED 14 / NORMALIZED 4 / IMPLEMENTED 3

Current analytics surface:
VERIFIED 17 / ESTABLISHED 17 / NORMALIZED 3 / IMPLEMENTED 0

This means the analytics document is no longer faithfully derived from the ledger and canon. The analytics layer must therefore be normalized.

---

# 3. Goals

Pipeline 147 must:

1. Recompute verdict-family distributions using the canonical classification rules.
2. Update the analytics document so its counts match the canon-derived results.
3. Explicitly include the OTHER family for legacy verdicts outside canonical suffix patterns.
4. Preserve ledger and historical evidence unchanged.

---

# 4. Non-Goals

This pipeline must **not**:

- modify pipeline verdict strings
- modify ledger entries
- introduce new verdict families
- change classification canon rules

It only updates the analytics surface.

---

# 5. Normalization Procedure

### 5.1 Canon-Derived Recalculation

Use the classification rules defined in:

`docs/governance/verdict-family-classification-canon.md`

to recompute verdict-family counts from the ledger.

### 5.2 Analytics Update

Update the following sections of:

`docs/governance/pipeline-run-analytics.md`

- verdict family distribution
- summary tables
- derived counts

The values must match canonical recomputation exactly.

### 5.3 Legacy Verdict Representation

Add or confirm the presence of the `OTHER` verdict family representing legacy verdicts not matching canonical suffix patterns.

---

# 6. Artifact Bundle

Pipeline 147 must produce:

- 01-problem-statement.md
- 02-analytics-surface-inventory.md
- 03-canon-recomputation.md
- 04-analytics-normalization-plan.md
- 05-updated-analytics-surface.md
- 06-verification.md
- 07-final-verdict.md

---

# 7. Verification

Verification must confirm:

- analytics counts match canon-derived recomputation
- OTHER family counts match legacy verdict inventory
- ledger and canon documents remain unchanged

---

# 8. Expected Verdict

If normalization succeeds:

NORMALIZED_GOVERNANCE_RUN_ANALYTICS_SURFACE_TO_VERDICT_CANON

If minor legacy analytics limitations remain but canonical alignment is achieved:

NORMALIZED_GOVERNANCE_RUN_ANALYTICS_SURFACE_WITH_LIMITATIONS

---

# 9. Result

After Pipeline 147 completes, the governance analytics surface will be fully aligned with the canonical verdict-family classification rules.

This ensures analytics metrics remain deterministic and prepares the system for governance maturity scoring and higher-level governance intelligence pipelines.
