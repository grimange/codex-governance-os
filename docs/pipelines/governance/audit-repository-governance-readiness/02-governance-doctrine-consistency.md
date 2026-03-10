# Governance Doctrine Consistency

## Consistency Checks

| Check | Result | Severity | Notes |
|-------|--------|----------|-------|
| `AGENTS.md` authority references | consistent | informational | Constitution elevates repository state, doctrine, registered pipelines, and generated artifacts in a coherent order. |
| architecture doctrine authority model | consistent | informational | Doctrine refines the constitution without contradicting it. |
| contract authority expectations | partially specified | moderate | Constitution and doctrine route contracts to `docs/contracts/`, but no contract authority model exists yet because the surface is placeholder-only. |
| pipeline governance expectations | partially consistent | moderate | Constitution requires active pipelines to be registered, but pipeline `002` is active in practice and absent from the registry. |

## Contradictions

1. Active-pipeline discoverability is inconsistent.
   Evidence: `AGENTS.md` says active pipelines must be registered, while pipeline `002` is being executed but `docs/pipelines/registry/pipeline-registry.md` lists only `000` and `001`.

2. Catalog maturity exceeds non-governance documentation maturity.
   Evidence: governance doctrine and governance pipelines exist, while `docs/contracts/` and `docs/modernization/` remain placeholders.

## Conclusion

The core doctrine stack is internally coherent. The main consistency issues are operational completeness rather than conflicting authority language.
