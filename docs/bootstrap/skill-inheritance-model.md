# Skill Inheritance Model

## Purpose

This guide defines how a future governed repository inherits universal skills from the template and introduces project-local skills without duplicating reusable behavior.

## Universal Skills

Universal skills are reusable workflow packages supplied by the template for common governance task classes such as discovery, audit, doctrine authoring, contract work, remediation, verification, registry reconciliation, and bootstrap installation.

They remain generic and should stay suitable for multiple repositories.

## Inheritance Rules

- A new governed repository inherits the universal skill library as its default reusable behavior surface.
- Pipelines should reference inherited skills by canonical identity rather than restating stable procedures inline.
- The skill invocation standard decides when a skill is applicable and which surface has precedence.

## Local Skill Introduction

Add a local skill only when at least one of these is true:

- the repository has project-specific terminology or file layout
- the repository needs a bounded extension of a universal workflow
- the repository needs an explicit override that remains discoverable under `.codex/skills/`

Do not create a local skill merely to restate a universal workflow with different wording.

## Universal Versus Local Choice

- Prefer a universal skill when the task matches a generic governance workflow.
- Prefer a local skill when repository-specific constraints materially change the procedure.
- Keep local skills narrow so the inherited universal layer remains the default baseline.

## Anti-Duplication Rules

- Do not clone a universal skill into project-local space without a repository-specific reason.
- Do not let multiple skills compete for the same task class unless the boundary is explicit.
- When a pipeline uses inherited skills, keep artifact and verdict requirements in the pipeline itself.

## Pipeline Reference Model

Pipelines may reference inherited skills for reusable operations such as repository discovery, governed bootstrap, registry reconciliation, or contract alignment verification. The pipeline still owns:

- scope
- required outputs
- verification requirements
- promotion decisions
