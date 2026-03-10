# Surface Inventory

## Code Evidence

| Path | Role In System Behavior | Apparent Responsibility | Likely Governing Contract Class | Confidence | Classification |
|------|--------------------------|-------------------------|---------------------------------|------------|----------------|
| none present | no application behavior evidenced | no product subsystem currently implemented | none yet | high | ambiguous only in the sense of absent implementation |

## Document And Governance Evidence

| Path | Role In System Behavior | Apparent Responsibility | Likely Governing Contract Class | Confidence | Classification |
|------|--------------------------|-------------------------|---------------------------------|------------|----------------|
| `AGENTS.md` | repository-local constitutional authority | defines authority order, routing, and governance standards | governance authority contract | high | canonical |
| `.codex/AGENTS.md` | agent operating surface | constrains Codex behavior to repository governance expectations | governance authority contract | high | likely authority candidate |
| `docs/governance/architecture-doctrine.md` | architecture authority | defines repository architecture interpretation and source-of-truth rules | architecture doctrine contract | high | canonical |
| `docs/governance/contract-discovery-ledger.md` | not yet present at discovery start | durable planning surface for contract candidates | contract-root stewardship contract | high | missing candidate surface |
| `docs/pipelines/registry/pipeline-registry.md` | pipeline activation surface | records active governance pipelines | registry integrity contract | high | likely authority candidate |
| `docs/pipelines/governance/000--initialize-governed-project.md` | pipeline definition | governs repository bootstrap | pipeline orchestration contract | high | canonical |
| `docs/pipelines/governance/001--discover-existing-architecture-and-establish-doctrine.md` | pipeline definition | governs doctrine discovery | pipeline orchestration contract | high | canonical in practice, descriptive status label mismatch |
| `docs/pipelines/governance/002--audit-repository-governance-readiness.md` | pipeline definition | governs governance readiness audit | pipeline orchestration contract | medium | active but currently unregistered |
| `docs/pipelines/governance/003--discover-contract-candidates-and-authority-surfaces.md` | pipeline definition | governs contract discovery | pipeline orchestration contract | high | likely authority candidate during execution |
| `docs/pipelines/governance/initialize-governed-project/*.md` | execution evidence | records pipeline `000` outputs | pipeline artifact contract | high | derived/projection |
| `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/*.md` | execution evidence | records pipeline `001` outputs | pipeline artifact contract | high | derived/projection |
| `docs/pipelines/governance/audit-repository-governance-readiness/*.md` | execution evidence | records pipeline `002` outputs | pipeline artifact contract | high | derived/projection |
| `docs/contracts/.gitkeep` | placeholder contract root | reserves canonical location for future contracts | contract-root stewardship contract | high | compatibility / placeholder |
| `docs/modernization/.gitkeep` | placeholder documentation root | reserves future modernization surface | compatibility and placeholder contract | high | compatibility / placeholder |

## Separation Of Evidence Types

- Code evidence: no product implementation surfaces are present.
- Document claims: governance documents assert authority, sequencing, and artifact rules.
- Inferred contract surfaces: governance authority, pipeline orchestration, registry integrity, artifact interpretation, and placeholder stewardship.
- Ambiguities: unregistered active pipelines and placeholder roots without substantive contracts.
