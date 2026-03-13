from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.governance.template_scaffold import (
    list_scaffold_manifests,
    realize_repository_scaffold,
)


class TemplateConformanceTests(unittest.TestCase):
    governance_core = {
        "docs/governance",
        "docs/pipelines",
        "docs/pipelines/governance",
        "docs/codex/templates",
        "docs/governance/registries/templates",
        "tools/governance",
        "tools/templates",
        "artifacts",
    }

    def test_supported_fixture_matrix_realizes_without_governance_drift(self) -> None:
        fixtures = (
            ("minimal-governed-repo", []),
            ("laravel-application", ["laravel"]),
            ("django-application", ["django"]),
            ("python-package", ["python-package"]),
            ("php-package", ["php-package"]),
            ("service-repository", ["service"]),
            ("monorepo", ["monorepo"]),
            ("node-typescript-service", ["node-typescript-service"]),
            ("cli-worker", ["cli-worker"]),
            ("node-typescript-service-in-monorepo", ["node-typescript-service", "monorepo"]),
            ("python-cli-worker", ["python-package", "cli-worker"]),
            ("php-cli-worker", ["php-package", "cli-worker"]),
            ("monorepo-cli-worker", ["monorepo", "cli-worker"]),
            ("node-cli-worker", ["node-typescript-service", "cli-worker"]),
        )

        manifests = {manifest.template_name: manifest for manifest in list_scaffold_manifests()}
        base_manifest = manifests["universal-base"]

        for fixture_name, overlays in fixtures:
            with self.subTest(fixture=fixture_name):
                with tempfile.TemporaryDirectory() as tmp:
                    selection = realize_repository_scaffold(
                        "universal-base",
                        Path(tmp),
                        overlays=list(overlays),
                        include_optional=False,
                    )
                    self.assertTrue(selection.exists())
                    for surface in self.governance_core:
                        self.assertTrue(
                            (Path(tmp) / surface).is_dir(),
                            msg=f"{fixture_name} missing governance core surface {surface}",
                        )
                    for overlay_name in overlays:
                        overlay = manifests[overlay_name]
                        self.assertEqual("overlay", overlay.template_type)
                        self.assertEqual("universal-base", overlay.base_template)
                        self.assertTrue(
                            set(overlay.required_surfaces).isdisjoint(self.governance_core),
                            msg=f"{overlay_name} redefines governance core surfaces",
                        )
                        for surface in overlay.required_surfaces:
                            target = Path(tmp) / surface
                            self.assertTrue(
                                target.exists(),
                                msg=f"{fixture_name} missing overlay surface {surface}",
                            )
                    for overlay_name in overlays:
                        self.assertIn(overlay_name, base_manifest.compatible_overlays)


if __name__ == "__main__":
    unittest.main()
