# Verification Plan

## Structural Checks

- confirm `docs/governance/registries/templates/` exists and contains `index.yaml` plus `entries/`
- confirm `docs/codex/templates/` exists and contains the admitted template bodies
- confirm root-level `registry/` and `templates/` no longer exist as active authority surfaces

## Reference Checks

- search the repository for stale references to `registry/templates/` and root-level `templates/`
- confirm policy documents now declare `docs/` as the canonical governance and Codex root
- confirm tooling defaults resolve only docs-root paths

## Operational Checks

- run governance unit tests
- run template registry validation and index build commands
- run template resolution commands
- run template lint commands against representative fixtures
