# Architecture Doctrine

## Purpose

This doctrine establishes the canonical architecture authority for this repository. It exists so future governance, contract, audit, remediation, verification, and promotion work can reason from explicit repository evidence instead of assumptions.

## Scope

This doctrine governs the repository's current architecture as evidenced in version control:

- the repository constitution in `AGENTS.md`
- the repository-local Codex operating surface in `.codex/AGENTS.md`
- governance doctrine under `docs/governance/`
- pipeline specifications under `docs/pipelines/`
- generated pipeline execution artifacts under `docs/pipelines/<category>/<pipeline-name>/`

This doctrine does not define any product-domain application architecture because no application implementation is currently present in the repository.

## Authority Precedence

Architecture and implementation decisions in this repository are governed in the following order:

1. Version-controlled repository state
2. `AGENTS.md`
3. This doctrine
4. Registered pipeline specifications in `docs/pipelines/`
5. Generated pipeline execution artifacts
6. Descriptive or placeholder documentation not elevated by the authorities above

Pipeline artifacts may record evidence and decisions, but they must not override the repository constitution, this doctrine, or the governing pipeline definition they were produced from.

## System Model

The current system implemented by this repository is a documentation-first governance system.

Its primary architectural layers are:

- constitutional authority: `AGENTS.md`
- agent operating surface: `.codex/AGENTS.md`
- doctrinal authority: `docs/governance/architecture-doctrine.md`
- procedural authority: pipeline definitions in `docs/pipelines/governance/`
- execution evidence: per-pipeline artifacts under `docs/pipelines/governance/<pipeline-name>/`
- registry surface: `docs/pipelines/registry/pipeline-registry.md`

There are no runtime services, databases, UI layers, queues, workers, or external integration modules currently established as canonical architecture within this repository.

## Source of Truth

The canonical source of truth is the version-controlled repository itself.

Within that repository state:

- `AGENTS.md` is the highest repository-local governance authority
- this doctrine is the canonical architecture authority
- registered pipeline definitions are the canonical process definitions
- pipeline artifacts are durable evidence of what was discovered, decided, verified, and promoted

No generated artifact, cache, mirrored note, or future convenience summary may be treated as a higher authority than the version-controlled source documents above.

## Layer Responsibilities

- `AGENTS.md` defines mission, routing, and governance authority ordering.
- `.codex/AGENTS.md` defines repository-local operating behavior for Codex agents.
- `docs/governance/architecture-doctrine.md` defines the canonical architecture model and interpretation rules for repository structure.
- `docs/pipelines/<category>/<id--name>.md` defines the authoritative workflow for a pipeline.
- `docs/pipelines/<category>/<pipeline-name>/NN-*.md` records execution evidence for a specific pipeline run and must remain inspectable and reproducible from repository state.
- `docs/pipelines/registry/pipeline-registry.md` records which pipelines are recognized as active governance surfaces.
- `docs/contracts/` and `docs/modernization/` are reserved canonical roots for future work but are not yet architecture-authoring surfaces in practice.

## State and Projection Rules

- Canonical governance state must be authored in version-controlled Markdown artifacts unless a higher-authority document explicitly permits another format.
- Pipeline definitions author process expectations.
- Pipeline execution artifacts project discovered state, design decisions, verification results, and promotion outcomes for a specific execution.
- Registry entries project activation status for pipelines but do not redefine the pipeline specification itself.
- Placeholder directories and `.gitkeep` files establish location only; they do not establish domain architecture, contracts, or operational truth.

## Compatibility and Legacy Rules

- Initialization-era doctrine or notes that describe only a bootstrap baseline are compatibility-era artifacts once replaced by stronger evidence-based doctrine.
- Proposed pipeline specifications are descriptive until registered and used as active governance surfaces.
- Empty documentation roots, placeholder files, and absent implementation layers must not be misread as evidence of an implemented subsystem.
- If future product code or operational surfaces are added, this doctrine must be revised through a documented pipeline rather than silently stretched to cover them.

## Terminology Rules

- "Repository state" means the tracked contents of version control at a given revision.
- "Constitution" means `AGENTS.md`.
- "Doctrine" means `docs/governance/architecture-doctrine.md`.
- "Pipeline definition" means a governing specification file under `docs/pipelines/`.
- "Pipeline artifact" means a phase output generated by running a pipeline.
- "Canonical" means authoritative for decision-making.
- "Descriptive" means informative but not authoritative by itself.
- "Placeholder" means a reserved surface with no implemented authority beyond location.

Because the repository currently has no application runtime, terms such as backend, frontend, service, database, event bus, and UI are non-canonical unless and until later repository evidence establishes them.

## Governance Implications

- Future architecture, contract, and audit pipelines must treat this repository as a governance-surface system first, not as an implied software product with hidden runtime layers.
- New authoritative architecture claims must be grounded in repository evidence and installed through version-controlled governance work.
- When future implementation code appears, downstream pipelines must explicitly determine whether this doctrine remains sufficient or requires replacement.
- Verification work must distinguish between authoritative documents, execution evidence, and placeholder surfaces.
- Promotion decisions must not treat empty folders or descriptive stubs as completed architecture.

## Non-Goals

This doctrine does not:

- define product-domain business architecture
- declare runtime or production behavior
- create subsystem contracts for absent systems
- certify that the repository is free of future architecture drift
- replace the need for later discovery, audit, remediation, or contract-authoring pipelines
