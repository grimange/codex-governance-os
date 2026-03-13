# Minimal Setup Checklist

Use this checklist when adopting the template into a new repository.

| step | status target | notes |
|------|---------------|-------|
| adopt template governance assets | required | Copy or otherwise inherit the template doctrine, skills access model, and pipeline surfaces. |
| establish local `AGENTS.md` | required | Define repository mission, authority order, and routing rules. |
| establish local `.codex/AGENTS.md` | required | Define repository-local Codex behavior and references to doctrine. |
| establish local docs roots | required | Confirm `docs/governance/`, `docs/contracts/`, `docs/pipelines/`, and `docs/bootstrap/` or equivalent adoption references. |
| establish architecture-discovery path | required | Create a local placeholder or immediately schedule `001--discover-existing-architecture-and-establish-doctrine.md`. |
| initialize registry | required | Ensure `docs/pipelines/registry/pipeline-registry.md` exists and will record active pipelines. |
| run initialization pipeline | conditional | Run `000--initialize-governed-project.md` if the repository is not yet governance-capable. |
| run architecture discovery pipeline | required | Run `001--discover-existing-architecture-and-establish-doctrine.md`. |
| run governance readiness audit | required | Run `002--audit-repository-governance-readiness.md`. |
| decide whether contract-oriented pipelines are needed | required | Treat `003` through `007` as conditional on stable bounded subsystem need, not as mandatory first-day work. |
| confirm universal skill access | required | Verify the repository can discover inherited universal skills and the skill invocation standard. |
| add local skills only if needed | conditional | Use `.codex/skills/` for bounded repository-specific behavior. |

The checklist is complete when the repository has a local constitution, a local doctrine path, registered active pipelines, and verified access to inherited governance doctrine and skills.
