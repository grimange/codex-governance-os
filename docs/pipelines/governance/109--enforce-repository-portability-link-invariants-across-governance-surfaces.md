---
artifact_bundle: docs/pipelines/governance/enforce-repository-portability-link-invariants-across-governance-surfaces
depends_on:
- 108
governance_type: doctrine-and-verification
lane: governance
layer: 0
pipeline: 109
registry_id: governance.portability.enforce-repository-portability-link-invariants
status: proposed
title: Enforce Repository Portability Link Invariants Across Governance
  Surfaces
---

# 109 --- Enforce Repository Portability Link Invariants Across Governance Surfaces

## Purpose

Establish and enforce a canonical **Repository Portability Link
Invariant** that prohibits workstation-local filesystem references from
appearing in governed repository surfaces.

This rule ensures the repository remains safe to clone, reuse, and
distribute as a **repo-template** across different machines, operating
systems, and developers.

Pipeline 108 performed targeted remediation of known portability
defects. Pipeline 109 formalizes the permanent governance rule that
prevents the defect class from reappearing.

------------------------------------------------------------------------

# Problem Statement

Earlier verification surfaced non-portable references such as:

    /home/username/...
    /Users/username/...
    C:\Users\username\...
    file:///...

These links are **machine-local filesystem paths** and violate the
portability requirements of a reusable repository template.

Such references:

-   break for other developers
-   break when the repository is cloned elsewhere
-   leak workstation filesystem structure
-   silently propagate through generated pipelines and documentation

The governance system must treat these patterns as **portability
violations**.

------------------------------------------------------------------------

# Repository Portability Link Invariant

The repository establishes the following canonical invariant:

**Canonical governance surfaces must not contain machine-local absolute
filesystem references.**

Forbidden references include (but are not limited to):

    /home/*
    /Users/*
    C:\*
    file://*
    ~/*

These patterns must not appear as:

-   markdown links
-   canonical references
-   documentation navigation paths
-   governance doctrine references

------------------------------------------------------------------------

# Permitted Link Forms

Repository references must use **portable link formats only**.

### Document-relative links

Example:

    ../../contracts/codex-session-state-machine-canon.md

### Repository-relative paths

Example:

    docs/contracts/codex-session-state-machine-canon.md

### Explicit external URLs

Example:

    https://example.com/specification

External URLs are allowed only when intentionally referencing external
systems or standards.

------------------------------------------------------------------------

# Governance Scope

This rule applies to all **governed repository surfaces**, including:

-   canonical governance doctrine
-   contracts
-   architecture documentation
-   pipeline definitions
-   pipeline artifact bundles
-   repository entry surfaces such as README
-   Codex discovery surfaces such as `.codex/AGENTS.md`

This rule does **not** require rewriting historical artifacts outside
governed scope unless explicitly remediated by a later pipeline.

------------------------------------------------------------------------

# Required Outputs

Create an artifact bundle at:

    docs/pipelines/governance/enforce-repository-portability-link-invariants-across-governance-surfaces/

The bundle must contain at minimum:

    01-problem-statement.md
    02-portability-invariant-definition.md
    03-governance-scope-definition.md
    04-enforcement-design.md
    05-surface-alignment-summary.md
    06-verification.md
    07-final-verdict.md

------------------------------------------------------------------------

# Required Repository Work

## 1. Establish the portability invariant

Add the **Repository Portability Link Invariant** to the appropriate
canonical governance doctrine surface.

Recommended placement:

-   Layer 0 governance safety doctrine
-   canonical surface protection rules
-   repository portability invariants section

The invariant must be discoverable from architecture entry surfaces.

------------------------------------------------------------------------

## 2. Align discoverability surfaces

Ensure the invariant is discoverable from:

-   `architecture-doctrine.md`
-   `.codex/AGENTS.md`
-   repository README when appropriate
-   governance safety or canonical surface doctrine

------------------------------------------------------------------------

## 3. Define enforcement design

The governance system must treat machine-local filesystem paths as
portability violations.

The enforcement model should support:

-   repository scan verification
-   pipeline verification lanes
-   future admission gates

This pipeline establishes the **rule**, not necessarily the automated
blocking mechanism.

------------------------------------------------------------------------

## 4. Preserve historical evidence

Historical artifact bundles that recorded the defect must remain intact.

Governance evidence must not be rewritten to hide past issues.

Only **canonical surfaces** should be normalized.

------------------------------------------------------------------------

# Verification Requirements

Verification must confirm that:

1.  The repository portability invariant exists in canonical doctrine.
2.  The invariant is discoverable from repository entry surfaces.
3.  The repository rules clearly prohibit machine-local filesystem
    references.
4.  The rule does not alter repository semantics beyond portability
    safety.
5.  Pipeline 108 remediation remains valid under the new invariant.

Verification may include deterministic scans for forbidden path patterns
within governed scope.

------------------------------------------------------------------------

# Final Verdict

The final verdict must be one of the following:

    REPOSITORY_PORTABILITY_LINK_INVARIANT_ESTABLISHED
    REPOSITORY_PORTABILITY_LINK_INVARIANT_ESTABLISHED_WITH_RESTRICTIONS
    REPOSITORY_PORTABILITY_LINK_INVARIANT_NOT_ESTABLISHED

Restrictions must be explicitly documented and evidence-backed.

------------------------------------------------------------------------

# Expected Governance Outcome

After this pipeline:

-   the repository formally enforces **portable documentation
    references**
-   governance doctrine protects repo-template portability
-   future pipelines cannot silently introduce workstation-local paths
-   verification pipelines can detect portability violations
    deterministically

This rule strengthens the repository's role as a **portable governance
OS template**.
