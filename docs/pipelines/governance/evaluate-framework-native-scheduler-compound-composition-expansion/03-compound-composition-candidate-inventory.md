# Compound Composition Candidate Inventory

| Candidate | Current State | Evidence | Decision |
|---|---|---|---|
| `laravel + monorepo + scheduler` | unsupported | [laravel.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/laravel.json), [monorepo.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/monorepo.json), [universal-template-composition-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/universal-template-composition-contract.md) | `SAFE_TO_OPEN_NEXT` |
| `django + monorepo + scheduler` | unsupported | [django.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/django.json), [monorepo.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/monorepo.json), [universal-template-composition-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/universal-template-composition-contract.md) | `SAFE_TO_OPEN_NEXT` |
| `laravel + cli-worker + scheduler` | unsupported with explicit Laravel worker conflict foundation | [laravel.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/laravel.json), [cli-worker.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/cli-worker.json), [template_capability_registry.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_capability_registry.json) | `KEEP_EXPLICITLY_REJECTED` |
| `django + cli-worker + scheduler` | unsupported | [django.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/django.json), [cli-worker.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/cli-worker.json), [template_capability_registry.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_capability_registry.json) | `DEFER_UNTIL_HIGHER_ORDER_COMPOSITION_MODEL` |
| `laravel + monorepo + cli-worker + scheduler` | unsupported | current matrix and role model | `DEFER_UNTIL_HIGHER_ORDER_COMPOSITION_MODEL` |
| `django + monorepo + cli-worker + scheduler` | unsupported | current matrix and role model | `DEFER_UNTIL_HIGHER_ORDER_COMPOSITION_MODEL` |

## Candidate Summary

Monorepo compounds are the only candidates that reuse already-certified pairwise
contracts on every edge:

- `framework + monorepo`
- `framework + scheduler`
- `monorepo + scheduler`

Worker compounds do not have that foundation and introduce a different ownership
model.
