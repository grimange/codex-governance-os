---
pipeline_id: 148
title: Verify Governance Run Analytics Canon Alignment
registry_id: governance.pipeline.verify-run-analytics-canon-alignment
status: active
stage: verification
owner: codex
classification:
  domain: governance
  layer: 5
  type: verification
  safety_criticality: medium
preconditions:
  - Pipeline 145 established the verdict family classification canon.
  - Pipeline 146 verified the canon across all ledger verdicts.
  - Pipeline 147 normalized the analytics surface against the canon.
  - docs/governance/pipeline-run-ledger.md exists as canonical governance memory.
  - docs/governance/pipeline-run-analytics.md exists as the derived analytics surface.
  - docs/governance/verdict-family-classification-canon.md exists.
triggers:
  - The analytics surface was normalized to match the verdict-family classification canon.
  - Governance requires a formal verification that analytics derivations match canonical rules.
inputs:
  - docs/governance/pipeline-run-ledger.md
  - docs/governance/pipeline-run-analytics.md
  - docs/governance/verdict-family-classification-canon.md
  - docs/pipelines/governance/
outputs:
  - docs/pipelines/governance/verify-governance-run-analytics-canon-alignment/
  - docs/pipelines/governance/verify-governance-run-analytics-canon-alignment/07-final-verdict.md
success_criteria:
  - Analytics verdict-family counts match canon-derived recomputation from the ledger.
  - The analytics document explicitly references the verdict classification canon.
  - The ledger and canon documents remain unchanged by the normalization.
  - Preflight verification passes with no violations.
failure_conditions:
  - Analytics values differ from canon-derived recomputation.
  - Ledger entries were modified during analytics normalization.
  - Canon rules were altered during analytics normalization.
---

# 148 — Verify Governance Run Analytics Canon Alignment

## 1. Purpose

Verify that the governance run analytics surface is now fully aligned with the canonical verdict-family classification rules established in Pipeline 145 and applied during normalization in Pipeline 147.

This verification confirms that governance analytics are deterministically derived from the centralized pipeline run ledger and classification canon.

---

# 2. Problem Statement

Pipeline 147 normalized the analytics document to align verdict-family distributions with canonical classification rules. However, a formal verification lane is required to ensure that:

- analytics values are derived strictly from the ledger
- classification rules are applied consistently
- no drift remains between analytics, canon, and ledger

Without this verification step, analytics could silently diverge from governance memory.

---

# 3. Goals

Pipeline 148 must verify:

1. Analytics verdict-family counts match canonical recomputation.
2. The analytics document references the classification canon explicitly.
3. The ledger remains unchanged after analytics normalization.
4. The classification canon remains unchanged.
5. Governance preflight validation passes.

---

# 4. Non-Goals

This pipeline must **not**:

- modify analytics values
- modify the ledger
- modify the classification canon

It verifies alignment only.

---

# 5. Verification Procedure

### 5.1 Canon-Derived Recalculation

Recompute verdict-family counts by applying mapping rules from:

`docs/governance/verdict-family-classification-canon.md`

to verdicts recorded in:

`docs/governance/pipeline-run-ledger.md`

### 5.2 Analytics Comparison

Compare recomputed values with the analytics document:

`docs/governance/pipeline-run-analytics.md`

The counts must match exactly.

### 5.3 Ledger Integrity Check

Confirm that:

`docs/governance/pipeline-run-ledger.md`

was not modified during analytics normalization.

### 5.4 Canon Integrity Check

Confirm that:

`docs/governance/verdict-family-classification-canon.md`

remains unchanged.

### 5.5 Preflight Verification

Run:

```
python tools/governance/preflight.py
```

Expected result:

```
PASS
```

---

# 6. Artifact Bundle

Pipeline 148 must produce:

- 01-problem-statement.md
- 02-analytics-surface-inventory.md
- 03-canon-recomputation.md
- 04-ledger-integrity-check.md
- 05-canon-integrity-check.md
- 06-preflight-verification.md
- 07-final-verdict.md

---

# 7. Expected Verdict

If verification succeeds:

```
GOVERNANCE_RUN_ANALYTICS_CANON_ALIGNMENT_VERIFIED
```

If minor bounded limitations remain but analytics alignment is confirmed:

```
GOVERNANCE_RUN_ANALYTICS_CANON_ALIGNMENT_VERIFIED_WITH_LIMITATIONS
```

---

# 8. Result

After Pipeline 148 completes, the governance analytics layer will be formally verified as canon-aligned, ensuring that governance metrics remain deterministic and trustworthy.

This verification enables the next governance capability: maturity scoring and governance intelligence layers.
