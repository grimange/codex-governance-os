# Required Registry And Matrix Updates

Repository changes applied:

- runtime composition support updated in [composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py)
- capability model updated in [template_capability_registry.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_capability_registry.json)
- matrix snapshot updated in [template_composition_matrix.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_composition_matrix.json)
- overlay manifests updated:
  - [laravel.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/laravel.json)
  - [scheduler.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/scheduler.json)

Key normalization:

- `laravel + scheduler` moved from explicit rejection into the certified supported matrix
- `django + scheduler` remains explicitly rejected
- capability registry now explicitly includes `laravel-native-scheduler-surface`
- framework and scheduler roles are compatible in the capability model, while matrix truth still fail-closes all non-certified framework scheduler combinations
