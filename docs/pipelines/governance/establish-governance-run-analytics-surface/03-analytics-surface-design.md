# Analytics Surface Design

Target surface:

- `docs/governance/pipeline-run-analytics.md`

Structure:

- Run Summary
- Pipeline Type Distribution
- Verdict Distribution
- Recent Governance Activity
- Historical Coverage

Data lineage rules:

- every value must be read from an explicit ledger field
- no derived scorecards are introduced beyond counting and grouping
- no ledger records are rewritten by this lane
- any non-standard values are kept literal so they remain auditable

Derived fields:

- `total_runs` = count of parsed `pipeline_id` records
- `latest_run_id` = max parsed `pipeline_id`
- `pipeline_type_distribution` = counts by `execution_class`
- `verdict_distribution` = counts by verdict family (heuristic family mapping)
- `restricted_count` = count where `restriction_status` != `none`
- `historical_backfill_count` = parsed records with `pipeline_id < 137`
