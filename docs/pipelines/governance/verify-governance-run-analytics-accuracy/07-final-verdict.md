# Final Verdict

Verdict: GOVERNANCE_RUN_ANALYTICS_SURFACE_VERIFIED_WITH_LIMITATIONS

## Summary

- Analytics surface exists and is derived from `docs/governance/pipeline-run-ledger.md`.
- Run count and latest run identity/checks pass exactly.
- Pipeline type distribution matches ledger truth exactly.
- Latest activity window matches ledger order exactly.
- Backfill count and explicit gap count match verified evidence.
- Registry cross-references are consistent.
- Verdict family aggregation is boundedly inconsistent:
  - analytics reported `VERIFIED: 17` and `NORMALIZED: 3`
  - ledger-derived grouping resolves to `VERIFIED: 16` and `NORMALIZED: 4`
- Limitation is explicitly documented and bounded, with no inferred runs added or ledger mutation.
