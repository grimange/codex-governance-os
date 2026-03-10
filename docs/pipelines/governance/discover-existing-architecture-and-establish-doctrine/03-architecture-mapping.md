# Architecture Mapping

## System Context

This repository currently implements a Codex-governed documentation and process-control system. Its primary purpose is to maintain deterministic governance artifacts, pipeline specifications, and pipeline execution evidence in version control.

## Major Components

| Component | Responsibility |
|-----------|----------------|
| Repository constitution (`AGENTS.md`) | Defines mission, authority order, artifact rules, and routing rules. |
| Local Codex operating surface (`.codex/AGENTS.md`) | Constrains agent behavior to repository governance expectations. |
| Architecture doctrine (`docs/governance/architecture-doctrine.md`) | Defines canonical architecture interpretation and authority rules. |
| Governance pipeline definitions (`docs/pipelines/governance/*.md`) | Define repeatable workflows for initialization, discovery, and later governance tasks. |
| Pipeline execution artifact directories | Preserve run-specific evidence, decisions, verification, and verdicts. |
| Pipeline registry (`docs/pipelines/registry/pipeline-registry.md`) | Records active pipeline surfaces for discoverability and governance routing. |
| Reserved documentation roots (`docs/contracts/`, `docs/modernization/`) | Hold places for future canonical documents but do not yet author domain truth. |

## State Authority Model

- Canonical state lives in version-controlled repository files.
- The constitution is the top repository-local governance authority.
- The doctrine is the top architecture interpretation authority.
- Pipeline definitions author procedure.
- Pipeline artifacts record evidence and decisions derived from a given procedure.
- Placeholder directories do not author architecture; they only reserve namespace.

## Flow Model

1. Repository governance starts from tracked files in version control.
2. The constitution establishes authority and routing.
3. The doctrine interprets the architectural meaning of repository surfaces.
4. A registered pipeline definition specifies required phases and outputs.
5. Pipeline execution generates phase artifacts documenting discovery, analysis, verification, promotion, and verdict.
6. Later governance work consumes those authoritative documents and artifacts without reversing the authority order.

There is no evidence of command processing, runtime eventing, persistence services, or UI projection beyond the document and file hierarchy itself.

## Dependency Model

- `.codex/AGENTS.md` depends on the constitution and doctrine for authority context.
- The doctrine depends on repository evidence and must remain subordinate to the constitution.
- Pipeline definitions depend on the constitution and doctrine for governance context.
- Pipeline artifacts depend on the corresponding pipeline definition and repository state.
- The registry depends on pipeline definitions to identify active surfaces.

External dependencies are not evidenced in the current repository beyond Git and Markdown as operating media.

## Legacy And Compatibility Zones

- The pre-existing bootstrap doctrine is a compatibility-era baseline rather than sufficient final doctrine.
- Placeholder roots under `docs/contracts/` and `docs/modernization/` are reserved, not active architectural subsystems.
- The discovery pipeline's `PROPOSED` status was a transitional signal until this execution installs it as an operational governance surface.
