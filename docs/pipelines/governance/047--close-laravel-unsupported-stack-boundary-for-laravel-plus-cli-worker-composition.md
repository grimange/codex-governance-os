---
pipeline_id: "047"
registry_id: governance.templates.close-laravel-cli-worker-composition-boundary
title: Close Laravel Unsupported Stack Boundary for Laravel + CLI Worker Composition
stage: governance
type: expansion
status: proposed
created: 2026-03-14
governance_domain: template-composition
---

# 047 — Close Laravel Unsupported Stack Boundary for Laravel + CLI Worker Composition

## Problem Statement

Pipeline 046 verified that the template composition matrix remains coherent after the admission of the `laravel + monorepo` composition. The governance verification confirmed that unsupported combinations remain correctly rejected.

One composition remains intentionally unsupported but not yet formally governed as a closed boundary:

- `laravel + cli-worker`

Currently this composition fails closed through explicit rejection logic, but the boundary has not yet been formally normalized through governance artifacts.

Without explicit governance normalization:

- scaffold logic may drift
- template manifests may accidentally admit the combination
- future template expansion may reintroduce ambiguity
- the composition matrix may lose deterministic behavior

The governance system must either **admit the composition with a contract** or **permanently close the boundary with canonical rejection reasoning**.

---

## Governance Objective

Normalize the governance boundary for the `laravel + cli-worker` composition by:

1. Verifying the current rejection behavior
2. Documenting the canonical rejection reason
3. Ensuring template scaffolding fails closed
4. Ensuring the composition matrix explicitly encodes the unsupported boundary

This pipeline does **not introduce a new supported composition**.

Instead, it transforms an **implicit unsupported state into a governed explicit boundary**.

---

## Scope

This pipeline governs the following layers:

- Template composition matrix
- Template manifest compatibility declarations
- Scaffold composition enforcement
- Governance test coverage
- Explicit unsupported-boundary documentation

---

## Boundary Classification

The composition under governance:

```
laravel + cli-worker
```

Current classification:

```
explicitly-unsupported
```

Canonical reasoning:

1. Laravel applications already provide internal worker mechanisms through:
   - queue workers
   - scheduled tasks
   - horizon-based job processing

2. The `cli-worker` overlay represents a **standalone worker runtime pattern**, which conflicts with Laravel’s internal execution model.

3. Mixing these two models introduces ambiguity in:
   - process ownership
   - runtime orchestration
   - worker lifecycle governance

For governance clarity, the boundary must remain **explicitly rejected**.

---

## Required Actions

### 1. Normalize Template Composition Policy

Ensure the composition matrix explicitly declares:

```
laravel + cli-worker -> explicitly-rejected
```

The rejection must be deterministic and enforced at scaffold time.

---

### 2. Verify Manifest Compatibility Rules

Confirm that:

- Laravel manifests do **not** declare compatibility with `cli-worker`
- CLI worker manifests do **not** declare compatibility with `laravel`

If compatibility declarations exist, they must be removed.

---

### 3. Harden Scaffold Enforcement

Verify the scaffold system rejects the composition with a canonical error:

Example rejection:

```
Unsupported template composition:
laravel + cli-worker

Reason:
Laravel applications already provide native worker execution models.
The CLI worker overlay is designed for standalone service runtimes.
```

The scaffold must fail closed.

---

### 4. Extend Governance Test Coverage

Add governance tests ensuring the boundary remains enforced.

Example test expectation:

```
laravel + cli-worker -> explicitly-rejected
```

Test location:

```
tests/governance/test_template_composition_matrix.py
```

The test must verify:

- scaffold rejection
- matrix classification
- deterministic failure reason

---

### 5. Update Template Composition Documentation

Update the template composition documentation to include the unsupported boundary.

File:

```
docs/codex/templates/README.md
```

Add entry:

```
Unsupported Composition

- laravel + cli-worker
  Reason: runtime model conflict
```

---

## Verification Procedure

Run the following verification commands:

List template manifests:

```
python tools/governance/template_scaffold.py list-manifests --output json
```

List template registry:

```
python tools/templates/list_templates.py --output json
```

Run governance test suite:

```
python -m unittest discover -s tests/governance -p "test_*.py"
```

Expected outcome:

```
All tests pass
Explicit unsupported boundary enforced
```

---

## Evidence Artifacts

The pipeline must produce the following artifact bundle:

```
docs/pipelines/governance/
close-laravel-cli-worker-composition-boundary/
```

Artifacts:

```
01-problem-statement.md
02-current-composition-state.md
03-boundary-classification.md
04-scaffold-enforcement.md
05-governance-test-coverage.md
06-verification.md
07-final-verdict.md
```

---

## Final Verdict Format

The final verdict must be recorded as:

```
LARAVEL_CLI_WORKER_COMPOSITION_BOUNDARY_CLOSED_WITH_EXPLICIT_REJECTION
```

Meaning:

- the composition matrix is deterministic
- unsupported stack boundaries are explicitly governed
- scaffold behavior fails closed
- future template expansion cannot accidentally admit the combination

---

## Governance Impact

After this pipeline:

- Laravel template composition rules become deterministic
- unsupported runtime combinations are explicitly governed
- template scaffold drift risk is reduced
- the composition matrix remains stable as additional overlays are introduced

This pipeline strengthens the **governed template composition system** for the Codex Governance OS.

---

## Next Recommended Pipeline

```
048 — Reverify Template Composition Matrix After Boundary Closure
```

This reverification ensures that:

- the matrix remains coherent
- the scaffold still enforces the boundary
- no unintended composition regressions occur.