# Artifact Path Decision

Canonical path chosen for Pipeline `137`:

`docs/pipelines/governance/verify-multi-session-continuity-evidence-harness-implementation/`

Decision basis:

- `verify-multi-session-continuity-evidence-harness/` is already occupied by
  Pipeline `133`
- the chosen path remains semantically specific to the implemented harness
  verification lane
- the path is deterministic and stable for future discoverability
- the path preserves existing historical artifacts created during the restricted
  Pipeline `137` execution

Why prior naming was collision-prone:

- Pipeline `133` and Pipeline `137` share the same title stem
- title-stem-only derivation would direct both lanes toward the same bundle root

Why this decision is canonical:

- the path is already recorded in the registry for Pipeline `137`
- Pipeline `137` now records the same path in frontmatter and lane body
- Pipeline `138` preserves, rather than replaces, the historical executed path
