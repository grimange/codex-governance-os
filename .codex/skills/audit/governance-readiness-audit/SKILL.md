---
name: governance-readiness-audit
description: Audit whether repository governance surfaces, doctrine, registry state, and artifact practices are sufficient for governed operation.
---

# Governance Readiness Audit

## Purpose

Evaluate whether a repository is ready to operate as a governed project.

## When To Use

- governance readiness reviews
- template adoption checks
- post-bootstrap governance audits

## When Not To Use

- when auditing implementation against a subsystem contract
- when the task is merely to initialize missing governance surfaces

## Inputs

- constitution
- doctrine documents
- pipeline registry
- pipeline catalog
- existing artifact bundles

## Procedure

1. inspect governance authorities and doctrine presence
2. check pipeline and registry consistency
3. assess artifact bundle completeness and sequencing
4. record gaps, risks, and readiness level

## Outputs

- governance readiness findings
- gap list
- promotion recommendation when needed

## Boundaries

This skill audits governance maturity. It does not perform bootstrap installation or contract-specific compliance work.

## Failure Modes

- confusing active and merely proposed surfaces
- ignoring missing registry entries
- treating incomplete doctrine as sufficient without recording risk

## Example Invocation

Use `governance-readiness-audit` to assess whether a newly bootstrapped repository is ready for deeper governed workflows.

## Expected Artifacts Or Deliverables

Readiness audit findings, risk assessment, and explicit outcome classification.
