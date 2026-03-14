# Problem Statement

Pipeline `116` used one non-canonical discoverability path in its lane text:

- `docs/architecture/architecture-doctrine.md`

The repository's canonical doctrine path is:

- `docs/governance/architecture-doctrine.md`

Pipeline `117` performs a bounded documentation normalization so the `116`
verification lane and the affected `116` verification-bundle references use the
repository's actual doctrine path.
