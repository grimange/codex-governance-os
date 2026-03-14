# Unsupported Boundary Checks

Representative unsupported scheduler combinations were exercised for fail-closed behavior:

- `scheduler + laravel`
- `scheduler + django`
- `scheduler + service`

Observed behavior:

- scaffold generation raised explicit `RegistryError`
- no successful scheduler scaffold was left behind for those unsupported cases
- `scheduler + laravel` remained `reason_code: unsupported`

This confirms the generator does not silently widen scheduler support beyond the certified matrix.
