# Canonical State Definition

Established canonical authority:

- [codex-session-state-machine-canon.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/codex-session-state-machine-canon.md)

Canonical states:

- `SESSION_INITIALIZED`
- `SESSION_ACTIVE`
- `SESSION_HANDOFF_PENDING`
- `SESSION_HANDOFF_COMPLETED`
- `SESSION_RESUMED`
- `SESSION_CLOSURE_PENDING`
- `SESSION_CLOSED`

State meaning summary:

- `SESSION_INITIALIZED` records governed session creation before active
  execution
- `SESSION_ACTIVE` records live governed execution
- `SESSION_HANDOFF_PENDING` records in-progress handoff preparation
- `SESSION_HANDOFF_COMPLETED` records satisfied continuity and handoff
  completion
- `SESSION_RESUMED` records successor-session continuation under the handoff
  continuity context
- `SESSION_CLOSURE_PENDING` records close preparation before final closure
- `SESSION_CLOSED` records irreversible closure
