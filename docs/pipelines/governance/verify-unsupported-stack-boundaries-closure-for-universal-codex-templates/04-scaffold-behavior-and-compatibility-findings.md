# Scaffold Behavior And Compatibility Findings

## Verified Supported Cases

- base-only admitted and created the governance core surfaces
- `node-typescript-service` admitted and created `package.json`, `src/`, `tests/`, and `scripts/`
- `cli-worker` admitted and created `bin/`, `jobs/`, and `worker/`
- `node-typescript-service` composes with `monorepo` and realizes `package.json`, `packages/`, `services/`, and `shared/`
- `cli-worker` composes with package overlays as documented by the manifests

## Verified Fail-Closed Case

- `laravel` + `cli-worker` is rejected with: `Overlay cli-worker is not compatible with overlay laravel`

## Compatibility Assessment

The scaffold runtime now enforces overlay-to-overlay compatibility rather than guessing. The new overlays do not redefine governance core surfaces and they preserve docs-root governance placement.
