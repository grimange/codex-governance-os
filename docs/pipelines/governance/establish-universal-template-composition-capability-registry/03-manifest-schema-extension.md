# Manifest Schema Extension

All scaffold manifests under [docs/codex/templates/manifests](/home/ramjf/python-projects/codex-governance-os/docs/codex/templates/manifests) now declare a `capabilities` object with:

- `provides`
- `requires`
- `conflicts`
- `composition_role`

These declarations are loaded by [template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_scaffold.py) and validated against the governed registry before manifest inventory is admitted.
