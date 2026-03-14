# Session Close Enforcement

Integrated enforcement rules:

- an in-scope governed session must create a handoff packet before closure when
  continuity evidence is required
- session closure is incomplete until the required packet exists
- if the required packet is absent, the session should be treated as having a
  `SESSION_CONTINUITY_VIOLATION`
- continuity violations must remain visible in execution records rather than
  being smoothed away

These rules were integrated into:

- [layer-6-codex-session-orchestration-and-handoff-discipline.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md)
- [codex-session-handoff-packet-and-continuity-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/codex-session-handoff-packet-and-continuity-contract.md)
