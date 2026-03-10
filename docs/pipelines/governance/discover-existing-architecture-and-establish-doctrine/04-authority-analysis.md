# Authority Analysis

## Authority Classification

| Surface | Classification | Justification |
|---------|----------------|---------------|
| Version-controlled repository state | canonical authority | Highest evidence and control surface; every other authority is expressed through tracked files. |
| `AGENTS.md` | canonical authority | Explicitly defines repository-local authority precedence and governance model. |
| `docs/governance/architecture-doctrine.md` | canonical authority after replacement | Intended doctrine surface and the only document dedicated to architecture authority. |
| Registered pipeline definitions | canonical authority | The constitution explicitly elevates registered pipeline definitions. |
| `docs/pipelines/registry/pipeline-registry.md` | likely authority candidate | Operational activation surface, but subordinate to the definitions it references. |
| `.codex/AGENTS.md` | likely authority candidate | Repository-local agent instruction surface aligned to higher authorities. |
| Pipeline execution artifacts | descriptive but non-authoritative | Required durable evidence, but they record outcomes rather than outrank governing docs. |
| Placeholder roots and `.gitkeep` files | descriptive but non-authoritative | They indicate intended location only. |

## Implementation Authority Versus Document Authority

- Implementation authority and document authority are effectively the same today because the repository contains documentation-based governance surfaces and no separate application implementation.
- The authoritative implementation is the repository structure plus the tracked governance files themselves.

## Runtime Truth Versus UI Truth

- No runtime layer or UI layer is present.
- Any future runtime or UI truth model would require new evidence and likely doctrine revision.

## Persistent Truth Versus Derived Truth

- Persistent truth: tracked Markdown and support files in version control.
- Derived truth: pipeline summaries, verification artifacts, and registry views derived from those tracked sources.

## Command Path Versus Event Path

- The canonical command path is pipeline-definition-driven document authoring in version control.
- No event-driven architecture is evidenced.

## Canonical Lifecycle Vocabulary Versus Competing Vocabularies

- Canonical vocabulary already present: constitution, doctrine, pipeline definition, registry, verification, promotion, verdict.
- Competing vocabulary risk: treating initialization-only doctrine as final architecture doctrine, or treating placeholder folders as real subsystems.

## Direct State Mutation Versus Projected State Consumption

- Direct state mutation occurs when authoritative governance files are edited in version control.
- Projected state consumption occurs when agents or later pipelines read doctrines, registry entries, and prior pipeline artifacts to decide future actions.

## Conclusion

The repository's strongest present authority structure is a document-governed architecture in which the constitution and doctrine define meaning, registered pipelines define process, and pipeline artifacts record evidence. No stronger non-document authority source is evidenced.
