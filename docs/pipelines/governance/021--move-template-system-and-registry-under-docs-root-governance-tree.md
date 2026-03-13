---
title: "021 -- Move Template System and Registry Surfaces Under Docs Root Governance Tree"
lane: "implementation"
status: "proposed"
created_at: "2026-03-14"
owner: "OpenAI Codex"
objective: "Relocate universal template and registry surfaces under the repository docs root, and establish docs/ as the canonical root for all governance and codex-related files."
tags:
  - governance-os
  - codex
  - templates
  - registry
  - docs-root
  - repository-structure
---

# 021 -- Move Template System and Registry Surfaces Under Docs Root Governance Tree

## Purpose

This pipeline establishes a canonical documentation-rooted structure for governance and Codex operations. It moves the template system folder and registry folder into the `docs/` tree, and declares `docs/` as the authoritative root for all governance-related, Codex-related, and policy-bearing repository assets.

The goal is to eliminate split authority between repository root and documentation surfaces, reduce routing ambiguity, simplify discovery, and ensure every governance artifact lives under one explicit root.

---

## Problem Statement

The current repository shape allows governance and Codex-related assets to exist outside the `docs/` root. When template definitions, registries, routing files, rules, evidence packs, and pipeline artifacts are distributed across multiple top-level locations, the system becomes harder to reason about and more error-prone.

This creates several governance risks:

1. **Authority ambiguity**  
   There is no single clearly-declared documentation root for governance and Codex files.

2. **Routing drift**  
   Tools, prompts, and automation may resolve paths differently when governance assets are split between root-level folders and docs-level folders.

3. **Template inconsistency**  
   Template definitions can drift from the governance documentation that explains and governs them.

4. **Registry fragmentation**  
   Registry state and the documentation that justifies it can diverge if they live in separate top-level surfaces.

5. **Onboarding friction**  
   Operators and agents must remember multiple root locations for conceptually related assets.

This pipeline corrects that by making `docs/` the canonical root and relocating relevant folders beneath it.

---

## Scope

This pipeline covers:

- moving the templates system folder into `docs/`
- moving the registry folder into `docs/`
- declaring `docs/` as the canonical root for governance and Codex-related files
- updating path references, routing references, and internal documentation
- preserving compatibility through a controlled migration boundary
- defining verification requirements for post-move integrity

This pipeline does **not** by itself:

- redesign the internal schema of templates
- redesign the internal schema of the registry
- change substantive governance policy logic
- remove unrelated top-level folders that are not governance or Codex-related

---

## Target Repository Model

The repository should converge toward this canonical structure:

```text
repo-root/
  docs/
    governance/
      pipelines/
      rules/
      registries/
      evidence/
      reports/
      routing/
    codex/
      templates/
      instructions/
      agents/
      contracts/
    README.md
```

Minimum structural requirement for this lane:

```text
repo-root/
  docs/
    governance/
      ...
    codex/
      templates/
    registries/
      ...
```

If the project prefers a more unified shape, the registry may instead live under `docs/governance/registries/`. The key invariant is that both the template system and registry surfaces must now live under `docs/`.

---

## Canonical Decision

The authoritative root for all governance and Codex-related files is now:

`docs/`

Any governance or Codex asset placed outside `docs/` should be treated as:

- legacy
- transitional
- explicitly exempted
- or non-compliant

This means the repository root should no longer be treated as an equal authority surface for governance assets.

---

## Required Structural Moves

### Move 1: Templates system into `docs/`

If the current repository contains a top-level templates folder such as:

```text
/templates
```

it must be moved to one of the approved canonical locations:

Preferred:

```text
/docs/codex/templates
```

Acceptable alternative if the repo treats templates as governance-first rather than codex-first:

```text
/docs/governance/templates
```

Recommended default for universal Codex template systems:

```text
/docs/codex/templates
```

### Move 2: Registry folder into `docs/`

If the current repository contains a top-level registry folder such as:

```text
/registry
/registries
```

it must be moved into `docs/`, preferably:

```text
/docs/governance/registries
```

If there are multiple registries, they should be grouped there rather than spread across the root.

### Move 3: Declare `docs/` as governance root

The repository must explicitly document that:

- `docs/` is the canonical root for governance artifacts
- `docs/` is the canonical root for Codex operation artifacts
- new governance or Codex files should not be created at repo root without an explicit exception
- tools and prompts should resolve governance references from `docs/` first

---

## Required Artifacts

This pipeline should produce the following artifacts under the pipeline artifact bundle:

1. `01-problem-statement.md`  
   Describes current folder layout problems and why split authority is unsafe.

2. `02-current-vs-target-structure.md`  
   Shows the current structure and the desired `docs/`-rooted target structure.

3. `03-migration-plan.md`  
   Defines exact move operations, destination paths, and transition steps.

4. `04-reference-update-surface.md`  
   Lists all files, scripts, prompts, docs, and automation surfaces that need path updates.

5. `05-docs-root-governance-policy.md`  
   Declares `docs/` as the authoritative governance and Codex root.

6. `06-verification-plan.md`  
   Defines the checks required after migration.

7. `07-final-verdict.md`  
   Records whether the repo is structurally ready, partially ready, or blocked.

---

## Implementation Requirements

### A. Inventory current top-level governance and Codex surfaces

The implementation must first identify all relevant root-level folders and files, including but not limited to:

- `templates/`
- `registry/`
- `registries/`
- `governance/`
- `codex/`
- `pipelines/`
- route or instruction entry files referencing old paths
- scripts with hard-coded paths
- README or operator documentation referencing old paths

### B. Normalize destination tree

Before moving files, the target structure under `docs/` must be defined and created consistently.

Recommended structure:

```text
docs/
  governance/
    pipelines/
    registries/
    rules/
    routing/
    evidence/
    reports/
  codex/
    templates/
    instructions/
    agents/
    contracts/
```

### C. Perform deterministic moves

Moves should be explicit and reproducible.

Examples:

- `templates/` -> `docs/codex/templates/`
- `registry/` -> `docs/governance/registries/`
- `registries/` -> `docs/governance/registries/`

If collisions exist, they must be resolved by documented normalization, not silent overwrite.

### D. Update all path references

After the move, all affected references must be updated, including:

- governance scripts
- registry sync scripts
- route resolution logic
- README guidance
- pipeline references
- template loaders
- linter paths
- instruction entry points
- verification tooling

No governance-critical path may continue to rely on a removed root-level folder unless a temporary compatibility shim is explicitly documented.

### E. Establish transition boundary

If immediate hard cutover is risky, a short-lived compatibility boundary may be used, such as:

- deprecation notes in old locations
- redirect stubs
- compatibility path support in tooling

But the authoritative path must still become the `docs/` path, not the legacy root path.

### F. Add policy-level declaration

At least one canonical repository document must explicitly state:

> The `docs/` directory is the authoritative root for all governance and Codex-related files in this repository.

That declaration should be discoverable by both humans and automation.

---

## Safety Rules

1. **Fail closed on ambiguous merges**  
   If multiple folders contain conflicting template or registry assets, do not silently merge them.

2. **Do not overwrite without cataloging**  
   Any filename collision must be recorded and resolved explicitly.

3. **Do not break verification tooling silently**  
   Scripts that depend on old paths must either be updated or blocked with a clear error.

4. **Do not preserve dual authority indefinitely**  
   Legacy root-level locations may exist only as temporary migration shims.

5. **Do not move unrelated business logic**  
   This lane only governs governance and Codex-related surfaces.

---

## Acceptance Criteria

This pipeline is complete when all of the following are true:

- the template system folder no longer exists as an authoritative root-level governance surface
- the registry folder no longer exists as an authoritative root-level governance surface
- both surfaces now live under `docs/`
- `docs/` is explicitly documented as the canonical root for governance and Codex files
- scripts and documents referencing old root-level paths have been updated or explicitly deprecated
- repository operators can locate governance, registry, and template assets by entering `docs/` first
- verification confirms there is no unresolved structural ambiguity

---

## Verification

Verification should include:

### Structural verification

- confirm the template system now resolves under `docs/`
- confirm registry assets now resolve under `docs/`
- confirm expected subdirectories exist

### Reference verification

- search the repository for stale references to old root-level paths
- confirm key scripts resolve the new paths
- confirm documentation matches the new structure

### Policy verification

- confirm at least one canonical document declares `docs/` as the root
- confirm no active governance document asserts root-level dual authority

### Operational verification

- run any registry sync, routing, path lint, or governance preflight commands that depend on these locations
- confirm they still succeed or fail with explicit, expected migration notes

---

## Suggested Final Verdict Values

Use one of the following:

- `DOCS_ROOT_GOVERNANCE_STRUCTURE_ESTABLISHED`
- `DOCS_ROOT_GOVERNANCE_STRUCTURE_ESTABLISHED_WITH_TRANSITION_SHIMS`
- `DOCS_ROOT_GOVERNANCE_STRUCTURE_BLOCKED_BY_PATH_COLLISIONS`
- `DOCS_ROOT_GOVERNANCE_STRUCTURE_BLOCKED_BY_UNMIGRATED_REFERENCES`

---

## Recommended Follow-up Pipelines

Recommended immediate next lanes after this pipeline:

1. **Verify Docs-Root Governance Structure**
2. **Update Governance Routing to Prefer Docs-Root Resolution**
3. **Lint Root-Level Governance Surface Violations**
4. **Deprecate Legacy Root Governance Paths**
5. **Verify Universal Template Linter Against New Docs Paths**

---

## Operator Guidance

Once this pipeline is adopted, operators should assume this navigation rule:

- start from `docs/` for any governance, Codex, template, rule, registry, evidence, or pipeline work

The repository root remains the software project root, but no longer the governance-document authority root.

---

## Implementation Notes for `codex-governance-os`

For `codex-governance-os`, this pipeline is especially useful because the project is already converging toward a repository-aware governance operating system. A `docs/`-rooted design gives the system:

- a single discovery surface
- cleaner deterministic routing
- less prompt/tool ambiguity
- easier package portability across Laravel, Django, and other stacks
- simpler future enforcement for “no governance asset outside docs without explicit exception”

This makes the governance OS more universal and more transferable across projects.

---

## Final Recommendation

Adopt this pipeline before broader universal template expansion. Structural authority should be stabilized first, so template systems, registries, routing, and governance automation all inherit the same canonical root model.
