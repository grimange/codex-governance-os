---
name: implementation-contract-audit
description: Audit repository implementation or governance state against a canonical contract and record evidence-based compliance and drift findings.
---

# Implementation Contract Audit

## Purpose

Evaluate whether current repository state conforms to a canonical contract.

## When To Use

- after a canonical contract exists
- when drift or ambiguity needs evidence-based audit
- before remediation planning

## When Not To Use

- when no canonical contract exists
- when the task is only to create the contract

## Inputs

- canonical contract
- architecture doctrine
- relevant implementation or documentation surfaces

## Procedure

1. extract audit criteria from the contract
2. inspect relevant repository surfaces
3. compare evidence to the contract's authority, lifecycle, and interface rules
4. record compliant, partial, and non-compliant findings

## Outputs

- compliance matrix
- audit findings
- documented drift assessment

## Boundaries

This skill audits and records findings. It does not implement remediation.

## Failure Modes

- auditing against inferred rules instead of contract text
- mixing evidence with recommendation without separating them
- failing to identify ambiguous surfaces

## Example Invocation

Use `implementation-contract-audit` to assess whether repository behavior matches a newly authored canonical contract.

## Expected Artifacts Or Deliverables

Audit artifacts, finding summaries, and an explicit promotion or next-step recommendation when needed.
