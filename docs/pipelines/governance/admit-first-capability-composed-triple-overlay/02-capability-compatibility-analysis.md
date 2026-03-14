# Capability Compatibility Analysis

The admitted triple is:

- `cli-worker + monorepo + python-package`

Capability fit:

- `cli-worker`
  - provides `worker-runtime`
  - role `worker`
- `monorepo`
  - provides `workspace-orchestration`
  - role `topology`
- `python-package`
  - provides `package-distribution`, `python-runtime`
  - role `package`

Why it is supportable:

- all overlays still inherit `runtime-environment` from `universal-base`
- no overlay in the composition declares a conflicting capability against the others
- the capability role registry now admits `worker + topology + package`
- no Laravel-style explicit worker conflict is introduced
