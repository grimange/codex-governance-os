# Current Supported And Rejected Scheduler State

## Already Supported

- `scheduler`
- `scheduler + cli-worker`
- `scheduler + monorepo`
- `scheduler + python-package`
- `scheduler + cli-worker + monorepo`
- `scheduler + cli-worker + python-package`
- `laravel + scheduler`
- `django + scheduler`

## Currently Rejected Or Unsupported

- `laravel + monorepo + scheduler` -> unsupported
- `django + monorepo + scheduler` -> unsupported
- `laravel + cli-worker + scheduler` -> unsupported
- `django + cli-worker + scheduler` -> unsupported

## Interpretation

The current closure is matrix-based rather than silent. The compound candidates
fail because they are not present in the certified matrix, not because of hidden
runtime behavior. That makes them suitable for explicit evaluation.
