# Session Admission Model

Established canonical authority:

- [codex-session-admission-and-activation-rules.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/codex-session-admission-and-activation-rules.md)

Canonical admission model:

1. `SESSION_INITIALIZED` means the session exists but is not yet authorized to
   execute governed work.
2. `SESSION_ADMITTED` means the admission gate has passed and governed
   execution may begin.
3. `SESSION_ACTIVE` means the admitted session has begun a valid governed
   action.

The model requires admission to precede active execution for both new and
resumed sessions.
