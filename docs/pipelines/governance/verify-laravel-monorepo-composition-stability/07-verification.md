# Verification

Commands executed:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
python tools/governance/template_scaffold.py doctor-composition --overlays django laravel --output json
python tools/governance/template_scaffold.py doctor-composition --overlays service monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker python-package --output json
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Verification outcome:

- `laravel + monorepo` is supported and certified
- placement metadata remains stable at `apps/backend/laravel-app`
- previously codified unsupported Laravel boundaries remain explicitly rejected
- previously certified supported controls remain supported
- governance suite passed without regression
