# Conformance Surface Alignment

Updated conformance surfaces:

- [layer-6-codex-session-orchestration-and-handoff-discipline.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md)
  now references and summarizes the canonical lifecycle state machine
- [codex-session-registry.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/codex-session-registry.md)
  now uses the canonical state names for `lifecycle_status`
- [codex-session-ledger.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/codex-session-ledger.md)
  now ties event recording to the state machine and includes `from_state` and
  `to_state` for transition evidence
- [codex-session-handoff-packet-and-continuity-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/codex-session-handoff-packet-and-continuity-contract.md)
  now treats lifecycle meaning as governed by the state machine canon and
  includes `lifecycle_state` in the required handoff field family
- [architecture-doctrine.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/architecture-doctrine.md),
  [.codex/AGENTS.md](/home/ramjf/python-projects/codex-governance-os/.codex/AGENTS.md),
  and [README.md](/home/ramjf/python-projects/codex-governance-os/README.md)
  now expose the canon as a discoverable authority surface
- [pipeline-registry.md](/home/ramjf/python-projects/codex-governance-os/docs/pipelines/registry/pipeline-registry.md)
  now registers pipeline `102`
