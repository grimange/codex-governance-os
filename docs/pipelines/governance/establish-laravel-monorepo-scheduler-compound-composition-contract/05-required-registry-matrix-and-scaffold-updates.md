# Required Registry Matrix And Scaffold Updates

This lane updates the following governed surfaces:

- [composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py)
  - adds `laravel + monorepo + scheduler` to the certified runtime matrix
  - extends capability registry loading to carry explicit compound contracts
- [template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_scaffold.py)
  - adds most-specific compound override resolution
  - rejects ambiguous same-specificity compound overrides
  - renders placed Laravel scheduler files under the monorepo app root
- [laravel.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/laravel.json)
  - adds the explicit `monorepo+scheduler` compound override
- [template_capability_registry.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_capability_registry.json)
  - records the compound contract explicitly
- [template_composition_matrix.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_composition_matrix.json)
  - records the supported triplet snapshot

The lane also aligns the certified documentation surfaces:

- [universal-template-composition-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/universal-template-composition-contract.md)
- [template-scaffold-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/template-scaffold-contract.md)
- [README.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/README.md)
- [README.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/overlays/laravel/README.md)
- [README.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/overlays/monorepo/README.md)
- [README.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/overlays/scheduler/README.md)
