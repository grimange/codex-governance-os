from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_scaffold import list_scaffold_manifests
from tools.templates.composition_contract import (
    detect_contract_drift,
    load_contract_document_matrix,
)


class TemplateCompositionContractDriftTests(unittest.TestCase):
    def test_live_contract_runtime_and_manifest_surfaces_are_aligned(self) -> None:
        manifests = list_scaffold_manifests()
        report = detect_contract_drift(manifests)
        self.assertTrue(report.valid, msg="\n".join(report.errors))

        document = load_contract_document_matrix()
        self.assertIn(("django", "monorepo"), document.certified_multi_overlay)
        self.assertIn(("monorepo", "service"), document.certified_multi_overlay)
        self.assertIn(("cli-worker", "python-package"), document.certified_multi_overlay)
        self.assertIn(("cli-worker", "laravel"), document.certified_fail_closed)

    def test_contract_document_drift_is_detected(self) -> None:
        repo = Path(__file__).resolve().parents[2]
        source = repo / "docs/contracts/universal-template-composition-contract.md"
        with tempfile.TemporaryDirectory() as tmp:
            drifted = Path(tmp) / "universal-template-composition-contract.md"
            text = source.read_text()
            text = text.replace(
                "- `django + monorepo`\n",
                "- `django + monorepo`\n- `django + cli-worker`\n",
            )
            drifted.write_text(text)

            report = detect_contract_drift(
                list_scaffold_manifests(),
                contract_path=drifted,
            )
            self.assertFalse(report.valid)
            self.assertIn(
                "CONTRACT_DRIFT_DETECTED: contract documents unsupported runtime support for cli-worker + django",
                report.errors,
            )

    def test_manifest_drift_is_detected(self) -> None:
        repo = Path(__file__).resolve().parents[2]
        with tempfile.TemporaryDirectory() as tmp:
            manifest_dir = Path(tmp)
            shutil.copytree(repo / "docs/codex/templates/manifests", manifest_dir, dirs_exist_ok=True)
            laravel_path = manifest_dir / "laravel.json"
            payload = json.loads(laravel_path.read_text())
            payload["compatible_overlays"] = ["cli-worker"]
            laravel_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

            manifests = []
            for path in sorted(manifest_dir.glob("*.json")):
                raw = json.loads(path.read_text())
                manifests.append(type("Manifest", (), raw)())

            report = detect_contract_drift(manifests)
            self.assertFalse(report.valid)
            self.assertIn(
                "CONTRACT_DRIFT_DETECTED: laravel declares unsupported composition cli-worker + laravel; run: python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker laravel",
                report.errors,
            )


if __name__ == "__main__":
    unittest.main()
