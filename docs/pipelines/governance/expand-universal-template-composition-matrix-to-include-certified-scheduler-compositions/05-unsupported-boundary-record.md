# Unsupported Boundary Record

Representative unsupported scheduler boundaries remain fail-closed:

- `scheduler + laravel`
- `scheduler + django`
- `scheduler + service`

Observed behavior remains:

- `supported: false`
- `reason_code: unsupported`
- no silent fallback into admitted support

This lane did not broaden scheduler support beyond the already-certified matrix.
