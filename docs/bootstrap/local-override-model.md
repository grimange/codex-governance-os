# Local Override Model

## Purpose

This guide defines how future repositories specialize the inherited template without weakening the universal governance foundation.

## What May Be Overridden Locally

- repository mission and local operating instructions in `AGENTS.md` and `.codex/AGENTS.md`
- project-specific architecture doctrine after local discovery
- local contracts under `docs/contracts/`
- local pipelines under `docs/pipelines/`
- local skills under `.codex/skills/` when repository-specific behavior is required

## What Must Not Be Overridden Casually

- authority ordering established by the repository constitution
- doctrine-foundation rules under `docs/governance/` unless the repository intentionally replaces them through version-controlled governance work
- universal skill semantics when no repository-specific need exists
- pipeline verification and promotion expectations for active local pipelines

## Conflict Resolution

When inherited and local instructions conflict, use this order:

1. version-controlled repository state
2. local repository constitution
3. local architecture doctrine and inherited doctrine foundation
4. active pipeline definitions
5. generated pipeline artifacts

Local specialization may narrow inherited guidance, but it must not silently contradict a higher-authority surface.

## AGENTS Interaction

- `AGENTS.md` defines the local repository's constitutional routing and authority.
- `.codex/AGENTS.md` defines local Codex operating behavior.
- These files may supplement inherited guidance, but they should stay concise and route back to canonical doctrine and pipeline surfaces rather than duplicating them.

## Local Contracts And Pipelines

- Introduce local contracts after architecture discovery reveals stable subsystem boundaries.
- Introduce local pipelines when repeated governance-affecting work needs deterministic execution and durable artifacts.
- Register active pipelines so discoverability remains accurate.

## Override Discipline

- Extend first; replace only when the repository has a clear reason.
- Keep local changes discoverable in canonical folders.
- Record material specialization in version control so later audits can explain why the inherited baseline changed.
