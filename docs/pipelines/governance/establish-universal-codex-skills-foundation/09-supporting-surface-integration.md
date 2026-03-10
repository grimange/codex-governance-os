# Supporting Surface Integration

## Updated

- `AGENTS.md`
  Reason: added routing for universal and project-local skills and clarified the governed location of the skill foundation.
- `.codex/AGENTS.md`
  Reason: instructed agents to use the universal skills index and invocation standard when applicable.
- `docs/governance/architecture-doctrine.md`
  Reason: recognized the universal skill library and project-local skill extension surface within the repository architecture model.
- `docs/pipelines/registry/pipeline-registry.md`
  Reason: registered pipeline `009` as an active governance surface.

## References Added

- references to `docs/governance/universal-skills-index.md`
- references to `docs/governance/skill-invocation-standard.md`
- routing references for `skills/` and `.codex/skills/`

## Intentionally Left Unchanged

- Pipeline definitions `000` through `008`
  Reason: pipeline `010` exists to normalize older pipeline bodies to skill references.
- Existing doctrine-foundation documents from pipeline `008`
  Reason: they already provide the governing law that this skills foundation builds on.
- Template README surfaces
  Reason: no repository README currently needs skill-foundation integration.

## Residual Stale Guidance

- Older pipelines still embed reusable behavior inline and do not yet reference the new universal skill library.
- Future pipeline specifications continue to show `Status: PROPOSED` text even when registry activation now makes them operationally discoverable.
