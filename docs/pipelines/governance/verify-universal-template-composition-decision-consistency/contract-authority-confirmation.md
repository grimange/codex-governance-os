# Contract Authority Confirmation

The single decision authority remains `tools/templates/composition_contract.py`.

Verification confirms:

- doctor output is derived from `explain_template_composition(...)`
- scaffold rejection is derived from `validate_template_composition(...)`
- manifest inspection drift detection is derived from `validate_manifest_inventory(...)`
- template listing inherits the same manifest validation surface

No adapter introduces its own alternate compatibility rules.
