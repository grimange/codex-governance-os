# Target Boundary Classification Model

Chosen governance state for both rejected framework scheduler combinations:

- `scheduler + laravel` -> conditionally supportable only through framework-native constraints
- `scheduler + django` -> conditionally supportable only through framework-native constraints

Canonical reason-code model:

- top-level decision: `explicitly-rejected`
- canonical conflict code: `framework-native-scheduler-required`

Canonical rejection reasons:

- `scheduler + laravel` -> `missing Laravel-native scheduler composition contract`
- `scheduler + django` -> `missing Django-native scheduler composition contract`

Meaning:

- the universal scheduler overlay is not directly composable with a full framework runtime
- a future support path would require a dedicated Laravel-native or Django-native scheduler contract lane
- this is not current support, partial support, or support with warning
