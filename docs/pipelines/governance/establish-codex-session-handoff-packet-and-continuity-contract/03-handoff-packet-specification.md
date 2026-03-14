# Handoff Packet Specification

The canonical contract is established at
[codex-session-handoff-packet-and-continuity-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/codex-session-handoff-packet-and-continuity-contract.md).

The canonical packet root is:

- [handoffs](/home/ramjf/python-projects/codex-governance-os/docs/codex/sessions/handoffs)

Established specification:

- packet filenames use `codex-session-handoff-{session-id}.md`
- packets contain session identity, objective, authoritative close-state,
  mutation scope summary, evidence produced, restrictions, recommended next
  path, and next-session mutation boundaries
- packets supplement the session registry and execution ledger rather than
  replacing them
- a template packet is available at
  [codex-session-handoff-template.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/sessions/handoffs/codex-session-handoff-template.md)

The handoff packet root may remain empty of real session packets until a later
governed lane records an actual handoff.
