# Universal Skills Index

## Purpose

This index is the canonical discovery surface for the repository's universal Codex skills foundation.

## Taxonomy Overview

- discovery
- audit
- doctrine
- contracts
- remediation
- verification
- governance
- bootstrap

## Available Universal Skills

- `repository-discovery`
  Location: `skills/discovery/repository-discovery/`
  Use cases: repository inventories, authority discovery, structure mapping.
- `governance-readiness-audit`
  Location: `skills/audit/governance-readiness-audit/`
  Use cases: governance maturity checks, readiness reviews, gap identification.
- `architecture-doctrine-authoring`
  Location: `skills/doctrine/architecture-doctrine-authoring/`
  Use cases: evidence-based doctrine installation or revision.
- `contract-candidate-discovery`
  Location: `skills/contracts/contract-candidate-discovery/`
  Use cases: subsystem candidate ranking, authority-surface discovery.
- `canonical-contract-authoring`
  Location: `skills/contracts/canonical-contract-authoring/`
  Use cases: writing canonical contracts under `docs/contracts/`.
- `implementation-contract-audit`
  Location: `skills/audit/implementation-contract-audit/`
  Use cases: contract compliance audits and drift evidence gathering.
- `implementation-drift-remediation`
  Location: `skills/remediation/implementation-drift-remediation/`
  Use cases: remediation planning and bounded execution against documented drift.
- `contract-alignment-verification`
  Location: `skills/verification/contract-alignment-verification/`
  Use cases: post-remediation verification and promotion readiness assessment.
- `pipeline-registry-reconciliation`
  Location: `skills/governance/pipeline-registry-reconciliation/`
  Use cases: registry updates, active-pipeline discoverability checks, normalization.
- `governed-project-bootstrap`
  Location: `skills/bootstrap/governed-project-bootstrap/`
  Use cases: initializing governed repository structure from the template baseline.

## Universal Versus Local Skills

- Universal skills live under `skills/` and must remain generic and reusable across repositories.
- Project-local skills live under `.codex/skills/` and may narrow, extend, or override universal skills when repository-specific behavior is required.

## Extension Guidance

- Add a project-local skill instead of editing a universal skill when the new behavior depends on one repository's domain or file layout.
- Override a universal skill only through the precedence rules in `docs/governance/skill-invocation-standard.md`.
- Keep future skills bounded and class-aligned so the library remains discoverable.

## Adoption Proportionality

- Small repositories may rely mostly on `repository-discovery`, `governed-project-bootstrap`, `governance-readiness-audit`, and `architecture-doctrine-authoring` during early adoption.
- Contract-oriented and remediation-oriented skills become relevant when a repository has stable bounded surfaces worth governing explicitly.
- Repositories should add local skills only when repository-specific constraints materially change a universal workflow.

## Current Pipeline Adoption

- Governance pipelines `000` through `007` now reference the universal skill library directly for their main reusable procedures.
- Pipelines `008` and `009` remain only partially normalized because their remaining reusable behavior does not yet justify or require additional universal skills.
