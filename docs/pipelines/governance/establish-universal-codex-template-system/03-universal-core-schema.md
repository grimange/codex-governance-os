# Universal Core Schema

## Required Universal Fields

- `title`
- `status`
- `category`
- `stage`
- `objective`
- `depends_on`
- `outputs`
- `success_criteria`
- `governance_mode`
- `execution_mode`
- `restrictions`
- `non_claims`
- `id` or `pipeline_id`

## Family-Specific Normalization

- pipeline documents require `pipeline_id` and normalize `id` as an alias
- other families use `id`
- template aliases are defined in `docs/governance/templates/template-registry.yaml`

## Schema Rule

Optional fields must be declared explicitly in the registry. Informal omission is not treated as an optionality definition.
