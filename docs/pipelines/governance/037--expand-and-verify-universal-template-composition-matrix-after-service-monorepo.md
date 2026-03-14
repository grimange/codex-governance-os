---
pipeline: 037
title: Expand and Verify Universal Template Composition Matrix After Service Monorepo Expansion
registry_id: governance.templates.expand-and-verify-universal-template-composition-matrix-after-service-monorepo
stage: verification
governance_layer: codex-governance-os
classification: GOVERNANCE_VERIFICATION
status: PROPOSED
created: 2026-03-14
related_pipelines:
  - 033
  - 034
  - 035
  - 036
---

# 037 — Expand and Verify Universal Template Composition Matrix After Service Monorepo Expansion

## 1. Problem Statement

Pipeline **036** closed the `service + monorepo` composition boundary and promoted it into the certified supported matrix.

This represents the **second structural expansion** of the Universal Template Composition system.

After each boundary closure, the entire composition matrix must be re-verified to ensure that:

- existing supported combinations remain valid
- previously rejected combinations remain rejected
- scaffold placement rules remain deterministic
- overlay ownership boundaries do not conflict
- contract enforcement and explainability remain aligned

Without a full matrix re-verification, subtle regressions may occur in:

- normalization logic
- overlay admission rules
- manifest compatibility checks
- scaffold generation behavior

---

## 2. Governance Objective

Re-certify the entire Universal Template Composition matrix after the introduction of the `service + monorepo` composition.

Verification must prove that:

- all supported compositions remain scaffoldable
- rejected compositions remain explicitly rejected
- governance enforcement surfaces remain consistent
- no accidental composition expansion occurs

---

## 3. Expanded Supported Matrix

After pipelines **033** and **036**, the supported matrix becomes:

| Composition |
|-------------|
| base-only |
| node-typescript-service + monorepo |
| node-typescript-service + cli-worker |
| cli-worker + monorepo |
| cli-worker + python-package |
| cli-worker + php-package |
| django + monorepo |
| service + monorepo |

Each supported composition must be verified across all governance surfaces.

---

## 4. Remaining Explicit Rejections

The remaining unsupported combinations must remain rejected:

| Composition |
|-------------|
| laravel + cli-worker |
| laravel + django |

These boundaries must remain **fail-closed**.

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

### Supported Compositions

Each supported composition must:

- return `supported: true`
- scaffold successfully
- generate deterministic repository structure
- pass manifest validation

Example verification command:

```
template_scaffold.py doctor-composition --overlays service monorepo
```

Expected:

```
supported: true
```

---

### Rejected Compositions

Each rejected composition must:

- return `supported: false`
- produce consistent rejection diagnostics across all surfaces

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

A new verification suite should be introduced:

```
tests/governance/test_template_composition_matrix_service_monorepo_expansion.py
```

Tests must validate:

- supported matrix integrity
- rejection matrix stability
- scaffold generation correctness
- doctor surface accuracy
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
docs/pipelines/governance/expand-and-verify-universal-template-composition-matrix-after-service-monorepo/
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

Verify the new supported composition.

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays service monorepo --output json
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

---

## 11. Expected Outcome

After this pipeline:

- the expanded template composition matrix is certified
- scaffold generation remains deterministic
- governance surfaces remain aligned with the canonical contract
- the system safely supports generic services inside monorepos

---

## 12. Final Verdict

Expected verdict:

```
UNIVERSAL_TEMPLATE_COMPOSITION_MATRIX_EXPANDED_AND_VERIFIED_AFTER_SERVICE_MONOREPO
```