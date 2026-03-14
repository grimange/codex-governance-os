# Scheduler Overlay Definition

The new overlay is:

- `scheduler`

It is defined canonically in [scheduler.json](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests/scheduler.json) and documented in [scheduler/README.md](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/overlays/scheduler/README.md).

Governed capability declaration:

- `provides: ["scheduler-runtime"]`
- `requires: ["runtime-environment"]`
- `conflicts: []`
- `composition_role: "scheduler"`

Deterministic scaffold surfaces:

- `scheduler/`
- `scheduler/schedule.py`
- `scheduler/scheduler_runtime.py`
