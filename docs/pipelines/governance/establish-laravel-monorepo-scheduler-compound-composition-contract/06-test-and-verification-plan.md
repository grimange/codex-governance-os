# Test And Verification Plan

## Positive Verification

- `python tools/governance/template_scaffold.py doctor-composition --overlays laravel monorepo scheduler --output json`
- `python tools/governance/template_scaffold.py verify-composition-matrix --output json`
- `python -m unittest tests.governance.test_laravel_monorepo_scheduler_compound_composition`
- targeted regression suites covering Laravel direct pair, Laravel monorepo pair,
  matrix drift, capability preservation, and scaffold behavior

## Negative Verification

- ambiguous compound override resolution must raise `RegistryError`
- `django + monorepo + scheduler` must remain unsupported
- `laravel + cli-worker` and worker-oriented framework compounds must remain closed

## Drift Protection

The supported triplet is now protected by:

- runtime certified matrix
- snapshot verification
- capability registry explicit compound-contract inventory
- dedicated compound composition tests
