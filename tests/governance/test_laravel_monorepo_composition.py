from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_scaffold import list_scaffold_manifests, realize_repository_scaffold
from tools.templates.composition_contract import explain_template_composition


class LaravelMonorepoCompositionTests(unittest.TestCase):
    def test_laravel_manifest_and_monorepo_manifest_admit_each_other(self) -> None:
        manifests = {manifest.template_name: manifest for manifest in list_scaffold_manifests()}
        self.assertIn("monorepo", manifests["laravel"].compatible_overlays)
        self.assertIn("laravel", manifests["monorepo"].compatible_overlays)

    def test_scaffold_realization_matches_canonical_laravel_monorepo_layout(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            selection = realize_repository_scaffold(
                "universal-base",
                Path(tmp),
                overlays=["laravel", "monorepo"],
            )
            payload = json.loads(selection.read_text())
            self.assertEqual(["laravel", "monorepo"], payload["overlays"])
            self.assertEqual(
                "apps/backend/laravel-app",
                payload["composition_metadata"]["laravel"]["placement"],
            )
            expected = {
                "apps/backend/laravel-app/composer.json",
                "apps/backend/laravel-app/bootstrap/app.php",
                "apps/backend/laravel-app/config/app.php",
                "apps/backend/laravel-app/routes/web.php",
                "apps/backend/laravel-app/public/index.php",
                "apps/backend/laravel-app/app/Console",
                "apps/backend/laravel-app/app/Http",
                "packages",
                "services",
                "shared",
            }
            self.assertTrue(expected.issubset(set(payload["created_surfaces"])))

    def test_doctor_surface_reports_laravel_monorepo_as_supported(self) -> None:
        explanation = explain_template_composition(["laravel", "monorepo"])
        self.assertTrue(explanation.supported)
        self.assertEqual(("laravel", "monorepo"), explanation.normalized_overlays)

        run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_scaffold.py",
                "doctor-composition",
                "--overlays",
                "laravel",
                "monorepo",
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
        self.assertEqual(["laravel", "monorepo"], payload["normalized_overlays"])


if __name__ == "__main__":
    unittest.main()
