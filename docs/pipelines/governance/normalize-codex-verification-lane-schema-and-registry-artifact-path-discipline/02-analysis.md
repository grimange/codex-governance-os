# Analysis

Documented drift sources confirmed:

- [099--verify-end-to-end-codex-session-continuity-enforcement.md](/home/ramjf/python-projects/codex-governance-os/docs/pipelines/governance/099--verify-end-to-end-codex-session-continuity-enforcement.md)
  used `session_start` and `session_end`
- [098--integrate-codex-session-handoff-enforcement-into-governance-execution.md](/home/ramjf/python-projects/codex-governance-os/docs/pipelines/governance/098--integrate-codex-session-handoff-enforcement-into-governance-execution.md)
  used the same deprecated field names
- the prior registry contract required only a single canonical path, while
  recent normalization lanes already depended on explicit artifact-bundle path
  discoverability

Normalization strategy selected:

- define a canonical schema contract for Codex session-governance surfaces
- upgrade the pipeline-registry integrity contract to require both definition
  and artifact-bundle paths
- normalize the active lane definitions carrying deprecated field names
- rewrite the active pipeline registry into explicit
  `pipeline_definition_path` and `artifact_bundle_path` columns
