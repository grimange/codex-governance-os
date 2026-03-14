# Canonical Matrix Snapshot

The governed matrix snapshot now lives at [template_composition_matrix.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_composition_matrix.json).

It records:

- certified supported multi-overlay pairs
- explicit unsupported pairs
- canonical rejection reasons for explicit boundaries

This snapshot is not a replacement for the contract; it is the continuous-verification input that must remain aligned with:

- [docs/contracts/universal-template-composition-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/universal-template-composition-contract.md)
- runtime composition logic in [composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py)
- manifest declarations under [docs/codex/templates/manifests](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests)
