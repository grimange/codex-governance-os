# Scaffold Realization Verification

The full supported matrix was re-checked through scaffold realization.

Key observations:

- `service + monorepo` now realizes the canonical nested service under `services/service-app/`
- `django + monorepo` continues to realize under `apps/backend/django-service/`
- previously supported combinations such as `node-typescript-service + monorepo` and `cli-worker + python-package` still realize successfully
- no supported composition regressed to rejection
- no rejected composition became scaffold-admissible

The dedicated regression suite for this lane is `tests/governance/test_template_composition_matrix_service_monorepo_expansion.py`.
