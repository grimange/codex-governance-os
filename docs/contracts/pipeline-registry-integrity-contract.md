# Pipeline Registry Integrity Contract

## Purpose

This contract defines how the pipeline registry must represent active governance pipelines and how repository governance work must interact with that registry.

## Scope

This contract governs:

- `docs/pipelines/registry/pipeline-registry.md`
- active pipeline definitions under `docs/pipelines/`
- the relationship between registry state and pipeline activation
- governance work that depends on accurate pipeline discoverability

This contract does not define pipeline-internal phase logic, artifact content rules, or product-domain architecture.

## Governing Authority

Authority for this contract is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. this contract
5. active pipeline definitions
6. generated pipeline artifacts

This contract refines registry behavior without overriding higher-order governance authority.

## Canonical Rules

1. A governance pipeline is active when the repository is using it as an operational workflow for current or future governed work.
2. Every active pipeline must have exactly one corresponding registry entry in `docs/pipelines/registry/pipeline-registry.md`.
3. Each registry entry must include pipeline ID, pipeline name, status, category, and canonical path.
4. Registry entries must point to real pipeline definition files in version control.
5. The pipeline ID in the registry must match the ID declared or implied by the pipeline filename.
6. The registry records activation and discoverability status only; it must not redefine the pipeline's substantive procedure.
7. Proposed or draft status text inside a pipeline definition does not excuse omission from the registry when the pipeline is operationally active.
8. Placeholder category directories are not active pipelines and must not be entered in the registry.
9. Registry updates must occur no later than the same governed change set that activates a pipeline for operational use.

## Allowed Behaviors

- registering a pipeline when it becomes active
- correcting stale paths, names, or IDs in existing registry entries
- leaving inactive placeholder category roots unregistered
- using the registry as a discoverability surface for governance routing and audit

## Prohibited Behaviors

- operating an active pipeline without a registry entry
- creating duplicate registry entries for one active pipeline
- using the registry to override higher-order governance authority
- registering missing, placeholder, or non-operative surfaces as if they were active pipelines

## Compliance Signals

Compliance is indicated when:

- every active pipeline in `docs/pipelines/` appears once in the registry
- every registry entry resolves to an existing pipeline definition
- IDs, names, and paths remain internally consistent
- audits can determine active governance coverage from the registry without reconstructing it from scattered evidence

Non-compliance is indicated when:

- active pipelines are absent from the registry
- registry entries point to missing files
- duplicate or contradictory entries exist
- audits must infer active status from artifacts alone

## Ambiguity Handling

- If a pipeline exists but is not yet operationally active, it may remain unregistered.
- If a pipeline is being actively executed, it is operationally active even if its definition still says `PROPOSED`.
- If activation status is disputed, the repository must resolve the dispute explicitly in version control rather than leaving the registry silent.

## Governance Implications

- Future governance audits may treat registry omissions for active pipelines as a contract violation.
- Contract discovery and contract authoring pipelines should use this contract to decide whether registry state is sufficient for downstream work.
- Promotion of new governance workflows must include registry discipline as part of operational readiness.

## Non-Goals

This contract does not:

- define artifact numbering inside a pipeline
- define lifecycle sequencing across all governance categories
- authorize product-domain contracts
- replace the architecture doctrine or repository constitution
