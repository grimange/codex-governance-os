---
pipeline_id: 040
registry_id: governance.templates.codify-laravel-cli-worker-explicit-unsupported-composition-boundary
title: Codify Laravel + CLI-worker as Explicit Unsupported Template Composition Boundary
stage: implementation
classification: governance
status: proposed
created_by: codex
depends_on:
  - 039
outputs:
  - docs/pipelines/governance/codify-laravel-cli-worker-explicit-unsupported-composition-boundary/01-problem-statement.md
  - docs/pipelines/governance/codify-laravel-cli-worker-explicit-unsupported-composition-boundary/02-boundary-definition.md
  - docs/pipelines/governance/codify-laravel-cli-worker-explicit-unsupported-composition-boundary/03-manifest-boundary-codification.md
  - docs/pipelines/governance/codify-laravel-cli-worker-explicit-unsupported-composition-boundary/04-doctor-surface-verification.md
  - docs/pipelines/governance/codify-laravel-cli-worker-explicit-unsupported-composition-boundary/05-test-boundary-enforcement.md
  - docs/pipelines/governance/codify-laravel-cli-worker-explicit-unsupported-composition-boundary/06-verification.md
  - docs/pipelines/governance/codify-laravel-cli-worker-explicit-unsupported-composition-boundary/07-final-verdict.md
---

# 040 — Codify Laravel + CLI-worker as Explicit Unsupported Template Composition Boundary

## Objective

Convert the **analysis decision from Pipeline 039** into a **codified governance boundary** so the template composition system explicitly and permanently rejects:

```
laravel + cli-worker
```

The rejection must become:

- explicit
- documented
- test-backed
- drift-resistant

This prevents accidental admission through scaffold evolution.

---

# Background

Pipeline **039 — Exercise Laravel + CLI-worker Template Composition Boundary** determined:

```
LARAVEL_CLI_WORKER_COMPOSITION_EXPLICITLY_UNSUPPORTED
```

Reason:

The pair lacks a bounded composition contract covering:

- Laravel application root ownership
- worker runtime lifecycle
- command dispatch surface
- scaffold entrypoint coordination

Admitting the pair would require designing a **new Laravel-specific worker composition model**, not simply enabling a manifest compatibility flag.

Therefore the correct governance outcome is **explicit rejection**, not silent incompatibility.

---

# Scope

This pipeline must:

1. Encode the unsupported pair into composition policy.
2. Ensure the scaffold composition doctor rejects the pair deterministically.
3. Add governance tests verifying the boundary.
4. Ensure reporting surfaces clearly reflect the unsupported status.

This pipeline **must not attempt to implement support**.

---

# Boundary Definition

The following composition is declared unsupported:

```
laravel + cli-worker
```

Rationale:

- Laravel controls the application root runtime.
- CLI-worker assumes standalone worker lifecycle control.
- No defined contract currently coordinates:
  - worker lifecycle
  - job dispatch model
  - entrypoint integration

Until such a contract exists, the combination remains unsupported.

---

# Implementation Tasks

## 1. Codify Boundary in Composition Policy

Ensure the template scaffold composition logic explicitly rejects:

```
laravel + cli-worker
```

This may be implemented through:

- composition compatibility rules
- manifest constraints
- scaffold policy guards

The rejection must produce a deterministic diagnostic.

Example:

```
UNSUPPORTED_COMPOSITION: laravel + cli-worker
reason: missing Laravel worker composition contract
```

---

## 2. Manifest Boundary Visibility

Verify template manifests do **not declare compatibility** between:

```
laravel
cli-worker
```

Ensure manifest interpretation cannot accidentally treat the pair as valid.

---

## 3. Doctor Composition Reporting

Confirm that:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays laravel cli-worker \
  --output json
```

returns a **clear unsupported boundary diagnostic**.

The diagnostic should include:

- composition pair
- rejection reason
- explicit unsupported classification

---

## 4. Add Governance Tests

Add test coverage ensuring the boundary remains stable.

Example test suite:

```
tests/governance/test_laravel_cli_worker_unsupported_boundary.py
```

Tests should verify:

- rejection remains deterministic
- rejection reason is stable
- doctor-composition surface reports the boundary
- existing supported compositions remain unaffected

---

# Expected Artifacts

The pipeline must produce an artifact bundle:

```
docs/pipelines/governance/codify-laravel-cli-worker-explicit-unsupported-composition-boundary/
```

Files:

1. **01-problem-statement.md**

   Why the boundary must be codified.

2. **02-boundary-definition.md**

   Formal description of the unsupported pair.

3. **03-manifest-boundary-codification.md**

   Explanation of how the boundary is enforced in scaffold logic.

4. **04-doctor-surface-verification.md**

   Evidence that doctor-composition reports the boundary.

5. **05-test-boundary-enforcement.md**

   Description of the new governance tests.

6. **06-verification.md**

   Execution evidence.

7. **07-final-verdict.md**

   Final outcome of the pipeline.

---

# Verification

Verification steps:

Run governance tests:

```
python -m unittest discover -s tests/governance -p "test_*.py"
```

Expected:

```
OK
```

Verify the composition boundary:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays laravel cli-worker \
  --output json
```

Expected result:

```
unsupported
```

Confirm that supported compositions remain unaffected.

---

# Final Verdict Format

The final verdict must be:

```
LARAVEL_CLI_WORKER_EXPLICIT_UNSUPPORTED_BOUNDARY_CODIFIED
```

---

# Safety Constraints

This pipeline must **not**:

- implement Laravel worker integration
- introduce a new composition contract
- change existing supported overlay combinations

It strictly **codifies the boundary** discovered in Pipeline 039.

---

# Next Pipelines

After completion, the recommended follow-up lane is:

```
041 — Verify Explicit Laravel + CLI-worker Unsupported Boundary Enforcement
```

This ensures the boundary cannot drift or silently disappear in future template expansions.