---
pipeline: "067"
title: "Verify Django Scheduler Composition Remains Non-Drifting"
status: "proposed"
lane: "governance"
stage: "verification"
classification: "verification"
registry_id: "governance.templates.verify-django-scheduler-composition-non-drifting"
depends_on:
  - "066"
allowed_inputs:
  - "tools/governance/composition_contract.py"
  - "tools/governance/template_capability_registry.json"
  - "tools/governance/template_composition_matrix.json"
  - "tools/governance/template_scaffold.py"
  - "docs/codex/templates/universal-template-composition-contract.md"
  - "docs/codex/templates/README.md"
  - "docs/governance/template-scaffold-contract.md"
  - "docs/codex/templates/django/README.md"
  - "docs/codex/templates/scheduler/README.md"
allowed_outputs:
  - "docs/pipelines/governance/verify-django-scheduler-composition-remains-non-drifting/"
  - "docs/pipelines/governance/067--verify-django-scheduler-composition-remains-non-drifting.md"
successors:
  - "068"
---

# 067 — Verify Django Scheduler Composition Remains Non-Drifting

## Purpose

Verify that the Django-native scheduler composition contract introduced in Pipeline 066 remains aligned across implementation, registry, composition matrix, scaffold generation rules, documentation, and test coverage.

This pipeline ensures that the newly supported `django + scheduler` composition does not silently drift after its introduction.

## Background

Pipeline 066 established the Django-native scheduler composition contract and converted `django + scheduler` from an explicit rejection into a supported governed composition when the Django scheduler contract is satisfied.

The governed Django scheduler surfaces introduced are:

- `manage.py`
- `project/settings.py`
- `project/urls.py`
- `project/asgi.py`
- `project/celery.py`
- `project/scheduler.py`

These surfaces form the canonical evidence set for Django-native scheduler support.

Before expanding scheduler support into broader compound framework combinations, this pipeline verifies that the Django contract remains stable and non-drifting.

## Objectives

1. Verify that `django + scheduler` remains a supported composition.
2. Confirm that all governance truth sources agree about the support state.
3. Ensure the canonical Django scheduler surfaces remain unchanged.
4. Confirm incomplete Django scheduler implementations fail closed.
5. Verify Laravel-native scheduler support remains unchanged.
6. Verify generic scheduler compositions remain unchanged.
7. Confirm compound combinations such as `django + monorepo + scheduler` remain explicitly unsupported unless intentionally opened.

## Verification Surfaces

The following repository surfaces must remain aligned.

### Implementation

- `composition_contract.py`
- `template_scaffold.py`

### Registry

- `template_capability_registry.json`

### Composition Matrix

- `template_composition_matrix.json`

### Documentation

- `universal-template-composition-contract.md`
- `README.md`
- `template-scaffold-contract.md`
- `django/README.md`
- `scheduler/README.md`

### Test Suites

- Django-native scheduler tests
- Laravel-native scheduler tests
- scheduler overlay tests
- framework scheduler boundary tests
- capability composition tests
- composition matrix tests
- composition drift tests

## Verification Requirements

### Supported Composition Verification

Confirm that:

```
django + scheduler -> supported
reason_code: certified-multi-overlay
```

### Canonical Scheduler Surface Verification

Verify the Django-native scheduler contract continues to require:

- `manage.py`
- `project/settings.py`
- `project/urls.py`
- `project/asgi.py`
- `project/celery.py`
- `project/scheduler.py`

These must remain the authoritative evidence set for Django scheduler support.

### Negative Case Verification

Ensure the following fail closed:

- Django present without scheduler contract surfaces
- Partial scheduler evidence
- malformed scheduler configuration
- unsupported compound overlay combinations

### Boundary Preservation Verification

Confirm unrelated scheduler compositions remain unchanged:

- `scheduler`
- `scheduler + cli-worker`
- `scheduler + monorepo`
- `scheduler + python-package`
- `scheduler + cli-worker + monorepo`
- `scheduler + cli-worker + python-package`
- `scheduler + laravel`

### Documentation Alignment Verification

Ensure documentation does not contradict implementation truth regarding:

- Django scheduler support
- unsupported framework scheduler combinations
- required scheduler contract surfaces

## Recommended Verification Commands

Example verification sequence:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler django --output json

python tools/governance/template_scaffold.py doctor-composition --overlays scheduler laravel --output json

python tools/governance/template_scaffold.py verify-composition-matrix --output json

python -m unittest   tests.governance.test_django_native_scheduler_composition   tests.governance.test_laravel_native_scheduler_composition   tests.governance.test_framework_scheduler_unsupported_boundaries   tests.governance.test_template_scheduler_overlay   tests.governance.test_template_capability_composition   tests.governance.test_template_composition_matrix   tests.governance.test_template_composition_drift   tests.governance.test_scheduler_scaffold_generation_matrix

python -m unittest discover -s tests/governance -p 'test_*.py'
```

## Artifact Bundle

Create verification bundle:

```
docs/pipelines/governance/
verify-django-scheduler-composition-remains-non-drifting/
```

Minimum artifacts:

1. `01-problem-statement.md`
2. `02-contract-surface-inventory.md`
3. `03-composition-matrix-verification.md`
4. `04-negative-case-verification.md`
5. `05-drift-alignment-check.md`
6. `06-verification-log.md`
7. `07-final-verdict.md`

## Expected Final Verdict

Preferred verdict:

```
DJANGO_NATIVE_SCHEDULER_BOUNDARIES_VERIFIED_NON_DRIFTING
```

Acceptable variant if restrictions remain:

```
DJANGO_NATIVE_SCHEDULER_CONTRACT_VERIFIED_NON_DRIFTING_WITH_RESTRICTIONS
```

## Safety Guarantees

This pipeline ensures:

- no silent expansion of framework scheduler support
- no regression of Laravel-native scheduler support
- no regression of generic scheduler combinations
- no divergence between documentation, registry, matrix, and implementation
- unsupported combinations remain explicitly rejected

## Recommended Next Pipeline

After successful verification:

**068 — Evaluate Framework-Native Scheduler Compound Composition Expansion**

This lane would determine whether combinations like:

- `django + monorepo + scheduler`
- `laravel + monorepo + scheduler`

should be intentionally supported.
