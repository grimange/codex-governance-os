# Subsystem Boundary Discovery

## Strong Contract Candidates

| Subsystem Name | Purpose | Inputs | Outputs | Owned State Or Resources | Boundary Type | Upstream Dependencies | Downstream Consumers | Likely Contract Need | Current Documentation State |
|----------------|---------|--------|---------|--------------------------|---------------|-----------------------|----------------------|----------------------|-----------------------------|
| Governance authority stack | Define mission, authority precedence, and architecture interpretation | repository state, governance decisions | governing rules for repository work | constitutional and doctrinal meaning | authority boundary | version-controlled files | all later pipelines and agents | explicit governance authority contract | partially documented across constitution and doctrine |
| Pipeline orchestration layer | Define required governance workflows and artifact expectations | repository state, doctrine, prior artifacts | phase artifacts, decisions, verdicts | pipeline specifications and phase outputs | orchestration boundary | constitution, doctrine | agents, audits, later pipelines | explicit pipeline orchestration contract | partially documented across pipeline definitions |
| Pipeline registry surface | Expose which pipelines are active governance surfaces | pipeline definitions, governance decisions | active-pipeline listing | registry markdown table | discoverability boundary | pipeline definitions | agents and future audits | explicit registry integrity contract | partially documented, currently incomplete operationally |
| Contract-root stewardship surface | Hold future canonical contracts without misrepresenting maturity | repository structure decisions | reserved contract namespace | `docs/contracts/` | namespace/authority boundary | constitution, doctrine | future contract authoring pipelines | explicit contract-root stewardship contract | missing |
| Pipeline artifact evidence layer | Preserve phase outputs as inspectable evidence without superseding authority | pipeline execution | phase artifact markdown | per-pipeline artifact directories | evidence/projection boundary | pipeline definitions | audits, verifications, future governance decisions | explicit pipeline artifact contract | implied but not consolidated as a standalone contract |

## Non-Boundaries

- placeholder category roots under `docs/pipelines/remediation/`, `docs/pipelines/verification/`, and `docs/pipelines/promotion/` are not yet true governance subsystems because they do not own active behavior
- `docs/modernization/.gitkeep` is only a reserved location, not a subsystem
- absent application modules, APIs, state stores, queues, or UI layers are not contract candidates because no evidence of real subsystem behavior exists
