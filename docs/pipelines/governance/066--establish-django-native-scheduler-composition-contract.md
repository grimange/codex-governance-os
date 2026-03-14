---
pipeline: "066"
title: "Establish Django-Native Scheduler Composition Contract"
status: "proposed"
lane: "governance"
stage: "analysis"
classification: "design"
registry_id: "governance.templates.establish-django-native-scheduler-composition-contract"
depends_on:
  - "062"
  - "063"
  - "064"
  - "065"
allowed_inputs:
  - "docs/pipelines/governance/062--close-framework-scheduler-composition-boundaries-with-explicit-contract-rejection.md"
  - "docs/pipelines/governance/063--verify-framework-scheduler-composition-boundaries-remain-non-drifting.md"
  - "docs/pipelines/governance/064--establish-the-first-framework-native-scheduler-composition-contract.md"
  - "docs/pipelines/governance/065--verify-laravel-scheduler-composition-remains-non-drifting.md"
  - "tools/governance/composition_contract.py"
  - "tools/governance/template_capability_registry.json"
  - "tools/governance/template_composition_matrix.json"
  - "tools/governance/template_scaffold.py"
  - "docs/codex/templates/universal-template-composition-contract.md"
  - "docs/codex/templates/README.md"
  - "docs/governance/template-scaffold-contract.md"
  - "docs/codex/templates/django/README.md"
  - "docs/codex/templates/scheduler/README.md"
allowed_outputs:
  - "docs/pipelines/governance/establish-django-native-scheduler-composition-contract/"
  - "docs/pipelines/governance/066--establish-django-native-scheduler-composition-contract.md"
successors:
  - "067"
  - "068"
---
# 066 — Establish Django-Native Scheduler Composition Contract

## Purpose

Establish the Django-native scheduler composition contract as the second governed framework-native scheduler path, converting `django + scheduler` from an explicit rejection into a supported composition only when the Django-native scheduler contract is fully satisfied.

This pipeline follows the pattern already proven in the Laravel path:

- Pipeline 062 made framework-native scheduler boundaries explicit
- Pipeline 063 verified those explicit rejections remained non-drifting
- Pipeline 064 established the first supported framework-native scheduler contract for Laravel
- Pipeline 065 verified Laravel-native scheduler support remained non-drifting

The next safe and logical progression is to open the Django-native scheduler path with the same discipline: explicit contract, fail-closed behavior, aligned truth surfaces, and dedicated verification coverage.

## Problem Statement

The current scheduler composition model now supports:

- `scheduler`
- `scheduler + cli-worker`
- `scheduler + monorepo`
- `scheduler + python-package`
- `scheduler + cli-worker + monorepo`
- `scheduler + cli-worker + python-package`
- `scheduler + laravel`

But it still explicitly rejects:

- `scheduler + django`

That explicit rejection is currently correct because no Django-native scheduler composition contract has yet been established. As long as the repository lacks a canonical, governed Django scheduler evidence set, support must remain closed.

However, Django is a first-class framework surface in the template system. A complete framework-native scheduler track should not stop at Laravel alone. The repository now needs a Django-native scheduler contract that is:

- explicit rather than inferred
- governed rather than ad hoc
- additive rather than destabilizing
- aligned across implementation, matrix, registry, scaffold generation, and documentation

## Objectives

1. Define the canonical Django-native scheduler composition contract.
2. Convert `django + scheduler` from explicit rejection to governed support only when the contract is satisfied.
3. Preserve fail-closed behavior for missing, partial, or malformed Django scheduler surfaces.
4. Preserve the Laravel-native scheduler contract unchanged.
5. Preserve existing supported generic scheduler compositions unchanged.
6. Keep broader framework-native scheduler combinations unsupported unless this pipeline explicitly opens them.
7. Make the support state visible and identical across all governance truth surfaces.

## Scope

### In Scope

- Defining the canonical Django-native scheduler contract
- Updating composition logic to admit direct `django + scheduler` support only when the contract is satisfied
- Updating capability registry and composition matrix truth
- Updating scaffold generation requirements
- Updating template and scaffold documentation
- Adding focused Django-native scheduler coverage
- Recording the implementation artifact bundle and final verdict

### Out of Scope

- Changing Laravel-native scheduler semantics
- Expanding Django scheduler support into `django + monorepo + scheduler` unless intentionally chosen in this lane
- Implementing runtime process orchestration or deployment scheduler infrastructure
- Broad multi-framework abstraction beyond what is required to support Django cleanly
- Opening unsupported framework-native scheduler combinations by implication

## Required Inputs

This pipeline may inspect and reason over the following repository surfaces:

- `tools/governance/composition_contract.py`
- `tools/governance/template_capability_registry.json`
- `tools/governance/template_composition_matrix.json`
- `tools/governance/template_scaffold.py`
- `docs/codex/templates/universal-template-composition-contract.md`
- `docs/codex/templates/README.md`
- `docs/governance/template-scaffold-contract.md`
- `docs/codex/templates/django/README.md`
- `docs/codex/templates/scheduler/README.md`
- scheduler, composition, capability, drift, and unsupported-boundary test suites
- the implementation and verification bundles from Pipelines 062 through 065

## Required Outputs

Create the artifact bundle:

- `docs/pipelines/governance/establish-django-native-scheduler-composition-contract/`

At minimum, the bundle should contain:

1. `01-problem-statement.md`
2. `02-current-django-scheduler-boundary-state.md`
3. `03-django-native-scheduler-contract.md`
4. `04-required-registry-matrix-and-scaffold-updates.md`
5. `05-test-and-verification-plan.md`
6. `06-implementation-summary.md`
7. `07-final-verdict.md`

The normalized pipeline definition file must remain at:

- `docs/pipelines/governance/066--establish-django-native-scheduler-composition-contract.md`

## Canonical Contract Requirements

The Django-native scheduler composition contract must be explicit, testable, and fail closed. It must define the minimum governed evidence required to support `django + scheduler`.

The exact files may follow repository conventions, but the contract must clearly specify a canonical Django-native scheduler evidence set.

At minimum, the contract must satisfy all of the following requirement classes.

### 1. Framework Identity Requirement

The contract must positively identify that the target scaffold includes the Django framework overlay and is not merely a generic Python package, worker, or service.

### 2. Scheduler Surface Requirement

The contract must require canonical Django-native scheduler declaration surfaces. The repository must not accept generic cron fragments, arbitrary scripts, or unrelated worker definitions as equivalent scheduler evidence.

The contract should define a small, governed Django-native scheduler evidence set that is discoverable and enforceable.

### 3. Ownership Boundary Requirement

The contract must clearly assign scheduler responsibilities across:

- Django-native scheduler declaration surfaces
- the generic scheduler overlay
- any related worker/process overlays, if present

This prevents duplicate authority and silent conflicts about where scheduling truth lives.

### 4. Composition Compatibility Requirement

The contract must explicitly state whether support applies only to the direct pair:

- `django + scheduler`

or also to any compound combinations. No broader support may be inferred.

If compound support is not intentionally opened in this pipeline, the matrix must keep those combinations explicitly unsupported.

### 5. Failure Classification Requirement

The contract must fail closed when:

- Django is present but the canonical scheduler surface is absent
- the scheduler evidence is partial or malformed
- unsupported overlay combinations are attempted
- scheduler ownership is ambiguous
- the scaffold shape does not meet the Django scheduler contract

### 6. Documentation Symmetry Requirement

The support state and contract rules for `django + scheduler` must be identical across:

- composition code
- capability registry
- composition matrix
- scaffold generation rules
- universal template composition documentation
- template README
- scaffold contract documentation
- Django and scheduler overlay documentation

No hidden or partially documented support is allowed.

## Recommended Django Contract Shape

This pipeline should define a Django-native scheduler contract that is clear enough for automated verification and scaffold generation. The exact filenames may vary with repository conventions, but the contract should prefer a compact, explicit, governed evidence set rather than loose pattern matching.

The contract should aim for:

- one or more canonical Django scheduler declaration surfaces
- explicit scheduler configuration ownership
- no ambiguity between application scheduling and worker execution
- scaffold generation rules that can materialize the required evidence set deterministically

The important rule is not which specific filenames are chosen, but that the chosen filenames become the only canonical evidence set for `django + scheduler` support and are enforced consistently.

## Implementation Requirements

### A. Composition Contract Logic

Update composition recognition so that:

- `scheduler + django` is no longer globally rejected
- support is granted only when the Django-native scheduler contract is satisfied
- incomplete or malformed Django scheduler states remain explicitly rejected
- `scheduler + laravel` remains supported and unchanged
- generic scheduler support remains unchanged

### B. Capability Registry

Update the capability registry so that Django-native scheduler support is represented explicitly and not inferred from generic Python or generic scheduler capability alone.

### C. Composition Matrix

Update the composition matrix to reflect the exact supported state of:

- `scheduler + django`
- any intentionally approved compound combinations, if any
- continued rejection of unsupported broader framework scheduler combinations

### D. Scaffold Generation

Update scaffold generation requirements so the Django-native scheduler contract can be generated, verified, and inspected deterministically.

The scaffold layer must know what governed surfaces are required for a valid `django + scheduler` template.

### E. Documentation

Refresh documentation so a maintainer can answer all of the following from docs alone:

- Is `scheduler + django` supported?
- What exact contract must exist for support?
- What evidence set is canonical?
- What remains unsupported?
- What failure mode applies when the contract is incomplete?

### F. Tests

Add or update tests proving all of the following.

#### Positive Cases

- a valid Django-native scheduler composition is accepted
- Laravel-native scheduler support remains accepted
- existing supported generic scheduler compositions remain accepted

#### Negative Cases

- Django without the required scheduler contract is rejected
- partial or malformed Django scheduler evidence is rejected
- unsupported framework scheduler combinations remain rejected
- unsupported compound Django scheduler combinations remain rejected unless explicitly opened

#### Drift Cases

- code, registry, matrix, scaffold logic, and docs do not disagree about the supported Django scheduler state
- previously supported scheduler combinations remain unchanged unless intentionally expanded

## Recommended Test Surfaces

Coverage should include repository tests analogous to:

- framework scheduler unsupported boundary tests
- Django-native scheduler composition tests
- scheduler overlay tests
- capability composition tests
- composition matrix tests
- composition drift tests
- scaffold generation matrix tests

If a dedicated Django-native scheduler test module is added, it should verify both contract satisfaction and fail-closed behavior.

## Verification Steps

The implementation should be considered complete only after successful recorded evidence for an equivalent sequence such as:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler django --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler laravel --output json
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -m unittest tests.governance.test_django_native_scheduler_composition
python -m unittest tests.governance.test_framework_scheduler_unsupported_boundaries
python -m unittest tests.governance.test_template_scheduler_overlay
python -m unittest tests.governance.test_template_capability_composition
python -m unittest tests.governance.test_template_composition_matrix
python -m unittest tests.governance.test_template_composition_drift
python -m unittest tests.governance.test_scheduler_scaffold_generation_matrix
python -m unittest discover -s tests/governance -p 'test_*.py'
```

The recorded artifact bundle should use the actual commands and outcomes executed in the repository.

## Expected Final Verdict

Preferred successful verdict:

- `DJANGO_NATIVE_SCHEDULER_CONTRACT_ESTABLISHED`

Acceptable narrower variant if explicit restrictions remain:

- `DJANGO_NATIVE_SCHEDULER_CONTRACT_ESTABLISHED_WITH_RESTRICTIONS`

Any restriction variant must explicitly state what remains unsupported and why.

## Safety Conditions

This pipeline must preserve all of the following:

- no implicit expansion of framework-native scheduler support
- no regression of Laravel-native scheduler support
- no regression of previously supported generic scheduler compositions
- no documentation claim that exceeds matrix or code truth
- no acceptance of partial Django scheduler evidence
- no hidden broadening into unsupported compound combinations

## Recommended Follow-Up Pipelines

After this pipeline, the recommended next lanes are:

- `067 — Verify Django Scheduler Composition Remains Non-Drifting`
- `068 — Evaluate Whether Framework-Native Scheduler Compound Compositions Should Be Opened Explicitly`

## Operator Notes

This pipeline should mirror the discipline of the Laravel-native scheduler lane without forcing Django into Laravel-shaped semantics. The goal is not symmetry of filenames; the goal is symmetry of governance quality:

- explicit evidence
- deterministic scaffold rules
- fail-closed behavior
- aligned truth surfaces
- clear unsupported boundaries

That makes this the correct second framework-native scheduler contract lane.
