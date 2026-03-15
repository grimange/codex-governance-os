# Run-Type and Verdict Distribution Check

## Run-Type Distribution

The ledger-derived `execution_class` frequency was computed directly from all parsed records in `docs/governance/pipeline-run-ledger.md` and compared to the analytics section.

Ledger and analytics match exactly:

- implementation: `4`
- verification: `19`
- expansion: `3`
- certification: `1`
- exercise: `3`
- boundary-closure: `1`
- reverification: `3`
- establishment: `14`
- admission: `2`
- evaluation: `1`
- enforcement: `2`
- integration: `1`
- normalization: `3`
- remediation: `1`
- capability-establishment: `1`
- historical-normalization: `1`

Result: **PASS**

## Verdict Family Distribution

This lane uses a deterministic family grouping rule:

- `VERIFIED` if verdict string contains `VERIFIED`
- `NORMALIZED` if verdict string contains `NORMALIZED`
- `ESTABLISHED` if verdict string contains `ESTABLISHED` or `IMPLEMENTED`
- `WITH_LIMITATIONS` if verdict string contains `WITH_LIMITATIONS` or `WITH_RESTRICTIONS`
- `WITH_GAPS` if verdict string contains `GAP`/`GAPS`
- `OTHER` for remaining verdicts

Ledger-derived actual families:

- ESTABLISHED: `17`
- VERIFIED: `16`
- NORMALIZED: `4`
- WITH_LIMITATIONS: `10`
- WITH_GAPS: `1`
- OTHER: `12`

Analytics-reported families:

- ESTABLISHED: `17`
- VERIFIED: `17`
- NORMALIZED: `3`
- WITH_LIMITATIONS: `10`
- WITH_GAPS: `1`
- OTHER: `12`

Variance:

- one verdict should belong to `NORMALIZED` instead of `VERIFIED` (`MULTI_SESSION_CONTINUITY_EVIDENCE_HARNESS_PIPELINE_NORMALIZED`).

Result: **FAIL (bounded)**.
