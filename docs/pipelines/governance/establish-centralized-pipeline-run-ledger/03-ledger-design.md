# Ledger Design

Canonical ledger location:

- `docs/governance/pipeline-run-ledger.md`

Design objectives:

- centralized governance visibility
- append-only recording discipline
- deterministic artifact-bundle traceability
- exact final-verdict preservation
- explicit bounded-history notes when full retrospective backfill is incomplete

Authority model:

- subordinate to repository state, `AGENTS.md`, architecture doctrine, and the
  pipeline registry integrity contract
- authoritative for centralized pipeline execution history once a run is
  recorded
- not a replacement for the pipeline registry or artifact bundles

Initial establishment scope:

- create the canonical ledger surface
- backfill recent runs `137`, `138`, and `139`
- defer older retrospective backfill to later governed work
