# Verification Log

## Commands

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler django --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler laravel --output json
python tools/governance/template_scaffold.py doctor-composition --overlays django monorepo scheduler --output json
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -m unittest tests.governance.test_django_native_scheduler_composition tests.governance.test_laravel_native_scheduler_composition tests.governance.test_framework_scheduler_unsupported_boundaries tests.governance.test_template_scheduler_overlay tests.governance.test_template_capability_composition tests.governance.test_template_composition_matrix tests.governance.test_template_composition_drift tests.governance.test_scheduler_scaffold_generation_matrix
python -m unittest discover -s tests/governance -p 'test_*.py'
```

## Results

- `doctor-composition --overlays scheduler django --output json`
  - `supported: true`
  - `reason_code: certified-multi-overlay`
  - `normalized_overlays: ["django", "scheduler"]`
- `doctor-composition --overlays scheduler laravel --output json`
  - `supported: true`
  - `reason_code: certified-multi-overlay`
  - Laravel-native scheduler support unchanged
- `doctor-composition --overlays django monorepo scheduler --output json`
  - `supported: false`
  - `reason_code: unsupported`
  - `rejection_reason: not present in certified composition matrix`
- `verify-composition-matrix --output json`
  - `{ "valid": true, "errors": [] }`
- targeted verification suite
  - `Ran 33 tests ... OK`
- full governance suite
  - `Ran 120 tests ... OK`
