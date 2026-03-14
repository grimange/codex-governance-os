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

- `python -m unittest discover -s tests/governance -p 'test_*.py'` -> `Ran 39 tests in 1.267s` and `OK`
- supported doctor probe -> `supported: true`, `normalized_overlays: ["cli-worker", "python-package"]`, `reason_code: "certified-multi-overlay"`
- rejected doctor probe -> `supported: false`, `normalized_overlays: ["cli-worker", "laravel"]`, `reason_code: "explicitly-rejected"`, `rejection_reason: "incompatible runtime assumptions"`
- `python tools/templates/list_templates.py --output json` -> succeeded with canonical overlay inventory
- `python tools/governance/template_scaffold.py list-manifests --output json` -> succeeded with canonical manifest inventory

## Consistency Observation

The dedicated surface-consistency test also verified that an identical invalid manifest mutation causes `list-manifests` and `list_templates` to return the same structured failure payload.
