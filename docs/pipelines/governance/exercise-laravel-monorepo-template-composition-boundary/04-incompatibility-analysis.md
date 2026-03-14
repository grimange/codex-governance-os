# Incompatibility Analysis

## What Is Blocking The Pair Today

The current rejection is caused by missing admission surfaces:

- `laravel.json` declares no compatible overlays
- `monorepo.json` does not list `laravel`
- the certified contract does not include `laravel + monorepo`
- no Laravel monorepo placement override exists

That is materially different from a pair like `django + laravel`, which is explicitly rejected because the frameworks collide directly.

## Why This Does Not Look Structural

Laravel and monorepo do not inherently claim the same semantic role:

- Laravel defines application runtime structure
- monorepo defines repository topology and workspace segmentation

The repository already supports this exact category of composition for:

- `django + monorepo`
- `service + monorepo`
- `node-typescript-service + monorepo`

Those precedents show that monorepo composition is solved here by deterministic nested placement rather than root-level overlay merging.

## Likely Required Bounded Changes

Support would likely require only a Laravel-specific monorepo placement contract, for example:

- a canonical Laravel service location such as `apps/backend/laravel-app/` or `services/laravel-app/`
- a `composition_overrides.monorepo` entry in the Laravel manifest
- reciprocal manifest compatibility declarations
- overlay documentation updates
- matrix and scaffold verification coverage

## Residual Design Question

The main unresolved question is placement choice, not composability class:

- should Laravel follow the Django-style backend-app placement pattern
- or the generic service-style placement pattern

That is a bounded scaffold decision with clear precedents.
