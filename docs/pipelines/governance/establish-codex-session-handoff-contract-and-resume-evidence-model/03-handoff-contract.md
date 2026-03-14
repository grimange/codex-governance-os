# Handoff Contract

Established canonical authority:

- [codex-session-handoff-contract-and-resume-evidence-model.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md)

Canonical handoff requirements:

- handoff is explicit and not inferred from interruption or memory
- a valid handoff requires source session identity, bounded subject, current
  canonical state, preserved restrictions, evidence references, next valid
  action, and an explicit completion declaration
- a handoff packet is the minimum continuity unit between sessions
- `SESSION_HANDOFF_COMPLETED` means the source session reached a valid
  successor-capable boundary, not that a successor already resumed
