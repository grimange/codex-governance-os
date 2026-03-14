# Normalization Specification

Installed canonical schema surface:

- [codex-governance-surface-schema-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/codex-governance-surface-schema-contract.md)

Canonical field names established or reaffirmed:

- `session_id`
- `start_date`
- `closure_date`
- `registry_id`
- `pipeline_definition_path`
- `artifact_bundle_path`

Deprecated aliases now treated as non-canonical in authoritative lane
definitions:

- `session_start`
- `session_end`

Normalization target:

- authoritative contracts, doctrine references, active lane definitions, and
  the pipeline registry

Historical artifact bundles remain preserved as evidence even when they still
mention the pre-normalization drift.
