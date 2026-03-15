# Ledger Structure

Each run record in `docs/governance/pipeline-run-ledger.md` preserves:

- `pipeline_id`
- `title`
- `registry_id`
- `execution_class`
- `execution_scope`
- `execution_date`
- `artifact_bundle`
- `final_verdict`
- `restriction_status`
- `supersedes`
- `notes`

Structural rules established by Pipeline `139`:

- run records are appended in execution order
- historical records are never overwritten
- artifact bundle paths must be deterministic and match repository truth
- verdict strings must be exact copies of the recorded final verdicts
- bounded limitations such as partial historical backfill must be explicit

Initial ordering recorded in the new ledger:

- `137`
- `138`
- `139`
