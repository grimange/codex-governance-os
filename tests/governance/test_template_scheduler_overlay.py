from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_scaffold import list_scaffold_manifests, realize_repository_scaffold
from tools.templates.composition_contract import explain_template_composition, validate_capability_composition


class TemplateSchedulerOverlayTests(unittest.TestCase):
    def test_scheduler_manifest_is_admitted(self) -> None:
        manifests = {manifest.template_name: manifest for manifest in list_scaffold_manifests()}
        scheduler = manifests["scheduler"]
        self.assertEqual("overlay", scheduler.template_type)
        self.assertEqual(("scheduler-runtime",), scheduler.provides)
        self.assertEqual("scheduler", scheduler.composition_role)

    def test_scheduler_supported_compositions_are_admitted(self) -> None:
        manifests = list_scaffold_manifests()
        for overlays in (
            ["scheduler", "django"],
            ["scheduler", "cli-worker"],
            ["scheduler", "monorepo"],
            ["scheduler", "python-package"],
            ["scheduler", "cli-worker", "monorepo"],
            ["scheduler", "cli-worker", "python-package"],
        ):
            result = validate_capability_composition(manifests, overlays)
            self.assertTrue(result.supported, msg=f"expected supported composition: {overlays}")
            self.assertEqual("certified-multi-overlay", result.reason_code)

    def test_scheduler_scaffold_realization_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            selection = realize_repository_scaffold(
                "universal-base",
                Path(tmp),
                overlays=["scheduler", "cli-worker"],
                include_optional=False,
            )
            payload = json.loads(selection.read_text())
            self.assertEqual(["cli-worker", "scheduler"], payload["overlays"])
            self.assertTrue((Path(tmp) / "scheduler").is_dir())
            self.assertTrue((Path(tmp) / "scheduler/schedule.py").is_file())
            self.assertTrue((Path(tmp) / "scheduler/scheduler_runtime.py").is_file())

    def test_scheduler_doctor_surface_reports_supported_pair(self) -> None:
        run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_scaffold.py",
                "doctor-composition",
                "--overlays",
                "scheduler",
                "cli-worker",
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
        self.assertEqual(["cli-worker", "scheduler"], payload["normalized_overlays"])

    def test_scheduler_framework_native_pairs_are_supported(self) -> None:
        laravel = explain_template_composition(["scheduler", "laravel"])
        self.assertTrue(laravel.supported)
        self.assertEqual("certified-multi-overlay", laravel.reason_code)

        django = explain_template_composition(["scheduler", "django"])
        self.assertTrue(django.supported)
        self.assertEqual("certified-multi-overlay", django.reason_code)


if __name__ == "__main__":
    unittest.main()
