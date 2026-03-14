# Ownership And Authority Boundary Analysis

## Monorepo Candidates

For both framework-plus-monorepo-plus-scheduler candidates, scheduler authority
can remain singular if the framework-native scheduler surfaces continue to own
scheduler truth:

- Laravel authority:
  - `app/Console/Kernel.php`
  - `routes/console.php`
  - `config/scheduler.php`
- Django authority:
  - `project/celery.py`
  - `project/scheduler.py`
  - companion framework surfaces already required by the direct pair

In these compounds, `monorepo` only adds placement and repository topology. It
does not introduce a second scheduler authority. That makes monorepo compounds
supportable in principle.

## Worker Candidates

Worker compounds are materially different.

- [laravel.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/laravel.json) explicitly conflicts with `worker-runtime`
- [template_capability_registry.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_capability_registry.json) does not permit `framework + worker` role composition
- [cli-worker.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/cli-worker.json) introduces a second execution-ownership model oriented around command and worker entrypoints

For `laravel + cli-worker + scheduler`, the worker conflict is already strong
enough to justify keeping the boundary explicitly rejected.

For `django + cli-worker + scheduler`, there is no dedicated explicit rejection
yet, but the role model still excludes `framework + worker`, and opening it
would require a new execution-ownership doctrine rather than just a placement
contract. That makes it a higher-order model problem, not the next safe
expansion.
