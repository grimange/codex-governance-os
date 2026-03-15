# Historical Backfill, Gap, and Registry Check

## Historical Backfill and Gap Accuracy

- Ledger-derived historical backfill count (`pipeline_id < 137`): `55`
- Analytics-reported backfill count: `55`
- Explicit gap entries from `backfill-historical-pipeline-run-ledger-coverage/02-historical-artifact-inventory.md`: `6`
- Analytics-reported explicit gap count: `6`
- Exact gap paths were confirmed unchanged.

Result: **PASS**

## Registry Cross-Reference Check

Registry reflects both analytics establishment and this verification lane:

- `143` row exists and points to `docs/pipelines/governance/143--establish-governance-run-analytics-surface.md`
- `144` row exists and points to `docs/pipelines/governance/verify-governance-run-analytics-accuracy/`
- ledger canonicality note still points to `docs/governance/pipeline-run-ledger.md`

Result: **PASS**
