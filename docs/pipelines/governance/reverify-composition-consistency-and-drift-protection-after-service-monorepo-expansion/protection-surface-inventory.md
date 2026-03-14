# Protection Surface Inventory

## Decision Consistency Surfaces

- `tools/templates/composition_contract.py`
- `tools/governance/template_scaffold.py doctor-composition`
- `tools/governance/template_scaffold.py realize-repository`
- `tools/governance/template_scaffold.py list-manifests`
- `tools/templates/list_templates.py`

## Drift Protection Surfaces

- `detect_contract_drift(...)` in `tools/templates/composition_contract.py`
- `tests/governance/test_template_composition_contract_drift.py`
- `tests/governance/test_template_composition_post_expansion_protections.py`
- `tests/governance/test_template_composition_post_service_monorepo_protections.py`

These surfaces were re-verified against the post-`036` supported matrix.
