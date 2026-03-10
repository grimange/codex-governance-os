# Supporting Surface Updates

## Updated

- `docs/governance/contract-discovery-ledger.md`
  Reason: installed the durable governance ledger required by this pipeline.
- `.codex/AGENTS.md`
  Reason: added an explicit pointer so agents can treat the contract discovery ledger as an operational planning surface.

## Intentionally Left Unchanged

- `AGENTS.md`
  Reason: the constitution already points contract work to `docs/contracts/` and does not need ledger-specific routing to remain valid.
- `docs/governance/architecture-doctrine.md`
  Reason: the doctrine already supports evidence-based contract discovery and did not require revision for this pipeline.
- `docs/pipelines/registry/pipeline-registry.md`
  Reason: this discovery pipeline records contract candidates but does not itself resolve registry completeness gaps.

## Stale References Remaining

- active pipeline registration remains incomplete because pipeline `002` is still absent from the registry
- some active pipeline definitions still carry descriptive status labels that lag operational use
