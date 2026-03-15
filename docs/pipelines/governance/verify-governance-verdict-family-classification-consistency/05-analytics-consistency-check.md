# Analytics Consistency Check

Canonical recomputation from the ledger and direct aggregation yields:

- VERIFIED: `16`
- ESTABLISHED: `14`
- NORMALIZED: `4`
- IMPLEMENTED: `3`
- WITH_LIMITATIONS: `10`
- WITH_GAPS: `1`
- RESTRICTED: `0`
- OTHER: `12`

Current analytics report (`docs/governance/pipeline-run-analytics.md`) reports:

- VERIFIED: `17`
- ESTABLISHED: `17`
- NORMALIZED: `3`
- IMPLEMENTED: `0`
- WITH_LIMITATIONS: `10`
- WITH_GAPS: `1`
- OTHER: `12`

## Variance

- VERIFIED is +1 in analytics, expected to be one less.
- ESTABLISHED is +3 in analytics, expected to be three less.
- NORMALIZED is -1 in analytics, expected to be one more.
- IMPLEMENTED is missing from analytics (`0` vs expected `3`).

The variance is bounded to the following canonical-rule drift:

- `UNIVERSAL_TEMPLATE_LINTER_IMPLEMENTED_AND_READY_FOR_GOVERNED_ADMISSION` (pipeline `20`) is expected `IMPLEMENTED` but is not present in current analytics families.
- `LARAVEL_MONOREPO_COMPOSITION_IMPLEMENTED_AND_CERTIFIED` (pipeline `44`) is expected `IMPLEMENTED` but is not present in current analytics families.
- `MULTI_SESSION_CONTINUITY_EVIDENCE_HARNESS_IMPLEMENTED` (pipeline `136`) is expected `IMPLEMENTED` but is not present in current analytics families.
- `MULTI_SESSION_CONTINUITY_EVIDENCE_HARNESS_PIPELINE_NORMALIZED` (pipeline `138`) is expected `NORMALIZED` but is currently aggregated as `VERIFIED`.

Status: **FAIL (bounded and explainable)** for strict analytics consistency.
