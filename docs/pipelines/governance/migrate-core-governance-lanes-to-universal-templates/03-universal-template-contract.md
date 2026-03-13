# Universal Template Contract

The migration baseline used for the core lane set is the repository’s canonical pipeline template family:

- `docs/codex/templates/pipelines/universal-base.md`
- `docs/governance/templates/template-registry.yaml`

The normalized lane contract requires:

- governed frontmatter with deterministic scalar/list values
- canonical top-level sections:
  - `Purpose`
  - `Problem Statement`
  - `Objectives`
  - `Scope`
  - `Preconditions`
  - `Execution Steps`
  - `Expected Outputs`
  - `Verification Method`
  - `Restrictions`
  - `Non-Claims`
  - `Final Verdict`

For this migration, each lane preserved:

- original lane number
- original lane title
- original stage intent
- original artifact bundle root

And each lane gained:

- governed frontmatter
- explicit inputs, entry conditions, exit conditions, validation, and rollback metadata
- a stable universal-pipeline top-level body shape
