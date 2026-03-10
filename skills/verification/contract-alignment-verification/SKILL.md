---
name: contract-alignment-verification
description: Verify that repository state now conforms to a canonical contract or governed target after remediation or installation work.
---

# Contract Alignment Verification

## Purpose

Confirm whether the governed target is now satisfied by current repository state.

## When To Use

- after remediation work
- after doctrine or contract installation when explicit verification is required
- before promotion decisions that rely on alignment claims

## When Not To Use

- when no governing target exists
- when remediation has not yet been applied or inspected

## Inputs

- governing contract or doctrine
- prior audit or remediation artifacts
- current repository state

## Procedure

1. restate the criteria that must be verified
2. re-inspect relevant repository surfaces
3. classify each criterion as verified, partial, non-compliant, or unverifiable
4. summarize residual risk and promotion readiness

## Outputs

- verification findings
- updated compliance view
- promotion recommendation when applicable

## Boundaries

This skill verifies alignment. It does not author the original contract or implement remediation itself.

## Failure Modes

- asserting verification without evidence
- collapsing residual uncertainty into a false pass
- ignoring unverifiable criteria

## Example Invocation

Use `contract-alignment-verification` to confirm remediation closure before promoting a subsystem as aligned.

## Expected Artifacts Or Deliverables

Verification artifacts, residual-risk notes, and an explicit end-state assessment.
