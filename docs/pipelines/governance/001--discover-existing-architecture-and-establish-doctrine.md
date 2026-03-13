---
pipeline_id: "001"
title: "Discover Existing Architecture and Establish Doctrine"
status: active
category: governance
stage: discovery
objective: "Discover the repository architecture from evidence and publish a canonical architecture doctrine."
depends_on: ["000"]
outputs: ["docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/"]
success_criteria: ["Repository evidence is inventoried.", "A doctrine is authored and installed.", "Supporting governance surfaces are updated and verified."]
governance_mode: fail-closed
execution_mode: advisory-then-enforcing
restrictions: ["Do not invent architecture without evidence.", "Do not treat descriptive notes as canonical authority."]
non_claims: ["Does not create subsystem contracts.", "Does not certify implementation correctness."]
classification: governance.foundation
authority: repo-governance
autonomy: advisory-only
problem_statement: "A governance-capable repository still lacks architectural authority until its real implementation and documentation surfaces are interpreted into doctrine."
scope: "Discover repository evidence, map architecture, analyze authority, author doctrine, and verify installation."
inputs: ["Initialized governance repository", "Repository files and docs", "Architecture doctrine authoring guidance"]
entry_conditions: ["Governance bootstrap exists but canonical architecture doctrine is missing or insufficient."]
exit_conditions: ["Doctrine is installed and supporting governance surfaces reference it."]
validation: ["Inspect evidence inventory and doctrine output.", "Confirm doctrine integration and verification artifacts."]
rollback: "Restore prior doctrine and lane body from version control if normalization introduces semantic drift."
---

# Discover Existing Architecture and Establish Doctrine

## Purpose

Discover the repository’s architecture from version-controlled evidence and establish an explicit doctrine that later governance lanes can treat as the canonical architecture authority.

## Problem Statement

Initialization installs governance mechanics, but it does not determine what implementation layers, authority surfaces, and state ownership patterns are actually canonical.

## Objectives

- inventory repository evidence relevant to architecture
- map the current architecture and authority boundaries
- record drift, ambiguity, and architectural risk
- author and install the canonical doctrine

## Scope

In scope: evidence discovery, architecture mapping, authority analysis, doctrine authoring, supporting-surface updates, and doctrine verification.

Out of scope: subsystem contract authoring, implementation remediation, or runtime-specific optimization.

## Preconditions

- pipeline `000` has established the baseline governance surfaces
- repository evidence exists to inspect
- doctrine publication under `docs/governance/` is allowed

## Execution Steps

1. Publish the discovery summary and scope boundaries.
2. Inventory repository evidence and map architectural layers.
3. Analyze authority, source-of-truth ownership, ambiguity, and drift risk.
4. Design and author the canonical doctrine.
5. Update supporting governance surfaces and verify doctrine installation.
6. Record the promotion decision and final verdict.

Universal skills:

- `repository-discovery`
- `architecture-doctrine-authoring`

## Expected Outputs

- artifact bundle under `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/`
- canonical doctrine at `docs/governance/architecture-doctrine.md`
- updated supporting governance surfaces that reference the doctrine

## Verification Method

- inspect the evidence inventory and architecture mapping artifacts
- confirm doctrine installation and supporting-surface integration
- verify the final verdict is supported by recorded evidence

## Restrictions

- fail closed on ambiguous architecture claims
- do not elevate undocumented assumptions into doctrine

## Non-Claims

- does not contract every subsystem
- does not prove governance readiness by itself

## Final Verdict

Use a bounded doctrine-installation verdict such as `ARCHITECTURE_DOCTRINE_ESTABLISHED` or an explicitly restricted equivalent.
