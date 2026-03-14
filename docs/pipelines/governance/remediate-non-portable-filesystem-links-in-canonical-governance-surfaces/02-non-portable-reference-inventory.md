# Non-Portable Reference Inventory

## In-Scope References Remediated

| source document | non-portable reference pattern | intended canonical target | portable replacement |
|-----------------|-------------------------------|---------------------------|----------------------|
| `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md` | `/home/.../docs/contracts/codex-session-state-machine-canon.md` | `docs/contracts/codex-session-state-machine-canon.md` | `../contracts/codex-session-state-machine-canon.md` |
| `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md` | `/home/.../docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md` | `docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md` | `codex-session-handoff-contract-and-resume-evidence-model.md` |
| `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md` | `/home/.../docs/governance/codex-session-admission-and-activation-rules.md` | `docs/governance/codex-session-admission-and-activation-rules.md` | `codex-session-admission-and-activation-rules.md` |
| `docs/contracts/codex-session-handoff-packet-and-continuity-contract.md` | `/home/.../docs/contracts/codex-session-state-machine-canon.md` | `docs/contracts/codex-session-state-machine-canon.md` | `codex-session-state-machine-canon.md` |
| `docs/contracts/codex-session-handoff-packet-and-continuity-contract.md` | `/home/.../docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md` | `docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md` | `../governance/codex-session-handoff-contract-and-resume-evidence-model.md` |
| `docs/governance/codex-session-registry.md` | `/home/.../docs/contracts/codex-session-state-machine-canon.md` | `docs/contracts/codex-session-state-machine-canon.md` | `../contracts/codex-session-state-machine-canon.md` |
| `docs/governance/codex-session-registry.md` | `/home/.../docs/governance/codex-session-ledger.md` | `docs/governance/codex-session-ledger.md` | `codex-session-ledger.md` |
| `docs/governance/codex-session-ledger.md` | `/home/.../docs/contracts/codex-session-state-machine-canon.md` | `docs/contracts/codex-session-state-machine-canon.md` | `../contracts/codex-session-state-machine-canon.md` |
| `docs/codex/sessions/handoffs/README.md` | `/home/.../docs/contracts/codex-session-handoff-packet-and-continuity-contract.md` | `docs/contracts/codex-session-handoff-packet-and-continuity-contract.md` | `../../../contracts/codex-session-handoff-packet-and-continuity-contract.md` |
| `docs/codex/sessions/handoffs/README.md` | `/home/.../docs/governance/codex-session-registry.md` | `docs/governance/codex-session-registry.md` | `../../../governance/codex-session-registry.md` |
| `docs/codex/sessions/handoffs/README.md` | `/home/.../docs/governance/codex-session-ledger.md` | `docs/governance/codex-session-ledger.md` | `../../../governance/codex-session-ledger.md` |
| `docs/pipelines/governance/verify-codex-session-admission-and-activation-rules/02-verification-scope.md` | `/home/...` links to inspected surfaces | active Layer 6 sources and `106` verdict artifact | document-relative links to the same targets |
| `docs/pipelines/governance/verify-codex-session-admission-and-activation-rules/03-layer-authority-verification.md` | `/home/.../docs/contracts/codex-session-state-machine-canon.md` | `docs/contracts/codex-session-state-machine-canon.md` | `../../../contracts/codex-session-state-machine-canon.md` |
| `docs/pipelines/governance/verify-codex-session-admission-and-activation-rules/06-discoverability-verification.md` | `/home/...` links to entry surfaces | `architecture-doctrine.md`, `.codex/AGENTS.md`, `README.md` | document-relative links to the same targets |
| `docs/pipelines/governance/verify-codex-session-admission-and-activation-rules/08-final-verdict.md` | `/home/.../docs/contracts/codex-session-state-machine-canon.md` | `docs/contracts/codex-session-state-machine-canon.md` | `../../../contracts/codex-session-state-machine-canon.md` |

## In-Scope Path-Truth Drift Corrected

| source document | pre-remediation path text | canonical repository truth | remediation |
|-----------------|---------------------------|----------------------------|-------------|
| `docs/pipelines/governance/107--verify-codex-session-admission-and-activation-rules.md` | `docs/governance/codex-session-state-machine-canon.md` in `affects` | `docs/contracts/codex-session-state-machine-canon.md` | updated active lane definition to the canonical contracts path |

## Repository-Wide Drift Left Out Of Scope

The repository still contains many historical `/home/...` links outside the
Layer 6 and `107`-bundle scope of this lane. Those remaining references were
inventoried during discovery but intentionally not normalized here to keep
pipeline `108` bounded to the surfaces it names.
