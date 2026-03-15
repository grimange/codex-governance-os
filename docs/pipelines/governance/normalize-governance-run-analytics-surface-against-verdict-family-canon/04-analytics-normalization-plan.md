# Analytics Normalization Plan

1. Preserve all non-verdict sections of `docs/governance/pipeline-run-analytics.md`:
   - total runs
   - latest run
   - run-type distribution
   - latest 10 run activity
   - historical backfill and gap counts
2. Replace only the verdict-family distribution block to the canon-aligned values.
3. Ensure the canonical family set is explicit and include `OTHER`.
4. Preserve provenance statements that analytics remains derived from
   `docs/governance/pipeline-run-ledger.md` and no ledger mutation occurs.
