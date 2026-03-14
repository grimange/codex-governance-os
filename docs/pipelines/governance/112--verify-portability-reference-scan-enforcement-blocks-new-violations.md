---
artifact_bundle: docs/pipelines/governance/verify-portability-reference-scan-enforcement-blocks-new-violations
depends_on:
- 111
governance_type: verification
lane: governance
layer: 0
pipeline: 112
registry_id: governance.portability.verify-portability-reference-scan-enforcement
status: proposed
title: Verify Portability Reference Scan Enforcement Blocks New
  Violations
---

# 112 --- Verify Portability Reference Scan Enforcement Blocks New Violations

## Purpose

Verify that the enforcement mechanism introduced in Pipeline 111
correctly detects and blocks newly introduced machine-local filesystem
references within governed repository surfaces.

This lane proves that the portability enforcement system behaves
**fail‑closed** when a violation is present and **passes cleanly** when
no violations exist.

The verification focuses specifically on the deterministic scan
implemented in:

-   `tools/governance/portability_scan.py`
-   `tools/governance/preflight.py`

------------------------------------------------------------------------

# Background

Pipeline progression for the portability control:

-   **107** --- portability defect discovered
-   **108** --- targeted remediation of machine‑local filesystem links
-   **109** --- Repository Portability Link Invariant established
-   **110** --- remediation verified across governed scope
-   **111** --- deterministic portability scan enforcement implemented

Pipeline 112 verifies that this enforcement actually blocks new
violations.

------------------------------------------------------------------------

# Verification Objectives

This pipeline must demonstrate with evidence that:

1.  A newly introduced non‑portable filesystem reference is detected by
    the scan.
2.  `tools/governance/preflight.py` fails when such a violation exists.
3.  `tools/governance/portability_scan.py scan-active` reports the
    violation.
4.  Removing the violation restores successful execution.
5.  Rule examples and preserved historical evidence are not
    misclassified.

------------------------------------------------------------------------

# Verification Scenario Design

The verification must simulate an intentional violation.

## Step 1 --- Introduce a controlled violation

Create a temporary reference within a governed surface such as:

    /home/example-user/project/file.md

This path must exist only for the purpose of verification.

------------------------------------------------------------------------

## Step 2 --- Execute the portability scan

Run:

    python tools/governance/portability_scan.py scan-active --output json

Expected outcome:

-   the violation appears in scan results
-   the file and pattern are reported

------------------------------------------------------------------------

## Step 3 --- Execute governance preflight

Run:

    python tools/governance/preflight.py

Expected outcome:

-   preflight fails
-   the portability violation is reported

------------------------------------------------------------------------

## Step 4 --- Remediate the violation

Remove or correct the test reference to a portable link form.

------------------------------------------------------------------------

## Step 5 --- Re-run verification

Run the same commands again:

    python tools/governance/portability_scan.py scan-active --output json
    python tools/governance/preflight.py

Expected outcome:

-   no violations detected
-   preflight succeeds

------------------------------------------------------------------------

# Exception Handling Verification

Confirm that the scan **does not falsely trigger** on:

-   rule examples describing forbidden patterns
-   scan definition strings
-   preserved historical artifact evidence

These must be classified correctly rather than treated as violations.

------------------------------------------------------------------------

# Verification Scope

The scan must inspect the following governed surfaces:

-   governance doctrine
-   contracts
-   architecture documentation
-   pipeline definitions
-   pipeline registry
-   README and repository entry surfaces
-   `.codex/AGENTS.md`

Historical artifact bundles may contain preserved evidence and should be
classified accordingly.

------------------------------------------------------------------------

# Required Outputs

Create an artifact bundle at:

    docs/pipelines/governance/verify-portability-reference-scan-enforcement-blocks-new-violations/

The bundle must contain at minimum:

    01-problem-statement.md
    02-verification-plan.md
    03-controlled-violation-test.md
    04-scan-detection-results.md
    05-preflight-failure-verification.md
    06-remediation-and-retest.md
    07-exception-classification-check.md
    08-final-verdict.md

------------------------------------------------------------------------

# Verification Evidence

Evidence should include:

-   scan output logs
-   preflight failure output
-   preflight success output after remediation
-   classification of any detected matches

------------------------------------------------------------------------

# Acceptance Criteria

The verification succeeds only if:

-   the portability scan detects the controlled violation
-   preflight fails when the violation exists
-   the violation disappears after remediation
-   enforcement behavior aligns with the Repository Portability Link
    Invariant

------------------------------------------------------------------------

# Restriction Handling

Restrictions may be recorded if:

-   enforcement exists only in preflight and not in automatic admission
    hooks
-   some repository surfaces are excluded from scan scope
-   deterministic scan patterns require refinement

Restrictions must be evidence‑based.

------------------------------------------------------------------------

# Final Verdict

The final verdict must be one of:

    PORTABILITY_REFERENCE_SCAN_ENFORCEMENT_VERIFIED
    PORTABILITY_REFERENCE_SCAN_ENFORCEMENT_VERIFIED_WITH_RESTRICTIONS
    PORTABILITY_REFERENCE_SCAN_ENFORCEMENT_FAILED

------------------------------------------------------------------------

# Expected Outcome

Successful completion of this pipeline confirms that:

-   the portability invariant is actively enforced
-   the governance system blocks new machine‑local filesystem references
-   repository portability protections operate deterministically

This establishes a **complete governance loop** for portability
violations: detection → remediation → invariant → verification →
enforcement → enforcement verification.
