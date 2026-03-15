# Verification

Verification checks performed:

1. Confirmed `docs/governance/pipeline-run-analytics.md` exists.
2. Confirmed summary fields match canonical ledger parsing:
   - total runs: `60`
   - latest run id: `141`
   - latest run title: `Backfill Historical Pipeline Run Ledger Coverage`
3. Confirmed run-type distribution covers the same `execution_class` frequencies as the parsed ledger records.
4. Confirmed verdict family counts are derived from literal `final_verdict` strings and remain traceable.
5. Confirmed recent activity list contains the latest 10 parsed ledger records and matching artifact bundle paths.
6. Confirmed historical backfill and gap counts are copied from ledger text and do not add inferred runs.

Result: verification conditions satisfied for a derived analytics surface.
