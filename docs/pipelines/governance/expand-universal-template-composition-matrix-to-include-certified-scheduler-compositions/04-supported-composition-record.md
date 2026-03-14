# Supported Composition Record

Scheduler-certified composition truth after this lane:

- `scheduler`
- `cli-worker + scheduler`
- `monorepo + scheduler`
- `python-package + scheduler`
- `cli-worker + monorepo + scheduler`
- `cli-worker + python-package + scheduler`

These results remain distributed across the governed sources in this order:

1. scaffold runtime logic
2. manifest inventory
3. composition contract
4. governance verification suites
