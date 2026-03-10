# Skill Authoring Standard

## Purpose

This doctrine defines the minimum writing standard for repository-governed Codex skills so skills remain reusable, bounded, and auditable.

## Definitions

- A skill is a reusable operating package that gives Codex a bounded workflow, decision rules, and outputs for a class of tasks.
- A universal skill is a skill intended to be inherited across multiple repositories without relying on one project's business-domain assumptions.

## Required Skill Shape

Each governed skill must live in its own folder and include a `SKILL.md` file with YAML frontmatter containing:

- `name`
- `description`

## Required Sections

Every governed `SKILL.md` should include:

1. purpose
2. when to use
3. when not to use
4. inputs
5. procedure
6. outputs
7. boundaries
8. failure modes
9. example invocation
10. expected artifacts or deliverables when relevant

Sections may be brief, but the skill must still make these elements clear.

## Scope Declaration Rule

- The skill must state what task class it covers.
- The skill must not imply authority over adjacent tasks it does not actually define.
- If the skill assumes a particular governance doctrine, contract, or file location, it should name that dependency explicitly.

## Input And Output Rule

- Inputs must describe the information or repository surfaces the skill expects.
- Outputs must describe the artifacts, decisions, or repository changes the skill is expected to produce.
- Skills that are advisory only should say so explicitly.

## Boundary And Non-Goal Rule

- Each skill must define what remains outside its scope.
- Universal skills must avoid domain-specific business or runtime assumptions unless the skill is explicitly project-local.

## Examples Rule

- Example invocations should be short and representative.
- Examples must demonstrate trigger conditions without turning the skill into a verbose tutorial.

## Writing Quality Rule

- Skills should be concise, operational, and specific.
- Avoid mega-skills with vague responsibilities.
- Prefer progressive disclosure: keep `SKILL.md` lean and use optional bundled resources only when the task genuinely benefits from them.
