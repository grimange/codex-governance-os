from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.governance.template_registry import RegistryError
from tools.governance.template_scaffold import scaffold_document


class TemplateScaffoldTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
