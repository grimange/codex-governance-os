# Verification Log

## Commands Run

```bash
python -m unittest discover -s tests/governance -p 'test_*.py'
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
python - <<'PY'
import json
import tempfile
from pathlib import Path
from tools.governance.template_scaffold import realize_repository_scaffold
from tools.governance.template_registry import RegistryError
cases = [
    ("base-only", []),
    ("node-typescript-service", ["node-typescript-service"]),
    ("cli-worker", ["cli-worker"]),
    ("node-typescript-service-in-monorepo", ["node-typescript-service", "monorepo"]),
]
results = []
for name, overlays in cases:
    with tempfile.TemporaryDirectory() as tmp:
        selection = realize_repository_scaffold("universal-base", Path(tmp), overlays=overlays, include_optional=False)
        payload = json.loads(selection.read_text())
        results.append({
            "case": name,
            "overlays": overlays,
            "result": "admitted",
            "created_surfaces": payload["created_surfaces"],
        })
try:
    with tempfile.TemporaryDirectory() as tmp:
        realize_repository_scaffold("universal-base", Path(tmp), overlays=["laravel", "cli-worker"], include_optional=False)
except RegistryError as exc:
    results.append({
        "case": "invalid-laravel-cli-worker",
        "overlays": ["laravel", "cli-worker"],
        "result": "blocked",
        "reason": str(exc),
    })
print(json.dumps(results, indent=2))
PY
```

## Observed Outcomes

- governance tests passed: `Ran 27 tests ... OK`
- template inventory lists both `node-typescript-service` and `cli-worker`
- manifest inventory matches support docs and scaffold contract claims
- valid new overlay cases were admitted and realized expected surfaces
- the invalid Laravel plus CLI-worker combination failed closed with an explicit compatibility error
