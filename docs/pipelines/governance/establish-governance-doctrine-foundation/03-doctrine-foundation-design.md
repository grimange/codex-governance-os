# Doctrine Foundation Design

## Design Principles

- The doctrine set must be generic across project domains.
- Each document must define one governance surface cleanly enough that future pipelines can reference it instead of restating baseline rules.
- The doctrine set must complement, not replace, the constitution and architecture doctrine.

## `docs/governance/governance-lifecycle.md`

- Intent: define the standard lifecycle model for governed work.
- Required contents: lifecycle purpose, standard stages, default stage order, permitted deviations, dependency rules, and how promotion relates to completion.
- Design choice: describe a reusable stage model rather than hard-coding one numeric pipeline sequence.

## `docs/governance/pipeline-artifact-standard.md`

- Intent: define how pipeline runs are recorded as durable artifact bundles.
- Required contents: artifact principles, minimum bundle surfaces, numbering expectations, directory placement, naming consistency, evidence requirements, and exceptions policy.
- Design choice: standardize closure expectations while allowing explicitly justified phase omissions.

## `docs/governance/pipeline-naming-standard.md`

- Intent: make pipeline identity deterministic at the file, directory, and registry levels.
- Required contents: filename pattern, numeric prefix rules, slug logic, category expectations, registry identity matching, and collision/supersession handling.
- Design choice: preserve the existing `NNN--verb-first-slug.md` convention and formalize its constraints.

## `docs/governance/contract-writing-standard.md`

- Intent: provide a standard shape for future canonical subsystem contracts.
- Required contents: contract purpose, required sections, authority expression, scope and non-goals, lifecycle/interface expectations where relevant, compatibility treatment, and governance implications.
- Design choice: define a normative minimum section set while allowing section depth to vary by subsystem complexity.

## `docs/governance/governance-terminology.md`

- Intent: establish controlled meanings for recurring governance terms used across doctrine, contracts, pipelines, and artifacts.
- Required contents: operational definitions for contract, authority, architecture doctrine, pipeline, registry, drift, remediation, verification, promotion, canonical, compatibility layer, legacy residual, subsystem, evidence, and final verdict.
- Design choice: keep definitions short and operational so they can be used during audits and promotion decisions without interpretation overhead.

## Cross-Document Relationship

- `governance-lifecycle.md` governs sequencing vocabulary.
- `pipeline-artifact-standard.md` governs evidence packaging.
- `pipeline-naming-standard.md` governs file and registry identity.
- `contract-writing-standard.md` governs contract authoring shape.
- `governance-terminology.md` governs shared word meaning.

Together these documents form the reusable doctrine foundation beneath future governance pipelines.
