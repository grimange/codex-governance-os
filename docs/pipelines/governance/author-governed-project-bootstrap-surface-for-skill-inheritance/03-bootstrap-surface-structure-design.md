# Bootstrap Surface Structure Design

## Canonical Structure

- Primary bootstrap guide: `docs/bootstrap/governed-project-bootstrap.md`
- Skill inheritance guide: `docs/bootstrap/skill-inheritance-model.md`
- Local override guide: `docs/bootstrap/local-override-model.md`
- Minimal setup checklist: `docs/bootstrap/minimal-setup-checklist.md`
- Example repository layout: `docs/bootstrap/example-governed-repository-layout.md`

## Reference Model

- The primary bootstrap guide is the entry point.
- The skill inheritance guide explains universal and local skill boundaries.
- The local override guide explains what a future repository may specialize locally.
- The checklist converts the model into an adoption sequence.
- The example layout provides a generic structural reference for future repositories.

## Discoverability Integration

- `AGENTS.md` should route bootstrap guidance to `docs/bootstrap/`.
- `.codex/AGENTS.md` should treat `docs/bootstrap/` as the canonical adoption surface.
- The pipeline registry should list this pipeline as an active governance surface so the bootstrap model is discoverable from the registry path.
