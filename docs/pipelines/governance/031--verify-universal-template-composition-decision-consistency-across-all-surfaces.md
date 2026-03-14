---
pipeline: 031
title: Verify Universal Template Composition Decision Consistency Across All Surfaces
registry_id: governance.templates.verify-universal-template-composition-decision-consistency
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
---

# 031 — Verify Universal Template Composition Decision Consistency Across All Surfaces

## 1. Problem Statement

The Universal Template Composition system now has four layers established:

- **Pipeline 027** — Composition matrix verified  
- **Pipeline 028** — Composition contract certified  
- **Pipeline 029** — Contract enforcement implemented  
- **Pipeline 030** — Explainability / doctor surface established  

However, multiple entry points now evaluate template composition decisions:

- `composition_contract.py`
- `template_scaffold.py scaffold`
- `template_scaffold.py doctor-composition`
- `template_scaffold.py list-manifests`
- `tools/templates/list_templates.py`

If any of these surfaces diverge in behavior, the governance system could:

- accept a composition in one surface but reject it in another
- produce conflicting explanations
- drift from the certified contract

This pipeline verifies that **all surfaces produce identical decisions for the same composition requests**.

---

## 2. Governance Objective

Guarantee that template composition evaluation is:

- deterministic
- centralized
- contract-aligned
- identical across all operational surfaces

After this pipeline, composition decisions must be **consistent regardless of the entry point used**.

---

## 3. Decision Authority

The single authoritative decision engine must remain:

```
tools/templates/composition_contract.py
```

All other surfaces must act as **thin adapters** that defer to this authority.

No surface may independently interpret or expand the composition matrix.

---

## 4. Surfaces Under Verification

The following surfaces must be validated.

### 4.1 Contract Engine

```
composition_contract.py
```

Primary validation logic.

---

### 4.2 Scaffold Generation

```
template_scaffold.py scaffold
```

Must reject unsupported compositions before file generation.

---

### 4.3 Doctor Surface

```
template_scaffold.py doctor-composition
```

Must return structured explanation consistent with enforcement behavior.

---

### 4.4 Manifest Inspection

```
template_scaffold.py list-manifests
```

Must validate manifest compatibility against the composition contract.

---

### 4.5 Template Listing

```
tools/templates/list_templates.py
```

Must remain aligned with the contract when reporting available templates.

---

## 5. Supported Composition Matrix

The following compositions must return **supported: true** across all surfaces.

| Composition |
|-------------|
| base-only |
| node-typescript-service + monorepo |
| node-typescript-service + cli-worker |
| cli-worker + monorepo |
| cli-worker + python-package |
| cli-worker + php-package |

---

## 6. Explicit Rejection Matrix

The following compositions must return **supported: false** across all surfaces.

| Composition | Reason |
|-------------|--------|
| laravel + cli-worker | incompatible runtime assumptions |
| django + monorepo | unsupported composition model |
| service + monorepo | scaffold structure conflict |
| laravel + django | cross-framework collision |

---

## 7. Verification Strategy

Verification must confirm that every surface produces identical:

- normalized overlay set
- support decision
- rejection reason
- reason code
- decision source

Example request:

```
doctor-composition --overlays laravel cli-worker
```

Expected across all surfaces:

```
supported: false
reason_code: UNSUPPORTED_COMPOSITION
decision_source: universal-template-composition-contract.md
```

---

## 8. Test Implementation

New governance tests should:

- simulate requests through each surface
- capture returned decision structures
- compare them against the contract engine result

Suggested test file:

```
tests/governance/test_template_composition_surface_consistency.py
```

Assertions must ensure that:

```
contract_result == scaffold_result == doctor_result == manifest_result
```

---

## 9. Fail-Closed Requirement

If any surface produces a decision inconsistent with the contract engine:

```
TEST FAILURE
```

The system must never silently widen or reinterpret the supported matrix.

---

## 10. Artifact Bundle

Artifacts must be recorded under:

```
docs/pipelines/governance/verify-universal-template-composition-decision-consistency/
```

Required artifacts:

1. problem-statement.md  
2. decision-surface-inventory.md  
3. contract-authority-confirmation.md  
4. verification-test-design.md  
5. verification-log.md  
6. decision-consistency-matrix.md  
7. final-verdict.md  

---

## 11. Verification Procedure

Run governance tests.

```
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Expected result:

```
Ran XX tests ... OK
```

Then verify doctor surface.

Example supported request:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays cli-worker python-package --output json
```

Expected:

```
supported: true
```

Example rejected request:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays laravel cli-worker --output json
```

Expected:

```
supported: false
reason_code: UNSUPPORTED_COMPOSITION
```

---

## 12. Expected Outcome

After this pipeline:

- all template composition entry points produce identical decisions
- the contract engine becomes the single governance authority
- explainability, enforcement, and verification surfaces remain aligned
- template governance becomes deterministic and stable

This pipeline completes the **Universal Template Composition Governance subsystem**.

---

## 13. Final Verdict

Expected verdict:

```
UNIVERSAL_TEMPLATE_COMPOSITION_DECISION_CONSISTENCY_VERIFIED
```