# Schema Review

Observed top-level fields in
`docs/governance/governance-system-gap-remediation-plan.json`:

- `generated_by`
- `planner_version`
- `remediation_plan`
- `sources`

Observed per-entry fields:

- `domain`
- `current_status`
- `remediation_strategy`
- `required_evidence`
- `recommended_action`
- `suggested_pipeline`
- `priority`
- `dependency_order`
- `promotion_target`

Schema review result:

- the remediation plan is valid JSON
- the schema is machine-readable and stable
- every remediation entry contains the required fields
