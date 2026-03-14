# Unsupported Boundary Verification

Representative unsupported scheduler controls verified in this lane:

- `scheduler + laravel`
- `scheduler + django`

Observed result:

- `supported: false`
- `reason_code: unsupported`
- rejection reason remained `not present in certified composition matrix`

This confirms scheduler certification has not expanded silently into unsupported
framework pairings.
