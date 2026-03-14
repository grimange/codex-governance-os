from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_scaffold import list_scaffold_manifests, realize_repository_scaffold, render_scaffold_surface
from tools.templates.composition_contract import explain_template_composition, validate_capability_composition


class LaravelMonorepoSchedulerCompoundCompositionTests(unittest.TestCase):
    def test_laravel_monorepo_scheduler_triplet_is_supported(self) -> None:
        explanation = explain_template_composition(["laravel", "monorepo", "scheduler"])
        self.assertTrue(explanation.supported)
        self.assertEqual("certified-multi-overlay", explanation.reason_code)
        self.assertEqual(("laravel", "monorepo", "scheduler"), explanation.normalized_overlays)

        result = validate_capability_composition(
            list_scaffold_manifests(),
            ["laravel", "monorepo", "scheduler"],
        )
        self.assertTrue(result.supported)
        self.assertEqual("certified-multi-overlay", result.reason_code)

    def test_compound_scaffold_realization_places_laravel_scheduler_surfaces_under_monorepo_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            selection = realize_repository_scaffold(
                "universal-base",
                Path(tmp),
                overlays=["laravel", "monorepo", "scheduler"],
                include_optional=False,
            )
            payload = json.loads(selection.read_text())
            self.assertEqual(["laravel", "monorepo", "scheduler"], payload["overlays"])
            self.assertEqual(
                "apps/backend/laravel-app",
                payload["composition_metadata"]["laravel"]["placement"],
            )
            self.assertEqual(
                "apps/backend/laravel-app/app/Console/Kernel.php",
                payload["composition_metadata"]["laravel"]["scheduler_surface"],
            )
            expected = {
                "apps/backend/laravel-app/composer.json",
                "apps/backend/laravel-app/bootstrap/app.php",
                "apps/backend/laravel-app/config/app.php",
                "apps/backend/laravel-app/routes/web.php",
                "apps/backend/laravel-app/public/index.php",
                "apps/backend/laravel-app/app/Console",
                "apps/backend/laravel-app/app/Http",
                "apps/backend/laravel-app/app/Console/Kernel.php",
                "apps/backend/laravel-app/app/Console/Commands",
                "apps/backend/laravel-app/routes/console.php",
                "apps/backend/laravel-app/config/scheduler.php",
                "packages",
                "services",
                "shared",
                "scheduler",
                "scheduler/schedule.py",
                "scheduler/scheduler_runtime.py",
            }
            self.assertTrue(expected.issubset(set(payload["created_surfaces"])))
            self.assertEqual(
                render_scaffold_surface("app/Console/Kernel.php"),
                (Path(tmp) / "apps/backend/laravel-app/app/Console/Kernel.php").read_text(),
            )
            self.assertEqual(
                render_scaffold_surface("routes/console.php"),
                (Path(tmp) / "apps/backend/laravel-app/routes/console.php").read_text(),
            )
            self.assertEqual(
                render_scaffold_surface("config/scheduler.php"),
                (Path(tmp) / "apps/backend/laravel-app/config/scheduler.php").read_text(),
            )

    def test_doctor_surface_reports_compound_triplet_as_supported(self) -> None:
        run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_scaffold.py",
                "doctor-composition",
                "--overlays",
                "laravel",
                "monorepo",
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
        self.assertEqual(["laravel", "monorepo", "scheduler"], payload["normalized_overlays"])


if __name__ == "__main__":
    unittest.main()
