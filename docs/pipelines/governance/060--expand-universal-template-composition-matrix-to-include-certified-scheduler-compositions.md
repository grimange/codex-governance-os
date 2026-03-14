# 060 --- Expand Universal Template Composition Matrix to Include Certified Scheduler Compositions

## Frontmatter

``` yaml
pipeline_id: 060
registry_id: governance.templates.expand-universal-template-composition-matrix-to-include-certified-scheduler-compositions
title: Expand Universal Template Composition Matrix to Include Certified Scheduler Compositions
stage: implementation
governance_domain: templates
pipeline_type: expansion
status: proposed
created_by: codex
requires:
  - 027
  - 058
  - 059
produces:
  - scheduler-certified-composition-matrix
  - scheduler-supported-overlay-contract
  - scheduler-overlay-boundary-definition
verification:
  - composition-matrix-verification
  - unsupported-boundary-verification
```

------------------------------------------------------------------------

# 1. Problem Statement

Pipelines **058** and **059** verified that the `scheduler` overlay:

-   generates deterministic scaffold surfaces
-   enforces drift-safe generated regions
-   passes scaffold generation matrix verification

However, the **scheduler overlay is not yet registered as a certified
participant in the universal template composition matrix**.

Without this step:

-   the governance template system cannot treat scheduler as an
    officially supported overlay
-   composition verification cannot reason about scheduler combinations
-   operator documentation cannot rely on scheduler composition truth

Therefore scheduler must be formally integrated into the **universal
template composition contract**.

------------------------------------------------------------------------

# 2. Governance Objective

Promote the `scheduler` overlay from **verified scaffold
implementation** to **certified template composition participant**
within the governance OS template system.

After this pipeline:

The template engine will explicitly recognize scheduler as part of the
supported overlay ecosystem.

------------------------------------------------------------------------

# 3. Target Certified Scheduler Compositions

The following compositions become **officially supported**.

### Base scheduler

    scheduler

### Scheduler with CLI worker

    scheduler + cli-worker

### Scheduler with monorepo

    scheduler + monorepo

### Scheduler with python package

    scheduler + python-package

### Combined compositions

    scheduler + cli-worker + monorepo
    scheduler + cli-worker + python-package

These combinations must be added to the **composition matrix truth
source**.

------------------------------------------------------------------------

# 4. Explicit Unsupported Scheduler Boundaries

The governance system must also record **unsupported combinations**.

Examples:

    scheduler + laravel
    scheduler + django
    scheduler + node-typescript-service
    scheduler + php-package

Unsupported combinations must:

-   fail closed
-   return explicit reason codes
-   never degrade silently

Example response:

``` json
{
  "supported": false,
  "reason_code": "unsupported-overlay-combination"
}
```

------------------------------------------------------------------------

# 5. Required Repository Changes

## 5.1 Update Composition Matrix Truth

Update the canonical composition contract used by:

    template_scaffold.py
    verify-composition-matrix
    doctor-composition

Add scheduler overlay participation.

Example logical structure:

``` python
SUPPORTED_OVERLAY_COMPOSITIONS = [

  ["scheduler"],

  ["scheduler", "cli-worker"],

  ["scheduler", "monorepo"],

  ["scheduler", "python-package"],

  ["scheduler", "cli-worker", "monorepo"],

  ["scheduler", "cli-worker", "python-package"]

]
```

------------------------------------------------------------------------

## 5.2 Update Template Documentation

Update the template documentation surface.

Example location:

    docs/codex/templates/README.md

Add scheduler overlay documentation:

    Scheduler Overlay

    Purpose:
    Provides governed background job scheduling infrastructure.

    Generated Surfaces:

    schedule.py
    scheduler_runtime.py

    Supported Compositions:

    scheduler
    scheduler + cli-worker
    scheduler + monorepo
    scheduler + python-package
    scheduler + cli-worker + monorepo
    scheduler + cli-worker + python-package

------------------------------------------------------------------------

## 5.3 Update Operator Discoverability

Ensure operator tooling surfaces scheduler.

Example commands:

    python tools/governance/template_scaffold.py list-overlays

Expected result includes:

    scheduler

------------------------------------------------------------------------

# 6. Governance Boundary Definition

Scheduler overlay responsibilities:

-   periodic job execution
-   background scheduling orchestration
-   execution boundary separation

Scheduler must **not**:

-   replace queue workers
-   replace runtime application loops
-   integrate directly with unsupported frameworks

This boundary prevents scheduler misuse across stacks.

------------------------------------------------------------------------

# 7. Verification Plan

Verification must prove that scheduler compositions are correctly
registered.

### Test 1 --- Supported Composition

    python tools/governance/template_scaffold.py doctor-composition   --overlays scheduler cli-worker

Expected:

    supported: true
    reason_code: certified-multi-overlay

------------------------------------------------------------------------

### Test 2 --- Unsupported Framework Pair

    python tools/governance/template_scaffold.py doctor-composition   --overlays scheduler laravel

Expected:

    supported: false
    reason_code: unsupported-overlay-combination

------------------------------------------------------------------------

### Test 3 --- Composition Matrix Validation

    python tools/governance/template_scaffold.py verify-composition-matrix

Expected:

``` json
{
  "valid": true,
  "errors": []
}
```

------------------------------------------------------------------------

### Test 4 --- Governance Test Suite

    python -m unittest discover -s tests/governance -p "test_*.py"

Expected:

    All tests passing

------------------------------------------------------------------------

# 8. Artifact Bundle

Pipeline artifacts must be recorded under:

    docs/pipelines/governance/expand-universal-template-composition-matrix-to-include-certified-scheduler-compositions/

Required artifacts:

    01-problem-statement.md
    02-current-composition-matrix.md
    03-expanded-scheduler-composition-matrix.md
    04-supported-composition-specification.md
    05-unsupported-boundary-definition.md
    06-verification-plan.md
    07-verification-results.md
    08-final-verdict.md

------------------------------------------------------------------------

# 9. Final Verdict

Expected verdict:

    SCHEDULER_OVERLAY_CERTIFIED_IN_UNIVERSAL_TEMPLATE_COMPOSITION_MATRIX

Meaning:

-   scheduler is now a **first-class overlay**
-   the universal composition matrix includes scheduler
-   unsupported combinations are explicitly governed
-   the template engine can safely reason about scheduler compositions

------------------------------------------------------------------------

# 10. Recommended Follow-Up Pipelines

Next governance pipelines:

    061 — Verify Universal Template Composition Matrix Includes Certified Scheduler Compositions

    062 — Refresh Universal Template Conformance Coverage for Scheduler-Aware Fixtures

    063 — Verify Scheduler Overlay Discoverability and Operator-Facing Contract Surfaces
