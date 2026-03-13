# Node Typescript Overlay Contract

## Overlay Name

`node-typescript-service`

## Applies To

- Node.js backend or service repositories
- TypeScript backend or service repositories
- API services using a package manifest and script-driven execution model

## Required Surfaces

- `package.json`
- `src/`
- `tests/`
- `scripts/`

## Optional Surfaces

- `tsconfig.json`
- `services/`
- `packages/`

## Compatibility Rules

- compatible with base scaffold
- compatible with `monorepo`
- not compatible with framework overlays such as `laravel` or `django`

## Invariants

- does not redefine governance core surfaces
- preserves docs-root governance placement
- treats package-manifest presence as a first-class signal via `package.json`
