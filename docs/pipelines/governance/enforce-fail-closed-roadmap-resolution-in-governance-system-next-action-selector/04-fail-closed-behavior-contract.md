# Fail-Closed Behavior Contract

When roadmap target resolution fails, the selector now emits a stable
machine-readable failure payload:

```json
{
  "status": "ERROR",
  "error_code": "UNRESOLVED_ROADMAP_RECOMMENDED_NEXT_TARGET",
  "message": "recommended_next_target could not be resolved against the remediation plan"
}
```

Contract guarantees:

- exit non-zero
- do not write `docs/governance/governance-system-next-action.json`
- preserve deterministic valid-state behavior
- never silently normalize invalid roadmap target state
