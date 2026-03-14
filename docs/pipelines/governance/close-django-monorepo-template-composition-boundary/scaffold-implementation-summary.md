# Scaffold Implementation Summary

## Manifest Changes

- `docs/codex/templates/manifests/django.json` now admits `monorepo`
- `docs/codex/templates/manifests/monorepo.json` now admits `django`
- `django.json` now carries `composition_overrides.monorepo` metadata including:
  - `placement`
  - `repository_structure`
  - nested required surfaces

## Scaffold Changes

- `tools/governance/template_scaffold.py` now resolves overlay composition overrides
- when `django` is composed with `monorepo`, scaffold realization uses nested Django service surfaces instead of root-level Django surfaces
- selection output now records `composition_metadata` for composition-specific placements

## Contract Changes

- `django + monorepo` was promoted into the certified supported matrix
- it was removed from the fail-closed boundary
