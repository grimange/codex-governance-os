# Scheduler Overlay Verification

The newly admitted scheduler compositions remained certified:

- `scheduler + cli-worker`
- `scheduler + monorepo`
- `scheduler + python-package`
- `scheduler + cli-worker + monorepo`
- `scheduler + cli-worker + python-package`

Observed result for each:

- `supported: true`
- `reason_code: certified-multi-overlay`
- `conflict_code: null`

The manifest inventory and runtime doctor surface both recognized the scheduler overlay consistently.
