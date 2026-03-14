# Supported Composition Verification

Supported scheduler-bearing compositions verified in this lane:

- `scheduler`
- `scheduler + cli-worker`
- `scheduler + monorepo`
- `scheduler + python-package`
- `scheduler + cli-worker + monorepo`
- `scheduler + cli-worker + python-package`

Observed result class:

- single overlay: `reason_code: single-overlay`
- certified multi-overlay scheduler compositions: `reason_code: certified-multi-overlay`

The scheduler overlay therefore remains both:

- admitted as a single-overlay realization
- certified as a bounded participant in the multi-overlay matrix
