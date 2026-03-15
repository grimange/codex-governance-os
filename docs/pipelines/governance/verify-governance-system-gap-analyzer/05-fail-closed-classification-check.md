# Fail-Closed Classification Check

Expected current fail-closed outcomes from Pipeline 166:

- `autonomous_governance_loop` -> `UNVERIFIED`
- `multi_agent_governance` -> `INVALID_STATE`
- `architecture_advisor` -> `UNVERIFIED`

Observed outcomes:

- `autonomous_governance_loop` -> `UNVERIFIED`
- `multi_agent_governance` -> `INVALID_STATE`
- `architecture_advisor` -> `UNVERIFIED`

Verification result:

- invalid or incomplete governance domains remain flagged
- the analyzer does not normalize missing registry-backed coverage
- fail-closed classification behavior is preserved
