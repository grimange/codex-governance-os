from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.governance.session_continuity import evaluate_scenarios, load_scenarios

DEFAULT_SCENARIO_DIR = (
    REPO_ROOT / "docs" / "pipelines" / "governance" / "establish-multi-session-continuity-evaluation-scenarios"
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate canonical multi-session continuity scenarios deterministically."
    )
    parser.add_argument("--scenario-dir", type=Path, default=DEFAULT_SCENARIO_DIR)
    parser.add_argument("--output", choices=("text", "json"), default="text")
    parser.add_argument("--run-scenarios", action="store_true")
    args = parser.parse_args(argv)

    if not args.run_scenarios:
        parser.error("the following arguments are required: --run-scenarios")

    scenarios = load_scenarios(args.scenario_dir)
    results = evaluate_scenarios(scenarios)
    payload = {
        "decision": "PASS" if all(result.matched_expectation for result in results) else "FAIL",
        "scenario_count": len(results),
        "results": [result.to_dict() for result in results],
    }

    if args.output == "json":
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print("multi_session_continuity_harness")
        print(f"decision: {payload['decision']}")
        print(f"scenario_count: {payload['scenario_count']}")
        for result in results:
            print(f"scenario_id: {result.scenario_id}")
            print(f"verdict: {result.verdict}")
            if result.classification:
                print(f"classification: {result.classification}")
            if result.failure_classification:
                print(f"failure_classification: {result.failure_classification}")
            print(f"matched_expectation: {str(result.matched_expectation).lower()}")

    return 0 if payload["decision"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
