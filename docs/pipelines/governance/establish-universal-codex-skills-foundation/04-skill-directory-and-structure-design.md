# Skill Directory And Structure Design

## Canonical Directory Model

- Universal template skills live under `skills/`.
- Skills are grouped by reusable function such as `skills/discovery/`, `skills/audit/`, `skills/doctrine/`, `skills/contracts/`, `skills/remediation/`, `skills/verification/`, `skills/governance/`, and `skills/bootstrap/`.
- Each individual skill lives in its own folder and must contain a `SKILL.md` file.

## Individual Skill Package Shape

Recommended skill package shape:

`skills/<class>/<skill-name>/SKILL.md`

Optional package contents:

- `references/` for detailed reference material loaded only when needed
- `scripts/` for deterministic helper automation
- `assets/` for reusable templates or artifacts
- `agents/openai.yaml` when UI metadata is later justified

## Naming Rules

- Skill folder names use lowercase ASCII kebab-case.
- Skill names should be short, verb-led or action-specific, and stable once referenced from governance surfaces.
- The folder name is the skill identity; `SKILL.md` is the required instruction surface inside that folder.

## Metadata Model

- Skill metadata lives in the YAML frontmatter of `SKILL.md`.
- Required metadata fields: `name` and `description`.
- Additional metadata is optional and should only be added when a higher-authority or tooling need justifies it.

## Extension And Override Shape

- Project-local extensions or overrides live under `.codex/skills/`.
- Universal template skills remain clean, domain-agnostic, and reusable.
- A project may add local skills without changing the universal library.
- A project may override a universal skill only through documented local precedence rules rather than by silently mutating the universal template definition in place.

## Structure Conclusion

The directory model preserves a stable universal skill root while giving downstream repositories a separate local customization surface.
