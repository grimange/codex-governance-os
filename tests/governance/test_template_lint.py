from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.governance.template_lint import validate_document
from tools.governance.template_scaffold import scaffold_document


class TemplateLintTests(unittest.TestCase):
    def test_scaffolded_pipeline_passes_lint(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = scaffold_document(
                family="pipeline",
                artifact_id="pipeline.test.example",
                title="Example Pipeline",
                output_path=Path(tmp) / "pipeline.md",
                overlays=["python-package"],
            )
            issues = validate_document(path, "pipeline")
            self.assertEqual([], issues)

    def test_missing_required_section_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.md"
            path.write_text(
                "---\n"
                'id: "bad.rule"\n'
                'title: "Bad Rule"\n'
                "status: proposed\n"
                "category: governance\n"
                "stage: policy\n"
                'objective: "x"\n'
                "depends_on: []\n"
                "outputs: []\n"
                "success_criteria: []\n"
                "governance_mode: fail-closed\n"
                "execution_mode: advisory-then-enforcing\n"
                "restrictions: []\n"
                "non_claims: []\n"
                "---\n\n"
                "# Bad Rule\n\n"
                "## Policy Intent\n\nREQUIRED\n"
            )
            issues = validate_document(path, "rule")
            self.assertTrue(any("Missing required section" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
