# Codex Governance Adoption Guide

## Purpose

This guide explains how to adopt the Codex governance template in a new repository and how the main governance surfaces work together.

## What The Template Provides

- a constitutional model in `AGENTS.md`
- a local agent operating model in `.codex/AGENTS.md`
- governance doctrine under `docs/governance/`
- reusable pipelines under `docs/pipelines/governance/`
- reusable universal skills plus local override support
- bootstrap guidance under `docs/bootstrap/`

## Minimal Adoption Path

1. Adopt the template into the target repository.
2. Review `AGENTS.md`, `.codex/AGENTS.md`, and `docs/governance/`.
3. Use `docs/bootstrap/governed-project-bootstrap.md` and `docs/bootstrap/minimal-setup-checklist.md` to establish the repository baseline.
4. Run pipeline `000` if the repository is not yet governance-capable.
5. Run pipeline `001` to establish local architecture doctrine from repository evidence.
6. Run pipeline `002` to verify governance readiness.
7. Adopt later pipelines only when the repository has bounded subsystem, contract, remediation, or verification needs.

## Governance Lifecycle

The reusable lifecycle is:

1. initialization
2. discovery
3. doctrine or contract establishment
4. audit
5. remediation
6. verification
7. promotion

Not every repository needs every stage immediately. Smaller repositories often start with initialization, discovery, and readiness audit only.

## How Pipelines And Skills Interact

- Doctrine defines reusable governance law.
- Skills provide reusable operational behavior.
- Pipelines define ordered work, required artifacts, and promotion decisions.
- Local repositories may add local skills or local pipelines when repository-specific behavior warrants them.

## Local Extension Model

- Keep inherited doctrine generic.
- Add repository-specific authority and scope in local `AGENTS.md` and `.codex/AGENTS.md`.
- Add local contracts only after discovery reveals stable bounded surfaces.
- Add local skills under `.codex/skills/` only when the repository needs a specialized workflow.

## Who Should Use This Template

Use this template when you want:

- explicit repository governance
- repeatable Codex workflow orchestration
- durable pipeline artifacts
- a domain-neutral baseline that can scale from a small repository to a monorepo

Do not use this template if the repository does not need documented governance workflows or if the team is unwilling to maintain explicit doctrine and pipeline artifacts.
