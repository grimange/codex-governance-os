# Severity And Blocking Rules

Severity model used in Pipeline 166:

- `critical`
  - inconsistent governance state blocks trustworthy analysis
- `high`
  - invalid-state domain prevents mature governance reasoning
- `medium`
  - unverified or partial domain materially limits system maturity
- `low`
  - bounded issue with limited maturity impact

Current observed mapping:

- `multi_agent_governance` -> `high`
- `autonomous_governance_loop` -> `medium`
- `architecture_advisor` -> `medium`

Every emitted gap records a `blocking_effect` field explaining why the gap
prevents full governance-system maturity.
