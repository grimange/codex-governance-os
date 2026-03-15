# Pipeline Run Analytics Surface

This document is derived from [`docs/governance/pipeline-run-ledger.md`](pipeline-run-ledger.md#L1) and is for operational interpretation only.
Verdict-family counts in section 3 are derived by applying
[`docs/governance/verdict-family-classification-canon.md`](verdict-family-classification-canon.md#L1)
to each ledger final verdict.

It summarizes governance execution history while preserving ledger-recorded truth.

## 1) Run Summary

Total recorded runs: `60`  
Latest recorded run: pipeline `141`  
Latest recorded title: `Backfill Historical Pipeline Run Ledger Coverage`  
Latest recorded verdict: `PIPELINE_RUN_LEDGER_HISTORICAL_COVERAGE_BACKFILLED_WITH_GAPS`  
Restricted or limited runs: `12`

## 2) Pipeline Type Distribution

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

## 3) Verdict Distribution

- IMPLEMENTED: `3`
- ESTABLISHED: `14`
- VERIFIED: `16`
- NORMALIZED: `4`
- WITH_LIMITATIONS: `10`
- WITH_GAPS: `1`
- RESTRICTED: `0`
- OTHER: `12`

## 4) Recent Governance Activity (Latest 10 Runs)

| Pipeline ID | Title | Final Verdict | Artifact Bundle |
|---|---|---|---|
| 132 | Establish Multi-Session Continuity Evidence Harness | MULTI_SESSION_CONTINUITY_EVIDENCE_HARNESS_ESTABLISHED_WITH_STRICT_CROSS_SESSION_BOUNDS | docs/pipelines/governance/establish-multi-session-continuity-evidence-harness/ |
| 133 | Verify Multi-Session Continuity Evidence Harness | MULTI_SESSION_CONTINUITY_EVIDENCE_HARNESS_VERIFIED_WITH_STRICT_CROSS_SESSION_BOUNDS | docs/pipelines/governance/verify-multi-session-continuity-evidence-harness/ |
| 134 | Establish Multi-Session Continuity Evaluation Scenarios | MULTI_SESSION_CONTINUITY_EVALUATION_SCENARIOS_ESTABLISHED_WITH_BOUNDARY_COVERAGE | docs/pipelines/governance/establish-multi-session-continuity-evaluation-scenarios/ |
| 135 | Verify Multi-Session Continuity Evaluation Scenarios | MULTI_SESSION_CONTINUITY_EVALUATION_SCENARIOS_VERIFIED_WITH_FULL_BOUNDARY_COVERAGE | docs/pipelines/governance/verify-multi-session-continuity-evaluation-scenarios/ |
| 136 | Implement Multi-Session Continuity Evidence Harness | MULTI_SESSION_CONTINUITY_EVIDENCE_HARNESS_IMPLEMENTED | docs/pipelines/governance/implement-multi-session-continuity-evidence-harness/ |
| 137 | Verify Multi-Session Continuity Evidence Harness | MULTI_SESSION_CONTINUITY_EVIDENCE_HARNESS_VERIFIED_WITH_RESTRICTIONS | docs/pipelines/governance/verify-multi-session-continuity-evidence-harness-implementation/ |
| 138 | Normalize Multi-Session Continuity Evidence Harness Pipeline | MULTI_SESSION_CONTINUITY_EVIDENCE_HARNESS_PIPELINE_NORMALIZED | docs/pipelines/governance/normalize-multi-session-continuity-evidence-harness-pipeline/ |
| 139 | Establish Centralized Pipeline Run Ledger | CENTRALIZED_PIPELINE_RUN_LEDGER_ESTABLISHED_WITH_LIMITED_HISTORY | docs/pipelines/governance/establish-centralized-pipeline-run-ledger/ |
| 140 | Verify Centralized Pipeline Run Ledger Integrity and Historical Mapping | CENTRALIZED_PIPELINE_RUN_LEDGER_VERIFIED_WITH_LIMITATIONS | docs/pipelines/governance/verify-centralized-pipeline-run-ledger-integrity-and-historical-mapping/ |
| 141 | Backfill Historical Pipeline Run Ledger Coverage | PIPELINE_RUN_LEDGER_HISTORICAL_COVERAGE_BACKFILLED_WITH_GAPS | docs/pipelines/governance/backfill-historical-pipeline-run-ledger-coverage/ |

Note: Pipeline `142` (Verify Historical Pipeline Run Ledger Backfill Integrity) and `143` are not in this table because this analytics surface is derived from ledger state before execution of those lanes.

## 5) Historical Coverage

Backfilled historical runs: `55`  
Explicit unresolved gaps: `6`  
Unresolved gap paths are documented in:

- `docs/pipelines/governance/close-unsupported-framework-scheduler-composition-boundaries/`
- `docs/pipelines/governance/establish-codex-session-lifecycle-observation-discipline/`
- `docs/pipelines/governance/establish-codex-session-runtime-boundary-and-evidence-model/`
- `docs/pipelines/governance/migrate-core-governance-lanes-to-universal-templates/`
- `docs/pipelines/governance/move-template-system-and-registry-under-docs-root-governance-tree/`
- `docs/pipelines/governance/verify-framework-scheduler-composition-boundaries-remain-non-drifting/`

No inferred runs were added to this analytics surface. All numbers are derived from ledger records.
