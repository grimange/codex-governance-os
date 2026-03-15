# Fail-Closed Validation

## Injected Invalid Roadmap Target

Temporary mutation:

- changed roadmap `recommended_next_target` from `multi_agent_governance` to
  `invalid_target`

Observed selector stderr:

```json
{
  "status": "ERROR",
  "error_code": "UNRESOLVED_ROADMAP_RECOMMENDED_NEXT_TARGET",
  "message": "recommended_next_target could not be resolved against the remediation plan"
}
```

Observed result:

- selector exited with status `1`
- canonical next-action output hash remained unchanged
- invalid roadmap resolution no longer regenerates misleading canonical output

## Restoration

- canonical roadmap state was restored immediately after the test
- canonical next-action surface remained intact
