# Layer 6 Subordination Check

## Inputs Inspected

- `docs/governance/session-reconstruction-verification-harness.md`
- `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
- `docs/governance/governance-evidence-interpretation-canon.md`
- `docs/governance/governance-safety-invariants-canon.md`
- `docs/governance/codex-session-evidence-interpretation-model.md`
- `docs/governance/codex-session-reconstruction-rules.md`

## Findings

- The harness canon places the repository-wide evidence interpretation canon,
  governance safety invariants canon, Layer 6 orchestration doctrine, session
  evidence interpretation model, and session reconstruction rules above itself
  in its governing-authority order.
- The canon states that it verifies reconstructed narratives under the
  existing Layer 6 session authorities without overriding them.
- The canonical rules preserve the existing Layer 6 authority structure:
  - state-machine meaning is evaluated before registry summaries, observation,
    or runtime context
  - ledger history remains the durable event surface
  - registry identity remains authoritative for `session_id` and indexed
    summary state
  - lifecycle observation remains interpretive and subordinate
  - runtime context remains bounded supporting evidence only
- `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
  now routes session-reconstruction verification semantics to the new canon
  without weakening any lower authority.

## Classification

- Layer 6 hierarchy preserved: `VERIFIED`
- new authority tier introduced: `NOT OBSERVED`
- evidence precedence changed: `NOT OBSERVED`
- governance safety invariants displaced: `NOT OBSERVED`
