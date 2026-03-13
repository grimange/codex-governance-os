---
id: 025
title: Close Unsupported Stack Boundaries For Universal Codex Templates
slug: close-unsupported-stack-boundaries-for-universal-codex-templates
status: proposed
stage: implementation
category: governance
authority: codex
mode: governed
change_type: additive
risk_level: medium
registry_id: governance.templates.close-unsupported-stack-boundaries-for-universal-codex-templates
requires:
  - 023
suggests:
  - 024
  - 026
supersedes: []
blocks: []
---

# 025 — Close Unsupported Stack Boundaries For Universal Codex Templates

## 1. Purpose

Close the currently unsupported stack boundaries identified by the universal template conformance work so the template system becomes truly cross-stack rather than "universal with explicit exclusions."

This lane converts known unsupported boundaries into governed, testable, and intentionally supported template overlays. It is the implementation complement to the verification outcome produced in Pipeline 023.

## 2. Problem Statement

Pipeline 023 established that the universal codex template model already conforms across these supported repository classes:

- base-only governed repository
- Laravel
- Django
- Python package
- PHP package
- generic service
- monorepo

However, 023 also made the support boundary explicit:

- Node/TypeScript service overlay is not yet implemented
- CLI/worker overlay is not yet implemented

That means the system is currently **universally structured**, but not yet **universally deployable across the intended stack family**. As long as these unsupported boundaries remain open, the template layer still depends on manual interpretation when a governed repo falls into one of those classes.

## 3. Why This Pipeline Exists Now

This lane should follow directly after 023 because 023 already produced the authoritative boundary verdict:

**UNIVERSAL_TEMPLATE_CONFORMANCE_VERIFIED_WITH_RESTRICTIONS**

Once the unsupported boundaries are known and verified, the next valid move is not to keep re-verifying the gap. The next move is to close it by implementing the missing overlays, aligning generated outputs, and extending the conformance matrix so future verification reflects full coverage instead of known exclusions.

## 4. Objectives

This pipeline must:

1. Implement a governed Node/TypeScript service overlay.
2. Implement a governed CLI/worker overlay.
3. Preserve compatibility with the already-conformant stack set from 023.
4. Extend template selection and rendering logic so unsupported cases become first-class supported cases.
5. Add deterministic fixture coverage proving the new overlays render correctly.
6. Update the documented support matrix so unsupported boundaries are no longer hidden, stale, or ambiguous.

## 5. In Scope

The lane covers the following work:

- template overlay design for Node/TypeScript services
- template overlay design for CLI/worker runtimes
- shared template contract alignment across all overlays
- generator, resolver, or registry updates needed to select the new overlays
- fixture creation for each newly supported stack type
- conformance tests that include the new fixtures
- documentation updates for the support matrix and overlay boundaries
- explicit compatibility rules for mixed or monorepo placement where applicable

## 6. Out of Scope

This lane does **not**:

- redesign the whole universal template architecture from scratch
- change the already-supported overlays unless required for compatibility
- add unrelated stacks not already implied by the current gap analysis
- claim full runtime correctness for generated applications beyond template conformance
- introduce stack-specific business logic outside template/governance needs
- silently broaden support to frontend SPA stacks unless explicitly modeled and tested

## 7. Target Unsupported Boundaries To Close

### 7.1 Node/TypeScript service boundary

The resulting implementation should support repositories where the governed project is primarily:

- a Node.js backend or service
- a TypeScript backend or service
- an API service whose operational conventions differ from Laravel/Django/PHP/Python-package defaults

The overlay should account for common service-level structures such as:

- package manifest presence
- script-driven execution model
- environment and configuration conventions
- source/test directory expectations
- service entrypoint expectations
- optional monorepo placement rules when the service lives under a workspace package

### 7.2 CLI/worker boundary

The resulting implementation should support repositories where the governed project is primarily:

- a command-line application
- a scheduled worker
- a queue worker or background processor
- a daemon-like service with no route surface

The overlay should account for patterns such as:

- command-oriented entrypoints
- worker lifecycle notes
- scheduler/background execution surface
- absence of HTTP routing as the primary runtime
- queue, job, task, or batch-oriented structure

## 8. Required Design Principles

All new overlay support must follow these principles:

### 8.1 Additive over destructive

New overlays should extend the universal template system, not destabilize already working overlays.

### 8.2 Contract-first

Each overlay must express:

- when it applies
- what files or directories it contributes
- what invariants it assumes
- what outputs are mandatory versus optional

### 8.3 Explicit selection rules

Overlay selection must be deterministic. If two overlays may apply, precedence or composability rules must be written down and tested.

### 8.4 Fail-closed behavior

If a repository cannot be confidently classified into a supported overlay set, the system should still fail as unsupported rather than quietly generating the wrong template family.

### 8.5 Verification-backed support claims

No newly claimed support boundary may be declared closed without fixture-based conformance evidence.

## 9. Implementation Plan

### Step 1 — Capture the unsupported boundary inventory

Produce a short implementation inventory derived from Pipeline 023 and the current template resolver:

- unsupported stack classes
- current resolver behavior for those classes
- missing files, overlays, or selectors
- collision risks with existing overlays

### Step 2 — Define the overlay contract for Node/TypeScript services

Specify:

- stack detection signals
- required output files
- optional output files
- compatibility with base-only and monorepo overlays
- resolver precedence rules

### Step 3 — Define the overlay contract for CLI/worker runtimes

Specify:

- stack detection signals
- required output files
- optional output files
- no-route-surface assumptions
- coexistence rules with language overlays where relevant

### Step 4 — Implement template assets and resolver logic

Add the missing overlay templates and any resolver/registry wiring needed so the generator can correctly classify and render them.

### Step 5 — Add canonical fixtures

Introduce minimal fixtures that represent the newly supported boundaries, such as:

- Node service fixture
- TypeScript service fixture, if distinct from plain Node classification
- CLI application fixture
- worker/background processor fixture

If the implementation intentionally collapses some of these into a smaller number of canonical overlay classes, that collapse must be documented and reflected in tests.

### Step 6 — Extend conformance coverage

Update the conformance harness to ensure the new overlays are included in the template rendering matrix and compared against expected governed outputs.

### Step 7 — Refresh support documentation

Update the support matrix and any registry/documentation that previously marked the boundaries as unsupported.

### Step 8 — Verify closure through a follow-up verification lane

This lane should end with implementation complete and readiness for verification, not with an unsupported-boundary claim based only on intent. The closure verdict should be finalized by the follow-up verification lane.

## 10. Expected Repository Changes

Depending on repository structure, this pipeline will usually touch one or more of the following:

- universal template source directories
- template resolver/classification logic
- stack detection helpers
- fixture directories for supported repositories
- conformance test suites
- support matrix documentation
- pipeline registry and recommendation references if needed

## 11. Deliverables

This pipeline should produce a governed artifact bundle such as:

1. `01-problem-statement.md`
2. `02-unsupported-boundary-inventory.md`
3. `03-node-typescript-overlay-contract.md`
4. `04-cli-worker-overlay-contract.md`
5. `05-implementation-plan.md`
6. `06-fixture-and-test-expansion.md`
7. `07-verification-plan.md`
8. `08-final-verdict.md`

## 12. Acceptance Criteria

The lane is complete when all of the following are true:

- Node/TypeScript service overlay support exists in the generator/template system.
- CLI/worker overlay support exists in the generator/template system.
- Overlay selection rules are deterministic and documented.
- Newly added fixtures render without ad hoc manual fixes.
- The conformance suite includes the new fixtures.
- Existing supported fixtures continue to pass.
- Documentation no longer describes these boundaries as unsupported, unless a narrower residual restriction remains explicitly stated.
- The final implementation verdict is evidence-backed rather than aspirational.

## 13. Verification Requirements

At minimum, verification must prove:

1. Existing supported overlays still pass unchanged.
2. A Node/TypeScript service fixture now renders as supported.
3. A CLI/worker fixture now renders as supported.
4. Resolver logic does not misclassify existing Laravel, Django, package, or monorepo fixtures.
5. Residual unsupported cases, if any remain, are explicitly named.

Suggested verification commands should include the repository's canonical template-conformance and test execution commands, for example:

```bash
python -m unittest discover -s tests/governance -p 'test_*.py'
python tools/templates/list_templates.py --format json
python tools/templates/render_template.py --fixture <new-fixture>
```

Adjust command names to repository reality; do not invent success signals that the repo cannot actually execute.

## 14. Final Verdict Options

The final verdict for this implementation lane should be one of:

- `UNSUPPORTED_STACK_BOUNDARIES_IMPLEMENTED_READY_FOR_VERIFICATION`
- `UNSUPPORTED_STACK_BOUNDARIES_PARTIALLY_IMPLEMENTED_WITH_RESTRICTIONS`
- `UNSUPPORTED_STACK_BOUNDARIES_NOT_CLOSED`

Preferred successful outcome for this lane:

**UNSUPPORTED_STACK_BOUNDARIES_IMPLEMENTED_READY_FOR_VERIFICATION**

## 15. Recommended Next Pipeline

The natural follow-up lane is:

**026 — Verify Unsupported Stack Boundary Closure For Universal Codex Templates**

That verification lane should confirm whether Pipeline 025 actually converted the 023 restrictions into supported, evidence-backed template coverage.

## 16. Operator Notes

Use this lane name rather than the looser alternative because it is outcome-oriented and governance-clear:

**Close Unsupported Stack Boundaries For Universal Codex Templates**

Why this is the stronger name:

- it points to the exact known gap from 023
- it describes a closure objective, not merely "coverage addition"
- it remains compatible even if the implementation involves resolver rules, docs, and tests, not only overlays
- it fits governance language better because it frames the work as removing an explicit unsupported boundary

