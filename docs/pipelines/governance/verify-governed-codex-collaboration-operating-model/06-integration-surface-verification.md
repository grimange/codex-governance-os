# Integration Surface Verification

Layer 5 is discoverable from the required canonical entry surfaces:

- [architecture-doctrine.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/architecture-doctrine.md)
  - references Layer 5 among reusable governance law
  - states collaboration must not imply runtime orchestration, delegation, or
    authority beyond lower layers
- [.codex/AGENTS.md](/home/ramjf/python-projects/codex-governance-os/.codex/AGENTS.md)
  - references Layer 5 directly for collaboration, role handoff, restriction
    propagation, and bounded workflow questions
- [README.md](/home/ramjf/python-projects/codex-governance-os/README.md)
  - exposes Layer 5 in the governance architecture overview

Registry verification:

- pipeline `089` is present in
  [pipeline-registry.md](/home/ramjf/python-projects/codex-governance-os/docs/pipelines/registry/pipeline-registry.md)
  with the correct pipeline id, canonical title, and pipeline definition path
- the current registry schema does not record an explicit artifact bundle path
  for pipeline `089`, so the stricter registry-integrity requirement written in
  pipeline `090` is only partially satisfied

Prior artifact bundle presence:

- the `089` artifact bundle exists at
  [establish-governed-codex-collaboration-operating-model](/home/ramjf/python-projects/codex-governance-os/docs/pipelines/governance/establish-governed-codex-collaboration-operating-model)

Result: `INTEGRATION_SURFACES_VERIFIED_WITH_REGISTRY_RESTRICTION`
