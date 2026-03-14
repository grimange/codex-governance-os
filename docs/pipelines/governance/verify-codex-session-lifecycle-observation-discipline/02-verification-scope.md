# Verification Scope

The verification scope for Pipeline `116` includes:

- `docs/governance/codex-session-lifecycle-observation-discipline.md`
- `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
- `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`
- `docs/contracts/codex-session-state-machine-canon.md`
- `docs/governance/codex-session-registry.md`
- `docs/governance/codex-session-ledger.md`
- `docs/governance/architecture-doctrine.md`
- `.codex/AGENTS.md`
- `README.md`
- `docs/pipelines/registry/pipeline-registry.md`

Verification criteria:

1. Lifecycle observation remains subordinate to the state machine.
2. `session_id` remains the canonical lifecycle-observation identity.
3. Registry authority remains intact and no parallel registry is introduced.
4. Ledger authority remains intact and no ledger replacement is introduced.
5. Lifecycle observation remains interpretive and runtime-neutral.
6. Discoverability remains complete across the required entry surfaces.
