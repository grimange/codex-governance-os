from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.governance.template_registry import RegistryError
from tools.governance.template_scaffold import (
    DEFAULT_SCAFFOLD_MANIFEST_DIRECTORY,
    list_scaffold_manifests,
    load_scaffold_manifest,
    realize_repository_scaffold,
)
from tools.templates import composition_contract
from tools.templates.composition_contract import detect_contract_drift, explain_template_composition


class TemplateCompositionPostExpansionProtectionsTests(unittest.TestCase):
    supported_cases = (
        [],
        ["django", "monorepo"],
        ["service", "monorepo"],
        ["node-typescript-service", "monorepo"],
        ["node-typescript-service", "cli-worker"],
        ["cli-worker", "monorepo"],
        ["cli-worker", "python-package"],
        ["cli-worker", "php-package"],
    )

    rejected_cases = (
        ["laravel", "cli-worker"],
        ["laravel", "django"],
    )

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

    def test_supported_matrix_remains_consistent_across_contract_doctor_and_scaffold(self) -> None:
        for overlays in self.supported_cases:
            with self.subTest(overlays=overlays or ["base-only"]):
                explanation = explain_template_composition(overlays)
                code, doctor = self._doctor(list(overlays))
                self.assertTrue(explanation.supported)
                self.assertEqual(0, code)
                self.assertEqual(list(explanation.normalized_overlays), doctor["normalized_overlays"])
                self.assertEqual(explanation.reason_code, doctor["reason_code"])
                self.assertEqual(explanation.decision_source, doctor["decision_source"])
                with tempfile.TemporaryDirectory() as tmp:
                    selection = realize_repository_scaffold(
                        "universal-base",
                        Path(tmp),
                        overlays=list(overlays),
                    )
                    payload = json.loads(selection.read_text())
                    self.assertEqual(list(explanation.normalized_overlays), payload["overlays"])

    def test_rejected_matrix_remains_fail_closed_across_contract_doctor_and_scaffold(self) -> None:
        for overlays in self.rejected_cases:
            with self.subTest(overlays=overlays):
                explanation = explain_template_composition(overlays)
                code, doctor = self._doctor(list(overlays))
                self.assertFalse(explanation.supported)
                self.assertNotEqual(0, code)
                self.assertEqual(list(explanation.normalized_overlays), doctor["normalized_overlays"])
                self.assertEqual(explanation.reason_code, doctor["reason_code"])
                with tempfile.TemporaryDirectory() as tmp:
                    with self.assertRaises(RegistryError):
                        realize_repository_scaffold(
                            "universal-base",
                            Path(tmp),
                            overlays=list(overlays),
                        )

    def test_contract_removal_drift_for_django_monorepo_is_detected(self) -> None:
        repo = Path(__file__).resolve().parents[2]
        source = repo / "docs/contracts/universal-template-composition-contract.md"
        with tempfile.TemporaryDirectory() as tmp:
            drifted = Path(tmp) / "universal-template-composition-contract.md"
            text = source.read_text().replace("- `django + monorepo`\n", "")
            drifted.write_text(text)
            report = detect_contract_drift(
                list_scaffold_manifests(),
                contract_path=drifted,
            )
            self.assertFalse(report.valid)
            self.assertIn(
                "CONTRACT_DRIFT_DETECTED: runtime supports undocumented composition django + monorepo",
                report.errors,
            )

    def test_runtime_expansion_drift_for_service_cli_worker_is_detected(self) -> None:
        expanded = composition_contract.CERTIFIED_MULTI_OVERLAY_COMPOSITIONS | {
            ("cli-worker", "service")
        }
        manifests = [
            load_scaffold_manifest(path.stem, manifest_dir=DEFAULT_SCAFFOLD_MANIFEST_DIRECTORY)
            for path in sorted(DEFAULT_SCAFFOLD_MANIFEST_DIRECTORY.glob("*.json"))
        ]
        with patch.object(
            composition_contract,
            "CERTIFIED_MULTI_OVERLAY_COMPOSITIONS",
            expanded,
        ):
            report = detect_contract_drift(manifests)
        self.assertFalse(report.valid)
        self.assertIn(
            "CONTRACT_DRIFT_DETECTED: runtime supports undocumented composition cli-worker + service",
            report.errors,
        )

    def test_manifest_drift_for_service_cli_worker_is_detected(self) -> None:
        repo = Path(__file__).resolve().parents[2]
        with tempfile.TemporaryDirectory() as tmp:
            manifest_dir = Path(tmp)
            shutil.copytree(repo / "docs/codex/templates/manifests", manifest_dir, dirs_exist_ok=True)
            service_path = manifest_dir / "service.json"
            payload = json.loads(service_path.read_text())
            payload["compatible_overlays"] = ["cli-worker"]
            service_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

            manifests = []
            for path in sorted(manifest_dir.glob("*.json")):
                raw = json.loads(path.read_text())
                manifests.append(type("Manifest", (), raw)())

            report = detect_contract_drift(manifests)
            self.assertFalse(report.valid)
            self.assertIn(
                "CONTRACT_DRIFT_DETECTED: service declares unsupported composition cli-worker + service; run: python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker service",
                report.errors,
            )


if __name__ == "__main__":
    unittest.main()
