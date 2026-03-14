# Required Registry, Matrix, And Scaffold Updates

Repository changes applied:

- runtime composition support updated in [composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py)
- capability vocabulary updated in [template_capability_registry.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_capability_registry.json)
- matrix snapshot updated in [template_composition_matrix.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_composition_matrix.json)
- overlay manifests updated:
  - [django.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/django.json)
  - [scheduler.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/scheduler.json)
- scaffold generation updated in [template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_scaffold.py)

Canonical Django-native generated surfaces added:

- `manage.py`
- `project/settings.py`
- `project/urls.py`
- `project/asgi.py`
- `project/celery.py`
- `project/scheduler.py`

Preserved restrictions:

- `django + monorepo + scheduler` is not admitted by this lane
- Laravel-native scheduler semantics remain unchanged
