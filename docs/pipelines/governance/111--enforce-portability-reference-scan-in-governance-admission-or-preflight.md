---
artifact_bundle: docs/pipelines/governance/enforce-portability-reference-scan-in-governance-admission-or-preflight
depends_on:
- 109
- 110
governance_type: enforcement
lane: governance
layer: 0
pipeline: 111
registry_id: governance.portability.enforce-portability-reference-scan
status: proposed
title: Enforce Portability Reference Scan In Governance Admission Or
  Preflight
---

# 111 --- Enforce Portability Reference Scan In Governance Admission Or Preflight

## Purpose

Introduce a **fail‑closed enforcement gate** that prevents new
machine‑local filesystem references from entering governed repository
surfaces.

Pipelines 108--110 remediated the original defect, established the
Repository Portability Link Invariant, and verified that governed
surfaces are currently clean. This lane converts that invariant into
**active governance enforcement**.

Once implemented, the governance system must automatically detect and
block new portability violations during **pipeline admission or
preflight checks**.

------------------------------------------------------------------------

# Background

Previous pipelines established the following progression:

-   **107** --- verification surfaced a non‑portable filesystem path
-   **108** --- remediation replaced machine‑local links with portable
    ones
-   **109** --- Repository Portability Link Invariant established
-   **110** --- verification confirmed remediation across governed scope

However, the repository still relies on **manual verification**. Without
automated enforcement, future pipelines could accidentally reintroduce
non‑portable references.

Pipeline 111 closes this gap by introducing an **automated scan gate**.

------------------------------------------------------------------------

# Portability Enforcement Rule

Machine‑local filesystem references must never appear in governed
repository surfaces.

The enforcement scan must detect patterns including (but not limited
to):

    /home/
    /Users/
    C:\
    file://
    ~/

These patterns represent workstation‑specific paths and violate
repository template portability.

------------------------------------------------------------------------

# Enforcement Model

The governance system must perform a **deterministic repository scan**
during one of the following stages:

-   governance **preflight**
-   governance **lane admission**
-   governance **run‑lane validation**

If forbidden patterns appear in governed surfaces, the governance system
must treat them as **portability violations**.

------------------------------------------------------------------------

# Exception Classification

Certain appearances of these patterns must be **explicitly allowed**
when they represent rule definitions or preserved evidence.

Allowed classifications include:

### Rule Examples

Examples appearing inside governance doctrine that explain the rule.

### Scan Definitions

Patterns appearing as literal strings used by scanning logic.

### Historical Evidence

Artifact bundles preserving past defects for governance audit purposes.

These exceptions must be explicitly classified rather than silently
ignored.

------------------------------------------------------------------------

# Failure Behavior

If a new machine‑local filesystem reference appears in an active
governed surface, the governance system must:

1.  classify the match as a portability violation
2.  block the pipeline admission or execution
3.  report the offending file and pattern
4.  require remediation before the lane can execute

This behavior enforces **fail‑closed governance**.

------------------------------------------------------------------------

# Enforcement Scope

The scan must inspect the following repository surfaces when present:

-   governance doctrine files
-   contracts
-   architecture documentation
-   pipeline definitions
-   pipeline registry
-   README and entry surfaces
-   Codex discovery surfaces such as `.codex/AGENTS.md`

Artifact bundles may be excluded when they represent historical
evidence.

------------------------------------------------------------------------

# Required Outputs

Create an artifact bundle at:

    docs/pipelines/governance/enforce-portability-reference-scan-in-governance-admission-or-preflight/

The bundle must include at minimum:

    01-problem-statement.md
    02-enforcement-model.md
    03-forbidden-pattern-definition.md
    04-exception-classification-rules.md
    05-governance-integration-plan.md
    06-verification.md
    07-final-verdict.md

------------------------------------------------------------------------

# Required Repository Work

## 1. Implement deterministic scan logic

Add repository scanning logic capable of detecting forbidden patterns
within governed surfaces.

The scan must be deterministic and reproducible.

------------------------------------------------------------------------

## 2. Integrate enforcement into governance flow

The scan must run automatically during either:

-   governance preflight
-   lane admission
-   run‑lane validation

The exact integration point must be documented.

------------------------------------------------------------------------

## 3. Define exception handling

Introduce classification rules allowing:

-   rule examples
-   scan definitions
-   historical artifact evidence

These exceptions must be explicitly documented.

------------------------------------------------------------------------

## 4. Record enforcement behavior

Document the expected blocking behavior when violations occur and ensure
error messages provide sufficient remediation guidance.

------------------------------------------------------------------------

# Verification Requirements

Verification must confirm:

1.  the scan detects forbidden filesystem patterns
2.  the scan executes during governance preflight or admission
3.  the governance system blocks new violations
4.  exception classifications prevent false positives
5.  enforcement aligns with the Repository Portability Link Invariant

------------------------------------------------------------------------

# Final Verdict

The final verdict must be one of:

    PORTABILITY_REFERENCE_SCAN_ENFORCEMENT_ESTABLISHED
    PORTABILITY_REFERENCE_SCAN_ENFORCEMENT_ESTABLISHED_WITH_RESTRICTIONS
    PORTABILITY_REFERENCE_SCAN_ENFORCEMENT_NOT_ESTABLISHED

------------------------------------------------------------------------

# Expected Outcome

After this pipeline:

-   new portability violations are automatically detected
-   governance admission fails closed for machine‑local path references
-   the repository remains safe as a reusable governance OS template
-   portability protection becomes a permanent enforcement rule
