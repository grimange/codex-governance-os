# Contract Surface Inventory

## Laravel Overlay

Current authority surfaces:

- [docs/codex/templates/manifests/laravel.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/laravel.json)
  - `compatible_overlays: []`
  - required surfaces: `app`, `bootstrap`, `routes`, `config`
  - runtime shapes: `application`, `service`
- [docs/codex/templates/overlays/laravel/README.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/overlays/laravel/README.md)
  - currently defines Laravel as a standalone runtime overlay, with no monorepo composition note

Laravel therefore owns an application root but has no declared nested placement contract.

## Monorepo Overlay

Current authority surfaces:

- [docs/codex/templates/manifests/monorepo.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/monorepo.json)
  - compatible with `django`, `service`, `node-typescript-service`, and `cli-worker`
  - required surfaces: `packages`, `services`, `shared`
- [docs/codex/templates/overlays/monorepo/README.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/overlays/monorepo/README.md)
  - already documents canonical placement patterns for composed overlays

## Existing Composition Pattern

Two existing overlays already demonstrate the current reusable pattern:

- [docs/codex/templates/manifests/django.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/django.json)
  - uses `composition_overrides.monorepo` with placement `apps/backend/django-service`
- [docs/codex/templates/manifests/service.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/service.json)
  - uses `composition_overrides.monorepo` with placement `services/service-app`

The scaffold layer in [template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_scaffold.py) already supports this placement-based override model.
