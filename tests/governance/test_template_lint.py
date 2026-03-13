from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_lint import (
    _result_to_json,
    format_result_text,
    lint_template,
    lint_templates,
    validate_document,
)
from tools.governance.template_scaffold import scaffold_document


class TemplateLintTests(unittest.TestCase):
    fixtures = Path(__file__).resolve().parent / "fixtures" / "lint"

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

    def test_valid_fixture_passes_as_is(self) -> None:
        result = lint_template(self.fixtures / "valid-pipeline-template.md")
        self.assertEqual("VALID_AS_IS", result.decision)
        self.assertEqual((), result.issues)

    def test_invalid_fixture_blocks_with_portability_and_placeholder_findings(self) -> None:
        result = lint_template(self.fixtures / "invalid-universal-rule-template.md")
        self.assertEqual("BLOCKED", result.decision)
        rule_ids = {issue.rule_id for issue in result.issues}
        self.assertIn("UTL-005", rule_ids)
        self.assertIn("UTL-006", rule_ids)
        self.assertIn("UTL-007", rule_ids)

    def test_normalized_fixture_reports_normalized_and_valid(self) -> None:
        result = lint_template(self.fixtures / "normalized-skill-template.md")
        self.assertEqual("NORMALIZED_AND_VALID", result.decision)
        self.assertTrue(result.normalizations)

    def test_repo_lint_on_fixture_root_is_deterministic(self) -> None:
        first = lint_templates(roots=(self.fixtures,))
        second = lint_templates(roots=(self.fixtures,))
        self.assertEqual(
            json.dumps([_result_to_json(result) for result in first], sort_keys=True),
            json.dumps([_result_to_json(result) for result in second], sort_keys=True),
        )

    def test_cli_json_and_text_outputs_work(self) -> None:
        fixture = self.fixtures / "valid-pipeline-template.md"
        json_run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_lint.py",
                "lint-template",
                str(fixture),
                "--family",
                "pipeline",
                "--output",
                "json",
            ],
            cwd=Path(__file__).resolve().parents[2],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(json_run.stdout)
        self.assertEqual("VALID_AS_IS", payload["decision"])

        text_result = lint_template(fixture, family="pipeline")
        rendered = format_result_text(text_result)
        self.assertIn("VALID_AS_IS", rendered)

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
