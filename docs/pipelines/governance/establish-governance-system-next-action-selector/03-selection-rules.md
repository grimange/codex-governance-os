# Selection Rules

Pipeline 172 implements these deterministic selection rules:

1. Prefer the roadmap `recommended_next_target`.
2. Resolve that target against the ordered remediation plan.
3. If the target is missing from the remediation plan, fail closed.
4. Classify the action from the remediation strategy.
5. Preserve any uncertainty already present in remediation linkage.

Current selection result:

- target domain:
  - `multi_agent_governance`
- current status:
  - `INVALID_STATE`
- selected action type:
  - `state_normalization`
