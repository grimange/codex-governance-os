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

- `python -m unittest discover -s tests/governance -p 'test_*.py'` -> `Ran 36 tests in 0.445s` and `OK`
- supported doctor probe returned:
  - `supported: true`
  - `normalized_overlays: ["cli-worker", "python-package"]`
  - `decision_source: "docs/contracts/universal-template-composition-contract.md"`
- unsupported doctor probe returned:
  - `supported: false`
  - `normalized_overlays: ["cli-worker", "laravel"]`
  - `rejection_reason: "incompatible runtime assumptions"`
  - `closest_supported` suggestions rooted in the certified matrix
- manifest listing and template listing remained aligned with the certified contract
