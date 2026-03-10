---
name: governed-project-bootstrap
description: Install or extend the baseline governance surfaces required to convert a repository into a governed Codex project.
---

# Governed Project Bootstrap

## Purpose

Create the minimum repository surfaces needed for governed Codex operation.

## When To Use

- when initializing a non-governed repository
- when extending a partial bootstrap to the canonical baseline
- when preparing a template-derived project for governed workflows

## When Not To Use

- when the repository is already governance-capable and the task is deeper doctrine or contract work
- when the task is only to audit readiness rather than install the baseline

## Inputs

- repository state
- constitution requirements
- governance doctrine requirements
- pipeline catalog expectations

## Procedure

1. inspect current repository readiness
2. install or normalize constitution, local agent surface, governance docs, pipeline roots, and registry
3. record what was created or left unchanged
4. verify that the repository is governance-capable

## Outputs

- bootstrap surface changes
- initialization artifacts
- explicit governance baseline summary

## Boundaries

This skill establishes the baseline. It does not discover full architecture or author subsystem contracts.

## Failure Modes

- conflating bootstrap with architecture discovery
- omitting registry or doctrine surfaces
- leaving the repository only partially governable without recording the gap

## Example Invocation

Use `governed-project-bootstrap` to convert a standard repository into a governance-capable Codex repository.

## Expected Artifacts Or Deliverables

Installed governance surfaces, initialization records, and baseline verification.
