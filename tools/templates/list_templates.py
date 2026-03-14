from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.governance.template_scaffold import list_scaffold_manifests
from tools.governance.template_registry import RegistryError


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="List universal scaffold manifests.")
    parser.add_argument("--manifest-dir", type=Path, default=None)
    parser.add_argument("--output", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    try:
        manifests = list_scaffold_manifests(args.manifest_dir)
        if args.output == "json":
            payload = [
                {
                    "template_name": manifest.template_name,
                    "template_type": manifest.template_type,
                    "base_template": manifest.base_template,
                    "compatible_overlays": list(manifest.compatible_overlays),
                    "supported_runtime_shapes": list(manifest.supported_runtime_shapes),
                    "maturity": manifest.maturity,
                }
                for manifest in manifests
            ]
            print(json.dumps(payload, indent=2, sort_keys=True))
        else:
            for manifest in manifests:
                print(
                    f"{manifest.template_name} [{manifest.template_type}] "
                    f"runtime={','.join(manifest.supported_runtime_shapes)}"
                )
        return 0
    except RegistryError as exc:
        if args.output == "json":
            print(json.dumps({"valid": False, "errors": [str(exc)]}, indent=2, sort_keys=True))
        else:
            print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
