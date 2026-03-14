# Prioritized Boundary Roadmap

## Highest-Value Next Candidates

1. `laravel + monorepo`
   - highest-value because the repository already has successful monorepo composition patterns for `django`, `service`, and `node-typescript-service`
   - the likely work is a Laravel-specific placement contract, not a new composition class from scratch
2. `cli-worker + service`
   - high-value because `cli-worker + node-typescript-service` is already certified, so a generic service-plus-worker contract could be reusable
3. `monorepo + python-package`
   - medium-value because monorepo package placement is a bounded structural problem with clear precedent
4. `monorepo + php-package`
   - same rationale as Python package, but slightly lower leverage in the current matrix

## Low-Priority Explicit Codification Candidates

1. `django + service`
2. `laravel + service`
3. `laravel + node-typescript-service`
4. `php-package + python-package`

These look more like structural collisions than missing small contracts. If they remain interesting, the next governance action should likely be explicit codification rather than support work.

## Suggested Next Lane

The most defensible next lane is:

`043 — Exercise Laravel + Monorepo Template Composition Boundary`

That lane would follow the proven pattern from pipelines `039` to `041`, but target the unsupported pair with the strongest reuse path from already-certified monorepo compositions.
