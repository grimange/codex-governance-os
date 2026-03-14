from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_scaffold import list_scaffold_manifests, realize_repository_scaffold, render_scaffold_surface
from tools.templates.composition_contract import explain_template_composition, validate_capability_composition


class DjangoNativeSchedulerCompositionTests(unittest.TestCase):
    def test_django_and_scheduler_manifests_admit_each_other(self) -> None:
        manifests = {manifest.template_name: manifest for manifest in list_scaffold_manifests()}
        self.assertIn("scheduler", manifests["django"].compatible_overlays)
        self.assertIn("django", manifests["scheduler"].compatible_overlays)

    def test_django_native_scheduler_pair_is_supported(self) -> None:
        explanation = explain_template_composition(["django", "scheduler"])
        self.assertTrue(explanation.supported)
        self.assertEqual("certified-multi-overlay", explanation.reason_code)
        self.assertEqual(("django", "scheduler"), explanation.normalized_overlays)

        result = validate_capability_composition(list_scaffold_manifests(), ["django", "scheduler"])
        self.assertTrue(result.supported)
        self.assertEqual("certified-multi-overlay", result.reason_code)

    def test_django_native_scheduler_scaffold_realization_matches_contract_surfaces(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            selection = realize_repository_scaffold(
                "universal-base",
                Path(tmp),
                overlays=["django", "scheduler"],
                include_optional=False,
            )
            payload = json.loads(selection.read_text())
            self.assertEqual(["django", "scheduler"], payload["overlays"])
            self.assertEqual(
                "project/celery.py",
                payload["composition_metadata"]["django"]["scheduler_surface"],
            )
            expected = {
                "backend",
                "config",
                "apps",
                "scheduler",
                "scheduler/schedule.py",
                "scheduler/scheduler_runtime.py",
                "manage.py",
                "project/settings.py",
                "project/urls.py",
                "project/asgi.py",
                "project/celery.py",
                "project/scheduler.py",
            }
            self.assertTrue(expected.issubset(set(payload["created_surfaces"])))
            self.assertEqual(
                render_scaffold_surface("project/celery.py"),
                (Path(tmp) / "project/celery.py").read_text(),
            )
            self.assertEqual(
                render_scaffold_surface("project/scheduler.py"),
                (Path(tmp) / "project/scheduler.py").read_text(),
            )
            self.assertEqual(
                render_scaffold_surface("project/settings.py"),
                (Path(tmp) / "project/settings.py").read_text(),
            )

    def test_doctor_surface_reports_django_native_scheduler_pair_as_supported(self) -> None:
        run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_scaffold.py",
                "doctor-composition",
                "--overlays",
                "scheduler",
                "django",
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
        self.assertEqual(["django", "scheduler"], payload["normalized_overlays"])


if __name__ == "__main__":
    unittest.main()
