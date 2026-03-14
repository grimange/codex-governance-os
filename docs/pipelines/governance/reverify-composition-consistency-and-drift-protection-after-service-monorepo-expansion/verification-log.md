# Verification Log

## Commands

```bash
python -m unittest discover -s tests/governance -p 'test_*.py'
python tools/governance/template_scaffold.py doctor-composition --overlays service monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
```

## Results

- `python -m unittest discover -s tests/governance -p 'test_*.py'` -> `Ran 66 tests in 4.182s` and `OK`
- `python tools/governance/template_scaffold.py doctor-composition --overlays service monorepo --output json` -> `supported: true`, `reason_code: "certified-multi-overlay"`
- `python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json` -> `supported: false`, `reason_code: "explicitly-rejected"`
- `python tools/templates/list_templates.py --output json` -> succeeded with the twice-expanded compatibility inventory
- `python tools/governance/template_scaffold.py list-manifests --output json` -> succeeded with both Django and service monorepo placement override metadata
