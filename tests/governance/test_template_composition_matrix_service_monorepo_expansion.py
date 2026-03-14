from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_registry import RegistryError
from tools.governance.template_scaffold import realize_repository_scaffold
from tools.templates.composition_contract import explain_template_composition


class TemplateCompositionMatrixServiceMonorepoExpansionTests(unittest.TestCase):
    supported_cases = (
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

    def test_supported_matrix_after_service_monorepo_expansion_is_admitted_everywhere(self) -> None:
        for overlays in self.supported_cases:
            with self.subTest(overlays=overlays or ["base-only"]):
                explanation = explain_template_composition(overlays)
                self.assertTrue(explanation.supported)
                code, payload = self._doctor(list(overlays))
                self.assertEqual(0, code)
                self.assertTrue(payload["supported"])
                self.assertEqual(list(explanation.normalized_overlays), payload["normalized_overlays"])
                with tempfile.TemporaryDirectory() as tmp:
                    selection = realize_repository_scaffold(
                        "universal-base",
                        Path(tmp),
                        overlays=list(overlays),
                    )
                    created = set(json.loads(selection.read_text())["created_surfaces"])
                    self.assertTrue(created)

    def test_rejected_matrix_after_service_monorepo_expansion_remains_fail_closed(self) -> None:
        for overlays in self.rejected_cases:
            with self.subTest(overlays=overlays):
                explanation = explain_template_composition(overlays)
                self.assertFalse(explanation.supported)
                code, payload = self._doctor(list(overlays))
                self.assertNotEqual(0, code)
                self.assertFalse(payload["supported"])
                self.assertEqual(explanation.reason_code, payload["reason_code"])
                with tempfile.TemporaryDirectory() as tmp:
                    with self.assertRaises(RegistryError):
                        realize_repository_scaffold(
                            "universal-base",
                            Path(tmp),
                            overlays=list(overlays),
                        )


if __name__ == "__main__":
    unittest.main()
