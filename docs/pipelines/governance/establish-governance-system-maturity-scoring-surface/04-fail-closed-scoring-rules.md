# Fail-Closed Scoring Rules

Pipeline 164 implements these fail-closed rules:

## Unknown Capability

If a maturity domain expects a capability that is absent from the capability
registry:

- domain score = `0`
- classification = `INVALID_STATE`

Current example:

- `multi_agent_governance`

## Missing Verification

If a capability is declared but not yet complete in the registry:

- domain score = `0`
- classification = `UNVERIFIED`

Current examples:

- `autonomous_governance_loop`
- `architecture_advisor`

## Partial Domains

If some domain capabilities are complete and others are not, the domain is
scored proportionally and classified as `PARTIAL`.

## State Drift

The `maturity` CLI mode refuses to compute maturity when the underlying
governance state inspection detects cross-surface inconsistencies.
