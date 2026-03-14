from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_registry import RegistryError
from tools.governance.template_scaffold import realize_repository_scaffold
from tools.templates.composition_contract import explain_template_composition


class TemplateCompositionSurfaceConsistencyTests(unittest.TestCase):
    def _doctor(self, overlays: list[str]) -> tuple[int, dict]:
        run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_scaffold.py",
                "doctor-composition",
                "--overlays",
                *overlays,
                "--output",
                "json",
            ],
            cwd=Path(__file__).resolve().parents[2],
            check=False,
            capture_output=True,
            text=True,
        )
        return run.returncode, json.loads(run.stdout)

    def test_supported_decisions_match_between_contract_doctor_and_scaffold(self) -> None:
        cases = (
            [],
            ["laravel", "monorepo"],
            ["django", "monorepo"],
            ["service", "monorepo"],
            ["node-typescript-service", "monorepo"],
            ["node-typescript-service", "cli-worker"],
            ["cli-worker", "monorepo"],
            ["cli-worker", "python-package"],
            ["cli-worker", "php-package"],
        )

        for overlays in cases:
            with self.subTest(overlays=overlays or ["base-only"]):
                contract = explain_template_composition(overlays)
                code, doctor = self._doctor(overlays)
                self.assertTrue(contract.supported)
                self.assertEqual(0, code)
                self.assertEqual(list(contract.requested_overlays), doctor["requested_overlays"])
                self.assertEqual(list(contract.normalized_overlays), doctor["normalized_overlays"])
                self.assertEqual(contract.supported, doctor["supported"])
                self.assertEqual(contract.reason_code, doctor["reason_code"])
                self.assertEqual(contract.decision_source, doctor["decision_source"])
                with tempfile.TemporaryDirectory() as tmp:
                    selection = realize_repository_scaffold("universal-base", Path(tmp), overlays=overlays)
                    payload = json.loads(selection.read_text())
                    self.assertEqual(list(contract.normalized_overlays), payload["overlays"])

    def test_rejected_decisions_match_between_contract_doctor_and_scaffold(self) -> None:
        cases = (
            ["laravel", "cli-worker"],
            ["laravel", "django"],
        )

        for overlays in cases:
            with self.subTest(overlays=overlays):
                contract = explain_template_composition(overlays)
                code, doctor = self._doctor(overlays)
                self.assertFalse(contract.supported)
                self.assertNotEqual(0, code)
                self.assertEqual(list(contract.requested_overlays), doctor["requested_overlays"])
                self.assertEqual(list(contract.normalized_overlays), doctor["normalized_overlays"])
                self.assertEqual(contract.supported, doctor["supported"])
                self.assertEqual(contract.reason_code, doctor["reason_code"])
                self.assertEqual(contract.rejection_reason, doctor["rejection_reason"])
                self.assertEqual(contract.decision_source, doctor["decision_source"])
                with tempfile.TemporaryDirectory() as tmp:
                    with self.assertRaises(RegistryError) as exc:
                        realize_repository_scaffold("universal-base", Path(tmp), overlays=overlays)
                message = str(exc.exception)
                self.assertIn(f"requested: {' + '.join(contract.normalized_overlays)}", message)
                self.assertIn(f"reason: {contract.reason_code}", message)
                self.assertIn(contract.decision_source, message)

    def test_manifest_and_template_listing_fail_with_consistent_contract_drift_signal(self) -> None:
        repo = Path(__file__).resolve().parents[2]
        with tempfile.TemporaryDirectory() as tmp:
            manifest_dir = Path(tmp)
            shutil.copytree(repo / "docs/codex/templates/manifests", manifest_dir, dirs_exist_ok=True)
            laravel_path = manifest_dir / "laravel.json"
            payload = json.loads(laravel_path.read_text())
            payload["compatible_overlays"] = ["cli-worker"]
            laravel_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

            manifest_run = subprocess.run(
                [
                    sys.executable,
                    "tools/governance/template_scaffold.py",
                    "list-manifests",
                    "--manifest-dir",
                    str(manifest_dir),
                    "--output",
                    "json",
                ],
                cwd=repo,
                check=False,
                capture_output=True,
                text=True,
            )
            template_run = subprocess.run(
                [
                    sys.executable,
                    "tools/templates/list_templates.py",
                    "--manifest-dir",
                    str(manifest_dir),
                    "--output",
                    "json",
                ],
                cwd=repo,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertNotEqual(0, manifest_run.returncode)
            self.assertNotEqual(0, template_run.returncode)
            manifest_payload = json.loads(manifest_run.stdout)
            template_payload = json.loads(template_run.stdout)
            self.assertEqual(manifest_payload, template_payload)
            self.assertIn("unsupported composition cli-worker + laravel", manifest_payload["errors"][0])
            self.assertIn("doctor-composition --overlays cli-worker laravel", manifest_payload["errors"][0])


if __name__ == "__main__":
    unittest.main()
