# Governance Surface Inventory

| surface family | locations | relevance to template system |
|----------------|-----------|------------------------------|
| doctrine foundation | `docs/governance/` | provides lifecycle, artifact, naming, terminology, and meta-governance rules the templates must preserve |
| active pipeline catalog | `docs/pipelines/governance/` | provides the main governed artifact family that needs shape-stable templating |
| adoption and bootstrap surfaces | `README.md`, `docs/adoption/`, `docs/bootstrap/` | provide publication and inheritance paths that should become template-aware later |
| registry surface | `docs/pipelines/registry/pipeline-registry.md` | records active pipeline discoverability and must remain aligned with template-driven artifacts |
| governance tooling roots | `tools/governance/` | previously absent; created by this pipeline for registry loading, linting, and scaffolding |
| governance test roots | `tests/governance/` | previously absent; created by this pipeline for deterministic template-system verification |

The repository had doctrine, pipelines, and publication surfaces but no canonical cross-family template layer before this pipeline.
