# Verification Log

## Commands

```bash
python -m unittest discover -s tests/governance -p 'test_*.py'
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
```

## Results

- `python -m unittest discover -s tests/governance -p 'test_*.py'` -> `Ran 42 tests in 1.314s` and `OK`
- supported doctor probe -> `supported: true`, `reason_code: "certified-multi-overlay"`
- rejected doctor probe -> `supported: false`, `reason_code: "explicitly-rejected"`, `rejection_reason: "incompatible runtime assumptions"`
- `python tools/templates/list_templates.py --output json` -> succeeded with canonical overlay inventory
- `python tools/governance/template_scaffold.py list-manifests --output json` -> succeeded with canonical manifest inventory

## Drift Simulation Outcome

The new drift tests confirmed that:

- a temporary contract document that adds an undocumented rejected pair is classified as `CONTRACT_DRIFT_DETECTED`
- a temporary manifest inventory that declares `laravel + cli-worker` is classified as `CONTRACT_DRIFT_DETECTED`
