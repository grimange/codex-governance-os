# Doctrine Authoring Plan

## File Creation Order

1. `docs/governance/governance-terminology.md`
2. `docs/governance/governance-lifecycle.md`
3. `docs/governance/pipeline-artifact-standard.md`
4. `docs/governance/pipeline-naming-standard.md`
5. `docs/governance/contract-writing-standard.md`

This order establishes shared vocabulary first, then lifecycle, then artifact and naming rules, and finally contract-writing guidance that depends on those baseline terms.

## Source Fragments To Normalize

- Authority, artifact, and routing rules from `AGENTS.md`
- Operating expectations from `.codex/AGENTS.md`
- Artifact and lifecycle patterns from executed governance bundles under `docs/pipelines/governance/`
- Naming and registry identity behavior already implemented by pipeline filenames and `docs/pipelines/registry/pipeline-registry.md`
- Contract section requirements from `docs/pipelines/governance/004--author-canonical-contract-for-highest-priority-subsystem.md`
- Terminology fragments from `docs/governance/architecture-doctrine.md` and existing governance pipeline bodies

## Embedded Rules To Move Out Of Pipelines

- repeated expectations that pipelines produce summaries, explicit promotion decisions, and explicit final verdicts
- repeated assumptions about lifecycle sequence between discovery, audit, remediation, verification, and promotion
- repeated contract section requirements in contract-authoring workflows
- repeated filename and artifact-numbering conventions currently enforced only by imitation

## Expected Cross-References

- `AGENTS.md` should reference the doctrine set in `docs/governance/`
- `.codex/AGENTS.md` should direct agents to use the doctrine foundation operationally
- `docs/governance/architecture-doctrine.md` should acknowledge the doctrine foundation as part of the repository’s doctrinal layer
- `docs/pipelines/registry/pipeline-registry.md` should register pipeline `008` as an active governance surface

## Supporting Surfaces Expected To Need Updates

- `AGENTS.md`
- `.codex/AGENTS.md`
- `docs/governance/architecture-doctrine.md`
- `docs/pipelines/registry/pipeline-registry.md`

## Intentionally Outside Doctrine

- project-specific architecture truths
- subsystem-specific contracts
- automatic normalization of every existing pipeline body
- domain-specific lifecycle rules
- non-Markdown artifact formats except where a future higher-authority document justifies them
