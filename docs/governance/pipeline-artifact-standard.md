# Pipeline Artifact Standard

## Purpose

This doctrine defines the minimum standard for durable pipeline artifact bundles so governance work remains inspectable, reproducible, and efficient to reuse.

## Artifact Bundle Principles

- Every executed pipeline must leave durable artifacts under `docs/pipelines/<category>/<pipeline-name>/` unless a higher-authority surface explicitly authorizes another location.
- Artifact bundles must be concise enough to inspect quickly and specific enough to justify their conclusions.
- The bundle must make stage progression and closure explicit rather than implied.

## Minimum Artifact Expectations

Unless a pipeline definition explicitly narrows or expands the requirement, an executed pipeline bundle should include:

- a `00-` summary artifact
- numbered phase artifacts for each materially executed phase
- an explicit promotion-decision artifact when promotion is part of the pipeline
- a final-verdict artifact that states the end result

If a phase is skipped legitimately, the bundle should either omit the artifact with explicit justification elsewhere or include a brief artifact stating why the phase was not required.

## Numbering Expectations

- Phase artifacts use a two-digit leading numeric prefix such as `00-`, `01-`, or `14-`.
- Numeric order must match the governing pipeline definition's phase order.
- Filenames should remain stable across executions of the same pipeline model so comparison and discovery remain deterministic.

## Directory Placement

- The artifact directory name should use the pipeline slug without the numeric ID prefix.
- Governance pipeline artifacts belong under `docs/pipelines/governance/`.
- Other categories must follow the same pattern under their own category root.

## Evidence Documentation Expectations

- Artifacts must record the evidence basis for major conclusions when the evidence is not self-evident from repository state alone.
- Promotion and final-verdict surfaces must summarize the result in decision language, not just descriptive prose.
- Supporting-surface updates should record what changed, what remained unchanged, and any residual stale guidance.

## Naming Consistency Rules

- Artifact filenames should use lowercase kebab-case after the numeric prefix.
- Summary, promotion, and final-verdict artifact names should remain semantically consistent across pipelines where practical.
- Artifact names must be descriptive enough that a reader can predict their role without opening the file.

## Exceptions Policy

An executed pipeline may depart from the typical bundle shape only when:

- the pipeline definition explicitly omits a typical phase
- a phase is genuinely not applicable to the repository state
- a higher-authority governance surface authorizes a narrower record

Exceptions must be recorded explicitly so later audits do not need to guess whether an omission was intentional.
