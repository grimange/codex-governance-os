# Decision Surface Inventory

## Primary Authority

- `tools/templates/composition_contract.py`

## Adapters Verified

- `tools/governance/template_scaffold.py realize-repository`
- `tools/governance/template_scaffold.py doctor-composition`
- `tools/governance/template_scaffold.py list-manifests`
- `tools/templates/list_templates.py`

## Verification Coverage

- direct API comparison between contract and doctor outputs
- scaffold realization success for supported cases
- scaffold rejection message comparison for explicit fail-closed cases
- manifest and template listing drift probes using the same invalid manifest mutation
