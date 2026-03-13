# Migration Plan

## Move Operations

1. Move `registry/templates/` to `docs/governance/registries/templates/`.
2. Move `templates/` to `docs/codex/templates/`.
3. Leave `docs/governance/templates/` in place as the canonical family-definition surface.

## Reference Updates

Update all governance-critical references in:

- `tools/governance/template_registry.py`
- `tools/governance/template_lint.py`
- `AGENTS.md`
- `.codex/AGENTS.md`
- `README.md`
- `docs/governance/architecture-doctrine.md`
- `docs/governance/templates/README.md`
- admitted registry entries
- tests and pipeline artifacts that described the previously admitted locations

## Transition Boundary

No long-lived root-level compatibility shim is retained. The move is a hard cutover inside the same governed change set:

- tooling defaults point only at docs-root paths
- canonical docs describe only docs-root paths
- root-level `registry/` and `templates/` are removed as authority surfaces
