# Implementation Plan

## Implemented Surfaces

- scaffold layer documentation under `docs/codex/templates/`
- stack and topology overlay stubs under `docs/codex/templates/overlays/`
- machine-readable scaffold manifests under `docs/codex/templates/manifests/`
- scaffold contract doctrine under `docs/governance/template-scaffold-contract.md`
- manifest schema under `tools/templates/manifest.schema.json`
- manifest discovery helper under `tools/templates/list_templates.py`
- repository scaffold realization support in `tools/governance/template_scaffold.py`

## Realization Model

The scaffold tool now supports:

- governed document scaffolding
- manifest inventory listing
- repository scaffold realization from a base manifest plus selected overlays

The realization flow records the selected scaffold under `docs/governance/scaffold-selection.json` in the generated repository root.
