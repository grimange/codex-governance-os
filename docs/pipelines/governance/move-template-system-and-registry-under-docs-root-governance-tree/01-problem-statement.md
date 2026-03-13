# Problem Statement

Before this pipeline, the universal template system was split across three authority surfaces:

- canonical family definitions under `docs/governance/templates/`
- admitted registry state under `registry/templates/`
- admitted template bodies under `templates/`

That split made the docs tree only partially authoritative. Operators could start in `docs/` and still miss active registry state or admitted template bodies. Tooling also encoded root-level paths, which preserved dual authority instead of a single docs-root routing model.

This is unsafe for a governed repository because:

- authority discovery becomes ambiguous
- tooling can drift from documentation
- template governance and admitted-template execution surfaces can separate
- future repos inheriting this template would copy a split authority model by default
