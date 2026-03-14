---
pipeline: 038
title: Reverify Composition Consistency and Drift Protection After Service Monorepo Expansion
registry_id: governance.templates.reverify-composition-consistency-and-drift-protection-after-service-monorepo-expansion
stage: verification
governance_layer: codex-governance-os
classification: GOVERNANCE_VERIFICATION
status: PROPOSED
created: 2026-03-14
related_pipelines:
  - 034
  - 035
  - 036
  - 037
---

# 038 — Reverify Composition Consistency and Drift Protection After Service Monorepo Expansion

## 1. Problem Statement

Pipeline **036** closed the `service + monorepo` template composition boundary and promoted it into the supported matrix.

Pipeline **037** verified the expanded matrix after this promotion.

However, the governance protections that guarantee **system safety** were originally certified prior to this second expansion.

Specifically:

- **Pipeline 031** established cross-surface decision consistency.
- **Pipeline 032** established contract drift detection.

These protections were re-certified once after the first expansion (`django + monorepo`) in pipeline **035**.

Because the supported matrix has now expanded again, governance protections must be **re-verified once more** to ensure they still function correctly.

Without this step, it is possible that:

- newly admitted compositions introduce decision inconsistencies
- drift detection fails to detect divergence around the expanded matrix
- contract and runtime logic diverge silently

---

## 2. Governance Objective

Re-certify governance protection layers after the second matrix expansion.

This pipeline must verify that:

- cross-surface composition decisions remain consistent
- contract drift detection remains accurate
- rejection guarantees remain stable
- the expanded supported matrix does not weaken fail-closed protections

---

## 3. Supported Matrix Under Verification

After pipelines **033** and **036**, the supported matrix is:

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

All protections must remain correct for each supported combination.

---

## 4. Remaining Explicit Rejections

The following combinations must remain rejected:

| Composition |
|-------------|
| laravel + cli-worker |
| laravel + django |

Rejection behavior must remain deterministic and consistent across all governance surfaces.

---

## 5. Consistency Verification

The following governance surfaces must produce identical decisions.

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
- reason code
- rejection reason
- decision source

---

## 6. Drift Detection Verification

Drift detection introduced in pipeline 032 must still detect divergence around the expanded matrix.

Simulated drift cases must include:

### Case A — Contract Removal Drift

Temporarily remove:

```
service + monorepo
```

from the contract while runtime still supports it.

Expected result:

```
CONTRACT_DRIFT_DETECTED
```

---

### Case B — Runtime Expansion Drift

Temporarily allow:

```
laravel + cli-worker
```

in the runtime engine while the contract still rejects it.

Expected result:

```
CONTRACT_DRIFT_DETECTED
```

---

### Case C — Manifest Drift

Introduce a temporary manifest declaring:

```
laravel + cli-worker
```

Expected result:

```
CONTRACT_DRIFT_DETECTED
```

---

## 7. Test Coverage

A new verification suite should be introduced:

```
tests/governance/test_template_composition_post_service_monorepo_protections.py
```

Tests must confirm:

- cross-surface decision equality
- scaffold enforcement correctness
- doctor output consistency
- manifest validation alignment
- contract drift detection accuracy
- rejection matrix stability

---

## 8. Fail-Closed Requirement

If any governance surface diverges from the contract engine:

```
TEST FAILURE
```

If drift detection fails to detect simulated divergence:

```
TEST FAILURE
```

Governance protections must remain deterministic and fail-closed.

---

## 9. Artifact Bundle

Artifacts must be recorded under:

```
docs/pipelines/governance/reverify-composition-consistency-and-drift-protection-after-service-monorepo-expansion/
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

Run the governance test suite.

```
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Expected:

```
Ran XX tests ... OK
```

Verify supported composition.

```
template_scaffold.py doctor-composition --overlays service monorepo
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

- cross-surface decision consistency remains intact
- contract drift detection continues to function correctly
- rejection guarantees remain stable
- governance protections remain reliable after the second matrix expansion

The Universal Template Composition governance subsystem remains safe to expand further.

---

## 12. Final Verdict

Expected verdict:

```
COMPOSITION_CONSISTENCY_AND_DRIFT_PROTECTION_REVERIFIED_AFTER_SERVICE_MONOREPO_EXPANSION
```