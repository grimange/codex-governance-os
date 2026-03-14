# Unsupported Boundary Verification

The explicit fail-closed boundaries remained stable under reverification:

- `laravel + cli-worker`
  - `reason_code: explicitly-rejected`
  - `rejection_reason: missing Laravel worker composition contract`
- `django + laravel`
  - `reason_code: explicitly-rejected`
  - `rejection_reason: cross-framework application collision`

This confirms that the capability registry did not dilute the previously certified rejection boundaries or mutate their canonical reasons.
