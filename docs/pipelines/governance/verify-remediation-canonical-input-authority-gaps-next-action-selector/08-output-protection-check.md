# Output Protection Check

Observed output protection results:

- consensus-violation scenario:
  - next-action hash unchanged
- ambiguous-candidate scenario:
  - next-action hash unchanged

Observed valid-state behavior:

- canonical next-action output is still regenerated normally on valid state

Result:

- canonical output protection is preserved during both remediated failure
  scenarios
