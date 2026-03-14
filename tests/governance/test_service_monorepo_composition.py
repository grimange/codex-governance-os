from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_scaffold import list_scaffold_manifests, realize_repository_scaffold
from tools.templates.composition_contract import explain_template_composition


class ServiceMonorepoCompositionTests(unittest.TestCase):
    def test_service_manifest_and_monorepo_manifest_admit_each_other(self) -> None:
        manifests = {manifest.template_name: manifest for manifest in list_scaffold_manifests()}
        self.assertIn("monorepo", manifests["service"].compatible_overlays)
        self.assertIn("service", manifests["monorepo"].compatible_overlays)

    def test_scaffold_realization_matches_canonical_service_monorepo_layout(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            selection = realize_repository_scaffold(
                "universal-base",
                Path(tmp),
                overlays=["service", "monorepo"],
            )
            payload = json.loads(selection.read_text())
            self.assertEqual(["monorepo", "service"], payload["overlays"])
            self.assertEqual(
                "services/service-app",
                payload["composition_metadata"]["service"]["placement"],
            )
            expected = {
                "services/service-app/src",
                "services/service-app/tests",
                "services/service-app/pyproject.toml",
                "services/service-app/README.md",
                "services/service-app/service_entrypoint",
                "packages",
                "services",
                "shared",
            }
            self.assertTrue(expected.issubset(set(payload["created_surfaces"])))

    def test_doctor_surface_reports_service_monorepo_as_supported(self) -> None:
        explanation = explain_template_composition(["service", "monorepo"])
        self.assertTrue(explanation.supported)
        self.assertEqual(("monorepo", "service"), explanation.normalized_overlays)

        run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_scaffold.py",
                "doctor-composition",
                "--overlays",
                "service",
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
        self.assertEqual(["monorepo", "service"], payload["normalized_overlays"])


if __name__ == "__main__":
    unittest.main()
