# Governance Risk Assessment

| Severity | Affected Governance Surface | Description | Evidence |
|----------|-----------------------------|-------------|----------|
| MODERATE | pipeline registry | Active pipeline `002` is not registered even though the constitution requires registration for active pipelines. | `AGENTS.md` registration rule and current registry contents. |
| MODERATE | governance sequencing | Lifecycle coverage stops at audit; remediation, verification, and promotion categories exist only as placeholders. | Empty category roots under `docs/pipelines/`. |
| MODERATE | contract and modernization surfaces | Canonical roots exist without authority or operational content, which can lead to overstated governance maturity. | `.gitkeep`-only directories in `docs/contracts/` and `docs/modernization/`. |
| LOW | worktree governance discipline | Pipeline `002` definition is currently modified in the worktree during execution, which means operational governance inputs are not yet fully settled in a committed snapshot. | `git diff` shows the pipeline text as an unstaged modification. |

## Assessment

No blocking governance defect is present. The main risks concern completeness and discoverability rather than authority collapse.
