# Verification Commands

Commands executed:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler laravel --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler django --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker python-package --output json
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -m unittest tests.governance.test_framework_scheduler_unsupported_boundaries
python -m unittest tests.governance.test_template_scheduler_overlay tests.governance.test_template_composition_matrix tests.governance.test_template_composition_drift
python -m unittest discover -s tests/governance -p 'test_*.py'
```
