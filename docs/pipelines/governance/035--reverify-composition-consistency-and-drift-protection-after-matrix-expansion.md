---
pipeline: 035
title: Reverify Composition Consistency and Drift Protection After Matrix Expansion
registry_id: governance.templates.reverify-composition-consistency-and-drift-protection-after-matrix-expansion
stage: verification
governance_layer: codex-governance-os
classification: GOVERNANCE_VERIFICATION
status: PROPOSED
created: 2026-03-14
related_pipelines:
  - 031
  - 032
  - 033
  - 034
---

# 035 — Reverify Composition Consistency and Drift Protection After Matrix Expansion

## 1. Problem Statement

Pipeline **033** closed the `django + monorepo` composition boundary and expanded the supported matrix.

Pipeline **034** verified that the expanded matrix behaves correctly.

However, the **governance protections themselves** were originally certified before this expansion:

- **Pipeline 031** established cross-surface decision consistency.
- **Pipeline 032** established contract drift detection.

Because the support matrix has now changed, these protections must be **re-certified against the expanded matrix**.

Without re-verification, it is possible that:

- new compositions introduce decision inconsistencies
- drift detection fails to detect divergence around newly supported pairs
- contract and runtime surfaces silently diverge

---

## 2. Governance Objective

Re-certify that governance protections remain valid after expanding the supported composition matrix.

Specifically verify that:

- decision consistency guarantees remain intact
- contract drift detection remains accurate
- the expanded supported matrix does not weaken governance safety

---

## 3. Expanded Supported Matrix Under Test

The supported matrix after pipeline 033:

| Composition |
|-------------|
| base-only |
| node-typescript-service + monorepo |
| node-typescript-service + cli-worker |
| cli-worker + monorepo |
| cli-worker + python-package |
| cli-worker + php-package |
| django + monorepo |

All protections must work correctly for every supported combination.

---

## 4. Remaining Rejection Matrix

These combinations must remain rejected:

| Composition |
|-------------|
| laravel + cli-worker |
| service + monorepo |
| laravel + django |

Rejection guarantees must remain stable.

---

## 5. Consistency Verification

The following governance surfaces must produce identical decisions:

### Contract Engine

```
composition_contract.py
```

### Doctor Surface

```
template_scaffold.py doctor-composition
```

### Scaffold Generator

```
template_scaffold.py scaffold
```

### Manifest Inspection

```
template_scaffold.py list-manifests
```

### Template Listing

```
tools/templates/list_templates.py
```

For each composition, these surfaces must agree on:

- normalized overlays
- support decision
- rejection reason
- reason code
- decision source

---

## 6. Drift Detection Verification

Drift detection introduced in pipeline 032 must still detect contract divergence.

Simulated drift cases must include:

### Case A — Contract Removal Drift

The contract temporarily removes:

```
django + monorepo
```

Runtime still supports it.

Expected result:

```
CONTRACT_DRIFT_DETECTED
```

---

### Case B — Runtime Expansion Drift

Runtime engine temporarily admits:

```
service + monorepo
```

Contract does not list it.

Expected result:

```
CONTRACT_DRIFT_DETECTED
```

---

### Case C — Manifest Drift

A manifest temporarily declares:

```
service + monorepo
```

Expected result:

```
CONTRACT_DRIFT_DETECTED
```

---

## 7. Test Coverage

New verification suite:

```
tests/governance/test_template_composition_post_expansion_protections.py
```

Tests must confirm:

- cross-surface decision equality
- doctor output consistency
- scaffold enforcement correctness
- drift detection accuracy
- rejection matrix stability

---

## 8. Fail-Closed Requirement

If any surface diverges from the contract engine:

```
TEST FAILURE
```

If drift detection fails to detect simulated divergence:

```
TEST FAILURE
```

Governance protections must remain deterministic.

---

## 9. Artifact Bundle

Artifacts must be recorded under:

```
docs/pipelines/governance/reverify-composition-consistency-and-drift-protection-after-matrix-expansion/
```

Required artifacts:

1. problem-statement.md  
2. protection-surface-inventory.md  
3. expanded-matrix-consistency-check.md  
4. drift-detection-revalidation.md  
5. verification-log.md  
6. governance-safety-report.md  
7. final-verdict.md  

---

## 10. Verification Procedure

Run governance test suite.

```
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Expected:

```
Ran XX tests ... OK
```

Verify new supported composition:

```
template_scaffold.py doctor-composition --overlays django monorepo
```

Expected:

```
supported: true
```

Verify rejected compositions remain rejected.

```
doctor-composition --overlays laravel cli-worker
```

Expected:

```
supported: false
```

Drift simulation tests must detect divergence.

---

## 11. Expected Outcome

After this pipeline:

- decision consistency remains intact after matrix expansion
- contract drift detection continues to function correctly
- governance protections remain stable
- the system is safe to expand further

---

## 12. Final Verdict

Expected verdict:

```
COMPOSITION_CONSISTENCY_AND_DRIFT_PROTECTION_REVERIFIED_AFTER_MATRIX_EXPANSION
```