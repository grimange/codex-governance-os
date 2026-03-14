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
python -c "from tools.governance.template_scaffold import list_scaffold_manifests; from tools.templates.composition_contract import load_template_capability_registry; manifests=list_scaffold_manifests(); registry=load_template_capability_registry(); manifest_caps=sorted({cap for m in manifests for cap in (*m.provides,*m.requires,*m.conflicts)}); print({'capability_count': len(registry.capabilities), 'taxonomy_count': len(registry.conflict_taxonomy), 'explicit_boundary_code_count': len(registry.explicit_boundary_codes), 'role_collision_code_count': len(registry.role_collision_codes), 'referenced_capabilities_valid': all(cap in registry.capabilities for cap in manifest_caps)})"
python tools/governance/template_scaffold.py verify-composition-matrix
python tools/governance/template_scaffold.py verify-composition-matrix --output json
python -m unittest discover -s tests/governance -p 'test_*.py'
```

Observed results:

- all certified pair controls returned `reason_code: certified-multi-overlay`
- the certified triple control returned `reason_code: certified-multi-overlay`
- `laravel + cli-worker` returned `reason_code: explicitly-rejected`, `conflict_code: worker-model-collision`
- `django + laravel` returned `reason_code: explicitly-rejected`, `conflict_code: cross-framework-application-collision`
- snapshot inspection returned `True` for the triple entry
- registry inspection returned `{'capability_count': 12, 'taxonomy_count': 6, 'explicit_boundary_code_count': 2, 'role_collision_code_count': 5, 'referenced_capabilities_valid': True}`
- `verify-composition-matrix` returned `composition-matrix: OK`
- `verify-composition-matrix --output json` returned `{ "valid": true, "errors": [] }`
- governance suite passed with `Ran 93 tests ... OK`
