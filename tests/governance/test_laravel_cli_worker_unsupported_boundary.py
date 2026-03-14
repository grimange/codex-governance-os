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


class LaravelCliWorkerUnsupportedBoundaryTests(unittest.TestCase):
    def _doctor(self) -> tuple[int, dict]:
        run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_scaffold.py",
                "doctor-composition",
                "--overlays",
                "laravel",
                "cli-worker",
                "--output",
                "json",
            ],
            cwd=Path(__file__).resolve().parents[2],
            check=False,
            capture_output=True,
            text=True,
        )
        return run.returncode, json.loads(run.stdout)

    def test_contract_marks_laravel_cli_worker_as_explicitly_unsupported(self) -> None:
        result = validate_template_composition(["laravel", "cli-worker"])
        self.assertFalse(result.supported)
        self.assertEqual(("cli-worker", "laravel"), result.normalized_overlays)
        self.assertEqual("explicitly-rejected", result.reason_code)
        self.assertEqual("missing Laravel worker composition contract", result.rejection_reason)

    def test_doctor_surface_reports_explicit_boundary_reason(self) -> None:
        code, payload = self._doctor()
        self.assertNotEqual(0, code)
        self.assertFalse(payload["supported"])
        self.assertEqual(["laravel", "cli-worker"], payload["requested_overlays"])
        self.assertEqual(["cli-worker", "laravel"], payload["normalized_overlays"])
        self.assertEqual("explicitly-rejected", payload["reason_code"])
        self.assertEqual(
            "missing Laravel worker composition contract",
            payload["rejection_reason"],
        )
        self.assertEqual(
            "docs/contracts/universal-template-composition-contract.md",
            payload["decision_source"],
        )

    def test_scaffold_realization_fails_closed_for_laravel_cli_worker(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(RegistryError) as exc:
                realize_repository_scaffold(
                    "universal-base",
                    Path(tmp),
                    overlays=["laravel", "cli-worker"],
                )
        self.assertIn("requested: cli-worker + laravel", str(exc.exception))
        self.assertIn("missing Laravel worker composition contract", str(exc.exception))

    def test_existing_supported_composition_remains_unaffected(self) -> None:
        explanation = explain_template_composition(["cli-worker", "python-package"])
        self.assertTrue(explanation.supported)
        self.assertEqual("certified-multi-overlay", explanation.reason_code)


if __name__ == "__main__":
    unittest.main()
