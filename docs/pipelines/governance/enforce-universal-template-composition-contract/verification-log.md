# Verification Log

## Commands

```bash
python -m unittest discover -s tests/governance -p 'test_*.py'
python tools/templates/list_templates.py --output json
python tools/governance/template_scaffold.py list-manifests --output json
python - <<'PY'
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

repo = Path.cwd()
manifest_source = repo / "docs/codex/templates/manifests"

with tempfile.TemporaryDirectory() as manifest_tmp:
    manifest_dir = Path(manifest_tmp)
    shutil.copytree(manifest_source, manifest_dir, dirs_exist_ok=True)
    laravel_path = manifest_dir / "laravel.json"
    payload = json.loads(laravel_path.read_text())
    payload["compatible_overlays"] = ["cli-worker"]
    laravel_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    run = subprocess.run(
        [sys.executable, "tools/governance/template_scaffold.py", "list-manifests", "--manifest-dir", str(manifest_dir), "--output", "json"],
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    print("INVALID_MANIFEST_RETURN", run.returncode)
    print("INVALID_MANIFEST_STDOUT", run.stdout.strip())

with tempfile.TemporaryDirectory() as out_tmp:
    output_root = Path(out_tmp) / "repo"
    run = subprocess.run(
        [sys.executable, "tools/governance/template_scaffold.py", "realize-repository", "universal-base", str(output_root), "--overlay", "laravel", "--overlay", "cli-worker"],
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    created = sorted(str(path.relative_to(output_root)) for path in output_root.rglob("*")) if output_root.exists() else []
    print("INVALID_SCAFFOLD_RETURN", run.returncode)
    print("INVALID_SCAFFOLD_STDOUT", run.stdout.strip())
    print("INVALID_SCAFFOLD_CREATED", created)
PY
```

## Results

- `python -m unittest discover -s tests/governance -p 'test_*.py'` -> `Ran 34 tests in 0.386s` and `OK`
- `python tools/templates/list_templates.py --output json` -> succeeded and returned the canonical manifest inventory
- `python tools/governance/template_scaffold.py list-manifests --output json` -> succeeded and returned the canonical manifest inventory with required surfaces
- invalid manifest drift probe -> non-zero exit with structured JSON:
  - `{"errors":["laravel declares unsupported composition cli-worker + laravel"],"valid":false}`
- invalid scaffold probe -> non-zero exit with deterministic rejection:
  - `unsupported template composition`
  - `requested: cli-worker + laravel`
  - `reason: explicitly-rejected (incompatible runtime assumptions)`
  - `allowed: see docs/contracts/universal-template-composition-contract.md`
- invalid scaffold probe created no files
