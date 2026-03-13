from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_registry import RegistryError
from tools.governance.template_scaffold import realize_repository_scaffold


class TemplateCompositionMatrixTests(unittest.TestCase):
    def test_supported_composition_matrix_realizes_expected_surfaces(self) -> None:
        cases = (
            ("base-only", [], {"docs/governance", "tools/templates"}),
            ("node-typescript-service-plus-monorepo", ["node-typescript-service", "monorepo"], {"package.json", "packages", "services", "shared"}),
            ("cli-worker-plus-monorepo", ["cli-worker", "monorepo"], {"bin", "jobs", "worker", "packages", "services", "shared"}),
            ("cli-worker-plus-php-package", ["cli-worker", "php-package"], {"bin", "jobs", "worker", "src", "tests", "config"}),
            ("cli-worker-plus-python-package", ["cli-worker", "python-package"], {"bin", "jobs", "worker", "src", "tests", "docs"}),
            ("cli-worker-plus-node-typescript-service", ["cli-worker", "node-typescript-service"], {"bin", "jobs", "worker", "package.json", "src", "tests", "scripts"}),
        )

        for case_name, overlays, expected in cases:
            with self.subTest(case=case_name):
                with tempfile.TemporaryDirectory() as tmp:
                    selection = realize_repository_scaffold(
                        "universal-base",
                        Path(tmp),
                        overlays=list(overlays),
                        include_optional=False,
                    )
                    payload = json.loads(selection.read_text())
                    created = set(payload["created_surfaces"])
                    self.assertTrue(expected.issubset(created), msg=f"{case_name} missing expected surfaces")

    def test_invalid_composition_matrix_fails_closed(self) -> None:
        cases = (
            ("laravel-plus-cli-worker", ["laravel", "cli-worker"]),
            ("django-plus-monorepo", ["django", "monorepo"]),
            ("service-plus-monorepo", ["service", "monorepo"]),
            ("laravel-plus-django", ["laravel", "django"]),
        )

        for case_name, overlays in cases:
            with self.subTest(case=case_name):
                with tempfile.TemporaryDirectory() as tmp:
                    with self.assertRaises(RegistryError):
                        realize_repository_scaffold(
                            "universal-base",
                            Path(tmp),
                            overlays=list(overlays),
                            include_optional=False,
                        )


if __name__ == "__main__":
    unittest.main()
