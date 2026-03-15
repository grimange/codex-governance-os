# Canon Recomputation

Recomputing verdict families from `docs/governance/pipeline-run-ledger.md` using
the first-match canon rules in
`docs/governance/verdict-family-classification-canon.md` yields:

- VERIFIED: `16`
- ESTABLISHED: `14`
- NORMALIZED: `4`
- IMPLEMENTED: `3`
- WITH_LIMITATIONS: `10`
- WITH_GAPS: `1`
- RESTRICTED: `0`
- OTHER: `12`

Total verdict records recomputed: `60`.

The recomputation is deterministic and matches the bounded overlap policy used by
Pipeline 146 (first-match precedence for overlapping patterns).
