# Matrix Consistency Report

## Supported Cases

The expanded matrix remains aligned across:

- `tools/templates/composition_contract.py`
- `template_scaffold.py doctor-composition`
- `template_scaffold.py realize-repository`
- `template_scaffold.py list-manifests`
- `tools/templates/list_templates.py`
- drift detection tests

## Rejected Cases

The remaining explicit rejections remain aligned across the same surfaces.

## Regression Outcome

No previously supported composition regressed.

No rejected composition was admitted accidentally after the `django + monorepo` promotion.

The matrix remains deterministic and fail-closed.
