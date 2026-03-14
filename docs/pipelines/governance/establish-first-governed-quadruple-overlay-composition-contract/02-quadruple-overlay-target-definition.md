# Quadruple-Overlay Target Definition

## Target Stack

- `cli-worker`
- `monorepo`
- `python-package`
- `scheduler`

## Selection Rationale

This is the lowest-risk first quadruple because the repository already certifies:

- `cli-worker + monorepo + python-package`
- `cli-worker + monorepo + scheduler`
- `cli-worker + python-package + scheduler`

No new composition role is introduced beyond the existing worker, topology,
package, and scheduler roles.
