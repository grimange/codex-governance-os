# Verification Log

Observed results:

- `scheduler + laravel` returned `reason_code: explicitly-rejected`, `conflict_code: framework-native-scheduler-required`, `rejection_reason: missing Laravel-native scheduler composition contract`
- `scheduler + django` returned `reason_code: explicitly-rejected`, `conflict_code: framework-native-scheduler-required`, `rejection_reason: missing Django-native scheduler composition contract`
- supported scheduler controls remained unchanged:
  - `scheduler` -> `single-overlay`
  - `scheduler + cli-worker` -> `certified-multi-overlay`
  - `scheduler + monorepo` -> `certified-multi-overlay`
  - `scheduler + python-package` -> `certified-multi-overlay`
  - `scheduler + cli-worker + monorepo` -> `certified-multi-overlay`
  - `scheduler + cli-worker + python-package` -> `certified-multi-overlay`
- `verify-composition-matrix --output json` returned `{ "valid": true, "errors": [] }`
- `python -m unittest tests.governance.test_framework_scheduler_unsupported_boundaries` passed with `Ran 4 tests ... OK`
- targeted scheduler matrix tests passed with `Ran 12 tests ... OK`
- repository-wide governance tests passed with `Ran 113 tests ... OK`
