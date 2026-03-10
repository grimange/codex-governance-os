# Supporting Surface Updates

## Updated

- `docs/governance/architecture-doctrine.md`
  Reason: replaced the bootstrap baseline with a repository-evidence-based doctrine.
- `docs/pipelines/registry/pipeline-registry.md`
  Reason: recorded pipeline 001 as an active governance surface so discoverability matches operational use.
- `.codex/AGENTS.md`
  Reason: clarified that agents must treat the architecture doctrine as the canonical interpretation layer for repository structure and pipeline artifacts.

## Intentionally Left Unchanged

- `AGENTS.md`
  Reason: the constitution already contains the correct high-level authority ordering and routing rules.
- `docs/contracts/` and `docs/modernization/`
  Reason: these remain reserved roots without current domain content.
- `docs/pipelines/governance/000--initialize-governed-project.md`
  Reason: initialization authority remains historically valid and does not need retroactive revision.

## Stale References Remaining

- `docs/pipelines/governance/001--discover-existing-architecture-and-establish-doctrine.md` still carries `Status: PROPOSED` in its body text, which is now a descriptive mismatch with active use. The registry update makes the active state discoverable, but the pipeline specification itself should eventually be normalized if the repository wants definition and registry status labels to match exactly.
