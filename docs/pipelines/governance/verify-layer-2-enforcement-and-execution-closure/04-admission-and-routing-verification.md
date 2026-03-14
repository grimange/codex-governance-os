# Admission And Routing Verification

Admission and routing are enforced in the current execution surface:

- `template_scaffold.py` restricts accepted commands explicitly
- unsupported composition requests are rejected through
  `doctor-composition` and `realize-repository`
- drift is surfaced through `verify-composition-matrix`
- registry-backed template operations fail closed when entries are invalid or
  ambiguous

Executed evidence:

- `python tools/governance/template_scaffold.py verify-composition-matrix --output json`
  -> `{ "errors": [], "valid": true }`
- `python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json`
  -> `supported: false`
  -> `reason_code: explicitly-rejected`
  -> `conflict_code: worker-model-collision`
- `python tools/governance/template_registry.py validate`
  -> `{ "entry_count": 6, "errors": [], "valid": true }`

Focused execution-surface tests passed:

- `python -m unittest tests.governance.test_template_scaffold tests.governance.test_template_composition_surface_consistency tests.governance.test_template_registry tests.governance.test_template_composition_drift`
  -> `Ran 42 tests ... OK`

Result: `ADMISSION_AND_ROUTING_VERIFIED`
