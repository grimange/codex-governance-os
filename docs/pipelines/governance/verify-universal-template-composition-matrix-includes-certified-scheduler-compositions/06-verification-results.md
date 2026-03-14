# Verification Results

Commands executed:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler laravel --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler django --output json
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -m unittest tests.governance.test_template_scheduler_overlay
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Observed results:

- `scheduler` returned `supported: true` and `reason_code: single-overlay`
- all certified scheduler multi-overlay combinations returned `supported: true` and `reason_code: certified-multi-overlay`
- `scheduler + laravel` and `scheduler + django` remained rejected with `reason_code: unsupported`
- `verify-composition-matrix --output json` returned `{ "valid": true, "errors": [] }`
- `python -m unittest tests.governance.test_template_scheduler_overlay` passed with `Ran 4 tests ... OK`
- `python -m unittest discover -s tests/governance -p 'test_*.py'` passed with `Ran 107 tests ... OK`
