# Output Protection Check

Observed output protection results:

- missing canonical surface:
  - next-action hash unchanged
- shadow surface injection:
  - next-action hash unchanged
- cross-surface inconsistency:
  - next-action hash changed
- multiple candidate inputs:
  - next-action hash remained unchanged, but selector still exited `0`

Interpretation:

- output protection works for some fail-closed scenarios
- output protection is not yet universally enforced because the selector still
  accepts certain invalid authority conditions
