# Conflict Reason Codes

The taxonomy is exposed separately from the existing decision class.

Current model:

- `reason_code`
  - preserves the top-level decision class such as `explicitly-rejected`, `capability-conflict`, or `capability-role-conflict`
- `conflict_code`
  - carries the canonical taxonomy classification

Representative outcomes:

- `laravel + cli-worker`
  - `reason_code: explicitly-rejected`
  - `conflict_code: worker-model-collision`
- `django + laravel`
  - `reason_code: explicitly-rejected`
  - `conflict_code: cross-framework-application-collision`
- package/application role collisions
  - `reason_code: capability-role-conflict`
  - `conflict_code: package-application-role-collision`
