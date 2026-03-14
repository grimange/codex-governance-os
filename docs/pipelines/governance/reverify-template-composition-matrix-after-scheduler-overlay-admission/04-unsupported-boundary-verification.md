# Unsupported Boundary Verification

The explicit unsupported controls remained unchanged after scheduler admission:

- `laravel + cli-worker`
  - `reason_code: explicitly-rejected`
  - `conflict_code: worker-model-collision`
  - `rejection_reason: missing Laravel worker composition contract`
- `django + laravel`
  - `reason_code: explicitly-rejected`
  - `conflict_code: cross-framework-application-collision`
  - `rejection_reason: cross-framework application collision`

This confirms the scheduler family did not weaken the existing fail-closed boundaries or taxonomy semantics.
