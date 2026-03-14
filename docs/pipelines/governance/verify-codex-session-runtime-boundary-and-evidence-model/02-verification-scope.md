# Verification Scope

The verification scope for Pipeline `114` includes:

- `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`
- `docs/contracts/codex-session-state-machine-canon.md`
- `docs/governance/codex-session-registry.md`
- `docs/governance/codex-session-ledger.md`
- `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
- `docs/governance/architecture-doctrine.md`
- `.codex/AGENTS.md`
- `README.md`
- `docs/pipelines/registry/pipeline-registry.md`

Verification criteria:

1. The runtime-boundary canon preserves the canonical session lifecycle and
   does not introduce conflicting lifecycle states.
2. `session_id` remains the authoritative session identity across runtime,
   registry, and ledger semantics.
3. Registry and ledger meaning remain canonical and documentation-governed.
4. The runtime-boundary canon introduces compatibility rules, not runtime
   implementation requirements.
5. The canon is discoverable from the required repository entry surfaces.
