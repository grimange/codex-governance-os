# Override And Extension Model

## Universal Versus Local Boundary

- Universal baseline skills stay under `skills/` and must remain domain-agnostic.
- Repository-specific skills, local refinements, or domain narrowings belong under `.codex/skills/`.

## Override Model

- Local skills may override universal skills only through explicit precedence defined in `docs/governance/skill-invocation-standard.md`.
- A local override should preserve higher-authority governance doctrine and should narrow behavior for repository-specific needs rather than replace baseline governance law.

## Collision Prevention

- Reuse the universal skill name only when the local skill is a deliberate override.
- Use a distinct name when the local skill is an additional specialization rather than a replacement.
- Keep skill folders in kebab-case and class-aligned to preserve discoverability.

## Safe Extension Rule

- Add domain-specific behavior locally instead of editing universal skills in place.
- Extend the universal library only when the new behavior is clearly reusable across future repositories.

## Deprecation Handling

- Do not silently delete or rename a published universal skill that pipelines or governance docs may reference.
- If a universal skill becomes obsolete, mark the supersession in governance documentation and introduce the replacement cleanly.

## Cleanliness Goal

This model allows real project specialization without polluting the template repository's universal skill foundation with one-off local behavior.
