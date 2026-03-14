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
- `scheduler`

Verified supported compositions:

- base-only
- `django + scheduler`
- `scheduler` as an admitted single-overlay realization
- `laravel + scheduler`
- `laravel + monorepo`
- `django + monorepo`
- `service + monorepo`
- `node-typescript-service + monorepo`
- `node-typescript-service + cli-worker`
- `cli-worker + monorepo`
- `cli-worker + monorepo + scheduler`
- `cli-worker + monorepo + python-package`
- `cli-worker + python-package`
- `cli-worker + python-package + scheduler`
- `cli-worker + scheduler`
- `cli-worker + php-package`
- `monorepo + scheduler`
- `python-package + scheduler`

Explicitly fail-closed examples:

- `laravel + cli-worker`
  Reason: missing Laravel worker composition contract
- `laravel + django`
  Reason: cross-framework application collision

Use `tools/templates/list_templates.py` to inspect the scaffold manifest inventory.

The certified composition boundary for these overlays is published in `docs/contracts/universal-template-composition-contract.md`, and scaffold plus manifest-inspection tooling enforce that boundary fail-closed.

Use `python tools/governance/template_scaffold.py doctor-composition --overlays ... --output json` to inspect why a composition is supported or rejected and to see the closest certified alternatives.

Use `python tools/governance/template_scaffold.py verify-composition-matrix` to continuously verify that the governed matrix snapshot, runtime behavior, manifest declarations, and explicit rejection reasons remain aligned.

Capability-based composition metadata is now governed through [template_capability_registry.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_capability_registry.json) and manifest `capabilities` declarations under [docs/codex/templates/manifests](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests).

Each admitted manifest now declares:

- `provides`
- `requires`
- `conflicts`
- `composition_role`

The capability layer does not replace the certified contract. It provides a universal vocabulary and resolution model that must preserve the already-certified matrix, and `verify-composition-matrix` now fails if capability evaluation diverges from the governed composition contract.

Capability conflicts are now classified with a formal taxonomy. The doctor surface keeps the top-level classification in `reason_code` and exposes the canonical taxonomy in `conflict_code`.

Current canonical conflict codes:

- `cross-framework-application-collision`
- `framework-native-scheduler-required`
- `runtime-ownership-collision`
- `worker-model-collision`
- `entrypoint-surface-collision`
- `package-application-role-collision`
- `workspace-orchestration-collision`

Framework-native scheduler support currently exists for the direct pairs `laravel + scheduler` and `django + scheduler`. The Django-native contract requires the canonical scheduler surface at `project/celery.py` and the companion surfaces `project/scheduler.py`, `project/settings.py`, and `manage.py`. Broader compound framework-native scheduler combinations remain unsupported unless a future lane admits them explicitly.
