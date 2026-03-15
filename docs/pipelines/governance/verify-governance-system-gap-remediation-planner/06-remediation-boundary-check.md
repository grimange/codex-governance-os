# Remediation Boundary Check

Observed suggested pipelines:

- `multi_agent_governance`
  - `establish-role-scoped-codex-sub-agent-specialization`
- `architecture_advisor`
  - `unknown`
- `autonomous_governance_loop`
  - `unknown`

Boundary result:

- the planner emits a concrete pipeline only where repository truth already
  supports one
- the planner emits `unknown` where canonical evidence does not support a
  specific lane
- no unsupported pipeline was invented
