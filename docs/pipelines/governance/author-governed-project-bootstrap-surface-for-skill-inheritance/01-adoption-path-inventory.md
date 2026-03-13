# Adoption Path Inventory

| adoption concern | current source | classification | notes |
|------------------|----------------|----------------|-------|
| copying or adopting the template | no dedicated guide | missing | The repository had no canonical adoption document for future projects. |
| inheriting governance doctrine | `AGENTS.md`, `.codex/AGENTS.md`, `docs/governance/architecture-doctrine.md` | informal but reusable | Authority surfaces implied inheritance but did not describe a clean bootstrap path. |
| inheriting universal skills | `docs/governance/universal-skills-index.md`, `docs/governance/skill-invocation-standard.md` | informal but reusable | Skills were discoverable, but inheritance and first-use guidance for adopters was scattered. |
| adding local overrides | `docs/governance/skill-invocation-standard.md`, `.codex/AGENTS.md` | incomplete | Skill overrides were partially defined; doctrine and local operating overrides were not consolidated. |
| initializing local governance files | `docs/pipelines/governance/000--initialize-governed-project.md` | canonical and reusable | The initialization pipeline already defined the minimum governance-capable baseline. |
| registering local pipelines | `docs/pipelines/registry/pipeline-registry.md`, pipeline `000` | canonical and reusable | Registry expectations were explicit and reusable. |
| separating universal and local assets | `AGENTS.md`, `docs/governance/architecture-doctrine.md`, `docs/governance/universal-skills-index.md` | canonical and reusable | The repository already separated `skills/` from `.codex/skills/` and doctrine from local specialization. |

The pre-existing bootstrap knowledge was sufficient to infer the intended model, but it was distributed across doctrine, skill, and pipeline surfaces rather than assembled into one practical adoption system.
