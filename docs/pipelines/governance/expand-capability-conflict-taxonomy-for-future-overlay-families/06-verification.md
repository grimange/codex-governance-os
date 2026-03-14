# Verification

Commands executed:

```bash
python -m unittest tests.governance.test_template_capability_conflicts tests.governance.test_template_capability_composition tests.governance.test_laravel_cli_worker_unsupported_boundary tests.governance.test_template_scaffold
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
python tools/governance/template_scaffold.py doctor-composition --overlays django laravel --output json
python tools/governance/template_scaffold.py verify-composition-matrix
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Observed results:

- focused taxonomy suite passed with `Ran 35 tests ... OK`
- `doctor-composition --overlays laravel cli-worker --output json`
  - `reason_code: explicitly-rejected`
  - `conflict_code: worker-model-collision`
- `doctor-composition --overlays django laravel --output json`
  - `reason_code: explicitly-rejected`
  - `conflict_code: cross-framework-application-collision`
- `verify-composition-matrix` returned `composition-matrix: OK`
- full governance suite passed with `Ran 93 tests ... OK`
