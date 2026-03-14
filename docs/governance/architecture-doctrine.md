# Architecture Doctrine

## Purpose

This doctrine establishes the canonical architecture authority for this repository. It exists so future governance, contract, audit, remediation, verification, and promotion work can reason from explicit repository evidence instead of assumptions.

## Scope

This doctrine governs the repository's current architecture as evidenced in version control:

- the repository constitution in `AGENTS.md`
- the repository-local Codex operating surface in `.codex/AGENTS.md`
- governance doctrine under `docs/governance/`, including the doctrine foundation documents for lifecycle, artifact, naming, contract-writing, and terminology rules
- universal skills under `.codex/skills/`
- repository-local skill extensions under `.codex/skills/`
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

The `docs/` directory is the authoritative root for all governance and Codex-related files in this repository.

Its primary architectural layers are:

- constitutional authority: `AGENTS.md`
- agent operating surface: `.codex/AGENTS.md`
- doctrinal authority: `docs/governance/architecture-doctrine.md` and the doctrine foundation documents under `docs/governance/`
- reusable skill authority: universal skills under `.codex/skills/`, interpreted through governance doctrine and skill invocation rules
- local skill specialization: `.codex/skills/`
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
- `docs/governance/governance-lifecycle.md`, `docs/governance/pipeline-artifact-standard.md`, `docs/governance/pipeline-naming-standard.md`, `docs/governance/contract-writing-standard.md`, `docs/governance/governance-terminology.md`, `docs/governance/governance-evidence-interpretation-canon.md`, `docs/governance/governance-safety-invariants-canon.md`, `docs/governance/layer-3-codex-rules-canon.md`, `docs/governance/layer-4-codex-role-model.md`, `docs/governance/layer-5-codex-collaboration-operating-model.md`, `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`, `docs/governance/codex-session-registry.md`, `docs/governance/codex-session-ledger.md`, `docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md`, `docs/governance/codex-session-admission-and-activation-rules.md`, `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`, `docs/governance/codex-session-lifecycle-observation-discipline.md`, `docs/governance/codex-session-evidence-interpretation-model.md`, `docs/governance/codex-session-reconstruction-rules.md`, `docs/governance/governance-evolution-model.md`, `docs/governance/templates/README.md`, `docs/governance/template-scaffold-contract.md`, `docs/contracts/codex-governance-surface-schema-contract.md`, `docs/contracts/codex-session-state-machine-canon.md`, `docs/contracts/codex-session-handoff-packet-and-continuity-contract.md`, and `docs/contracts/universal-template-composition-contract.md` define reusable governance law and template control surfaces that future pipelines and contracts should reference instead of duplicating.
- `docs/governance/skill-authoring-standard.md`, `docs/governance/skill-invocation-standard.md`, and `docs/governance/universal-skills-index.md` define how governed skills are authored, selected, and discovered.
- `skills/` contains reusable universal skill packages for template inheritance.
- `.codex/skills/` contains project-local skill extensions or overrides when repository-specific specialization is required.
- `docs/pipelines/<category>/<id--name>.md` defines the authoritative workflow for a pipeline.
- `docs/pipelines/<category>/<pipeline-name>/NN-*.md` records execution evidence for a specific pipeline run and must remain inspectable and reproducible from repository state.
- `docs/pipelines/registry/pipeline-registry.md` records which pipelines are recognized as active governance surfaces.
- `docs/contracts/` and `docs/modernization/` are reserved canonical roots for future work but are not yet architecture-authoring surfaces in practice.
- `docs/contracts/universal-template-composition-contract.md` defines the certified overlay composition boundary for the universal scaffold.
- `docs/contracts/codex-governance-surface-schema-contract.md` defines canonical field names and registry path discipline for Codex session-governance surfaces and related verification lanes.
- `docs/contracts/codex-session-state-machine-canon.md` defines the canonical Layer 6 session lifecycle states and transition model for governed Codex sessions.
- `docs/contracts/codex-session-handoff-packet-and-continuity-contract.md` defines the canonical continuity contract for session handoff packets under `docs/codex/sessions/handoffs/`.
- `docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md` defines the canonical admissibility model for governed handoff completion, predecessor-successor linkage, and resumed continuity claims.
- `docs/governance/codex-session-admission-and-activation-rules.md` defines the canonical admission gate, activation rules, and fail-closed execution-entry conditions for governed Codex sessions.
- `docs/governance/codex-session-runtime-boundary-and-evidence-model.md` defines the canonical boundary between documentation-governed session state and future runtime execution evidence, while keeping `session_id`, registry, and ledger compatibility authoritative.
- `docs/governance/codex-session-lifecycle-observation-discipline.md` defines how future lifecycle observations must be normalized into canonical registry and ledger evidence without introducing a competing runtime event schema.
- `docs/governance/codex-session-evidence-interpretation-model.md` defines how session truth is reconstructed from the state machine, ledger, registry, observation, and runtime-boundary surfaces without collapsing their distinct authorities.
- `docs/governance/codex-session-reconstruction-rules.md` defines the deterministic operational method for deriving one bounded session narrative from canonical Layer 6 evidence without inventing events or elevating runtime context.
- `docs/governance/templates/` contains canonical cross-family template definitions for machine-checkable governed artifacts.
- `docs/governance/template-scaffold-contract.md` defines the canonical universal scaffold contract for governed repositories.
- `docs/governance/registries/templates/` contains admitted template identities and the compiled template registry index.
- `docs/codex/templates/` contains admitted template bodies referenced by the template registry.
- `tools/governance/` contains governance tooling such as template registry loading, linting, scaffold generation, and governance preflight scanning for active portability enforcement.
- `tools/templates/` contains manifest schema and discovery helpers for repository-level scaffold inventory.

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
- Governance-framework mutations must follow the governance evolution doctrine so meta-governance changes remain versioned, compatible, and auditable.
- When future implementation code appears, downstream pipelines must explicitly determine whether this doctrine remains sufficient or requires replacement.
- Verification work must distinguish between authoritative documents, execution evidence, and placeholder surfaces.
- Verification and establishment work must interpret governance evidence through `docs/governance/governance-evidence-interpretation-canon.md` instead of relying on local narrative convention.
- Governance mutation, verification, and later normalization work must preserve the fail-closed rules in `docs/governance/governance-safety-invariants-canon.md`.
- Canonical governance and repository-entry references must preserve the repository portability link invariant in `docs/governance/governance-safety-invariants-canon.md`, so machine-local filesystem paths do not become live canonical links or navigation targets.
- Governed execution may use `python tools/governance/preflight.py` as the canonical repository preflight entrypoint, with portability reference violations failing closed before downstream governed execution proceeds.
- Codex-directed work must follow `docs/governance/layer-3-codex-rules-canon.md`, while remaining subordinate to the lower-layer doctrine, interpretation, and execution surfaces.
- Role-scoped Codex specialization must follow `docs/governance/layer-4-codex-role-model.md` and must not imply autonomous orchestration or authority beyond the lower layers.
- Codex collaboration behavior must follow `docs/governance/layer-5-codex-collaboration-operating-model.md` and must not imply runtime orchestration, delegation, or authority beyond Layers 0 through 4.
- Codex session orchestration and handoff behavior must follow `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md` and must not imply runtime orchestration enforcement, automatic delegation, or authority beyond Layers 0 through 5.
- Codex session identity and execution-event recording must follow `docs/governance/codex-session-registry.md` and `docs/governance/codex-session-ledger.md` and must remain documentation-level governance state unless a later lane verifies stronger execution support.
- Codex session handoff continuity must follow `docs/contracts/codex-session-handoff-packet-and-continuity-contract.md` and the canonical packet root at `docs/codex/sessions/handoffs/`, while preserving registry and ledger authority for identity and event truth.
- Codex session-governance field names and pipeline registry path recording must follow `docs/contracts/codex-governance-surface-schema-contract.md` so verification lanes use canonical session fields and deterministic artifact-bundle paths.
- Codex session lifecycle states, allowed transitions, and invalid transition boundaries must follow `docs/contracts/codex-session-state-machine-canon.md` so Layer 6 session-governance surfaces do not drift into incompatible lifecycle models.
- Codex session handoff completion and resumed continuity claims must follow `docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md` so successor sessions rely on explicit predecessor evidence, preserved restrictions, and fail-closed admissibility rules.
- Codex session admission and activation must follow `docs/governance/codex-session-admission-and-activation-rules.md` so initialized or resumed sessions do not become active without bounded scope, explicit restrictions, authoritative evidence, and an admissible first action.
- Future runtime Codex session implementations must follow `docs/governance/codex-session-runtime-boundary-and-evidence-model.md` so runtime-native identifiers and events map back into canonical `session_id`, registry, and ledger evidence rather than redefining Layer 6 session truth.
- Future lifecycle observation support must follow `docs/governance/codex-session-lifecycle-observation-discipline.md` so observed initialization, admission, activation, execution, and closure evidence remain reconstructable through canonical registry and ledger fields.
- Future session-truth reconstruction must follow `docs/governance/codex-session-evidence-interpretation-model.md` so state-machine, ledger, registry, observation, and runtime-boundary evidence are interpreted through one explicit Layer 6 precedence model.
- Future operational session reconstruction must follow `docs/governance/codex-session-reconstruction-rules.md` so governance observers use one explicit evidence-collection, normalization, interpretation, and fail-closed narrative-construction method.
- Governed session closure discipline must require handoff-packet recording when continuity evidence is required, with resulting packet references and continuity violations remaining visible in the session registry and execution ledger.
- Promotion decisions must not treat empty folders or descriptive stubs as completed architecture.

## Non-Goals

This doctrine does not:

- define product-domain business architecture
- declare runtime or production behavior
- create subsystem contracts for absent systems
- certify that the repository is free of future architecture drift
- replace the need for later discovery, audit, remediation, or contract-authoring pipelines
