# 05 — Analytics Aggregation Guidance

Analytics must derive verdict-family counts from `docs/governance/pipeline-run-ledger.md` using this canon and must not infer custom family semantics.

Aggregation requirements:

- classify each ledger final verdict using the mapping rules exactly
- total counts are the tally of classified results across all ledger records
- store only the derived totals and the canonical rule set used
- leave raw verdict strings unchanged
- treat any unmapped values as `OTHER`

Analytics values should reference this canon for reproducibility.
