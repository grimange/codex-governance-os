---
name: repository-discovery
description: Discover repository structure, authority surfaces, implementation evidence, and boundary candidates before doctrine, contract, or audit work.
---

# Repository Discovery

## Purpose

Produce a structured view of repository state before downstream governance decisions are made.

## When To Use

- initialization or bootstrap analysis
- architecture discovery
- contract candidate discovery
- governance evidence inventory

## When Not To Use

- when the task is purely remediation against already documented findings
- when a narrower audit skill is a cleaner fit

## Inputs

- current repository tree
- governance documents
- relevant pipeline definitions

## Procedure

1. inventory the repository surfaces relevant to the task
2. separate direct evidence from inference
3. identify authority surfaces, placeholders, and ambiguity
4. summarize discovered boundaries and risks

## Outputs

- evidence inventory
- boundary or authority summary
- explicit unknowns

## Boundaries

This skill discovers and summarizes. It does not author final doctrine or contracts by itself.

## Failure Modes

- treating placeholders as implemented systems
- inferring authority without evidence
- skipping higher-authority governance surfaces

## Example Invocation

Use `repository-discovery` to inventory the repository before authoring architecture doctrine.

## Expected Artifacts Or Deliverables

Discovery sections or artifacts that distinguish evidence, inference, and unresolved ambiguity.
