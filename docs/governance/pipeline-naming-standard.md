# Pipeline Naming Standard

## Purpose

This doctrine defines how governance pipelines are named so discovery, registration, and cross-reference remain deterministic as the catalog grows.

## Canonical Filename Pattern

Pipeline definition filenames must follow this pattern:

`docs/pipelines/<category>/<NNN--verb-first-slug>.md`

Where:

- `NNN` is a zero-padded numeric pipeline ID
- `verb-first-slug` is a lowercase kebab-case identifier beginning with an action verb

## Numbering Expectations

- Pipeline IDs must be unique within the repository.
- IDs should be allocated in ascending order.
- Existing IDs must not be reused for materially different workflows once a pipeline has become an active governance surface.

## Slug Conventions

- Use lowercase ASCII kebab-case.
- Start with a verb that describes the primary governance action such as `initialize`, `discover`, `audit`, `author`, `verify`, `establish`, `normalize`, or `publish`.
- Keep the slug specific enough to distinguish the workflow from nearby pipelines without encoding unnecessary detail.

## Category Alignment

- The category directory must match the pipeline's operational class such as `governance`, `verification`, `remediation`, or `promotion`.
- The pipeline's stated category in its body, registry entry, and filesystem path must agree.

## Registry Identity Rules

- The pipeline ID, human-readable name, category, and canonical path in `docs/pipelines/registry/pipeline-registry.md` must resolve to exactly one pipeline definition.
- The registry may record status and discoverability but must not rename the pipeline into a conflicting identity.

## Artifact Directory Rule

The execution artifact directory should reuse the definition slug without the numeric prefix, for example:

- definition: `008--establish-governance-doctrine-foundation.md`
- artifact directory: `docs/pipelines/governance/establish-governance-doctrine-foundation/`

## Collision And Supersession Handling

- Do not create near-duplicate slugs that differ only trivially in wording.
- If a pipeline supersedes an earlier pipeline, keep the old ID and slug historically stable and record the supersession in documentation rather than renaming history.
- If naming ambiguity cannot be avoided, choose a more specific verb-first slug before activation and registration.
