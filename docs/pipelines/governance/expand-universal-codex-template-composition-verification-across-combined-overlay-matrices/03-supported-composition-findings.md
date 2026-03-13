# Supported Composition Findings

| case | admission | notable realized surfaces |
|------|-----------|---------------------------|
| base-only | PASS | `docs/governance/`, `docs/pipelines/`, `tools/governance/`, `tools/templates/`, `artifacts/` |
| node-typescript-service + monorepo | PASS | `package.json`, `packages/`, `services/`, `shared/`, `src/`, `tests/`, `scripts/` |
| node-typescript-service + cli-worker | PASS | `package.json`, `src/`, `tests/`, `scripts/`, `bin/`, `jobs/`, `worker/` |
| cli-worker + monorepo | PASS | `bin/`, `jobs/`, `worker/`, `packages/`, `services/`, `shared/` |
| cli-worker + python-package | PASS | `bin/`, `jobs/`, `worker/`, `src/`, `tests/`, `docs/` |
| cli-worker + php-package | PASS | `bin/`, `jobs/`, `worker/`, `src/`, `tests/`, `config/` |

All supported cases admitted successfully and preserved the governance core surfaces.
