# Final Verdict

Verdict: `GOVERNANCE_RUN_ANALYTICS_CANON_ALIGNMENT_VERIFIED`

## Result

- Canonical verdict-family recomputation from ledger output is exact.
- `docs/governance/pipeline-run-analytics.md` verdict-family counts match recomputation.
- Ledger and canon were not modified during verification.
- Analytics now explicitly references the verdict-family canon.
- `python tools/governance/preflight.py` returns **PASS**.

## Distribution Check

- IMPLEMENTED: `3`
- ESTABLISHED: `14`
- VERIFIED: `16`
- NORMALIZED: `4`
- WITH_LIMITATIONS: `10`
- WITH_GAPS: `1`
- RESTRICTED: `0`
- OTHER: `12`
