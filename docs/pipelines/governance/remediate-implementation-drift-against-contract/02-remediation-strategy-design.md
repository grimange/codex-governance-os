# Remediation Strategy Design

| Drift Item | Proposed Change | Strategy Type | Risk Level | Migration Impact | Rollback Strategy |
|------------|-----------------|---------------|------------|------------------|-------------------|
| missing active `005` registry entry | add pipeline `005` to `docs/pipelines/registry/pipeline-registry.md` as `ACTIVE` | implementation correction | low | restores canonical discoverability for the completed audit stage | remove the row if later evidence proves the pipeline was not operationally active |
| current active `006` would otherwise repeat the same defect | add pipeline `006` to `docs/pipelines/registry/pipeline-registry.md` as `ACTIVE` in the same change set as this remediation | lifecycle normalization | low | prevents immediate reintroduction of the audited violation | remove the row if this remediation is later deemed non-operative |
| lingering `PROPOSED` labels in active definitions | defer direct normalization of status text | compatibility isolation | low | no functional change now; residual terminology drift remains visible | no rollback needed because no direct change is applied |

## Strategy Rationale

- The contract defines the registry as the canonical discoverability surface, so registry correction is the minimal authoritative fix.
- Registering `006` in the same change set is necessary because remediation work itself operationalizes that pipeline.
- Status-label normalization is optional for contract compliance and can be handled in later cleanup or verification work.
