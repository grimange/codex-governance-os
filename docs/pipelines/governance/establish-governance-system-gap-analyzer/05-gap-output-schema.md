# Gap Output Schema

Pipeline 166 establishes the canonical machine-readable gap surface:

- `docs/governance/governance-system-gaps.json`

Schema fields:

- `overall_gap_state`
- `detected_gaps`
- `sources`
- `current_governance_maturity_reference`
- `overall_system_maturity`

Per-gap fields:

- `gap_id`
- `domain`
- `classification`
- `severity`
- `reason`
- `evidence_sources`
- `blocking_effect`
- `recommended_remediation_type`
- `recommended_pipeline_candidates`
