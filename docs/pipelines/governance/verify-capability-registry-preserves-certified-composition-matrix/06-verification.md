# Verification

Commands executed:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays service monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
python tools/governance/template_scaffold.py doctor-composition --overlays django laravel --output json
python -m unittest tests.governance.test_template_capability_composition tests.governance.test_template_composition_matrix tests.governance.test_template_composition_drift
python tools/governance/template_scaffold.py verify-composition-matrix
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -c "from tools.governance.template_scaffold import list_scaffold_manifests; from tools.templates.composition_contract import load_template_capability_registry, verify_capability_matrix_preservation; manifests=list_scaffold_manifests(); registry=load_template_capability_registry(); report=verify_capability_matrix_preservation(manifests); print({'capability_count': len(registry.capabilities), 'role_count': len(registry.roles), 'valid': report.valid, 'errors': list(report.errors)})"
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Observed results:

- certified control probes returned `reason_code: certified-multi-overlay`
- explicit unsupported probes returned `reason_code: explicitly-rejected` with the canonical rejection reasons
- targeted capability-preservation suites passed with `Ran 13 tests ... OK`
- `verify-composition-matrix` returned `composition-matrix: OK` and `no drift detected`
- `verify-composition-matrix --output json` returned `{ "valid": true, "errors": [] }`
- capability registry inspection returned `{'capability_count': 12, 'role_count': 6, 'valid': True, 'errors': []}`
- full governance suite passed with `Ran 86 tests ... OK`
