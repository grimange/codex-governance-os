# Verification

Commands executed:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Verification criteria:

- doctor output must report `explicitly-rejected`
- doctor output must report `missing Laravel worker composition contract`
- template and manifest inventory must continue to show no compatibility declaration between `laravel` and `cli-worker`
- the governance suite must pass with the dedicated unsupported-boundary regression test included
