from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_scaffold import list_scaffold_manifests, realize_repository_scaffold
from tools.templates.composition_contract import explain_template_composition


class DjangoMonorepoCompositionTests(unittest.TestCase):
    def test_django_manifest_and_monorepo_manifest_admit_each_other(self) -> None:
        manifests = {manifest.template_name: manifest for manifest in list_scaffold_manifests()}
        self.assertIn("monorepo", manifests["django"].compatible_overlays)
        self.assertIn("django", manifests["monorepo"].compatible_overlays)

    def test_scaffold_realization_matches_canonical_django_monorepo_layout(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            selection = realize_repository_scaffold(
                "universal-base",
                Path(tmp),
                overlays=["django", "monorepo"],
            )
            payload = json.loads(selection.read_text())
            self.assertEqual(["django", "monorepo"], payload["overlays"])
            self.assertEqual(
                "apps/backend/django-service",
                payload["composition_metadata"]["django"]["placement"],
            )
            expected = {
                "apps/backend/django-service/manage.py",
                "apps/backend/django-service/pyproject.toml",
                "apps/backend/django-service/requirements.txt",
                "apps/backend/django-service/project/settings.py",
                "apps/backend/django-service/project/urls.py",
                "apps/backend/django-service/project/asgi.py",
                "apps/backend/django-service/app_modules",
                "packages",
                "services",
                "shared",
            }
            self.assertTrue(expected.issubset(set(payload["created_surfaces"])))

    def test_doctor_surface_reports_django_monorepo_as_supported(self) -> None:
        explanation = explain_template_composition(["django", "monorepo"])
        self.assertTrue(explanation.supported)
        self.assertEqual(("django", "monorepo"), explanation.normalized_overlays)

        run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_scaffold.py",
                "doctor-composition",
                "--overlays",
                "django",
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
        self.assertEqual(["django", "monorepo"], payload["normalized_overlays"])


if __name__ == "__main__":
    unittest.main()
