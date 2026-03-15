# Schema Review

Observed canonical fields in `docs/governance/governance-system-gaps.json`:

- `overall_gap_state`
- `detected_gaps`
- `sources`
- `current_governance_maturity_reference`
- `overall_system_maturity`

Observed per-gap fields:

- `gap_id`
- `domain`
- `classification`
- `severity`
- `reason`
- `evidence_sources`
- `blocking_effect`
- `recommended_remediation_type`
- `recommended_pipeline_candidates`

Schema review result:

- the gap surface is valid JSON
- the schema is machine-readable and stable
- required evidence, classification, and remediation-linkage fields are present
