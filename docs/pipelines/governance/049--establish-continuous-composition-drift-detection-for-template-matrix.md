---
pipeline_id: "049"
registry_id: governance.templates.establish-continuous-composition-drift-detection
title: Establish Continuous Composition Drift Detection for Template Matrix
stage: governance
type: protection
status: proposed
created: 2026-03-14
governance_domain: template-composition
---

# 049 — Establish Continuous Composition Drift Detection for Template Matrix

## Problem Statement

Pipelines 045 through 048 expanded, normalized, and reverifed the template composition system for the Codex Governance OS.

The composition matrix is now deterministic and governed:

Supported compositions are certified:

- laravel + monorepo
- service + monorepo
- cli-worker + monorepo
- cli-worker + python-package

Unsupported boundaries are explicitly enforced:

- laravel + cli-worker
- django + laravel

Although the current system is stable, the composition contract is still vulnerable to **future drift**.

Drift can occur when:

- new templates are introduced
- template manifests are modified
- scaffold logic changes
- compatibility declarations are edited
- new overlays are added

Without automated detection, these changes could silently alter the composition matrix.

The governance system must introduce **continuous drift detection** so the composition matrix remains permanently protected.

---

## Governance Objective

Establish a permanent governance mechanism that detects composition drift across the following surfaces:

- template manifests
- scaffold composition logic
- governance tests
- documentation
- canonical matrix definition

Any deviation between these surfaces must trigger a governance failure.

---

## Governance Scope

This pipeline introduces drift detection across the following components:

- template composition matrix snapshot
- scaffold runtime composition behavior
- template manifest compatibility declarations
- governance test coverage
- CI enforcement

---

## Canonical Matrix Snapshot

Create a canonical snapshot describing the composition matrix.

Example file:

```
tools/governance/template_composition_matrix.json
```

Example structure:

```
{
  "supported": [
    ["laravel", "monorepo"],
    ["service", "monorepo"],
    ["cli-worker", "monorepo"],
    ["cli-worker", "python-package"]
  ],
  "unsupported": [
    ["laravel", "cli-worker"],
    ["django", "laravel"]
  ]
}
```

This snapshot becomes the **governed truth source** for the composition matrix.

---

## Drift Detection Mechanism

Introduce a governance command that verifies the composition matrix against runtime scaffold behavior.

Example command:

```
python tools/governance/template_scaffold.py verify-composition-matrix
```

The command must verify that:

- scaffold composition classification matches the matrix snapshot
- manifest compatibility declarations match the matrix snapshot
- unsupported boundaries remain enforced
- supported compositions remain admitted

If any mismatch occurs, the command must fail.

---

## Governance Test Coverage

Add a dedicated governance test suite.

Example test file:

```
tests/governance/test_template_composition_drift.py
```

The test suite must verify:

- runtime scaffold results match the canonical matrix snapshot
- supported compositions remain certified
- unsupported compositions remain rejected
- canonical rejection reasons remain consistent

If drift is detected, the test suite must fail.

---

## Continuous Integration Enforcement

CI must run drift detection as part of the governance test suite.

Example CI command:

```
python tools/governance/template_scaffold.py verify-composition-matrix
```

Expected outcome:

```
composition-matrix: OK
no drift detected
```

If drift occurs:

```
composition-matrix: DRIFT DETECTED
```

CI must fail.

---

## Verification Procedure

Run the following commands.

List template manifests:

```
python tools/governance/template_scaffold.py list-manifests --output json
```

List template registry:

```
python tools/templates/list_templates.py --output json
```

Verify composition matrix:

```
python tools/governance/template_scaffold.py verify-composition-matrix
```

Run governance test suite:

```
python -m unittest discover -s tests/governance -p "test_*.py"
```

Expected result:

```
All tests pass
No composition drift detected
```

---

## Evidence Artifacts

The pipeline must produce the following artifact bundle:

```
docs/pipelines/governance/
establish-continuous-composition-drift-detection/
```

Artifacts:

```
01-problem-statement.md
02-canonical-matrix-snapshot.md
03-drift-detection-mechanism.md
04-governance-test-coverage.md
05-ci-enforcement.md
06-verification.md
07-final-verdict.md
```

---

## Final Verdict Format

The final verdict must be recorded as:

```
TEMPLATE_COMPOSITION_DRIFT_DETECTION_ESTABLISHED
```

Meaning:

- template composition behavior is protected against drift
- scaffold behavior must match the canonical matrix
- governance tests enforce composition invariants
- CI prevents silent composition changes

---

## Governance Impact

After this pipeline:

- template composition becomes a governed invariant
- future template changes cannot silently modify composition behavior
- the governance system gains permanent drift protection
- the composition matrix remains deterministic as the template ecosystem grows

This pipeline transforms the composition system from **verified state** into **self-protecting governance infrastructure**.

---

## Next Recommended Pipeline

```
050 — Establish Universal Template Composition Capability Registry
```

This pipeline will transition the template composition system from static overlay pairs to a capability-based composition model, allowing more flexible yet governed combinations of templates.