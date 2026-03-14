# Verification Log

## Commands

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel monorepo scheduler --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler laravel --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler django --output json
python tools/governance/template_scaffold.py doctor-composition --overlays django monorepo scheduler --output json
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -m unittest tests.governance.test_laravel_monorepo_scheduler_compound_composition tests.governance.test_laravel_native_scheduler_composition tests.governance.test_django_native_scheduler_composition tests.governance.test_framework_scheduler_unsupported_boundaries tests.governance.test_template_scheduler_overlay tests.governance.test_template_capability_composition tests.governance.test_template_composition_matrix tests.governance.test_template_composition_drift tests.governance.test_scheduler_scaffold_generation_matrix
python -m unittest discover -s tests/governance -p 'test_*.py'
```

## Results

- `doctor-composition --overlays laravel monorepo scheduler --output json`
  - `supported: true`
  - `reason_code: certified-multi-overlay`
- `doctor-composition --overlays scheduler laravel --output json`
  - `supported: true`
  - Laravel direct-pair scheduler support unchanged
- `doctor-composition --overlays scheduler django --output json`
  - `supported: true`
  - Django direct-pair scheduler support unchanged
- `doctor-composition --overlays django monorepo scheduler --output json`
  - `supported: false`
  - `reason_code: unsupported`
- `verify-composition-matrix --output json`
  - `{ "valid": true, "errors": [] }`
- targeted verification suite
  - `Ran 36 tests ... OK`
- full governance suite
  - `Ran 125 tests ... OK`
