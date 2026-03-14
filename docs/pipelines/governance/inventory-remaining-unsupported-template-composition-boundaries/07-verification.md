# Verification

Commands executed:

```bash
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Matrix inventory was derived by evaluating every two-overlay pair through:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays <overlayA> <overlayB> --output json
```

Observed totals:

- overlays: `8`
- unique overlay pairs: `28`
- supported pairs: `7`
- explicit rejections: `2`
- generic unsupported pairs: `19`

Governance verification remained green:

- `python -m unittest discover -s tests/governance -p 'test_*.py'` -> `Ran 70 tests ... OK`
