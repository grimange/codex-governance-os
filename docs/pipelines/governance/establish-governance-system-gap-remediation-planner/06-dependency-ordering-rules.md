# Dependency Ordering Rules

Current dependency ordering rules:

- resolve invalid registry or state alignment before attempting promotion of
  unverified domains
- preserve deterministic lexical ordering among equally classified gaps

Observed ordering result:

1. `multi_agent_governance`
2. `architecture_advisor`
3. `autonomous_governance_loop`

This ordering is deterministic and respects the requirement that invalid state
must be remediated before unverified domains.
