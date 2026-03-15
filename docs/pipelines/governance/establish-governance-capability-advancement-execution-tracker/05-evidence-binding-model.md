# Evidence Binding Model

Pipeline 160 binds capability state to canonical evidence through three linked
surfaces:

- `docs/governance/governance-capability-registry.md`
- `docs/governance/governance-capability-execution-map.md`
- `docs/governance/governance-capability-progress.md`

Evidence-binding rules:

- a capability may be marked `complete` only when canonical governance surfaces
  and implementing lanes already exist in repository truth
- a capability may be marked `in progress` only when active establishment,
  planning, or tracking surfaces are already in place
- a capability marked `planned` must remain explicitly unimplemented and may not
  cite future lanes as completed evidence
- planned pipeline references must remain visibly planned when no implementing
  lane is yet established

This keeps advancement tracking evidence-backed and fail-closed.
