# Verification Targets

Scheduler surface targets verified in this lane:

- `scheduler/schedule.py`
- `scheduler/scheduler_runtime.py`

Certified compositions exercised:

- `scheduler`
- `scheduler + cli-worker`
- `scheduler + monorepo`
- `scheduler + python-package`
- `scheduler + cli-worker + monorepo`
- `scheduler + cli-worker + python-package`

Control boundary exercised:

- `scheduler + laravel` remains unsupported
