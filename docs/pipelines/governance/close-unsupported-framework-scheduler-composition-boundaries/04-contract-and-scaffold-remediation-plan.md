# Contract And Scaffold Remediation Plan

Repository changes applied in this lane:

- updated [composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py) to treat `laravel + scheduler` and `django + scheduler` as explicit fail-closed boundaries
- updated [template_capability_registry.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_capability_registry.json) with the canonical taxonomy code `framework-native-scheduler-required`
- updated [template_composition_matrix.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_composition_matrix.json) so the explicit rejection snapshot matches runtime truth
- updated the contract and docs:
  - [universal-template-composition-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/universal-template-composition-contract.md)
  - [README.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/README.md)
  - [template-scaffold-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/template-scaffold-contract.md)

Non-goals preserved:

- no scheduler support expansion
- no Laravel-native scheduler generation
- no Django-native scheduler generation
- no changes to already-certified supported scheduler compositions
