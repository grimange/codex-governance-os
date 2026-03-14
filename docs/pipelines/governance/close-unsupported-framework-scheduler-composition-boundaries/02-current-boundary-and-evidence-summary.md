# Current Boundary And Evidence Summary

Observed pre-normalization behavior:

- `scheduler + laravel` -> `supported: false`, `reason_code: unsupported`
- `scheduler + django` -> `supported: false`, `reason_code: unsupported`

Evidence surfaces before closure:

- scaffold doctor output
- composition contract omission from the explicit fail-closed set
- tests covering supported scheduler cases but not locking framework scheduler reasons

Under-specification found:

- no canonical reason code
- no canonical rejection text
- no dedicated test proving the framework scheduler boundary was intentional
