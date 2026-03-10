# Authority Model Audit

| Audit Topic | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| source-of-truth ownership remains with version-controlled repository state | compliant | `AGENTS.md`, doctrine, contract, and registry are all tracked repository artifacts | no competing external authority surface was found |
| registry is treated as discoverability state rather than procedural authority | compliant | doctrine and contract both describe the registry as a discoverability surface subordinate to pipeline definitions | no registry entry attempts to redefine pipeline procedure |
| registered entries point to real pipeline definitions | compliant | registry entries `000` through `004` resolve to existing files | no stale or missing targets found |
| state mutations occur in the allowed layer | partially compliant | active-pipeline listing state lives in `docs/pipelines/registry/pipeline-registry.md`, but active use of `005` has not yet been reflected there | authority ownership is correct, update discipline is not |
| projections are not treated as authoritative over higher layers | compliant | generated artifacts consistently describe themselves as evidence and cite higher-order authorities | no artifact was found overriding doctrine, constitution, or contract |
| command boundaries are respected | non-compliant | the contract prohibits operating an active pipeline without a registry entry; `005` is currently being operated and is absent from the registry | this is the clearest contract violation in the current audit |
| lifecycle authority is consistent with doctrine | partially compliant | doctrine says proposed specifications become active when registered and used; repository history also shows active use can precede status-label normalization | operational reality is preserved, but descriptive labels still lag |

## Findings

- Compliant behavior: the authority stack is explicit and coherent across constitution, doctrine, contract, and registry.
- Partial compliance: the registry remains the intended owner of activation state, but not all operational activations are being recorded immediately.
- Authority violation: pipeline `005` is active in practice and absent from `docs/pipelines/registry/pipeline-registry.md`.
- Ambiguous surface: `006` and `007` are implemented definitions for downstream stages, but present evidence does not prove they are already operationally active.
