# Final Verdict

Verdict: `GOVERNANCE_VERDICT_FAMILY_CLASSIFICATION_VERIFIED_WITH_LEGACY_OTHER_VERDICTS`

## Summary

- Canonical ledger mapping is deterministic and complete for all `60` final verdicts.
- Legacy verdict strings outside canonical token patterns are explicitly and fully categorized as `OTHER` (`12` values).
- Overlapping textual rule matches are bounded and resolved by explicit first-match order.
- Preflight checks pass with no portability violations (`violations: 0`).

## Limitation

- Analytics consistency is not aligned with the canonical mapping yet.
- Expected canonical counts differ from `docs/governance/pipeline-run-analytics.md` by:
  - `VERIFIED` (`17` reported vs `16` expected),
  - `ESTABLISHED` (`17` vs `14`),
  - `NORMALIZED` (`3` vs `4`),
  - `IMPLEMENTED` (`0` vs `3`).
- The bounded mismatch is directly traceable to legacy aggregation semantics in the analytics surface and is explicitly documented.
