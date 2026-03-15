# Ledger Input Analysis

Input source:

- `docs/governance/pipeline-run-ledger.md`

Observed parse scope:

- total pipeline records: `60`
- seeded block and continuation records are included because they are part of canonical history
- backfilled runs are the historical records with `pipeline_id < 137`: `55`
- unresolved historical gaps remain explicit: `6`

Derived run set:

- all entries are parsed directly from `## Pipeline Run Record` blocks
- no synthetic rows or inferred history was introduced
- latest ledger run before this lane: `141`
