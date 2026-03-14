# Verification Log

## Commands

```bash
python -m unittest discover -s tests/governance -p 'test_*.py'
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
python - <<'PY'
from pathlib import Path
from tempfile import TemporaryDirectory
from tools.governance.template_scaffold import realize_repository_scaffold, RegistryError

supported = [
    [],
    ["node-typescript-service", "monorepo"],
    ["node-typescript-service", "cli-worker"],
    ["cli-worker", "monorepo"],
    ["cli-worker", "python-package"],
    ["cli-worker", "php-package"],
]
blocked = [
    ["laravel", "cli-worker"],
    ["django", "monorepo"],
    ["service", "monorepo"],
    ["laravel", "django"],
]
for overlays in supported:
    with TemporaryDirectory() as tmp:
        realize_repository_scaffold("universal-base", Path(tmp), overlays=overlays)
        label = "base-only" if not overlays else " + ".join(overlays)
        print(f"SUPPORTED {label}")
for overlays in blocked:
    label = " + ".join(overlays)
    try:
        with TemporaryDirectory() as tmp:
            realize_repository_scaffold("universal-base", Path(tmp), overlays=overlays)
    except RegistryError:
        print(f"BLOCKED {label}")
PY
```

## Results

- `python -m unittest discover -s tests/governance -p 'test_*.py'` -> `Ran 29 tests in 0.326s` and `OK`
- `python tools/templates/list_templates.py --output json` -> returned canonical overlay inventory including `cli-worker`, `monorepo`, and `node-typescript-service` with compatible overlay metadata
- `python tools/governance/template_scaffold.py list-manifests --output json` -> returned scaffold manifests with required surfaces and compatibility metadata
- explicit realization sweep matched the certified matrix exactly:
  - `SUPPORTED base-only`
  - `SUPPORTED node-typescript-service + monorepo`
  - `SUPPORTED node-typescript-service + cli-worker`
  - `SUPPORTED cli-worker + monorepo`
  - `SUPPORTED cli-worker + python-package`
  - `SUPPORTED cli-worker + php-package`
  - `BLOCKED laravel + cli-worker`
  - `BLOCKED django + monorepo`
  - `BLOCKED service + monorepo`
  - `BLOCKED laravel + django`
