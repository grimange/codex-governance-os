# Ordering Rules Check

Required ordering rule:

- `INVALID_STATE` gaps must appear before `UNVERIFIED` gaps

Observed remediation ordering:

1. `multi_agent_governance` -> `INVALID_STATE`
2. `architecture_advisor` -> `UNVERIFIED`
3. `autonomous_governance_loop` -> `UNVERIFIED`

Validation result:

- the required dependency ordering rule is satisfied
- invalid state remediation is scheduled before capability completion work
- ordering remains deterministic and stable
