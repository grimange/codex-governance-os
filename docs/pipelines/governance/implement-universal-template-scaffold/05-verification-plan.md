# Verification Plan

## Presence Checks

- confirm `docs/codex/templates/base/`, `governance/`, `shared/`, and `overlays/` exist
- confirm overlay directories exist for Laravel, Django, PHP package, Python package, service, and monorepo
- confirm scaffold manifests exist under `docs/codex/templates/manifests/`
- confirm `tools/templates/manifest.schema.json` and `tools/templates/list_templates.py` exist

## Operational Checks

- run governance tests
- run `python tools/templates/list_templates.py --output json`
- run `python tools/governance/template_scaffold.py list-manifests --output json`
- run `python tools/governance/template_scaffold.py realize-repository universal-base <tmp> --overlay django --include-optional`

## Integrity Checks

- confirm realized scaffolds create governance core surfaces
- confirm overlays extend the base scaffold without replacing it
- confirm incompatible or unknown overlays fail closed
