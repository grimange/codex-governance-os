# Verification

Commands executed:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays service monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker monorepo python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker monorepo --output json
python tools/governance/template_scaffold.py doctor-composition --overlays scheduler cli-worker python-package --output json
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
python tools/governance/template_scaffold.py doctor-composition --overlays django laravel --output json
python tools/governance/template_scaffold.py verify-composition-matrix
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python tools/governance/template_scaffold.py list-manifests --output json
python tools/templates/list_templates.py --output json
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Observed results:

- all existing certified controls returned `reason_code: certified-multi-overlay`
- all scheduler pair and triple controls returned `reason_code: certified-multi-overlay`
- `laravel + cli-worker` returned `reason_code: explicitly-rejected`, `conflict_code: worker-model-collision`
- `django + laravel` returned `reason_code: explicitly-rejected`, `conflict_code: cross-framework-application-collision`
- `verify-composition-matrix` returned `composition-matrix: OK`
- `verify-composition-matrix --output json` returned `{ "valid": true, "errors": [] }`
- manifest inventory and template inventory commands succeeded with scheduler present
- governance suite passed with `Ran 100 tests ... OK`
