# Scaffold Contract

The canonical scaffold contract is published in [docs/governance/template-scaffold-contract.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/template-scaffold-contract.md).

## Naming And Composition Rules

- base scaffold manifest: `universal-base`
- overlay manifests: stack or topology names such as `django`, `laravel`, `python-package`, `service`, and `monorepo`
- manifests are machine-readable JSON files under `docs/codex/templates/manifests/`
- each overlay declares the base template it extends

## Extension Restrictions

- overlays may add runtime directories
- overlays may not move governance core directories
- projects may add realization-specific surfaces, but they may not silently repurpose the governance core
