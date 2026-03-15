# Gap Model And Classification Rules

Pipeline 166 supports these gap classifications:

- `INVALID_STATE`
- `MISSING_CAPABILITY`
- `UNVERIFIED_CAPABILITY`
- `UNDECLARED_DOMAIN`
- `PARTIAL_COVERAGE`
- `BLOCKED_BY_DRIFT`
- `EVIDENCE_INSUFFICIENT`

Current implemented derivation rules:

- `INVALID_STATE`
  - maturity domain exists but required capability is absent from the registry
- `UNVERIFIED`
  - capability exists in the registry but is not yet complete
- `PARTIAL`
  - domain contains a mix of complete and incomplete declared capabilities
- `BLOCKED_BY_DRIFT`
  - self-inspection detects inconsistent canonical governance state

Only classifications supported by canonical evidence are emitted.
