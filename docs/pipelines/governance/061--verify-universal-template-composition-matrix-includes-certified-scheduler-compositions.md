# 061 --- Verify Universal Template Composition Matrix Includes Certified Scheduler Compositions

## Frontmatter

``` yaml
pipeline_id: 061
registry_id: governance.templates.verify-universal-template-composition-matrix-includes-certified-scheduler-compositions
title: Verify Universal Template Composition Matrix Includes Certified Scheduler Compositions
stage: verification
governance_domain: templates
pipeline_type: verification
status: proposed
created_by: codex
requires:
  - 027
  - 058
  - 059
  - 060
produces:
  - scheduler-composition-matrix-verification
  - scheduler-supported-composition-verification
  - scheduler-unsupported-boundary-verification
verification:
  - composition-matrix-truth-verification
  - template-scaffold-enforcement-verification
```

------------------------------------------------------------------------

# 1. Problem Statement

Pipeline **060** formally recorded scheduler overlay certification in
the **universal template composition matrix**.

However, governance correctness requires verification that:

-   the **composition contract**
-   the **template scaffold implementation**
-   the **verification tooling**
-   and the **operator-facing documentation**

remain aligned.

Without this verification step, scheduler certification could drift
between:

-   contract documentation
-   scaffold behavior
-   composition validation tooling

This pipeline ensures the scheduler overlay certification recorded in
**060** is **fully enforced and non-drifting** across governance
surfaces.

------------------------------------------------------------------------

# 2. Governance Objective

Verify that the **scheduler overlay certification**:

1.  Exists in the canonical composition matrix.
2.  Is enforced by `template_scaffold.py`.
3.  Produces correct results through `doctor-composition`.
4.  Remains consistent with repository documentation.

This pipeline **does not modify behavior** --- it verifies governance
truth.

------------------------------------------------------------------------

# 3. Verification Scope

The verification covers four governance surfaces.

### 1. Composition Contract

Example location:

    docs/codex/templates/universal-template-composition-contract.md

Must include scheduler combinations recorded in pipeline **060**.

------------------------------------------------------------------------

### 2. Template Scaffold Enforcement

Example implementation:

    tools/governance/template_scaffold.py

The scaffold system must recognize scheduler overlay combinations.

------------------------------------------------------------------------

### 3. Composition Verification Tooling

Tooling surfaces include:

    doctor-composition
    verify-composition-matrix

Both must correctly validate scheduler compositions.

------------------------------------------------------------------------

### 4. Operator Documentation

Example surfaces:

    docs/codex/templates/README.md
    docs/governance/template-scaffold-contract.md

Documentation must reflect the canonical scheduler matrix truth.

------------------------------------------------------------------------

# 4. Certified Scheduler Compositions

The following combinations must be verified as **supported**.

    scheduler
    scheduler + cli-worker
    scheduler + monorepo
    scheduler + python-package
    scheduler + cli-worker + monorepo
    scheduler + cli-worker + python-package

------------------------------------------------------------------------

# 5. Explicit Unsupported Boundaries

The governance system must verify these combinations **fail closed**.

Examples:

    scheduler + laravel
    scheduler + django
    scheduler + node-typescript-service
    scheduler + php-package

Expected response:

    supported: false
    reason_code: unsupported-overlay-combination

------------------------------------------------------------------------

# 6. Verification Procedure

## Test 1 --- Supported Composition

    python tools/governance/template_scaffold.py doctor-composition \
      --overlays scheduler cli-worker \
      --output json

Expected:

    {
      "supported": true,
      "reason_code": "certified-multi-overlay"
    }

------------------------------------------------------------------------

## Test 2 --- Unsupported Framework Pair

    python tools/governance/template_scaffold.py doctor-composition \
      --overlays scheduler laravel \
      --output json

Expected:

    {
      "supported": false
    }

------------------------------------------------------------------------

## Test 3 --- Composition Matrix Verification

    python tools/governance/template_scaffold.py verify-composition-matrix --output json

Expected:

    {
      "valid": true,
      "errors": []
    }

------------------------------------------------------------------------

## Test 4 --- Scheduler Conformance Tests

    python -m unittest tests.governance.test_template_scheduler_overlay

Expected:

    OK

------------------------------------------------------------------------

## Test 5 --- Global Governance Test Suite

    python -m unittest discover -s tests/governance -p "test_*.py"

Expected:

    All tests passing

------------------------------------------------------------------------

# 7. Drift Detection Requirements

This pipeline verifies that no drift exists between:

  Surface                   Drift Risk
  ------------------------- -------------------------------------------
  composition contract      documented matrix differs from scaffold
  scaffold implementation   scaffold admits undocumented combinations
  verification tooling      tools accept invalid overlays
  documentation             docs advertise unsupported overlays

Any detected mismatch must fail the pipeline.

------------------------------------------------------------------------

# 8. Artifact Bundle

Artifacts must be stored under:

    docs/pipelines/governance/verify-universal-template-composition-matrix-includes-certified-scheduler-compositions/

Required artifacts:

    01-problem-statement.md
    02-composition-contract-inspection.md
    03-scaffold-enforcement-verification.md
    04-supported-composition-verification.md
    05-unsupported-boundary-verification.md
    06-verification-results.md
    07-final-verdict.md

------------------------------------------------------------------------

# 9. Expected Final Verdict

    SCHEDULER_COMPOSITION_MATRIX_VERIFIED_AND_NON_DRIFTING

Meaning:

-   scheduler certification is correctly enforced
-   composition contract and scaffold behavior are aligned
-   unsupported boundaries remain governed
-   the universal template matrix remains consistent

------------------------------------------------------------------------

# 10. Recommended Next Pipelines

After this verification lane:

    062 — Refresh Universal Template Conformance Coverage for Scheduler-Aware Fixtures

    063 — Verify Scheduler Overlay Discoverability and Operator-Facing Contract Surfaces
