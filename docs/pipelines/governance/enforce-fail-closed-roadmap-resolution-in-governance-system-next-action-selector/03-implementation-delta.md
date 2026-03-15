# Implementation Delta

Pipeline 174 applied these implementation changes:

- next-action resolution now reads the canonical roadmap, remediation plan,
  gaps, and maturity JSON surfaces directly
- selector validates that `recommended_next_target`:
  - exists
  - is a recognized governance domain
  - exists in the remediation plan
  - exists in the detected gap set
  - has a non-`VERIFIED` maturity classification
  - has matching classification across remediation, gap, and maturity surfaces
- selector now exits non-zero and emits machine-readable failure on unresolved
  roadmap resolution
- selector no longer writes the canonical next-action surface on invalid
  resolution

Pipeline 174 also adds regression tests under
`tests/governance/test_governance_system_next_action.py`.
