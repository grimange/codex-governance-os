# Manifest And Runtime Drift Check

Manifest and runtime inventory checks passed:

- `python tools/governance/template_scaffold.py list-manifests --output json`
- `python tools/templates/list_templates.py --output json`

Key observations:

- Laravel now has `compatible_overlays: ["monorepo"]`
- monorepo now includes `laravel` in `compatible_overlays`
- Laravel manifest inventory contains `composition_overrides.monorepo`
- the placement remains `apps/backend/laravel-app`
- no unsupported pair appears accidentally admitted in the manifest inventory

This confirms the matrix expansion is reflected consistently in both manifest-detail and template-summary surfaces.
