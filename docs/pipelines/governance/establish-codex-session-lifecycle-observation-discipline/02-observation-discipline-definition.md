# Observation Discipline Definition

Pipeline `115` establishes
`docs/governance/codex-session-lifecycle-observation-discipline.md` as the
canonical Layer 6 surface for lifecycle observation normalization.

The new canon defines:

- what lifecycle observation means in this repository
- which observation families matter for governed sessions
- how observations remain subordinate to the state-machine, registry, ledger,
  admission, and runtime-boundary authorities
- what ordering guarantees observation evidence must preserve

The canon is explicit that observation does not create new lifecycle states and
does not authorize runtime implementation claims.
