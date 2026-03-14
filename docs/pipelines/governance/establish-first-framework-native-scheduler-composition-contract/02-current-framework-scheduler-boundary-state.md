# Current Framework Scheduler Boundary State

State before this lane:

- `scheduler + laravel` was explicitly rejected with:
  - `reason_code: explicitly-rejected`
  - `conflict_code: framework-native-scheduler-required`
  - `rejection_reason: missing Laravel-native scheduler composition contract`
- `scheduler + django` was explicitly rejected with the equivalent Django-native reason

That state was safe, but incomplete. Laravel already has a canonical scheduler
surface and could support a governed framework-native contract without weakening
the rest of the matrix.
