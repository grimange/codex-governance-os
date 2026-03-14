# Verification

Commands executed:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays service monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker monorepo python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
python tools/governance/template_scaffold.py doctor-composition --overlays django laravel --output json
python -c "import json, pathlib; payload=json.loads(pathlib.Path('tools/governance/template_composition_matrix.json').read_text()); print(['cli-worker','monorepo','python-package'] in payload['supported'])"
python tools/governance/template_scaffold.py verify-composition-matrix
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Observed results:

- all four certified pair controls returned `reason_code: certified-multi-overlay`
- the certified triple control returned `reason_code: certified-multi-overlay`
- both explicit unsupported controls returned `reason_code: explicitly-rejected` with their canonical reasons
- snapshot inspection returned `True` for the triple entry
- `verify-composition-matrix` returned `composition-matrix: OK`
- `verify-composition-matrix --output json` returned `{ "valid": true, "errors": [] }`
- governance suite passed with `Ran 88 tests ... OK`
