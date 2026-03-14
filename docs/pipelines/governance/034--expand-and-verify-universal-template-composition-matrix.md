---
pipeline: 034
title: Expand and Verify Universal Template Composition Matrix
registry_id: governance.templates.expand-and-verify-universal-template-composition-matrix
stage: verification
governance_layer: codex-governance-os
classification: GOVERNANCE_VERIFICATION
status: PROPOSED
created: 2026-03-14
related_pipelines:
  - 027
  - 028
  - 029
  - 030
  - 031
  - 032
  - 033
---

# 034 — Expand and Verify Universal Template Composition Matrix

## 1. Problem Statement

Pipeline **033** closed the `django + monorepo` composition boundary and promoted it into the certified supported matrix.

This expanded the Universal Template Composition system beyond its original certified set.

Any change to the support matrix introduces potential risks:

- normalization logic may behave differently
- nearby rejected combinations could accidentally become admitted
- scaffold behavior may change for other compositions
- manifest compatibility checks may drift
- explainability surfaces may diverge
- contract drift detection may no longer match the new matrix

Therefore the **entire composition matrix must be re-verified after expansion**.

---

## 2. Governance Objective

Re-certify the Universal Template Composition system after introducing a new supported composition.

The verification must prove that:

- the expanded matrix behaves deterministically
- all supported compositions scaffold correctly
- unsupported combinations remain rejected
- all governance surfaces remain aligned

---

## 3. Expanded Supported Matrix

After pipeline 033, the supported matrix becomes:

| Composition |
|-------------|
| base-only |
| node-typescript-service + monorepo |
| node-typescript-service + cli-worker |
| cli-worker + monorepo |
| cli-worker + python-package |
| cli-worker + php-package |
| django + monorepo |

Each supported composition must be verified across all governance surfaces.

---

## 4. Remaining Explicit Rejections

The following combinations must remain **explicitly unsupported**:

| Composition | Reason |
|-------------|--------|
| laravel + cli-worker | incompatible runtime assumptions |
| service + monorepo | undefined repository structure |
| laravel + django | cross-framework application collision |

The expansion must **not weaken rejection guarantees**.

---

## 5. Verification Surfaces

The following surfaces must produce consistent decisions.

### Contract Engine

```
composition_contract.py
```

### Scaffold Generator

```
template_scaffold.py scaffold
```

### Doctor Surface

```
template_scaffold.py doctor-composition
```

### Manifest Inspection

```
template_scaffold.py list-manifests
```

### Template Listing

```
tools/templates/list_templates.py
```

### Drift Detection

```
test_template_composition_contract_drift.py
```

---

## 6. Verification Requirements

The verification must confirm:

### Supported Matrix

Each supported composition must:

- return `supported: true`
- scaffold successfully
- produce deterministic repository layout
- pass manifest validation

Example verification command:

```
template_scaffold.py doctor-composition --overlays django monorepo
```

Expected:

```
supported: true
```

---

### Rejection Matrix

Each rejected composition must:

- return `supported: false`
- produce the same rejection reason across all surfaces

Example:

```
doctor-composition --overlays laravel cli-worker
```

Expected:

```
supported: false
reason_code: UNSUPPORTED_COMPOSITION
```

---

## 7. Test Coverage

The following tests must confirm matrix stability:

```
tests/governance/test_template_composition_matrix_expansion.py
```

Tests must validate:

- expanded supported matrix
- rejection guarantees remain intact
- scaffold generation for all supported combinations
- doctor surface correctness
- manifest compatibility
- cross-surface decision alignment

---

## 8. Fail-Closed Safety Requirement

If any unsupported composition becomes admitted accidentally:

```
TEST FAILURE
```

If any supported composition becomes rejected:

```
TEST FAILURE
```

Matrix stability is mandatory.

---

## 9. Artifact Bundle

Artifacts must be recorded under:

```
docs/pipelines/governance/expand-and-verify-universal-template-composition-matrix/
```

Required artifacts:

1. problem-statement.md  
2. expanded-supported-matrix.md  
3. rejection-matrix-verification.md  
4. scaffold-realization-verification.md  
5. verification-log.md  
6. matrix-consistency-report.md  
7. final-verdict.md  

---

## 10. Verification Procedure

Run governance tests.

```
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Expected result:

```
Ran XX tests ... OK
```

Then verify the new supported composition.

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays django monorepo --output json
```

Expected:

```
supported: true
```

Verify a rejected composition remains rejected.

```
doctor-composition --overlays laravel cli-worker
```

Expected:

```
supported: false
```

---

## 11. Expected Outcome

After this pipeline:

- the expanded template composition matrix is certified
- the system remains deterministic and fail-closed
- governance tooling continues to align with the canonical contract
- the template system can safely support Django services inside monorepos

---

## 12. Final Verdict

Expected verdict:

```
UNIVERSAL_TEMPLATE_COMPOSITION_MATRIX_EXPANDED_AND_VERIFIED
```