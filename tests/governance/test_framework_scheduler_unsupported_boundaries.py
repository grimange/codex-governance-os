from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_registry import RegistryError
from tools.governance.template_scaffold import realize_repository_scaffold
from tools.templates.composition_contract import explain_template_composition, validate_template_composition


class FrameworkSchedulerUnsupportedBoundaryTests(unittest.TestCase):
    def _doctor(self, framework: str) -> tuple[int, dict]:
        run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_scaffold.py",
                "doctor-composition",
                "--overlays",
                "scheduler",
                framework,
                "--output",
                "json",
            ],
            cwd=Path(__file__).resolve().parents[2],
            check=False,
            capture_output=True,
            text=True,
        )
        return run.returncode, json.loads(run.stdout)

    def test_contract_marks_node_scheduler_as_unsupported(self) -> None:
        result = validate_template_composition(["scheduler", "node-typescript-service"])
        self.assertFalse(result.supported)
        self.assertEqual("unsupported", result.reason_code)
        self.assertIsNone(result.conflict_code)

    def test_doctor_surface_reports_node_scheduler_as_unsupported(self) -> None:
        code, payload = self._doctor("node-typescript-service")
        self.assertNotEqual(0, code)
        self.assertFalse(payload["supported"])
        self.assertEqual("unsupported", payload["reason_code"])

    def test_scaffold_realization_fails_closed_for_node_scheduler_pair(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(RegistryError) as exc:
                realize_repository_scaffold(
                    "universal-base",
                    Path(tmp),
                    overlays=["scheduler", "node-typescript-service"],
                )
        self.assertIn("unsupported template composition", str(exc.exception))

    def test_existing_supported_scheduler_and_framework_native_pairs_remain_unaffected(self) -> None:
        explanation = explain_template_composition(["scheduler", "django"])
        self.assertTrue(explanation.supported)
        self.assertEqual("certified-multi-overlay", explanation.reason_code)


if __name__ == "__main__":
    unittest.main()
