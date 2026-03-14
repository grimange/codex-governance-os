# Supported Vs Rejected Matrix

## Supported

- base-only
- any single admitted overlay applied to `universal-base`
- `node-typescript-service + monorepo`
- `node-typescript-service + cli-worker`
- `cli-worker + monorepo`
- `cli-worker + python-package`
- `cli-worker + php-package`

## Rejected

- `laravel + cli-worker`
- `django + monorepo`
- `service + monorepo`
- `laravel + django`
- any multi-overlay combination not explicitly allowlisted by the certified contract
