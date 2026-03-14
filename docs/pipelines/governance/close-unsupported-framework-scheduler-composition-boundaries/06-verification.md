# Verification

Commands executed:

```bash
python -m unittest tests.governance.test_framework_scheduler_unsupported_boundaries tests.governance.test_template_scheduler_overlay tests.governance.test_template_capability_conflicts tests.governance.test_template_capability_composition tests.governance.test_template_composition_matrix tests.governance.test_template_composition_drift
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler laravel --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler django --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker --output json
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Observed results:

- focused boundary and scheduler suites passed with `Ran 28 tests ... OK`
- `scheduler + laravel` returned `reason_code: explicitly-rejected`, `conflict_code: framework-native-scheduler-required`, `rejection_reason: missing Laravel-native scheduler composition contract`
- `scheduler + django` returned `reason_code: explicitly-rejected`, `conflict_code: framework-native-scheduler-required`, `rejection_reason: missing Django-native scheduler composition contract`
- supported control `scheduler + cli-worker` remained `certified-multi-overlay`
- `verify-composition-matrix --output json` returned `{ "valid": true, "errors": [] }`
- full governance suite passed with `Ran 113 tests ... OK`
