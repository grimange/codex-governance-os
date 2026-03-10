# Drift Item Consolidation

| Drift Category | Contract Rule Violated | Implementation Surface | Severity | Evidence | Subsystem Impact |
|----------------|------------------------|------------------------|----------|----------|------------------|
| authority drift | every active pipeline must have a corresponding registry entry | `docs/pipelines/registry/pipeline-registry.md` | HIGH | active execution of `005` was not represented in the registry | canonical activation state was incomplete |
| lifecycle drift | registry updates must occur no later than the same governed change set that activates a pipeline | `docs/pipelines/registry/pipeline-registry.md` | HIGH | `005` became operational without same-change-set registry publication | lifecycle transition evidence was implicit rather than published |
| interface drift | audits should determine active governance coverage from the registry | `docs/pipelines/registry/pipeline-registry.md` | MODERATE | active `005` required inference from execution context | discoverability interface underreported active governance scope |
| compatibility drift | proposed text does not excuse omission and should not obscure active use | active pipeline definitions, especially `001`, `003`, `004`, `005`, and `006` | MODERATE | multiple active definitions still say `PROPOSED` | terminology drift increases interpretation cost but does not block discoverability once registry is correct |

## Consolidation Decision

The remediation target for this execution is the blocking registry completeness defect. Compatibility-era status-label drift remains relevant but is treated as secondary because the contract makes registry completeness, not definition-label normalization, the operative compliance boundary.
