from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_scaffold import list_scaffold_manifests
from tools.templates.composition_contract import (
    load_compound_composition_ledger,
    load_composition_matrix_snapshot,
    verify_composition_matrix,
)


class TemplateCompositionDriftTests(unittest.TestCase):
    def test_live_snapshot_matches_runtime_and_manifests(self) -> None:
        manifests = list_scaffold_manifests()
        report = verify_composition_matrix(manifests)
        self.assertTrue(report.valid, msg="\n".join(report.errors))

        snapshot = load_composition_matrix_snapshot()
        ledger = load_compound_composition_ledger()
        self.assertIn(("django", "scheduler"), snapshot.supported)
        self.assertIn(("cli-worker", "monorepo", "python-package", "scheduler"), snapshot.supported)
        self.assertIn(("laravel", "monorepo"), snapshot.supported)
        self.assertIn(("laravel", "monorepo", "scheduler"), snapshot.supported)
        self.assertIn(("cli-worker", "monorepo", "python-package"), snapshot.supported)
        self.assertIn(("cli-worker", "scheduler"), snapshot.supported)
        self.assertIn(("laravel", "scheduler"), snapshot.supported)
        self.assertIn(("monorepo", "scheduler"), snapshot.supported)
        self.assertIn(("python-package", "scheduler"), snapshot.supported)
        self.assertIn(("cli-worker", "monorepo", "scheduler"), snapshot.supported)
        self.assertIn(("cli-worker", "python-package", "scheduler"), snapshot.supported)
        self.assertIn(
            (("cli-worker", "laravel"), "missing Laravel worker composition contract"),
            snapshot.explicitly_rejected,
        )
        self.assertIn(("cli-worker", "monorepo", "python-package", "scheduler"), ledger.certified_compounds)
        self.assertIn(("laravel", "monorepo", "scheduler"), ledger.certified_compounds)
        self.assertIn(("django", "monorepo", "scheduler"), ledger.fail_closed_triple_boundaries)

    def test_snapshot_drift_is_detected_when_supported_pair_is_added(self) -> None:
        repo = Path(__file__).resolve().parents[2]
        source = repo / "tools/governance/template_composition_matrix.json"
        with tempfile.TemporaryDirectory() as tmp:
            drifted = Path(tmp) / "template_composition_matrix.json"
            payload = json.loads(source.read_text())
            payload["supported"].append(["django", "cli-worker"])
            drifted.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

            report = verify_composition_matrix(
                list_scaffold_manifests(),
                snapshot_path=drifted,
            )
            self.assertFalse(report.valid)
            self.assertIn(
                "COMPOSITION_MATRIX_DRIFT: snapshot declares unsupported runtime support for cli-worker + django",
                report.errors,
            )

    def test_snapshot_drift_is_detected_when_rejection_reason_changes(self) -> None:
        repo = Path(__file__).resolve().parents[2]
        source = repo / "tools/governance/template_composition_matrix.json"
        with tempfile.TemporaryDirectory() as tmp:
            drifted = Path(tmp) / "template_composition_matrix.json"
            payload = json.loads(source.read_text())
            payload["explicitly_rejected"][0]["reason"] = "runtime model conflict"
            drifted.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

            report = verify_composition_matrix(
                list_scaffold_manifests(),
                snapshot_path=drifted,
            )
            self.assertFalse(report.valid)
            self.assertTrue(
                any("rejection reason mismatch for cli-worker + laravel" in error for error in report.errors)
            )

    def test_verify_composition_matrix_cli_reports_success(self) -> None:
        run = subprocess.run(
            [
                sys.executable,
                "tools/governance/template_scaffold.py",
                "verify-composition-matrix",
                "--output",
                "json",
            ],
            cwd=Path(__file__).resolve().parents[2],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, run.returncode)
        payload = json.loads(run.stdout)
        self.assertTrue(payload["valid"])
        self.assertEqual([], payload["errors"])

    def test_ledger_drift_is_detected_when_unknown_compound_is_certified(self) -> None:
        repo = Path(__file__).resolve().parents[2]
        source = repo / "docs/governance/compound-composition-certification-ledger.md"
        with tempfile.TemporaryDirectory() as tmp:
            drifted = Path(tmp) / "compound-composition-certification-ledger.md"
            text = source.read_text()
            replacement = (
                "## Certified Compound Compositions\n\n"
                "- `cli-worker + monorepo + python-package + scheduler`\n"
                "- `cli-worker + monorepo + python-package`\n"
                "- `cli-worker + monorepo + scheduler`\n"
                "- `cli-worker + python-package + scheduler`\n"
                "- `laravel + monorepo + scheduler`\n"
                "- `django + monorepo + scheduler`\n"
            )
            drifted.write_text(
                text.replace(
                    "## Certified Compound Compositions\n\n"
                    "- `cli-worker + monorepo + python-package + scheduler`\n"
                    "- `cli-worker + monorepo + python-package`\n"
                    "- `cli-worker + monorepo + scheduler`\n"
                    "- `cli-worker + python-package + scheduler`\n"
                    "- `laravel + monorepo + scheduler`\n",
                    replacement,
                )
            )

            report = verify_composition_matrix(
                list_scaffold_manifests(),
                ledger_path=drifted,
            )
            self.assertFalse(report.valid)
            self.assertIn(
                "COMPOSITION_LEDGER_DRIFT: ledger certifies compound composition missing from runtime django + monorepo + scheduler",
                report.errors,
            )


if __name__ == "__main__":
    unittest.main()
