---
pipeline: "027"
title: "Expand Universal Codex Template Composition Verification Across Combined Overlay Matrices"
status: "proposed"
stage: "verification"
classification: "governance"
domain: "templates"
registry_id: "governance.templates.expand-universal-codex-template-composition-verification-across-combined-overlay-matrices"
depends_on:
  - "023"
  - "025"
  - "026"
blocks: []
unblocks: []
scope:
  - "combined universal codex template overlay matrix verification"
  - "supported multi-overlay composition verification"
  - "fail-closed invalid composition verification"
  - "manifest and documentation matrix truth verification"
  - "universal template composition boundary certification"
out_of_scope:
  - "introducing new overlay families"
  - "changing overlay semantics unless required by discovered verification defects"
  - "non-template governance architecture work"
inputs:
  - "docs/pipelines/governance/023--verify-universal-template-conformance-across-multi-stack-fixtures.md"
  - "docs/pipelines/governance/025--close-unsupported-stack-boundaries-for-universal-codex-templates.md"
  - "docs/pipelines/governance/026--verify-unsupported-stack-boundaries-closure-for-universal-codex-templates.md"
  - "docs/codex/templates/README.md"
  - "docs/governance/template-scaffold-contract.md"
  - "tools/governance/template_scaffold.py"
  - "tools/templates/list_templates.py"
  - "tests/governance/test_template_scaffold.py"
  - "tests/governance/test_template_conformance.py"
outputs:
  - "docs/pipelines/governance/expand-universal-codex-template-composition-verification-across-combined-overlay-matrices/01-problem-statement.md"
  - "docs/pipelines/governance/expand-universal-codex-template-composition-verification-across-combined-overlay-matrices/02-target-composition-matrix.md"
  - "docs/pipelines/governance/expand-universal-codex-template-composition-verification-across-combined-overlay-matrices/03-supported-composition-findings.md"
  - "docs/pipelines/governance/expand-universal-codex-template-composition-verification-across-combined-overlay-matrices/04-invalid-composition-fail-closed-findings.md"
  - "docs/pipelines/governance/expand-universal-codex-template-composition-verification-across-combined-overlay-matrices/05-docs-and-manifest-matrix-consistency-report.md"
  - "docs/pipelines/governance/expand-universal-codex-template-composition-verification-across-combined-overlay-matrices/06-verification-log.md"
  - "docs/pipelines/governance/expand-universal-codex-template-composition-verification-across-combined-overlay-matrices/07-final-verdict.md"
success_criteria:
  - "The repository proves a broader evidence-backed supported composition matrix beyond single-overlay existence checks."
  - "Supported multi-overlay compositions are explicitly exercised and verified through scaffold realization and conformance evidence."
  - "Invalid or unsupported overlay combinations fail closed with explicit compatibility outcomes."
  - "Template manifests, support docs, and scaffold contract documentation match the verified combined overlay matrix."
  - "The universal codex template system publishes an explicit supported-versus-unsupported composition boundary rather than relying on implication."
verification:
  - "Run python -m unittest discover -s tests/governance -p 'test_*.py'."
  - "Run python tools/templates/list_templates.py --output json."
  - "Run python tools/governance/template_scaffold.py list-manifests --output json."
  - "Exercise a representative composition matrix that includes supported and intentionally invalid combined overlay cases."
  - "Compare realized scaffold behavior against docs/codex/templates/README.md and docs/governance/template-scaffold-contract.md."
  - "Record the evidence-backed final verdict in 07-final-verdict.md."
canonical_artifact_dir: "docs/pipelines/governance/expand-universal-codex-template-composition-verification-across-combined-overlay-matrices"
authoring_mode: "governed"
---

# 027 — Expand Universal Codex Template Composition Verification Across Combined Overlay Matrices

## Purpose

Verify that the universal codex template system is trustworthy across a broader combined-overlay matrix now that the formerly unsupported stack boundaries have been implemented and closed.

## Problem Statement

Pipeline 023 established universal template conformance across the then-supported matrix and made unsupported boundaries explicit. Pipeline 025 implemented the missing `node-typescript-service` and `cli-worker` overlays. Pipeline 026 verified those overlays and closed the prior restriction.

That closes the existence question, but not yet the composition-confidence question.

A universal template system should not only prove that each overlay exists in isolation. It should also prove which overlay combinations are supported together, which combinations remain invalid, and whether those boundaries are enforced consistently by scaffold behavior, manifests, and documentation. Without that wider matrix verification, the system still risks accidental overclaim at the composition layer.

## Why This Pipeline Exists

The next governance need after restriction closure is combined-matrix confidence.

This lane exists to answer these questions:

1. Which overlay combinations are actually supported in repository truth?
2. Which combinations remain intentionally unsupported?
3. Does scaffold admission behave consistently across combined overlay requests?
4. Do supported combinations realize the expected files and structure?
5. Do docs and manifests describe the same matrix that the scaffold actually enforces?

This is the lane that turns universal template support from a set of verified overlay surfaces into a verified composition model.

## Entry Conditions

This pipeline may run when all of the following are true:

1. Pipeline 023 has established the baseline conformance model.
2. Pipeline 025 has implemented the formerly unsupported boundaries.
3. Pipeline 026 has concluded with `UNSUPPORTED_STACK_BOUNDARIES_VERIFIED_AND_RESTRICTION_CLOSED` or an equivalent fully closed verification result.
4. The repository contains runnable scaffold, manifest, docs, and governance tests for template verification.

## Required Verification Questions

The verification work must answer these questions directly:

1. Which combined overlay compositions are currently supported?
2. Which combinations are intentionally rejected by compatibility rules?
3. Does scaffold realization for supported combinations produce the expected file surfaces?
4. Do invalid combinations fail closed with explicit compatibility messaging?
5. Do manifests and docs truthfully describe the combined composition matrix?
6. Is the universal template boundary now explicit at the composition level, not just the single-overlay level?

## Target Composition Matrix

This lane should verify a representative set of combined overlay cases rather than a narrow single-surface sample. The exact matrix may be adapted to repository truth, but it should include all of the following classes.

### Supported candidate classes

At minimum, attempt representative cases from:

- base-only
- monorepo plus a supported runtime or service overlay
- `node-typescript-service + monorepo`
- `cli-worker + monorepo`, if the scaffold contract allows it
- `generic-service + monorepo`, if present in the supported manifest model
- package-oriented compositions where the repository contract defines them as valid

### Invalid candidate classes

At minimum, attempt representative invalid cases from:

- framework plus worker combinations that the compatibility rules reject
- mutually exclusive runtime overlays
- any composition that docs or manifests imply is unsupported
- any composition that the scaffold should fail closed rather than silently degrade

The lane is not required to invent new unsupported classes. It must verify the actual repository boundary.

## Verification Method

### 1. Governance test verification

Run the governance tests and identify which tests materially verify combined overlay behavior rather than simple overlay existence.

The record must distinguish between:

- generic passing tests
- specific matrix or compatibility tests
- conformance tests that prove supported combinations
- negative tests that prove fail-closed behavior

### 2. Matrix exercise verification

Exercise representative supported and invalid combinations through scaffold realization.

For each exercised case, record:

- requested composition
- whether admission succeeded or failed
- the exact compatibility outcome
- the realized file surfaces for successful cases
- whether behavior matched the documented contract

This should result in a canonical composition matrix rather than ad hoc examples.

### 3. Manifest and inventory verification

Use the manifest and listing commands to compare:

- declared template support
- realized template support
- combined overlay expectations
- any gaps between support declarations and actual behavior

### 4. Documentation truth verification

Compare actual combined composition behavior against:

- `docs/codex/templates/README.md`
- `docs/governance/template-scaffold-contract.md`
- relevant overlay README files, if they describe combination constraints

Any mismatch must be classified explicitly as:

- documentation stale
- manifest overclaim
- implementation defect
- test coverage gap
- no mismatch detected

### 5. Boundary certification

At the end of this lane, publish an explicit supported-versus-unsupported composition boundary for universal templates, backed by repository evidence.

This is the core governance deliverable of the lane.

## Required Artifact Bundle

Create the artifact bundle under:

`docs/pipelines/governance/expand-universal-codex-template-composition-verification-across-combined-overlay-matrices/`

Populate it with these files:

### `01-problem-statement.md`
Explain why the post-026 state still requires combined composition verification and what this lane is proving.

### `02-target-composition-matrix.md`
List the candidate supported and invalid combinations selected for verification, along with the reason each case is included.

### `03-supported-composition-findings.md`
Record all supported combinations exercised, their admission results, and their realized file surfaces.

### `04-invalid-composition-fail-closed-findings.md`
Record the intentionally invalid combinations exercised and whether they failed closed correctly.

### `05-docs-and-manifest-matrix-consistency-report.md`
Compare real combined matrix behavior against docs and manifest claims. Confirm alignment or record precise mismatches.

### `06-verification-log.md`
Record commands run, cases exercised, notable outputs, and evidence references.

### `07-final-verdict.md`
Publish the evidence-backed final verdict and the explicit composition boundary conclusion.

## Recommended Final Verdict

If the matrix verification succeeds while preserving explicit unsupported edges, the canonical target verdict is:

`UNIVERSAL_TEMPLATE_COMPOSITION_MATRIX_VERIFIED_WITH_EXPLICIT_BOUNDARIES`

If verification exposes mismatches or unclear edges, use a narrower verdict that preserves the uncertainty explicitly rather than overclaiming.

## Suggested Verification Commands

The lane should usually include evidence from commands such as:

```bash
python -m unittest discover -s tests/governance -p 'test_*.py'
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
```

In addition, execute a representative scaffold realization sweep for supported and invalid combined overlay compositions.

## Exit Conditions

This pipeline is complete when:

1. the full artifact bundle exists;
2. a representative supported and invalid composition matrix has been exercised;
3. scaffold behavior has been compared against manifests and documentation;
4. the repository now has an explicit evidence-backed composition boundary for universal templates;
5. the final verdict is recorded without overclaiming beyond repository truth.

## Follow-Up Guidance

If this lane succeeds, the next likely move is not another generic verification lane but one of these more advanced directions:

- expand into richer fixture coverage for language- and framework-specific combinations;
- add policy-driven composition certification if the repository wants stronger admission guarantees;
- normalize any remaining filename or pipeline-definition irregularities that affect governance hygiene.

If this lane finds residual matrix ambiguity, the next follow-up should be a narrow remediation lane for the exact unsupported or inconsistent composition class rather than a broad expansion lane.
