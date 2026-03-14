# Verification

Commands run:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker monorepo python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker monorepo scheduler --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker python-package scheduler --output json
python tools/governance/template_scaffold.py doctor-composition --overlays laravel monorepo scheduler --output json
python tools/governance/template_scaffold.py doctor-composition --overlays django monorepo scheduler --output json
python tools/governance/template_scaffold.py doctor-composition --overlays django cli-worker scheduler --output json
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker scheduler --output json
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -m unittest tests.governance.test_template_composition_drift tests.governance.test_template_composition_matrix tests.governance.test_template_scaffold tests.governance.test_laravel_monorepo_scheduler_compound_composition
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Results:

- targeted enforcement suite -> `Ran 36 tests ... OK`
- full governance suite -> `Ran 126 tests ... OK`
