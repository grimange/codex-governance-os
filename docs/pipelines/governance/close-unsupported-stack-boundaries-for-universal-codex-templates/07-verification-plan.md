# Verification Plan

## Commands

```bash
python -m unittest discover -s tests/governance -p 'test_*.py'
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
```

## Checks

- new overlays appear in the manifest inventory
- supported compositions realize the expected surfaces
- unsupported overlay pairs fail closed
- previously supported overlays continue to pass unchanged
- conformance tests include the new fixture classes
