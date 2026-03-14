# Verification Log

Commands executed:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler laravel --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler django --output json
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -m unittest tests.governance.test_laravel_native_scheduler_composition tests.governance.test_framework_scheduler_unsupported_boundaries tests.governance.test_template_scheduler_overlay tests.governance.test_template_capability_composition tests.governance.test_template_composition_matrix tests.governance.test_template_composition_drift tests.governance.test_scheduler_scaffold_generation_matrix
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Observed results:

- `scheduler + laravel` returned `supported: true`, `reason_code: certified-multi-overlay`
- `scheduler + django` returned `supported: false`, `reason_code: explicitly-rejected`, `conflict_code: framework-native-scheduler-required`
- `verify-composition-matrix --output json` returned `{ "valid": true, "errors": [] }`
- focused Laravel-native scheduler and related suites passed with `Ran 29 tests ... OK`
- full governance suite passed with `Ran 117 tests ... OK`
