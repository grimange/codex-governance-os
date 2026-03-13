---
name: architecture-doctrine-authoring
description: Author or refine repository architecture doctrine from evidence-backed authority, structure, and source-of-truth analysis.
---

# Architecture Doctrine Authoring

## Purpose

Create an evidence-based architecture doctrine that explains what the repository actually implements and how authority should be interpreted.

## When To Use

- after repository discovery
- when architecture doctrine is missing, weak, or stale
- when major repository architecture changes require doctrine revision

## When Not To Use

- when the task is a narrow contract authoring problem
- when no meaningful repository evidence exists yet beyond bootstrap placeholders

## Inputs

- discovery findings
- constitution
- existing doctrine
- pipeline catalog and artifact evidence

## Procedure

1. identify the repository's actual implemented model
2. define authority precedence and source-of-truth rules
3. describe major layers, responsibilities, and compatibility zones
4. state governance implications and non-goals clearly

## Outputs

- canonical architecture doctrine
- explicit authority model
- documented boundaries and caveats

## Boundaries

This skill authors repository architecture doctrine, not project-domain business architecture that lacks evidence.

## Failure Modes

- inventing runtime layers the repository does not contain
- overstating placeholders as canonical systems
- leaving authority ordering ambiguous

## Example Invocation

Use `architecture-doctrine-authoring` after discovery to establish the canonical interpretation layer for repository structure.

## Expected Artifacts Or Deliverables

An updated or newly authored architecture doctrine and supporting integration notes when needed.
