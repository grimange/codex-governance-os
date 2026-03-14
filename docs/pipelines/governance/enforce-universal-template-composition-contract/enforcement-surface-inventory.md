# Enforcement Surface Inventory

## Runtime Surfaces

- `tools/templates/composition_contract.py`
  - canonical resolver for supported and rejected compositions
  - deterministic rejection message formatting
  - manifest inventory drift validation
- `tools/governance/template_scaffold.py`
  - rejects unsupported compositions before any scaffold surfaces are created
  - rejects non-conformant manifest inventories during `list-manifests`
- `tools/templates/list_templates.py`
  - fails closed when manifest inspection surfaces drift from the certified contract

## Verification Surfaces

- `tests/governance/test_template_composition_contract.py`
- `tests/governance/test_template_scaffold.py`
- `tests/governance/test_template_composition_matrix.py`
- `tests/governance/test_template_conformance.py`
