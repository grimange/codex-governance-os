# Problem Statement

Pipeline `100` introduced the canonical schema and registry-path discipline
that recent Layer 6 Codex session-governance verification lanes depend on.

That normalization established:

- `docs/contracts/codex-governance-surface-schema-contract.md` as the
  canonical schema surface
- explicit `pipeline_definition_path` and `artifact_bundle_path` fields in the
  pipeline registry contract and registry table
- canonical session lifecycle field names `start_date` and `closure_date`

Pipeline `101` verifies that these normalized expectations are now reflected in
the active governance surfaces that use them, and that any deprecated field
names remain bounded to historical evidence or explanatory normalization
records rather than active schema dependencies.
