# Governance Doctrine Compatibility

| archetype | lifecycle doctrine | artifact standard | naming standard | contract writing standard | terminology doctrine | assessment |
|-----------|--------------------|-------------------|-----------------|---------------------------|---------------------|------------|
| backend service | compatible | compatible | compatible | compatible | compatible | strong fit |
| frontend application | compatible | compatible | compatible | partially compatible | compatible | strong fit with optional contract depth |
| CLI tool | compatible | compatible | compatible | partially compatible | compatible | compatible with lighter contract usage |
| infrastructure automation | compatible | compatible | compatible | compatible | compatible | strong fit |
| library or SDK | compatible | compatible | compatible | compatible | compatible | strong fit |
| mixed monorepository | compatible | compatible | compatible | compatible | compatible | strong fit with scale discipline required |

## Findings

- `docs/governance/governance-lifecycle.md` remains archetype-neutral because it defines ordering between governance stages rather than runtime architecture assumptions.
- `docs/governance/pipeline-artifact-standard.md` and `docs/governance/pipeline-naming-standard.md` are neutral administrative rules and work across all archetypes.
- `docs/governance/contract-writing-standard.md` is broadly reusable, but small CLI and frontend repositories may not need contract density early; this is a workload question, not a stack bias.
- `docs/governance/governance-terminology.md` stays generic and does not force backend, telecom, SaaS, or event-driven vocabulary.

Overall doctrine compatibility is high. The only recurring caveat is proportionality: smaller repositories may adopt the doctrine with fewer downstream contracts and fewer active pipelines.
