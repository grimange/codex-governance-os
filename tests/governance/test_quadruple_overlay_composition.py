from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_scaffold import realize_repository_scaffold
from tools.templates.composition_contract import explain_template_composition


class QuadrupleOverlayCompositionTests(unittest.TestCase):
    def test_cli_worker_monorepo_python_package_scheduler_is_supported(self) -> None:
        explanation = explain_template_composition(
            ["cli-worker", "monorepo", "python-package", "scheduler"]
        )
        self.assertTrue(explanation.supported)
        self.assertEqual("certified-multi-overlay", explanation.reason_code)
        self.assertEqual(
            ("cli-worker", "monorepo", "python-package", "scheduler"),
            explanation.normalized_overlays,
        )

    def test_quadruple_scaffold_realization_contains_all_governed_surfaces(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            selection = realize_repository_scaffold(
                "universal-base",
                Path(tmp),
                overlays=["cli-worker", "monorepo", "python-package", "scheduler"],
                include_optional=False,
            )
            payload = json.loads(selection.read_text())
            self.assertEqual(
                ["cli-worker", "monorepo", "python-package", "scheduler"],
                payload["overlays"],
            )
            expected = {
                "bin",
                "jobs",
                "worker",
                "packages",
                "services",
                "shared",
                "src",
                "tests",
                "docs",
                "scheduler",
                "scheduler/schedule.py",
                "scheduler/scheduler_runtime.py",
            }
            self.assertTrue(expected.issubset(set(payload["created_surfaces"])))

    def test_doctor_surface_reports_quadruple_as_supported(self) -> None:
        run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_scaffold.py",
                "doctor-composition",
                "--overlays",
                "cli-worker",
                "monorepo",
                "python-package",
                "scheduler",
                "--output",
                "json",
            ],
            cwd=Path(__file__).resolve().parents[2],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(run.stdout)
        self.assertTrue(payload["supported"])
        self.assertEqual("certified-multi-overlay", payload["reason_code"])
        self.assertEqual(
            ["cli-worker", "monorepo", "python-package", "scheduler"],
            payload["normalized_overlays"],
        )


if __name__ == "__main__":
    unittest.main()
