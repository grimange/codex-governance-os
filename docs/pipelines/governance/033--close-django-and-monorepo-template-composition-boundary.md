---
pipeline: 033
title: Close Django and Monorepo Template Composition Boundary
registry_id: governance.templates.close-django-monorepo-template-composition-boundary
stage: expansion
governance_layer: codex-governance-os
classification: GOVERNANCE_EXPANSION
status: PROPOSED
created: 2026-03-14
related_pipelines:
  - 027
  - 028
  - 029
  - 030
  - 031
  - 032
---

# 033 — Close Django and Monorepo Template Composition Boundary

## 1. Problem Statement

The Universal Template Composition contract currently defines the following **explicit fail-closed boundaries**:

| Composition | Status |
|-------------|--------|
| laravel + cli-worker | unsupported |
| django + monorepo | unsupported |
| service + monorepo | unsupported |
| laravel + django | unsupported |

These boundaries were intentionally enforced to prevent unsafe or undefined scaffold combinations.

However, the **django + monorepo** boundary represents a structural gap rather than a fundamental incompatibility.

The current rejection is primarily due to the absence of a canonical definition for:

- Django application placement inside a monorepo
- ownership boundaries between the monorepo root and the Django service
- scaffold layout rules
- manifest semantics for multi-package repositories

This pipeline closes the **django + monorepo boundary** by defining a safe canonical structure and extending the scaffold system accordingly.

---

## 2. Governance Objective

Promote the composition:

```
django + monorepo
```

from **explicitly unsupported** to **certified supported**, with full alignment across:

- composition contract
- scaffold generator
- manifest validation
- enforcement logic
- doctor/explain surfaces
- governance verification tests

The expansion must preserve the system’s **fail-closed safety model**.

---

## 3. Current Rejection Reason

The composition is currently rejected because the system lacks a canonical answer for:

- where the Django application should reside within the monorepo
- how governance files interact with monorepo root structure
- how template overlays resolve ownership conflicts
- how manifests describe nested application structures

Without these definitions, scaffold generation cannot guarantee deterministic structure.

---

## 4. Canonical Monorepo Layout for Django

The following structure becomes the canonical scaffold result.

```
repo-root/
│
├─ apps/
│   └─ backend/
│       └─ django-service/
│           ├─ manage.py
│           ├─ pyproject.toml
│           ├─ requirements.txt
│           ├─ project/
│           │   ├─ settings.py
│           │   ├─ urls.py
│           │   └─ asgi.py
│           └─ app_modules/
│
├─ packages/
│
├─ docs/
│
├─ .codex/
│
├─ AGENTS.md
└─ README.md
```

### Ownership Model

| Location | Ownership |
|--------|----------|
| repo root | monorepo overlay |
| apps/backend/django-service | django overlay |
| .codex | governance root |
| docs | repository documentation |

---

## 5. Manifest Model

The Django manifest must now support monorepo placement metadata.

Example manifest fields:

```
type: django-service
overlay: django
placement: apps/backend/django-service
repository_structure: monorepo
```

The scaffold generator must interpret these fields when composing overlays.

---

## 6. Scaffold Generator Changes

The scaffold system must be extended so that:

- monorepo overlay defines root repository structure
- django overlay generates the Django application under the defined placement
- root governance files remain at repository root
- no ownership conflicts occur between overlays

The scaffold must remain deterministic.

---

## 7. Composition Contract Update

The contract file must be updated.

File:

```
docs/codex/templates/universal-template-composition-contract.md
```

Add to the supported matrix:

| Composition |
|-------------|
| django + monorepo |

Remove it from the explicit rejection set.

---

## 8. Enforcement Updates

The following components must recognize the new supported composition:

- `composition_contract.py`
- scaffold enforcement logic
- manifest validation
- doctor-composition diagnostics
- template listing surfaces

All surfaces must remain aligned with the updated contract.

---

## 9. Verification Requirements

The pipeline must prove that the new composition is safe.

Verification steps:

1. Scaffold generation succeeds:

```
template_scaffold.py scaffold --overlays django monorepo
```

2. Generated structure matches canonical layout.

3. Manifest validation accepts the composition.

4. Doctor surface reports:

```
supported: true
```

5. Cross-surface consistency tests remain valid.

6. Drift detection continues to pass.

---

## 10. Test Coverage

New tests should be added:

```
tests/governance/test_django_monorepo_composition.py
```

These tests must verify:

- scaffold correctness
- manifest compatibility
- contract alignment
- doctor output correctness
- enforcement behavior

---

## 11. Artifact Bundle

Artifacts must be recorded under:

```
docs/pipelines/governance/close-django-monorepo-template-composition-boundary/
```

Required artifacts:

1. problem-statement.md  
2. boundary-diagnosis.md  
3. canonical-django-monorepo-layout.md  
4. scaffold-implementation-summary.md  
5. verification-log.md  
6. expanded-composition-matrix.md  
7. final-verdict.md  

---

## 12. Expected Outcome

After this pipeline:

- django + monorepo becomes a certified supported composition
- the scaffold system can safely generate Django services inside monorepos
- governance enforcement and explainability surfaces remain aligned
- the universal template composition matrix expands without weakening safety

---

## 13. Final Verdict

Expected verdict:

```
DJANGO_MONOREPO_TEMPLATE_COMPOSITION_BOUNDARY_CLOSED
```