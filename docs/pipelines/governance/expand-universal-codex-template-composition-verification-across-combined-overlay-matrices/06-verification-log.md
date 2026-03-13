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
supported = [
    ("base-only", []),
    ("node-typescript-service+monorepo", ["node-typescript-service", "monorepo"]),
    ("node-typescript-service+cli-worker", ["node-typescript-service", "cli-worker"]),
    ("cli-worker+monorepo", ["cli-worker", "monorepo"]),
    ("cli-worker+python-package", ["cli-worker", "python-package"]),
    ("cli-worker+php-package", ["cli-worker", "php-package"]),
]
invalid = [
    ("laravel+cli-worker", ["laravel", "cli-worker"]),
    ("django+monorepo", ["django", "monorepo"]),
    ("service+monorepo", ["service", "monorepo"]),
    ("laravel+django", ["laravel", "django"]),
]
results = {"supported": [], "invalid": []}
for name, overlays in supported:
    with tempfile.TemporaryDirectory() as tmp:
        selection = realize_repository_scaffold("universal-base", Path(tmp), overlays=overlays, include_optional=False)
        payload = json.loads(selection.read_text())
        results["supported"].append({"case": name, "overlays": overlays, "created_surfaces": payload["created_surfaces"]})
for name, overlays in invalid:
    try:
        with tempfile.TemporaryDirectory() as tmp:
            realize_repository_scaffold("universal-base", Path(tmp), overlays=overlays, include_optional=False)
    except RegistryError as exc:
        results["invalid"].append({"case": name, "overlays": overlays, "result": "blocked", "reason": str(exc)})
print(json.dumps(results, indent=2))
PY
```

## Observed Outcomes

- governance tests passed: `Ran 29 tests ... OK`
- manifest inventory and support listing matched the verified overlay set
- supported combined-overlay cases realized the expected surfaces
- invalid combinations failed closed with explicit compatibility errors
- no residual docs or manifest mismatch remained after the matrix documentation refresh
