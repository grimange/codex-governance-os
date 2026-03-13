---
name: implementation-drift-remediation
description: Design and execute bounded remediation for documented drift against a governing doctrine or canonical contract.
---

# Implementation Drift Remediation

## Purpose

Convert documented drift into a governed remediation path that changes repository state safely and explicitly.

## When To Use

- after audit findings exist
- when drift is already documented and scoped
- when a governed remediation plan is needed

## When Not To Use

- when there is no documented governing target
- when discovery or audit work is still incomplete

## Inputs

- audit findings or drift statement
- governing doctrine or contract
- relevant repository surfaces to change

## Procedure

1. consolidate drift items and risks
2. design a remediation strategy and impact analysis
3. implement bounded changes
4. record post-remediation evidence and residual risk

## Outputs

- remediation plan
- repository changes
- residual drift assessment

## Boundaries

This skill remediates documented drift. It does not substitute for later verification.

## Failure Modes

- changing state without mapping it to documented drift
- hiding residual risk
- treating remediation as verified before evidence exists

## Example Invocation

Use `implementation-drift-remediation` after a contract audit identifies clear drift that must be corrected.

## Expected Artifacts Or Deliverables

Remediation artifacts, changed repository state, and explicit residual-risk notes.
