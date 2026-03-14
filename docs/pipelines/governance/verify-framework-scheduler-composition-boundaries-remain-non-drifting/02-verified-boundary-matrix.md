# Verified Boundary Matrix

Verified supported scheduler matrix:

- `scheduler` -> `single-overlay`
- `scheduler + cli-worker` -> `certified-multi-overlay`
- `scheduler + monorepo` -> `certified-multi-overlay`
- `scheduler + python-package` -> `certified-multi-overlay`
- `scheduler + cli-worker + monorepo` -> `certified-multi-overlay`
- `scheduler + cli-worker + python-package` -> `certified-multi-overlay`

Verified explicit framework boundaries:

- `scheduler + laravel` -> `explicitly-rejected`, `framework-native-scheduler-required`
- `scheduler + django` -> `explicitly-rejected`, `framework-native-scheduler-required`
