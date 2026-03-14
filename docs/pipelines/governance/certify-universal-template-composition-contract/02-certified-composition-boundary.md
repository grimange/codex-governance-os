# Certified Composition Boundary

## Certified Supported Combinations

- base-only
- `node-typescript-service + monorepo`
- `node-typescript-service + cli-worker`
- `cli-worker + monorepo`
- `cli-worker + python-package`
- `cli-worker + php-package`

## Certified Fail-Closed Combinations

- `laravel + cli-worker`
- `django + monorepo`
- `service + monorepo`
- `laravel + django`

## Boundary Interpretation

- support is allowlisted, not inferred
- overlay compatibility is pairwise and explicit
- unsupported combinations must fail closed in scaffold realization
- expanding the boundary requires contract, docs, manifest, logic, and test updates in one governed change
