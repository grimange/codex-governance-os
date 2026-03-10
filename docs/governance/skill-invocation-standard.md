# Skill Invocation Standard

## Purpose

This doctrine defines how governed repositories decide when to use a skill, how skills are referenced, and how universal and project-local skills interact.

## Applicability Decision

Codex should invoke a skill when:

- the user explicitly requests a skill by name
- a governance pipeline or doctrine explicitly references the skill
- the task clearly matches the skill's defined task class and boundaries

A skill should not be invoked merely because it overlaps vaguely with the request.

## Reference Model

- Governance documents may reference skills by folder identity, for example `repository-discovery` or `pipeline-registry-reconciliation`.
- References should point to the skill's canonical folder under `skills/` or `.codex/skills/`.
- Pipelines should use skill references to avoid restating reusable procedures inline once the skill exists.

## Precedence Rules

Conflict resolution order for skill selection is:

1. explicit user-requested skill
2. applicable project-local skill under `.codex/skills/`
3. applicable universal skill under `skills/`
4. direct repository reasoning without a skill when no skill is a clean fit

## Universal Skill First-Use Conditions

Use a universal skill first when:

- the task matches a universal governance workflow
- no project-local specialization is required
- invoking the universal skill avoids duplicated baseline reasoning

## Local Override Conditions

A project-local skill may override a universal skill only when:

- the project has repository-specific constraints, terminology, or file layouts
- the override preserves the higher-authority governance doctrine
- the override is explicit and discoverable under `.codex/skills/`

## Anti-Duplication Rules

- Do not invoke multiple skills that solve the same task class without a clear decomposition reason.
- If work spans multiple task classes, decompose the workflow into bounded skill uses rather than inventing one broad synthetic skill.
- Do not keep duplicating stable skill logic in pipelines once a canonical governed skill exists.

## Orchestrator Rule

Pipelines, doctrines, and agent instructions may route work toward a skill, but the orchestrating surface must still preserve authority ordering, artifact expectations, and explicit promotion or verification requirements when applicable.
