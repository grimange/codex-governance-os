---
pipeline: "064"
title: "Establish the First Framework-Native Scheduler Composition Contract"
status: "proposed"
lane: "governance"
stage: "analysis"
classification: "design"
registry_id: "governance.templates.establish-first-framework-native-scheduler-composition-contract"
depends_on:
  - "062"
  - "063"
allowed_inputs:
  - "docs/pipelines/governance/062--close-framework-scheduler-composition-boundaries-with-explicit-contract-rejection.md"
  - "docs/pipelines/governance/063--verify-framework-scheduler-composition-boundaries-remain-non-drifting.md"
  - "tools/governance/composition_contract.py"
  - "tools/governance/template_capability_registry.json"
  - "tools/governance/template_composition_matrix.json"
  - "docs/codex/templates/universal-template-composition-contract.md"
  - "docs/codex/templates/README.md"
  - "docs/governance/template-scaffold-contract.md"
allowed_outputs:
  - "docs/pipelines/governance/establish-first-framework-native-scheduler-composition-contract/"
  - "docs/pipelines/governance/064--establish-the-first-framework-native-scheduler-composition-contract.md"
successors:
  - "065"
  - "066"
  - "067"
---
# 064 — Establish the First Framework-Native Scheduler Composition Contract

## Purpose

Convert the currently explicit-but-rejected framework scheduler boundary into the first governed supported framework-native scheduler composition contract, using Laravel as the inaugural implementation surface.

This pipeline exists because Pipeline 062 made the framework scheduler boundary explicit, and Pipeline 063 verified that the explicit rejection remains non-drifting. The next safe progression is not another generic rejection lane, but the first additive contract that turns one rejected framework pairing into a governed supported composition.

## Problem Statement

The current scheduler overlay model cleanly supports generic scheduler compositions such as:

- `scheduler`
- `scheduler + cli-worker`
- `scheduler + monorepo`
- `scheduler + python-package`
- `scheduler + cli-worker + monorepo`
- `scheduler + cli-worker + python-package`

However, Pipeline 063 verified that the following framework pairings remain explicitly rejected:

- `scheduler + laravel`
- `scheduler + django`

Those rejections are correct under the current contract because no framework-native scheduler composition contract exists yet. Leaving the state here is safe, but incomplete. A governed template system should eventually support framework-native scheduling where the framework has a canonical scheduler surface and the overlay can compose without ambiguity or hidden drift.

Laravel is the correct first supported framework-native scheduler contract because:

- Laravel exposes a centralized and recognizable scheduler surface.
- The scheduler semantics are framework-native rather than incidental.
- The required contract can be expressed with explicit file and capability boundaries.
- It establishes a reusable pattern for later Django-native scheduler support.

## Objectives

1. Define the first framework-native scheduler composition contract using Laravel.
2. Turn `scheduler + laravel` from `explicitly-rejected` into a governed supported composition only when all Laravel-native scheduler contract requirements are satisfied.
3. Preserve explicit rejection for incomplete, malformed, or partial Laravel scheduler surfaces.
4. Preserve existing supported scheduler compositions without drift.
5. Keep `scheduler + django` explicitly rejected until a separate Django-native contract is authored.
6. Make the support state visible and consistent across code, registry, matrix, and documentation.

## Scope

### In Scope

- Defining the canonical Laravel-native scheduler composition contract.
- Updating composition logic to recognize supported `scheduler + laravel` only when the contract is satisfied.
- Updating capability and composition registries.
- Updating template and scaffold documentation.
- Adding tests for positive, negative, and non-drift scenarios.
- Recording the implementation artifact bundle and final verdict.

### Out of Scope

- Implementing Django-native scheduler support.
- Generalizing all framework-native scheduler rules into a single abstract framework layer.
- Expanding scheduler execution semantics beyond contract recognition and scaffold boundary enforcement.
- Changing existing supported non-framework scheduler compositions unless necessary to preserve consistency.
- Adding runtime orchestration, deployment behavior, or hosting-specific scheduler infrastructure.

## Required Inputs

The pipeline may read and reason over the following repository surfaces:

- `tools/governance/composition_contract.py`
- `tools/governance/template_capability_registry.json`
- `tools/governance/template_composition_matrix.json`
- `docs/codex/templates/universal-template-composition-contract.md`
- `docs/codex/templates/README.md`
- `docs/governance/template-scaffold-contract.md`
- tests already covering scheduler overlays, composition matrices, and drift boundaries
- the implementation and verification bundles from Pipelines 062 and 063

## Required Outputs

Create the artifact bundle:

- `docs/pipelines/governance/establish-first-framework-native-scheduler-composition-contract/`

At minimum, the bundle should contain:

1. `01-problem-statement.md`
2. `02-current-framework-scheduler-boundary-state.md`
3. `03-laravel-native-scheduler-contract.md`
4. `04-required-registry-and-matrix-updates.md`
5. `05-test-and-verification-plan.md`
6. `06-implementation-summary.md`
7. `07-final-verdict.md`

The pipeline definition file itself must remain normalized at:

- `docs/pipelines/governance/064--establish-the-first-framework-native-scheduler-composition-contract.md`

## Canonical Contract Requirements

The Laravel-native scheduler composition contract must be explicit and testable. The exact repository paths may follow existing project conventions, but the contract must clearly define the minimum governed evidence required for support.

At minimum, the contract should express all of the following classes of requirements:

### 1. Framework Identity Requirement

The composition must positively identify that the target scaffold includes the Laravel framework overlay and not merely a PHP package or generic service.

### 2. Scheduler Surface Requirement

The composition must require a canonical Laravel-native scheduler declaration surface. The contract must not treat ad hoc cron text or unrelated worker files as equivalent evidence.

### 3. Ownership Boundary Requirement

The contract must clarify which scheduler responsibilities belong to:

- the framework-native Laravel scheduler surface
- the generic scheduler overlay
- any related worker or process overlays when present

This is required to prevent duplicated responsibility and silent semantic conflicts.

### 4. Composition Compatibility Requirement

The contract must specify whether `scheduler + laravel` is:

- supported as a direct pair only
- also supported with approved companion overlays such as `cli-worker` or `monorepo`

If compound support is allowed, the matrix must make that allowance explicit rather than inferred.

### 5. Failure Classification Requirement

The contract must continue to fail closed when:

- Laravel is present but the canonical scheduler surface is absent
- the scheduler surface is partial or malformed
- unsupported overlay combinations are attempted
- the composition would create ambiguous scheduler ownership

### 6. Documentation Symmetry Requirement

The support state and rules for `scheduler + laravel` must be aligned across:

- composition code
- capability registry
- composition matrix
- universal template composition contract documentation
- template README
- scaffold contract documentation

No hidden support is allowed.

## Implementation Requirements

### A. Composition Contract Logic

Update composition recognition so that:

- `scheduler + laravel` is no longer globally rejected
- support is granted only when the Laravel-native scheduler contract is satisfied
- unsupported or partial Laravel scheduler cases remain explicitly rejected with a reasoned classification
- `scheduler + django` remains explicitly rejected and unchanged

### B. Capability Registry

Update the capability registry so that scheduler capability support for Laravel is represented explicitly and not inferred from generic PHP or generic scheduler support.

### C. Composition Matrix

Update the composition matrix to reflect the exact supported state of:

- `scheduler + laravel`
- any approved compound combinations involving Laravel, if intentionally supported
- continued rejection of unsupported framework scheduler combinations

### D. Documentation

Refresh documentation so that a maintainer can answer all of the following without consulting implementation code:

- Is `scheduler + laravel` supported?
- What exact contract must exist for support?
- What still remains unsupported?
- What failure mode applies when the contract is incomplete?

### E. Tests

Add or update tests proving all of the following:

#### Positive Cases

- a valid Laravel-native scheduler composition is accepted
- existing supported scheduler compositions remain accepted

#### Negative Cases

- Laravel without the required scheduler contract is rejected
- partial or malformed Laravel scheduler evidence is rejected
- unsupported framework combinations remain rejected
- Django scheduler pairing remains explicitly rejected

#### Drift Cases

- code, registry, matrix, and docs do not disagree about the supported Laravel scheduler state
- previously supported scheduler combinations remain unchanged unless intentionally expanded

## Recommended Test Surfaces

The exact filenames may vary, but coverage should include repository tests analogous to:

- framework scheduler unsupported boundary tests
- scheduler overlay tests
- composition matrix tests
- composition drift tests

If a dedicated Laravel-native scheduler test module is added, it should verify both contract satisfaction and fail-closed behavior.

## Verification Steps

The implementation should be considered complete only after recording successful evidence for the equivalent of the following verification sequence:

- composition matrix verification command returns valid
- focused scheduler and framework-boundary unit tests pass
- full governance test discovery passes
- documentation and registry references are aligned with implementation truth

Representative commands may include:

```bash
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -m unittest tests.governance.test_framework_scheduler_unsupported_boundaries
python -m unittest tests.governance.test_template_scheduler_overlay
python -m unittest tests.governance.test_template_composition_matrix
python -m unittest tests.governance.test_template_composition_drift
python -m unittest discover -s tests/governance -p 'test_*.py'
```

The recorded verification bundle should use the actual commands and outcomes executed in the repository.

## Expected Final Verdict

The preferred successful verdict for this pipeline is:

- `FIRST_FRAMEWORK_NATIVE_SCHEDULER_CONTRACT_ESTABLISHED`

Acceptable narrower variants are allowed if they remain explicit, such as:

- `LARAVEL_NATIVE_SCHEDULER_CONTRACT_ESTABLISHED_WITH_RESTRICTIONS`

Any restriction variant must explicitly state what remains unsupported and why.

## Safety Conditions

This pipeline must preserve the following safety guarantees:

- no previously explicit rejection becomes implicit support
- no previously supported scheduler composition regresses silently
- framework-native support is additive and evidence-based
- unsupported framework scheduler pairings continue to fail closed
- documentation never claims support that the matrix and code do not enforce

## Recommended Follow-Up Pipelines

After this pipeline, the recommended progression is:

- `065 — Verify Laravel Scheduler Composition Remains Non-Drifting`
- `066 — Establish Django-Native Scheduler Composition Contract`
- `067 — Verify Django Scheduler Composition Remains Non-Drifting`

## Operator Notes

This is the correct bridge between “explicit rejection is stable” and “framework-native scheduler support exists.” It should be implemented as the first governed support opening, not as a broad framework abstraction attempt. The value of this pipeline is precision: one framework, one contract, one newly supported composition boundary, with all non-supported states still made explicit.
