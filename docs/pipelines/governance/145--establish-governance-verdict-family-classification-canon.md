---
pipeline_id: 145
title: Establish Governance Verdict Family Classification Canon
registry_id: governance.pipeline.establish-verdict-family-classification-canon
status: active
stage: establishment
owner: codex
classification:
  domain: governance
  layer: 5
  type: capability-establishment
  safety_criticality: medium
preconditions:
  - Pipeline 143 established the governance run analytics surface.
  - Pipeline 144 verified analytics accuracy and surfaced bounded classification ambiguity.
  - docs/governance/pipeline-run-analytics.md exists.
  - docs/governance/pipeline-run-ledger.md exists as canonical governance memory.
triggers:
  - Analytics verification surfaced ambiguity in verdict-family grouping.
  - Governance requires deterministic classification rules for verdict aggregation.
inputs:
  - docs/governance/pipeline-run-ledger.md
  - docs/governance/pipeline-run-analytics.md
  - docs/pipelines/governance/
  - artifact bundle directories under docs/pipelines/governance/*/
outputs:
  - docs/governance/verdict-family-classification-canon.md
  - docs/pipelines/governance/establish-governance-verdict-family-classification-canon/
primary_artifact_bundle: docs/pipelines/governance/establish-governance-verdict-family-classification-canon/
verdict_file: docs/pipelines/governance/establish-governance-verdict-family-classification-canon/07-final-verdict.md
success_criteria:
  - A canonical verdict-family taxonomy is defined.
  - Mapping rules from verdict strings to verdict families are explicit and deterministic.
  - Analytics aggregation rules reference the canon.
  - Historical verdicts remain unchanged; only classification semantics are defined.
failure_conditions:
  - Verdict families are defined ambiguously or depend on interpretation.
  - Canon attempts to rewrite historical verdict strings.
---

# 145 — Establish Governance Verdict Family Classification Canon

## 1. Purpose

Establish a canonical taxonomy for governance pipeline verdicts so that analytics and governance reporting classify results deterministically.

Pipeline verification (144) identified a bounded discrepancy where a verdict string:

`MULTI_SESSION_CONTINUITY_EVIDENCE_HARNESS_PIPELINE_NORMALIZED`

was grouped differently depending on interpretation. This pipeline creates an explicit classification canon so that analytics surfaces and governance reporting can derive verdict families consistently.

---

# 2. Problem Statement

Governance pipelines produce final verdict strings recorded in `07-final-verdict.md`. Analytics surfaces group those verdicts into families for reporting purposes.

Without a canonical classification rule:

- verdict families can be interpreted inconsistently
- analytics distributions may drift over time
- governance metrics become unreliable

A classification canon ensures that every verdict string maps deterministically to a verdict family.

---

# 3. Goals

Pipeline 145 must establish:

1. A canonical set of verdict families.
2. Deterministic mapping rules from verdict strings to verdict families.
3. Guidance for analytics surfaces to aggregate verdict families correctly.
4. Extension rules for future verdicts.

---

# 4. Non-Goals

This pipeline must **not**:

- change historical verdict strings.
- modify artifact bundle evidence.
- alter analytics counts directly.

It defines **classification semantics only**.

---

# 5. Canonical Location

Create the canon at:

```
docs/governance/verdict-family-classification-canon.md
```

This document becomes the authoritative classification reference for governance verdicts.

---

# 6. Canonical Verdict Families

The canon defines the deterministic family set:

- VERIFIED
- ESTABLISHED
- NORMALIZED
- IMPLEMENTED
- WITH_LIMITATIONS
- WITH_GAPS
- RESTRICTED
- OTHER

These families describe the nature of the pipeline result rather than the specific pipeline purpose.

---

# 7. Deterministic Mapping Rules

Verdict families must be derived using explicit rules, aligned with canonical mapping authority:

| Verdict String Pattern | Verdict Family |
|------------------------|---------------|
| contains `_WITH_GAPS` | WITH_GAPS |
| contains `_WITH_(LIMITATIONS|LIMITATION|RESTRICTION(S))` | WITH_LIMITATIONS |
| contains token `NORMALIZED` | NORMALIZED |
| contains `VERIFIED` | VERIFIED |
| contains token `ESTABLISHED` | ESTABLISHED |
| contains `_IMPLEMENTED` | IMPLEMENTED |
| contains `_RESTRICTED` | RESTRICTED |
| none matched | OTHER |

Rules must be literal and reproducible.

---

# 8. Analytics Aggregation Rules

Analytics surfaces must:

- classify verdict families using the canon
- derive distributions directly from ledger entries
- avoid private interpretation

---

# 9. Extension Rules

Future pipelines introducing new verdicts must:

1. follow existing suffix conventions where possible
2. update the classification canon if a new family is required
3. maintain deterministic mapping rules

---

# 10. Artifact Bundle

Pipeline 145 must produce:

```
01-problem-statement.md
02-verdict-surface-inventory.md
03-verdict-family-taxonomy.md
04-mapping-rules.md
05-analytics-aggregation-guidance.md
06-verification.md
07-final-verdict.md
```

---

# 11. Verification

Verification must confirm:

- the classification canon exists
- mapping rules cover all existing verdicts in the ledger
- analytics grouping rules reference the canon

---

# 12. Expected Verdict

If successful:

```
GOVERNANCE_VERDICT_FAMILY_CLASSIFICATION_CANON_ESTABLISHED
```

If minor legacy inconsistencies remain but the canon is valid:

```
GOVERNANCE_VERDICT_FAMILY_CLASSIFICATION_CANON_ESTABLISHED_WITH_LIMITATIONS
```

---

# 13. Result

After Pipeline 145 completes, the Governance OS will have a deterministic classification system for pipeline verdicts.

This canon enables analytics surfaces and future governance metrics to interpret pipeline results consistently across the repository's history.
