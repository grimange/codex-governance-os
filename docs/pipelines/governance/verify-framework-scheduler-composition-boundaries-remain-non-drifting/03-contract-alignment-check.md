# Contract Alignment Check

Aligned surfaces inspected in this lane:

- [composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py)
- [template_capability_registry.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_capability_registry.json)
- [template_composition_matrix.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_composition_matrix.json)
- [universal-template-composition-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/universal-template-composition-contract.md)
- [README.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/README.md)
- [template-scaffold-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/template-scaffold-contract.md)

Observed aligned facts:

- the runtime contract explicitly rejects both framework scheduler pairs
- the capability registry exposes `framework-native-scheduler-required`
- the matrix snapshot records both explicit rejection reasons
- contract and operator docs describe the same boundary semantics
- targeted tests assert the same conflict code and rejection reasons
