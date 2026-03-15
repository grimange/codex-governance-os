# Verdict Ledger Inventory

## Source

`docs/governance/pipeline-run-ledger.md`

Primary parsing assumptions:

- each `## Pipeline Run Record` contains one `final_verdict:`.
- each final verdict is read from the line immediately following `final_verdict:`.

## Counts

- total parsed ledger records: `60`
- unique final verdict strings observed: `60`
- latest ledger run: `141`
- latest ledger title: `Backfill Historical Pipeline Run Ledger Coverage`

## Canon Family Totals (ledger-derived)

- VERIFIED: `16`
- ESTABLISHED: `14`
- NORMALIZED: `4`
- IMPLEMENTED: `3`
- WITH_LIMITATIONS: `10`
- WITH_GAPS: `1`
- RESTRICTED: `0`
- OTHER: `12`

## Notes

- Pipeline 141 appears as the final record and remains `WITH_GAPS`.
- No ledger final verdict string was blank or unparseable under the block parser.
