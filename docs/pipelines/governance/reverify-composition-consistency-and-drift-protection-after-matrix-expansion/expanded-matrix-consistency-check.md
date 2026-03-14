# Expanded Matrix Consistency Check

The expanded supported matrix under protection re-verification was:

- base-only
- `django + monorepo`
- `node-typescript-service + monorepo`
- `node-typescript-service + cli-worker`
- `cli-worker + monorepo`
- `cli-worker + python-package`
- `cli-worker + php-package`

The remaining rejected matrix under protection re-verification was:

- `laravel + cli-worker`
- `service + monorepo`
- `laravel + django`

Verification confirmed that contract, doctor, and scaffold surfaces still agree on normalized overlays, support decision, reason code, and decision source for these cases.
