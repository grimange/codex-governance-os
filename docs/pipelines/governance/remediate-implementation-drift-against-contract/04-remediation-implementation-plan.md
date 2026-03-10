# Remediation Implementation Plan

| File | Change | Contract Rule Addressed |
|------|--------|-------------------------|
| `docs/pipelines/registry/pipeline-registry.md` | add `005` registry entry with canonical path and `ACTIVE` status | every active pipeline must have exactly one corresponding registry entry |
| `docs/pipelines/registry/pipeline-registry.md` | add `006` registry entry with canonical path and `ACTIVE` status in the same governed change set as execution | registry updates must occur no later than the same governed change set that activates a pipeline |
| `docs/pipelines/governance/remediate-implementation-drift-against-contract/*.md` | record remediation rationale, execution, evidence, and residual observations | remediation must be evidence-based and reviewable |

## Intentionally Deferred

- Direct edits to active pipeline definition status labels are deferred because registry completeness is the canonical compliance requirement and the current remediation objective is to eliminate the blocking discoverability defect first.
