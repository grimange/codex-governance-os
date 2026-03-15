# Stage Ordering Check

Required ordering rule:

- `INVALID_STATE` domains must appear before `UNVERIFIED` domains

Observed roadmap order:

1. `multi_agent_governance` in `state_normalization`
2. `architecture_advisor` in `capability_expansion`
3. `autonomous_governance_loop` in `capability_expansion`

Ordering result:

- invalid-state remediation appears before unverified capability expansion
- stage ordering remains dependency-safe and deterministic
