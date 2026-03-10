# Authority Surface Analysis

| Surface | Classification | Where Truth Appears To Originate | State Authoring Rule | Notes |
|---------|----------------|----------------------------------|----------------------|-------|
| version-controlled repository state | canonical authority | tracked files at a given revision | authors canonical repository truth | highest authority substrate |
| `AGENTS.md` | canonical authority | constitutional governance rules | authors repository-local governance expectations | governs routing and precedence |
| `docs/governance/architecture-doctrine.md` | canonical authority | architecture interpretation rules | authors architecture meaning and layer responsibilities | subordinate only to repository state and constitution |
| `.codex/AGENTS.md` | likely authority candidate | agent operating constraints | may constrain agent behavior but must not contradict higher surfaces | operational support surface |
| pipeline definitions under `docs/pipelines/governance/` | canonical authority when active | pipeline procedures | author required phases, outputs, and decisions | registry affects discoverability, not intrinsic semantics |
| `docs/pipelines/registry/pipeline-registry.md` | likely authority candidate | active-pipeline visibility | may state activation status but must not redefine pipeline logic | incomplete when active pipelines are omitted |
| per-pipeline artifact directories | derived/projection | prior execution evidence | may record decisions and verification results only | useful for audit, not higher-order authority |
| `docs/contracts/.gitkeep` | compatibility layer | none yet | must not author contract truth | placeholder only |
| `docs/modernization/.gitkeep` | compatibility layer | none yet | must not author governance or contract truth | placeholder only |

## Authority Questions Answered

- Truth originates in tracked governance documents and repository state, not in runtime systems.
- State authoring is limited to constitutional, doctrinal, registry, and pipeline-definition edits within version control.
- Pipeline artifacts consume and project state; they do not author higher-order truth.
- The most important contract boundaries are required around governance authority, pipeline orchestration, registry integrity, and placeholder handling to prevent false authority.
- The principal authority conflict today is operational: active pipeline usage is broader than the registry record.
