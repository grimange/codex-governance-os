from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.governance.portability_scan import REPO_ROOT, _result_to_json, format_result_text, scan_active_governed_surfaces


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description="Run deterministic governance preflight checks before governed execution."
    )
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--output", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    portability_result = scan_active_governed_surfaces(args.repo_root)
    payload = {
        "checks": [
            {
                "name": "portability_reference_scan",
                "decision": "PASS" if not portability_result.violations else "BLOCKED",
                "result": _result_to_json(portability_result),
            }
        ]
    }

    if args.output == "json":
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print("governance_preflight")
        print("check: portability_reference_scan")
        print(f"decision: {'PASS' if not portability_result.violations else 'BLOCKED'}")
        print(format_result_text(portability_result))

    return 0 if not portability_result.violations else 1


if __name__ == "__main__":
    sys.exit(main())
