from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_registry import RegistryError
from tools.governance.template_scaffold import (
    load_scaffold_manifest,
    list_scaffold_manifests,
    realize_repository_scaffold,
    scaffold_document,
)


class TemplateScaffoldTests(unittest.TestCase):
    def test_scaffold_manifest_inventory_is_available(self) -> None:
        manifests = list_scaffold_manifests()
        names = {manifest.template_name for manifest in manifests}
        self.assertIn("universal-base", names)
        self.assertIn("django", names)
        self.assertIn("node-typescript-service", names)
        self.assertIn("cli-worker", names)

    def test_scaffold_output_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first = scaffold_document(
                family="verification",
                artifact_id="verify.example",
                title="Verify Example",
                output_path=Path(tmp) / "first.md",
                overlays=["django"],
            )
            second = scaffold_document(
                family="verification",
                artifact_id="verify.example",
                title="Verify Example",
                output_path=Path(tmp) / "second.md",
                overlays=["django"],
            )
            self.assertEqual(first.read_text(), second.read_text())

    def test_repository_scaffold_realization_creates_required_surfaces(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            selection = realize_repository_scaffold(
                "universal-base",
                Path(tmp),
                overlays=["django"],
                include_optional=True,
            )
            self.assertTrue(selection.exists())
            payload = json.loads(selection.read_text())
            self.assertIn("django", payload["overlays"])
            self.assertTrue((Path(tmp) / "docs/governance").is_dir())
            self.assertTrue((Path(tmp) / "tools/templates").is_dir())
            self.assertTrue((Path(tmp) / "backend").is_dir())

    def test_overlay_composition_for_node_service_in_monorepo_is_supported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            selection = realize_repository_scaffold(
                "universal-base",
                Path(tmp),
                overlays=["node-typescript-service", "monorepo"],
                include_optional=False,
            )
            self.assertTrue(selection.exists())
            self.assertTrue((Path(tmp) / "package.json").is_file())
            self.assertTrue((Path(tmp) / "packages").is_dir())
            self.assertTrue((Path(tmp) / "services").is_dir())

    def test_overlay_composition_for_cli_worker_and_python_package_is_supported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            selection = realize_repository_scaffold(
                "universal-base",
                Path(tmp),
                overlays=["cli-worker", "python-package"],
                include_optional=False,
            )
            self.assertTrue(selection.exists())
            self.assertTrue((Path(tmp) / "bin").is_dir())
            self.assertTrue((Path(tmp) / "jobs").is_dir())
            self.assertTrue((Path(tmp) / "src").is_dir())

    def test_overlay_manifest_must_match_base_template(self) -> None:
        manifest = load_scaffold_manifest("django")
        self.assertEqual("overlay", manifest.template_type)
        self.assertEqual("universal-base", manifest.base_template)

    def test_multiple_stack_overlays_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(RegistryError):
                scaffold_document(
                    family="pipeline",
                    artifact_id="pipeline.invalid",
                    title="Invalid Pipeline",
                    output_path=Path(tmp) / "invalid.md",
                    overlays=["laravel", "django"],
                )

    def test_unknown_overlay_is_rejected_for_repository_realization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(RegistryError):
                realize_repository_scaffold("universal-base", Path(tmp), overlays=["unknown"])

    def test_incompatible_overlay_pair_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(RegistryError):
                realize_repository_scaffold(
                    "universal-base",
                    Path(tmp),
                    overlays=["laravel", "cli-worker"],
                )

    def test_list_templates_cli_outputs_json(self) -> None:
        run = subprocess.run(
            [
                sys.executable,
                "tools/templates/list_templates.py",
                "--output",
                "json",
            ],
            cwd=Path(__file__).resolve().parents[2],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(run.stdout)
        names = {item["template_name"] for item in payload}
        self.assertIn("universal-base", names)


if __name__ == "__main__":
    unittest.main()
