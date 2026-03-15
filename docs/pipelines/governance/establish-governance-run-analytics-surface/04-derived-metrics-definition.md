# Derived Metrics Definition

1) Governance Run Summary

- `total_runs`: number of parsed ledger records
- `latest_run_id`: numeric maximum across `pipeline_id`
- `latest_run_title`: ledger `title` for the max `pipeline_id`
- `latest_run_verdict`: ledger `final_verdict` for the max `pipeline_id`
- `restriction_count`: count of records with `restriction_status` not equal to `none`

2) Pipeline Type Distribution

- `execution_class_distribution`: grouped count of `execution_class` values
- distribution remains transparent to original execution classes even when non-canonical labels appear

3) Verdict Distribution

- `VERIFIED`: verdict string contains `VERIFIED`
- `ESTABLISHED`: verdict string contains `ESTABLISHED` or `IMPLEMENTED`
- `NORMALIZED`: verdict string contains `NORMALIZED`
- `WITH_LIMITATIONS`: verdict string contains `WITH_LIMITATIONS` or `WITH_RESTRICTIONS`
- `WITH_GAPS`: verdict string contains `GAP` or `GAPS`
- `OTHER`: any remaining ledger verdict not matching above rules

4) Recent Activity

- latest 10 records by ledger order (descending from appended surface)
- fields: `pipeline_id`, `title`, `final_verdict`, `artifact_bundle`

5) Historical Coverage

- `backfilled_runs`: count of entries with `pipeline_id < 137`
- `unresolved_gaps`: count of explicit entries where ledger states `registry_id unavailable in historical definition`
- these values are copied from ledger and verification inventory rather than inferred
