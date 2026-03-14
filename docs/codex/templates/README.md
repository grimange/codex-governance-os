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
- `laravel + monorepo`
- `django + monorepo`
- `service + monorepo`
- `node-typescript-service + monorepo`
- `node-typescript-service + cli-worker`
- `cli-worker + monorepo`
- `cli-worker + python-package`
- `cli-worker + php-package`

Explicitly fail-closed examples:

- `laravel + cli-worker`
- `laravel + django`

Use `tools/templates/list_templates.py` to inspect the scaffold manifest inventory.

The certified composition boundary for these overlays is published in `docs/contracts/universal-template-composition-contract.md`, and scaffold plus manifest-inspection tooling enforce that boundary fail-closed.

Use `python tools/governance/template_scaffold.py doctor-composition --overlays ... --output json` to inspect why a composition is supported or rejected and to see the closest certified alternatives.
