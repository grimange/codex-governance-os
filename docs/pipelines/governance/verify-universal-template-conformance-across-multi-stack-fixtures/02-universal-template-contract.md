# Universal Template Contract

## Base Universal Contract

Repository evidence defines the universal base scaffold in:

- `docs/governance/template-scaffold-contract.md`
- `docs/codex/templates/manifests/universal-base.json`

The base contract requires these governance core surfaces:

- `docs/governance/`
- `docs/pipelines/`
- `docs/pipelines/governance/`
- `docs/codex/templates/`
- `docs/governance/registries/templates/`
- `tools/governance/`
- `tools/templates/`
- `artifacts/`

## Overlay Contract

Supported overlays are declared in `docs/codex/templates/manifests/*.json` and must:

- identify `universal-base` as their base template
- add runtime-specific surfaces only
- avoid redefining governance core semantics

## Explicit Boundary

The current repository evidence supports these overlays:

- `laravel`
- `django`
- `python-package`
- `php-package`
- `service`
- `monorepo`

No manifest currently claims support for Node or TypeScript service overlays, CLI or worker overlays, or a distinct bare-repository overlay beyond the base scaffold itself.
