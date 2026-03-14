# Verification

Commands executed:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays service monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
python tools/governance/template_scaffold.py doctor-composition --overlays django laravel --output json
python tools/governance/template_scaffold.py list-manifests --output json
python tools/templates/list_templates.py --output json
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Verification outcome:

- supported compositions remain certified
- unsupported compositions remain explicitly rejected
- canonical rejection reasons remain consistent
- scaffold enforcement matches matrix truth
- documentation aligns with tests and runtime behavior
