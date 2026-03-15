# Dimension Mapping Verification

## Verified Dimensions In Scorecard

- Governance Execution
- Governance Safety
- Governance Coverage
- Governance Intelligence

## Evidence Mapping

Each scorecard dimension maps to observable repository evidence:

| Scorecard Dimension | Observable Evidence |
|---|---|
| Governance Execution | verdict-family counts in `docs/governance/pipeline-run-analytics.md` |
| Governance Safety | bounded verdict-family counts in `docs/governance/pipeline-run-analytics.md` |
| Governance Coverage | backfilled-run and unresolved-gap counts in `docs/governance/pipeline-run-analytics.md` and explicit gap statements in `docs/governance/pipeline-run-ledger.md` |
| Governance Intelligence | existence of ledger, analytics, and verdict canon surfaces under `docs/governance/` |

## Layer-Oriented Mapping Assessment

Pipeline 150 lists example governance dimensions such as Governance Doctrine,
Pipeline Governance, Execution Governance, Observability / Evidence, and
Governance Intelligence.

The scorecard does not use those exact labels. Instead, it uses
capability-oriented dimensions derived from cross-cutting evidence surfaces.

Verification result:

- dimension coverage is explicit and evidence-backed
- dimension naming is deterministic
- mapping to example governance layers is partial rather than literal

This is a bounded limitation, not a verification failure, because each
dimension still references observable artifacts and pipeline outcomes.
