# Universal Template Scaffold Surface

This directory is the docs-root Codex template surface for this repository.

It contains two kinds of assets:

- admitted governed template bodies used by the template registry
- universal scaffold surfaces used to model reusable repository structure

The scaffold model is organized into:

- `base/`: invariant base scaffold documentation
- `governance/`: governance-specific scaffold guidance
- `shared/`: reusable shared scaffold guidance
- `overlays/`: stack and topology overlays
- `manifests/`: machine-readable scaffold manifests used by tooling

Current supported overlays:

- `laravel`
- `django`
- `python-package`
- `php-package`
- `service`
- `monorepo`
- `node-typescript-service`
- `cli-worker`

Verified supported compositions:

- base-only
- `node-typescript-service + monorepo`
- `node-typescript-service + cli-worker`
- `cli-worker + monorepo`
- `cli-worker + python-package`
- `cli-worker + php-package`

Explicitly fail-closed examples:

- `laravel + cli-worker`
- `django + monorepo`
- `service + monorepo`
- `laravel + django`

Use `tools/templates/list_templates.py` to inspect the scaffold manifest inventory.
