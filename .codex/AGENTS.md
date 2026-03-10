# Codex Local Governance Surface

## Purpose

This file defines repository-local operating instructions for Codex agents working in this project.

## Operating Rules

- Follow repository governance artifacts before introducing new process.
- Prefer deterministic, file-backed pipeline execution over ad hoc changes.
- Record governance-relevant work in `docs/` so later agents can audit decisions.
- Preserve authority ordering defined in the repository constitution and architecture doctrine.
- Treat `docs/governance/architecture-doctrine.md` as the canonical interpretation layer for repository structure, authority, and pipeline artifact meaning.
- Treat `docs/contracts/pipeline-registry-integrity-contract.md` as the governing contract for registry completeness and active-pipeline discoverability.

## Repository Expectations

- Keep pipeline definitions under `docs/pipelines/`.
- Keep governance doctrine under `docs/governance/`.
- Treat `docs/governance/contract-discovery-ledger.md` as the planning surface for future contract authoring and contract audit work.
- Register active pipelines in the pipeline registry.
- Treat verification and promotion outcomes as explicit deliverables.
