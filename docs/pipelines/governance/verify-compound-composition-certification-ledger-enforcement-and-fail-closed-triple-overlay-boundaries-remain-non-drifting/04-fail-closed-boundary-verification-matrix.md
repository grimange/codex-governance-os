# Fail-Closed Boundary Verification Matrix

Verified fail-closed triplets:

- `django + monorepo + scheduler` -> unsupported
- `django + cli-worker + scheduler` -> unsupported
- `laravel + cli-worker + scheduler` -> unsupported

All three remained rejected by `doctor-composition`, and none resolved as
certified support.
