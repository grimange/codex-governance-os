# Governance Capability Inventory

## Canonical Inputs

- `docs/governance/pipeline-run-ledger.md`
  - canonical execution memory
  - reports append-only run history, artifact-bundle traceability, and explicit
    historical gaps
- `docs/governance/pipeline-run-analytics.md`
  - derived operational interpretation layer
  - reports total runs, verdict-family distribution, restriction signals, and
    historical coverage counts
- `docs/governance/verdict-family-classification-canon.md`
  - deterministic classification rules for verdict families used in analytics
    and maturity reporting

## Capability Signals Available For Scoring

- positive execution-family counts:
  - `IMPLEMENTED`: `3`
  - `ESTABLISHED`: `14`
  - `VERIFIED`: `16`
  - `NORMALIZED`: `4`
- bounded governance-family counts:
  - `WITH_LIMITATIONS`: `10`
  - `WITH_GAPS`: `1`
  - `RESTRICTED`: `0`
- governance history totals:
  - total recorded runs: `60`
  - backfilled historical runs: `55`
  - explicit unresolved historical gaps: `6`
- governance intelligence surfaces present:
  - ledger: present
  - analytics: present
  - verdict-family canon: present

## Boundaries

- Pipeline 149 derives scores from existing governance evidence only.
- Pipeline 149 does not add, rewrite, or normalize ledger history.
- Pipeline 149 does not recompute analytics into a competing source of truth.
