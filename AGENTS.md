# Repository Governance Constitution

## Mission

This repository is operated as a Codex-governed project. Its purpose is to maintain a deterministic, reviewable governance surface for repository evolution, pipeline execution, and artifact verification.

## Canonical Authorities

Authority precedence is:

1. Repository source of truth in version control
2. This repository constitution
3. Governance doctrine under [`docs/governance/`](docs/governance/), including [`docs/governance/architecture-doctrine.md`](docs/governance/architecture-doctrine.md)
4. Registered pipeline definitions in [`docs/pipelines/`](docs/pipelines/)
5. Generated pipeline artifacts that record execution evidence

If authorities conflict, the higher-precedence artifact governs until the conflict is resolved explicitly in version control.

## Pipeline Governance Model

- Governance-affecting work should be expressed through documented pipelines when a pipeline exists.
- Pipelines must produce durable artifacts under the repository documentation tree.
- Pipeline registration is mandatory for active pipelines.
- Deterministic sequencing is required: inputs, outputs, and promotion decisions must be recorded.
- When reusable universal skills exist for a pipeline's operational behavior, pipelines should reference those skills instead of restating the behavior inline.

## Artifact Standards

- Governance artifacts are written in Markdown unless a different format is justified.
- Artifacts must be named predictably and stored in canonical folders.
- Verification and promotion decisions must be explicit, not implied.
- Generated records should be concise, inspectable, and reproducible from repository state.
- Pipeline lifecycle, artifact, naming, contract-writing, and terminology doctrine should be sourced from canonical governance documents under `docs/governance/` rather than redefined ad hoc.

## Routing Rules

- Governance doctrine belongs in `docs/governance/`.
- Contracts belong in `docs/contracts/`.
- Pipelines belong in `docs/pipelines/` grouped by category.
- Registry state belongs in `docs/pipelines/registry/pipeline-registry.md`.
- Universal repository skills belong in `skills/`.
- Project-local skill extensions or overrides belong in `.codex/skills/`.
- Repository-local Codex operating instructions belong in `.codex/AGENTS.md`.
