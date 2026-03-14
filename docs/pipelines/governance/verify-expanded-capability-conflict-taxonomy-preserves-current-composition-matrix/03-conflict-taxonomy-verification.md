# Conflict Taxonomy Verification

The explicit unsupported boundaries remained unchanged at the decision level and now expose deterministic taxonomy classifications.

Verified controls:

- `laravel + cli-worker`
  - `reason_code: explicitly-rejected`
  - `conflict_code: worker-model-collision`
  - `rejection_reason: missing Laravel worker composition contract`
- `django + laravel`
  - `reason_code: explicitly-rejected`
  - `conflict_code: cross-framework-application-collision`
  - `rejection_reason: cross-framework application collision`

Important implementation note:

- the current governed design preserves `reason_code` as the top-level decision class
- taxonomy classification is carried in `conflict_code`

This means the taxonomy expanded explanation semantics without changing the contract’s supported vs rejected decision model.
