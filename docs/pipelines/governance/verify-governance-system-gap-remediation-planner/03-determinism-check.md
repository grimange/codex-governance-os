# Determinism Check

Pipeline 169 executed the remediation planner twice on unchanged repository
state and recorded the JSON hash after each run.

Observed hash after run 1:

- `6d3facfd82194e770430233a69b6522f570fec4a7bab7bd5697aee9cdf7148e1`

Observed hash after run 2:

- `6d3facfd82194e770430233a69b6522f570fec4a7bab7bd5697aee9cdf7148e1`

Result:

- repeated execution produced identical output
- deterministic regeneration of
  `docs/governance/governance-system-gap-remediation-plan.json` is verified
