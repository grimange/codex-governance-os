# Verification

Commands executed:

```bash
python -m unittest tests.governance.test_template_scheduler_overlay tests.governance.test_template_capability_composition tests.governance.test_template_scaffold tests.governance.test_template_composition_matrix tests.governance.test_template_composition_drift
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker python-package --output json
python tools/governance/template_scaffold.py verify-composition-matrix
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python tools/governance/template_scaffold.py list-manifests --output json
python tools/templates/list_templates.py --output json
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Observed results:

- focused scheduler suite passed with `Ran 40 tests ... OK`
- all direct scheduler pair and triple probes returned `reason_code: certified-multi-overlay`
- `verify-composition-matrix` returned `composition-matrix: OK`
- `verify-composition-matrix --output json` returned `{ "valid": true, "errors": [] }`
- manifest inventory and template inventory commands both succeeded with the scheduler overlay present
- full governance suite passed with `Ran 100 tests ... OK`
