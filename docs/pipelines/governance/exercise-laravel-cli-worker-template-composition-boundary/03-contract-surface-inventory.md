# Contract Surface Inventory

## Contract And Enforcement

- [docs/contracts/universal-template-composition-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/universal-template-composition-contract.md)
  - lists `laravel + cli-worker` in the certified fail-closed boundary
- [tools/templates/composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py)
  - defines `("cli-worker", "laravel"): "incompatible runtime assumptions"`
- [tools/governance/template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_scaffold.py)
  - consumes the contract decision and rejects unsupported scaffold requests

## Manifest Inventory

- [docs/codex/templates/manifests/laravel.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/laravel.json)
  - `compatible_overlays: []`
  - `required_surfaces`: `app`, `bootstrap`, `routes`, `config`
  - `supported_runtime_shapes`: `application`, `service`
- [docs/codex/templates/manifests/cli-worker.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/cli-worker.json)
  - `compatible_overlays`: `python-package`, `php-package`, `node-typescript-service`, `monorepo`
  - `required_surfaces`: `bin`, `jobs`, `worker`
  - `supported_runtime_shapes`: `cli`, `worker`, `batch`

## Overlay Documentation

- [docs/codex/templates/overlays/laravel/README.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/overlays/laravel/README.md)
  - frames Laravel as an application-oriented runtime overlay
- [docs/codex/templates/overlays/cli-worker/README.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/overlays/cli-worker/README.md)
  - frames CLI-worker as a command/batch/worker-oriented runtime overlay

## Verification Inventory

- [tests/governance/test_template_composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_composition_contract.py)
- [tests/governance/test_template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_scaffold.py)
- [tests/governance/test_template_composition_surface_consistency.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_composition_surface_consistency.py)
- [tests/governance/test_template_composition_post_service_monorepo_protections.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_template_composition_post_service_monorepo_protections.py)

These tests already treat any admission of `laravel + cli-worker` as drift or contract breakage.
