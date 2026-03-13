# Docs And Manifest Consistency Report

## Surfaces Checked

- `docs/codex/templates/README.md`
- `docs/governance/template-scaffold-contract.md`
- `docs/codex/templates/manifests/node-typescript-service.json`
- `docs/codex/templates/manifests/cli-worker.json`
- `docs/codex/templates/overlays/node-typescript-service/README.md`
- `docs/codex/templates/overlays/cli-worker/README.md`
- `tools/governance/template_scaffold.py`
- `tools/templates/list_templates.py`

## Result

No mismatch detected.

Current docs and manifests consistently claim:

- the new overlays are supported
- supported compositions are explicit
- unsupported combinations fail closed

Observed scaffold behavior matched those claims.
