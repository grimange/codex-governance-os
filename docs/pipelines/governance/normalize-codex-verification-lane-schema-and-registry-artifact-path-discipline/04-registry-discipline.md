# Registry Discipline

The pipeline registry now records:

- `pipeline_definition_path`
- `artifact_bundle_path`

Registry contract alignment:

- [pipeline-registry-integrity-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/pipeline-registry-integrity-contract.md)
  now requires both paths
- [pipeline-registry.md](/home/ramjf/python-projects/codex-governance-os/docs/pipelines/registry/pipeline-registry.md)
  now exposes both columns for active pipelines

Artifact-bundle path derivation rule:

- bundle roots use the canonical pipeline artifact directory, normally
  `docs/pipelines/<category>/<pipeline-slug>/`

This change removes the need for later verification lanes to infer artifact
bundle locations from naming convention alone.
