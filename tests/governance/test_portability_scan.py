from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.portability_scan import scan_active_governed_surfaces, scan_files


class PortabilityScanTests(unittest.TestCase):
    def test_repo_active_scan_has_no_violations(self) -> None:
        result = scan_active_governed_surfaces()
        self.assertEqual((), result.violations)

    def test_machine_local_link_in_active_surface_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            path = repo_root / "docs" / "governance" / "bad.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("[bad](/home/example/repo/docs/governance/thing.md)\n")
            result = scan_files([path], scope="test", repo_root=repo_root)
            self.assertEqual(1, len(result.violations))
            self.assertEqual("violation", result.violations[0].classification)

    def test_literal_rule_examples_are_classified_as_exceptions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            path = repo_root / "docs" / "governance" / "rule.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                "# Rule\n\n"
                "Forbidden examples:\n"
                "- `/home/...`\n"
                "- `file://...`\n"
                "```text\n"
                "~/\n"
                "```\n"
            )
            result = scan_files([path], scope="test", repo_root=repo_root)
            self.assertEqual((), result.violations)
            classifications = {item.classification for item in result.exceptions}
            self.assertIn("rule_example", classifications)
            self.assertIn("scan_definition", classifications)

    def test_preflight_cli_blocks_on_violation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            (repo_root / "docs" / "governance").mkdir(parents=True, exist_ok=True)
            (repo_root / "docs" / "contracts").mkdir(parents=True, exist_ok=True)
            (repo_root / "docs" / "pipelines" / "governance").mkdir(parents=True, exist_ok=True)
            (repo_root / "docs" / "pipelines" / "registry").mkdir(parents=True, exist_ok=True)
            (repo_root / ".codex").mkdir(parents=True, exist_ok=True)
            (repo_root / "README.md").write_text("# Repo\n")
            (repo_root / ".codex" / "AGENTS.md").write_text("# Agents\n")
            (repo_root / "docs" / "pipelines" / "registry" / "pipeline-registry.md").write_text("# Registry\n")
            (repo_root / "docs" / "governance" / "bad.md").write_text(
                "[bad](/Users/example/project/docs/governance/bad.md)\n"
            )
            run = subprocess.run(
                [
                    sys.executable,
                    "tools/governance/preflight.py",
                    "--repo-root",
                    str(repo_root),
                    "--output",
                    "json",
                ],
                cwd=Path(__file__).resolve().parents[2],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(1, run.returncode)
            payload = json.loads(run.stdout)
            self.assertEqual("BLOCKED", payload["checks"][0]["decision"])


if __name__ == "__main__":
    unittest.main()
