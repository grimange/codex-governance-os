# Current Registry Vs Repository Truth

Pre-normalization registry state for pipeline `089`:

- pipeline id present: `089`
- canonical title present: `Establish Governed Codex Collaboration Operating Model`
- status present: `ACTIVE`
- category present: `governance`
- pipeline definition path present:
  `docs/pipelines/governance/089--establish-governed-codex-collaboration-operating-model.md`
- explicit artifact-bundle path absent from the registry entry

Repository truth confirmed:

- pipeline definition exists at
  [089--establish-governed-codex-collaboration-operating-model.md](/home/ramjf/python-projects/codex-governance-os/docs/pipelines/governance/089--establish-governed-codex-collaboration-operating-model.md)
- the canonical artifact bundle exists at
  [establish-governed-codex-collaboration-operating-model](/home/ramjf/python-projects/codex-governance-os/docs/pipelines/governance/establish-governed-codex-collaboration-operating-model)
- the bundle contents correspond to the establishment lane for `089`

Mismatch identified:

- the registry entry reflected the pipeline definition file but not the
  executed artifact-bundle directory already present in repository state

Result: `REGISTRY_BEHIND_REPOSITORY_TRUTH_FOR_089`
