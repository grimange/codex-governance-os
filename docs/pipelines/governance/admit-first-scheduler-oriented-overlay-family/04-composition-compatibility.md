# Composition Compatibility

The scheduler family is now certified with these compositions:

- `scheduler + cli-worker`
- `scheduler + monorepo`
- `scheduler + python-package`
- `scheduler + cli-worker + monorepo`
- `scheduler + cli-worker + python-package`

Observed classification for each:

- `supported: true`
- `reason_code: certified-multi-overlay`
- `conflict_code: null`

This proves the scheduler family integrates cleanly with worker, package, and topology overlays without widening unrelated boundaries.
