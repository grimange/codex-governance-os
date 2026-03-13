---
name: pipeline-registry-reconciliation
description: Reconcile active pipeline definitions with the pipeline registry so governance discoverability remains accurate and deterministic.
---

# Pipeline Registry Reconciliation

## Purpose

Keep the pipeline registry aligned with the active pipeline catalog.

## When To Use

- when activating a new pipeline
- when auditing registry completeness
- when normalizing stale pipeline identity or path data

## When Not To Use

- when the task is to design pipeline logic rather than registry state
- when the repository does not use a pipeline registry

## Inputs

- pipeline registry
- active pipeline definitions
- registry-integrity contract

## Procedure

1. identify operationally active pipelines
2. compare registry entries to pipeline IDs, names, categories, and paths
3. add or correct entries as needed
4. record any residual mismatches such as stale status text in pipeline bodies

## Outputs

- updated pipeline registry
- reconciliation findings
- residual normalization notes

## Boundaries

This skill governs registry discoverability. It does not replace pipeline-internal doctrine or artifact standards.

## Failure Modes

- treating registry silence as proof of inactivity
- creating duplicate entries
- allowing identity drift between filename, body, and registry

## Example Invocation

Use `pipeline-registry-reconciliation` whenever a governance pipeline becomes operationally active.

## Expected Artifacts Or Deliverables

Registry updates and explicit notes about any remaining catalog inconsistencies.
