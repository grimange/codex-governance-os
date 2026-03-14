# Manifest Boundary Codification

The unsupported status is enforced from both policy and manifest inventory:

- [docs/codex/templates/manifests/laravel.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/laravel.json)
  - `compatible_overlays: []`
- [docs/codex/templates/manifests/cli-worker.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/cli-worker.json)
  - does not list `laravel`
- [tools/templates/composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py)
  - explicitly rejects `("cli-worker", "laravel")` with reason `missing Laravel worker composition contract`
- [docs/contracts/universal-template-composition-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/universal-template-composition-contract.md)
  - records the pair in the certified fail-closed boundary and states the specific rationale

This combination means manifest drift alone cannot silently admit the pair. Any attempted declaration remains a contract violation.
