# Scaffold Implementation Summary

## Manifest Changes

- `docs/codex/templates/manifests/service.json` now admits `monorepo`
- `docs/codex/templates/manifests/monorepo.json` now admits `service`
- `service.json` now carries `composition_overrides.monorepo` metadata including:
  - `placement`
  - `repository_structure`
  - nested required surfaces

## Scaffold Changes

- the existing composition-override mechanism in `tools/governance/template_scaffold.py` now applies to the service overlay
- when `service` is composed with `monorepo`, scaffold realization uses nested service surfaces under `services/service-app/`
- selection output records service placement metadata under `composition_metadata`

## Contract Changes

- `service + monorepo` was promoted into the certified supported matrix
- it was removed from the fail-closed boundary
