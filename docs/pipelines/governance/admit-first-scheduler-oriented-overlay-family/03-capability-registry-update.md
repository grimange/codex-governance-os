# Capability Registry Update

The capability registry at [template_capability_registry.json](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_capability_registry.json) now admits:

- capability `scheduler-runtime`
- role `scheduler`

The role is intentionally narrow. It is admitted with:

- `base`
- `worker`
- `package`
- `topology`

The conflict taxonomy also now classifies duplicate `scheduler-runtime` claims as `runtime-ownership-collision`, which gives future scheduler-family expansion a deterministic safety boundary.
