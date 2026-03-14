---
pipeline_id: 041
registry_id: governance.templates.verify-laravel-cli-worker-unsupported-boundary-enforcement
title: Verify Explicit Laravel + CLI-worker Unsupported Boundary Enforcement
stage: verification
classification: governance
status: proposed
created_by: codex
depends_on:
  - 040
outputs:
  - docs/pipelines/governance/verify-laravel-cli-worker-unsupported-boundary-enforcement/01-problem-statement.md
  - docs/pipelines/governance/verify-laravel-cli-worker-unsupported-boundary-enforcement/02-boundary-observation.md
  - docs/pipelines/governance/verify-laravel-cli-worker-unsupported-boundary-enforcement/03-contract-surface-consistency.md
  - docs/pipelines/governance/verify-laravel-cli-worker-unsupported-boundary-enforcement/04-doctor-diagnostic-verification.md
  - docs/pipelines/governance/verify-laravel-cli-worker-unsupported-boundary-enforcement/05-regression-test-verification.md
  - docs/pipelines/governance/verify-laravel-cli-worker-unsupported-boundary-enforcement/06-matrix-stability-check.md
  - docs/pipelines/governance/verify-laravel-cli-worker-unsupported-boundary-enforcement/07-verification.md
  - docs/pipelines/governance/verify-laravel-cli-worker-unsupported-boundary-enforcement/08-final-verdict.md
---

# 041 — Verify Explicit Laravel + CLI-worker Unsupported Boundary Enforcement

## Objective

Verify that the explicit unsupported template composition boundary introduced in **Pipeline 040** is:

- consistently enforced
- clearly diagnosed
- regression-protected
- stable across governance surfaces

The verification must confirm that the pair:

```
laravel + cli-worker
```

remains **explicitly rejected** with the canonical reason:

```
missing Laravel worker composition contract
```

---

# Background

Pipeline **039** determined that supporting this composition would require a new Laravel-specific worker integration contract.

Pipeline **040** codified the boundary by:

- updating the canonical composition contract
- tightening the rejection reason in `composition_contract.py`
- adding regression coverage
- aligning the doctor diagnostic with the contract

This verification lane ensures the boundary is now **stable governance policy**, not an incidental rejection.

---

# Scope

This pipeline verifies:

1. canonical contract alignment
2. scaffold composition doctor diagnostics
3. regression test enforcement
4. stability of the supported composition matrix

This pipeline **must not modify** scaffold logic.

It only verifies enforcement.

---

# Verification Steps

## 1. Observe Composition Rejection

Run:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays laravel cli-worker \
  --output json
```

Expected classification:

```
explicitly-rejected
```

Expected reason:

```
missing Laravel worker composition contract
```

The diagnostic must reference the explicit unsupported boundary.

---

## 2. Verify Contract Surface Alignment

Confirm that the canonical contract document reflects the boundary.

Example reference:

```
docs/governance/universal-template-composition-contract.md
```

The document must state that:

```
laravel + cli-worker
```

is an explicitly unsupported overlay combination.

---

## 3. Verify Doctor Diagnostic Stability

Ensure the diagnostic message returned by:

```
doctor-composition
```

matches the canonical rejection reason.

Doctor output must not return:

- generic rejection
- missing manifest
- unknown incompatibility

It must return the **specific contract reason**.

---

## 4. Verify Regression Tests

Run governance tests:

```
python -m unittest discover -s tests/governance -p "test_*.py"
```

Expected:

```
OK
```

Specifically verify:

```
test_laravel_cli_worker_unsupported_boundary.py
```

The tests must confirm:

- deterministic rejection
- canonical rejection reason
- no accidental admission

---

## 5. Verify Supported Matrix Stability

Ensure that tightening the boundary in Pipeline 040 did **not alter supported compositions**.

Run:

```
python tools/governance/template_scaffold.py doctor-composition \
  --overlays service monorepo \
  --output json
```

Expected:

```
supported
```

Run template discovery:

```
python tools/templates/list_templates.py --output json
```

Verify the template set remains unchanged.

---

# Expected Artifacts

The pipeline produces the verification bundle:

```
docs/pipelines/governance/verify-laravel-cli-worker-unsupported-boundary-enforcement/
```

Files:

1. **01-problem-statement.md**

   Why explicit boundary verification is necessary.

2. **02-boundary-observation.md**

   Evidence of the doctor rejection.

3. **03-contract-surface-consistency.md**

   Contract and diagnostic alignment.

4. **04-doctor-diagnostic-verification.md**

   Evidence from doctor-composition.

5. **05-regression-test-verification.md**

   Evidence from governance test execution.

6. **06-matrix-stability-check.md**

   Proof that supported compositions remain stable.

7. **07-verification.md**

   Full verification log.

8. **08-final-verdict.md**

   Final verification outcome.

---

# Final Verdict Format

The final verdict must be:

```
LARAVEL_CLI_WORKER_UNSUPPORTED_BOUNDARY_VERIFIED_AND_STABLE
```

---

# Safety Constraints

This pipeline must **not**:

- introduce new composition rules
- modify manifest compatibility
- change scaffold behavior
- alter overlay definitions

It only verifies enforcement of the boundary introduced in Pipeline 040.

---

# Next Pipelines

After this verification lane completes, the next governance step should analyze the **remaining unsupported overlay space**.

Recommended next pipeline:

```
042 — Inventory Remaining Unsupported Template Composition Boundaries
```

This will map the remaining rejected overlay pairs and determine which ones are worth exercising next.