# Composition Matrix Verification

## Verified Supported Pair

Command result from `doctor-composition`:

- `django + scheduler` -> `supported: true`
- `reason_code: certified-multi-overlay`
- `decision_source: docs/contracts/universal-template-composition-contract.md`

## Verified Canonical Django Scheduler Surfaces

The live manifest and scaffold contract continue to require the Django-native
scheduler evidence set:

- `manage.py`
- `project/settings.py`
- `project/urls.py`
- `project/asgi.py`
- `project/celery.py`
- `project/scheduler.py`

Evidence:

- [django.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/django.json)
- [template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_scaffold.py)
- [test_django_native_scheduler_composition.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_django_native_scheduler_composition.py)

## Boundary Preservation

Unrelated scheduler decisions remain unchanged:

- `laravel + scheduler` -> supported
- `django + monorepo + scheduler` -> unsupported
- `verify-composition-matrix --output json` -> `{ "valid": true, "errors": [] }`

This confirms the direct Django scheduler admission did not silently broaden
into unsupported compound framework-native combinations.
