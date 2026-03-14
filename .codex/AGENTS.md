# Codex Local Governance Surface

## Purpose

This file defines repository-local operating instructions for Codex agents working in this project.

## Operating Rules

- Follow repository governance artifacts before introducing new process.
- Prefer deterministic, file-backed pipeline execution over ad hoc changes.
- Record governance-relevant work in `docs/` so later agents can audit decisions.
- Preserve authority ordering defined in the repository constitution and architecture doctrine.
- Treat `docs/governance/architecture-doctrine.md` as the canonical interpretation layer for repository structure, authority, and pipeline artifact meaning.
- Use the doctrine foundation under `docs/governance/` as the canonical source for lifecycle, artifact, naming, contract-writing, and terminology rules.
- Use `docs/governance/governance-evidence-interpretation-canon.md` when deciding what evidence is sufficient to support a governance claim, verdict, restriction, or verification result.
- Use `docs/governance/governance-safety-invariants-canon.md` when deciding what governance mutation, summary, or normalization behavior must fail closed.
- Use `docs/governance/governance-evolution-model.md` when changing governance doctrine, active pipeline structure, registry policy, or other meta-governance surfaces.
- Treat `docs/` as the authoritative root for all governance and Codex-related files in this repository.
- Use `docs/governance/templates/` and `tools/governance/` when authoring, validating, or scaffolding governed artifact families from the universal template system.
- Use `docs/governance/template-scaffold-contract.md` and `tools/templates/` when working on repository-level scaffold manifests or overlay discovery.
- Use `docs/contracts/universal-template-composition-contract.md` when changing or verifying certified overlay composition boundaries.
- Use `docs/governance/registries/templates/` and `docs/codex/templates/` when admitting, resolving, or auditing governed template identities.
- Treat `docs/bootstrap/` as the canonical adoption surface for future repositories inheriting this template's governance baseline.
- Use `docs/governance/universal-skills-index.md` and `docs/governance/skill-invocation-standard.md` to decide when universal or project-local skills apply.
- When following a normalized pipeline, prefer the pipeline's referenced universal skills for reusable operational behavior and keep pipeline-specific artifact and verdict requirements explicit.
- Treat `docs/contracts/pipeline-registry-integrity-contract.md` as the governing contract for registry completeness and active-pipeline discoverability.

## Repository Expectations

- Keep pipeline definitions under `docs/pipelines/`.
- Keep governance doctrine under `docs/governance/`.
- Keep canonical governance templates under `docs/governance/templates/`.
- Keep the universal scaffold contract under `docs/governance/template-scaffold-contract.md`.
- Keep the certified universal template composition contract under `docs/contracts/universal-template-composition-contract.md`.
- Keep admitted template registry metadata under `docs/governance/registries/templates/`.
- Keep admitted template bodies under `docs/codex/templates/`.
- Keep template manifest tooling under `tools/templates/`.
- Keep governed-project bootstrap guides under `docs/bootstrap/`.
- Keep universal reusable skills under `skills/`.
- Keep project-local skill extensions under `.codex/skills/`.
- Treat `docs/governance/contract-discovery-ledger.md` as the planning surface for future contract authoring and contract audit work.
- Register active pipelines in the pipeline registry.
- Treat verification and promotion outcomes as explicit deliverables.
