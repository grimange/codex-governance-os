---
name: contract-candidate-discovery
description: Discover, classify, and prioritize candidate canonical contracts from repository authority surfaces, subsystem boundaries, and drift risks.
---

# Contract Candidate Discovery

## Purpose

Identify which repository subsystems or governance surfaces most need a canonical contract.

## When To Use

- before authoring a new canonical contract
- when authority rules are scattered
- when contract planning needs a ranked backlog

## When Not To Use

- when a specific canonical contract has already been selected and scoped
- when the task is purely to audit an existing contract

## Inputs

- architecture doctrine
- discovery artifacts
- governance documents
- existing contracts and ledgers

## Procedure

1. inventory candidate authority surfaces and subsystem boundaries
2. classify current contract state and ambiguity
3. assess governance risk and downstream impact
4. rank candidates and recommend the next contract

## Outputs

- candidate matrix
- ranking rationale
- recommended next contract action

## Boundaries

This skill selects and justifies candidates. It does not fully author the chosen contract.

## Failure Modes

- choosing a candidate without evidence of a real boundary
- ignoring higher-risk fragmented surfaces
- confusing doctrine needs with contract needs

## Example Invocation

Use `contract-candidate-discovery` to build a prioritized contract backlog after architecture doctrine is established.

## Expected Artifacts Or Deliverables

Contract candidate inventory, priority rationale, and recommendation outputs.
