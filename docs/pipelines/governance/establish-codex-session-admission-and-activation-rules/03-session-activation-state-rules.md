# Session Activation State Rules

State-machine alignment:

- [codex-session-state-machine-canon.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/codex-session-state-machine-canon.md)
  now includes `SESSION_ADMITTED`

Canonical activation transitions:

- `SESSION_INITIALIZED -> SESSION_ADMITTED`
- `SESSION_ADMITTED -> SESSION_ACTIVE`
- `SESSION_RESUMED -> SESSION_ADMITTED`

Invalid shortcut transitions now include:

- `SESSION_INITIALIZED -> SESSION_ACTIVE`
- `SESSION_RESUMED -> SESSION_ACTIVE`

Activation is defined as the first admitted governed act, not mere intent to
proceed.
