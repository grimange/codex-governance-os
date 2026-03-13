# Fixture-By-Fixture Results

| fixture | verdict | notes |
|---------|---------|-------|
| minimal-governed-repo | PASS | realized base governance core with no overlay contradiction |
| laravel-application | PASS | realized governance core plus `app`, `bootstrap`, `routes`, and `config` |
| django-application | PASS | realized governance core plus `backend`, `config`, and `apps` |
| python-package | PASS | realized governance core plus `src`, `tests`, and package docs surface |
| php-package | PASS | realized governance core plus `src`, `tests`, and `config` |
| service-repository | PASS | realized governance core plus `service`, `config`, and `scripts` |
| monorepo | PASS | realized governance core plus `packages`, `services`, and `shared` |
| node-typescript-service | UNSUPPORTED_BY_DESIGN | no overlay manifest present |
| cli-worker | UNSUPPORTED_BY_DESIGN | no overlay manifest present |

All supported fixtures passed the same realization and governance-core-preservation checks.
