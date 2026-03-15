# Surface Integrity Verification

Verified canonical next-action surface fields on clean state:

- `generated_by`
- `selector_version`
- `recommended_action_type`
- `target_domain`
- `reason`
- `derived_from`
- `current_status`
- `suggested_pipeline`

Observed clean-state integrity:

- target domain resolves to a documented governance gap
- action type matches the remediation strategy
- suggested pipeline resolves to an existing pipeline definition

Observed invalid-state integrity:

- canonical next-action surface is not rewritten when roadmap resolution fails
- fail-closed error output is machine-readable and stable
