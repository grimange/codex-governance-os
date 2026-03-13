# Governed Project Bootstrap

## Purpose

This guide is the canonical adoption surface for turning a new repository into a governed Codex project using this template's doctrine, universal skills, and pipeline model.

## What The Template Provides

- repository constitution model in `AGENTS.md`
- local agent operating model in `.codex/AGENTS.md`
- governance doctrine foundation under `docs/governance/`
- universal skills intended for reuse across repositories
- normalized governance pipelines under `docs/pipelines/governance/`
- pipeline registry model under `docs/pipelines/registry/pipeline-registry.md`

## What A New Project Must Add Locally

- a project-local `AGENTS.md` naming the repository mission and authority routing
- a project-local `.codex/AGENTS.md` describing repository-specific Codex behavior
- project-specific architecture doctrine after discovery
- project-local contracts under `docs/contracts/` as subsystems become bounded
- local pipelines and local execution artifacts that reflect that repository's work
- project-local skills under `.codex/skills/` only when repository-specific behavior is required

## Minimal Bootstrap Sequence

1. Adopt the template governance surfaces into the new repository.
2. Establish local `AGENTS.md` and `.codex/AGENTS.md`.
3. Preserve the doctrine foundation under `docs/governance/` as inherited baseline law.
4. Confirm access to the inherited universal skills and the skill invocation standard.
5. Initialize the local pipeline registry and register active local pipelines.
6. Run `000--initialize-governed-project.md` if the repository is not yet governance-capable.
7. Run `001--discover-existing-architecture-and-establish-doctrine.md` so the repository replaces bootstrap assumptions with evidence-backed local doctrine.
8. Run `002--audit-repository-governance-readiness.md` to verify the repository is usable as a governed project.

## Adoption Profiles

- Small repositories, CLI tools, and simple frontend apps usually stop at pipelines `000`, `001`, and `002` until stable bounded surfaces justify contract-oriented governance.
- Libraries and growing applications often adopt `003` through `007` later, once API, packaging, subsystem, or state-ownership boundaries need explicit contracts.
- Monorepositories may reuse the same sequence per bounded local scope rather than forcing one contract wave across the entire repository at once.

## Safe Starting Order

- Start from inherited generic governance law.
- Add only the local constitutional and operational surfaces required to name the project's authority and scope.
- Delay project-specific contracts and local skill overrides until discovery shows they are needed.
- Treat pipelines `003` through `007` as conditional downstream tools, not mandatory first-day steps for every repository.
- Keep bootstrap artifacts generic; project-specific architecture belongs in later local doctrine and contracts.

## How Doctrine, Skills, And Pipelines Relate

- Doctrine defines the reusable governance law.
- Skills define reusable operational behavior that pipelines can invoke.
- Pipelines define repository procedures, required artifacts, and promotion criteria.
- Local repositories inherit the generic doctrine and universal skills, then add project-specific doctrine, contracts, pipelines, and optional local skills without weakening higher-authority baseline rules.
