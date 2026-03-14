---
pipeline: 108
title: Remediate Non-Portable Filesystem Links In Canonical Governance Surfaces
lane: governance
layer: 0
status: proposed
depends_on:
  - 107
governance_type: remediation
registry_id: governance.portability.remediate-non-portable-filesystem-links
artifact_bundle: docs/pipelines/governance/remediate-non-portable-filesystem-links-in-canonical-governance-surfaces
---

# 108 — Remediate Non-Portable Filesystem Links In Canonical Governance Surfaces

## Purpose

Remove hard-coded machine-local filesystem paths from canonical governance and
pipeline surfaces and normalize all in-repository references to portable
repository-relative or document-relative links.

## Problem Statement

Pipeline 107 verification evidence surfaced a non-portable markdown link that
references a machine-local absolute path under `/home/...`. That path is not
valid as a reusable repository-template reference and leaks workstation-local
filesystem structure into canonical governance surfaces.

## Why This Matters

A repo-template must remain portable across:

- different clone locations
- different developers
- different operating systems
- future generated repositories

Machine-local absolute paths violate repository portability and can silently
propagate through later pipelines and generated artifacts.

## Scope

This lane is limited to documentation and repository-surface normalization only.

This lane may:

- identify machine-local absolute filesystem references in canonical markdown
  surfaces
- replace those references with portable repository-relative or
  document-relative links
- align pipeline artifacts and canonical docs with the repository’s true
  canonical paths
- update discoverability surfaces if required

This lane must not:

- introduce runtime path resolution logic
- change doctrine semantics beyond portability normalization
- broaden scope into unrelated markdown cleanup
- introduce hidden path aliasing conventions

## Required Outputs

Create an artifact bundle at:

`docs/pipelines/governance/remediate-non-portable-filesystem-links-in-canonical-governance-surfaces/`

with at least:

1. `01-problem-statement.md`
2. `02-non-portable-reference-inventory.md`
3. `03-canonical-path-truth-map.md`
4. `04-remediation-plan.md`
5. `05-applied-normalization-summary.md`
6. `06-verification.md`
7. `07-final-verdict.md`

## Required Repository Work

### 1. Inventory non-portable references

Inspect canonical governance surfaces and pipeline artifacts for path patterns
such as:

- `/home/`
- `/Users/`
- `C:\`
- `file://`
- other workstation-local absolute paths

### 2. Establish canonical truth

For each affected reference, record:

- the source document
- the current broken or non-portable link
- the intended canonical repository target
- the correct portable replacement

### 3. Normalize links

Replace machine-local absolute references with one of the following:

- document-relative markdown links, or
- repository-root-relative markdown links, if already accepted by doctrine

Preferred rule: use the most local portable relative form that remains stable
for repository cloning and markdown rendering.

### 4. Align pipeline 107 surfaces

Specifically verify whether the pipeline 107 verification bundle and any linked
summary surfaces incorrectly point to `docs/governance/...` when the canonical
target lives under `docs/contracts/...`.

Correct those references without altering the meaning of the restriction.

### 5. Preserve restriction semantics

Do not erase the underlying restriction by editing the wording to hide the
defect. The remediation must preserve the substantive claim while correcting the
link/path representation.

## Verification Requirements

Verification must confirm:

- no machine-local absolute filesystem links remain in the remediated canonical
  surfaces that were within scope
- the corrected links resolve to the intended repository files
- canonical path references now reflect repository truth
- no doctrine meaning changed beyond portability normalization
- pipeline 107 restriction language remains evidence-faithful after remediation

## Final Verdict

The final verdict must be one of:

- `NON_PORTABLE_FILESYSTEM_LINKS_REMEDIATED`
- `NON_PORTABLE_FILESYSTEM_LINKS_REMEDIATED_WITH_RESTRICTIONS`
- `NON_PORTABLE_FILESYSTEM_LINK_REMEDIATION_BLOCKED`