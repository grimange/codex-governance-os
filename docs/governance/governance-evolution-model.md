# Governance Evolution Model

## Purpose

This doctrine defines how the governance framework itself may change so doctrine, pipelines, registry policy, bootstrap guidance, and publication surfaces evolve in a controlled and auditable way.

## Scope

This doctrine governs mutations to:

- governance doctrine under `docs/governance/`
- active governance pipeline definitions under `docs/pipelines/`
- the pipeline registry
- constitutional and local agent governance instructions when they affect repository governance behavior
- bootstrap and adoption surfaces when they change the governed adoption path
- canonical governance documentation that materially changes framework interpretation

This doctrine does not govern product-domain implementation changes that do not mutate the governance framework itself.

## Mutation Classes

Governance mutations must be classified before implementation:

1. editorial clarification
2. additive compatible extension
3. behavioral refinement
4. breaking governance change
5. deprecation-managed transition
6. emergency corrective repair

Each mutation must record:

- target surface
- mutation class
- rationale
- expected compatibility impact
- whether migration or deprecation handling is required

## Versioning Model

- Editorial clarifications do not change the effective governance version.
- Additive compatible extensions increment the minor governance version.
- Behavioral refinements increment the minor version when compatibility is preserved and the major version when compatibility is not preserved.
- Breaking governance changes increment the major governance version.
- Emergency corrective repairs increment the patch governance version when they restore already-intended behavior without changing the public governance contract materially.

Version meaning is semantic rather than package-based. The authoritative record of governance version changes is the sequence of version-controlled doctrine and pipeline artifacts, not a separate generated build manifest.

## Compatibility Model

- A governance change is compatible when existing adopters can continue using the framework without mandatory structural rework.
- Additive doctrine, new optional pipelines, and clarified discoverability are normally compatible.
- Removing required surfaces, changing authority precedence, or changing active pipeline meaning is normally incompatible unless a migration and deprecation path is recorded.
- Compatibility must be evaluated for small repositories, libraries, CLI tools, frontend applications, backend services, and monorepositories when the affected surface is globally reused.

## Deprecation Model

- Deprecation is required before removing or materially replacing a widely referenced governance surface unless an emergency repair exception is explicitly recorded.
- Deprecation records must identify the deprecated surface, the replacement surface, the reason, and the expected sunset condition.
- Deprecated surfaces may remain as compatibility layers, but they must not be presented as the preferred canonical path once a replacement exists.

## Migration Model

- A migration is required when adopters must update repository structure, doctrine references, skill-routing behavior, or pipeline usage to stay aligned.
- Migration guidance must describe the old model, the new model, the required steps, and any compatibility period.
- Migration work should prefer bounded, inspectable changes and should be routed through a documented pipeline whenever a suitable pipeline exists.

## Control Rules

- No governance mutation may silently alter authority ordering established by the constitution and architecture doctrine.
- No active pipeline may change meaning materially without corresponding registry, documentation, and artifact updates.
- New governance law should be added to canonical doctrine rather than scattered across many pipeline bodies when reuse is expected.
- Governance mutations must preserve domain neutrality unless a higher-authority repository decision explicitly narrows scope.
- Promotion decisions for meta-governance work must remain explicit.

## Compliance Signals

Signals that this doctrine is being followed include:

- mutation class recorded in pipeline artifacts
- compatibility, deprecation, and migration impacts explicitly assessed
- supporting surfaces updated coherently
- architecture doctrine and registry alignment maintained
- final verdict or promotion artifacts describing the governance change outcome

## Non-Goals

This doctrine does not:

- prescribe application runtime versioning
- replace the pipeline catalog
- require numeric release tagging for every governance edit
- forbid urgent corrective work when repository safety requires it
