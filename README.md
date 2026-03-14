# Codex Governance Template

This repository is a documentation-first template for turning a standard repository into a governed Codex project.

The `docs/` directory is the authoritative root for all governance and Codex-related files in this repository.

## Start Here

- Quick start: `docs/adoption/quick-start.md`
- Full adoption guide: `docs/adoption/codex-governance-adoption-guide.md`
- Framework overview: `docs/adoption/framework-overview.md`
- Adoption guide: `docs/bootstrap/governed-project-bootstrap.md`
- Minimal setup checklist: `docs/bootstrap/minimal-setup-checklist.md`
- Skill inheritance model: `docs/bootstrap/skill-inheritance-model.md`
- Local override model: `docs/bootstrap/local-override-model.md`
- Active governance pipelines: `docs/pipelines/registry/pipeline-registry.md`

## What This Template Provides

- a repository constitution model in `AGENTS.md`
- repository-local Codex operating rules in `.codex/AGENTS.md`
- reusable governance doctrine under `docs/governance/`
- reusable governance pipelines under `docs/pipelines/governance/`
- reusable universal skills and a local override model
- publication-oriented adoption guides under `docs/adoption/`

## Adoption Profiles

- Small repository: start with bootstrap guidance, run pipelines `000`, `001`, and `002`, then add later contract-oriented pipelines only when the repository has stable bounded surfaces worth governing explicitly.
- Growing application or library: use `000` through `002` as the baseline, then use `003` through `007` once subsystem contracts, audits, remediation, and verification become operationally useful.
- Monorepository or multi-scope system: keep the same baseline, then apply later pipelines per bounded subsystem or local scope as complexity grows.

## Scope

This template is intended to remain domain-neutral, architecture-neutral, and language-neutral. It does not prescribe a single runtime model, framework, CI provider, or distribution pattern.

## Learn More

- Example adoption scenarios: `docs/adoption/example-adoption-scenarios.md`
- Governance lifecycle doctrine: `docs/governance/governance-lifecycle.md`
- Governance evidence interpretation canon: `docs/governance/governance-evidence-interpretation-canon.md`
- Governance safety invariants canon: `docs/governance/governance-safety-invariants-canon.md`
- Governance evolution model: `docs/governance/governance-evolution-model.md`
- Governance template system: `docs/governance/templates/README.md`
- Template scaffold contract: `docs/governance/template-scaffold-contract.md`
- Universal template composition contract: `docs/contracts/universal-template-composition-contract.md`
- Admitted template registry index: `docs/governance/registries/templates/index.yaml`
- Admitted template bodies: `docs/codex/templates/`
- Universal skills index: `docs/governance/universal-skills-index.md`
