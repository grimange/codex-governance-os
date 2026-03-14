from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_registry import RegistryError
from tools.governance.template_scaffold import list_scaffold_manifests
from tools.templates.composition_contract import (
    doctor_command_hint,
    explain_template_composition,
    format_rejection_message,
    validate_manifest_inventory,
    validate_template_composition,
)


class TemplateCompositionContractTests(unittest.TestCase):
    def test_base_and_single_overlay_realizations_are_supported(self) -> None:
        self.assertTrue(validate_template_composition([]).supported)
        self.assertTrue(validate_template_composition(["django"]).supported)

    def test_certified_multi_overlay_is_supported(self) -> None:
        result = validate_template_composition(["monorepo", "node-typescript-service"])
        self.assertTrue(result.supported)
        self.assertEqual(
            ("monorepo", "node-typescript-service"),
            result.normalized_overlays,
        )
        laravel_monorepo = validate_template_composition(["laravel", "monorepo"])
        self.assertTrue(laravel_monorepo.supported)
        self.assertEqual(("laravel", "monorepo"), laravel_monorepo.normalized_overlays)
        django_monorepo = validate_template_composition(["django", "monorepo"])
        self.assertTrue(django_monorepo.supported)
        self.assertEqual(("django", "monorepo"), django_monorepo.normalized_overlays)
        service_monorepo = validate_template_composition(["service", "monorepo"])
        self.assertTrue(service_monorepo.supported)
        self.assertEqual(("monorepo", "service"), service_monorepo.normalized_overlays)

    def test_explicit_rejection_has_deterministic_message(self) -> None:
        result = validate_template_composition(["laravel", "cli-worker"])
        self.assertFalse(result.supported)
        message = format_rejection_message(result, ["laravel", "cli-worker"])
        self.assertIn("unsupported template composition", message)
        self.assertIn("requested: cli-worker + laravel", message)
        self.assertIn("allowed: see docs/contracts/universal-template-composition-contract.md", message)
        self.assertIn(
            "Run: python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker",
            message,
        )

    def test_explain_surface_reports_supported_and_closest_supported(self) -> None:
        supported = explain_template_composition(["cli-worker", "python-package"])
        self.assertTrue(supported.supported)
        self.assertEqual((), supported.closest_supported)

        unsupported = explain_template_composition(["laravel", "cli-worker"])
        self.assertFalse(unsupported.supported)
        self.assertEqual("docs/contracts/universal-template-composition-contract.md", unsupported.decision_source)
        self.assertIn(("cli-worker", "python-package"), unsupported.closest_supported)
        self.assertEqual(
            "python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker",
            doctor_command_hint(["laravel", "cli-worker"]),
        )

    def test_manifest_inventory_validation_rejects_unsupported_pair(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(__file__).resolve().parents[2] / "docs/codex/templates/manifests"
            shutil.copytree(source, Path(tmp), dirs_exist_ok=True)
            laravel_path = Path(tmp) / "laravel.json"
            payload = json.loads(laravel_path.read_text())
            payload["compatible_overlays"] = ["cli-worker"]
            laravel_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

            with self.assertRaises(RegistryError):
                list_scaffold_manifests(Path(tmp))

            manifests = []
            for path in sorted(Path(tmp).glob("*.json")):
                manifests.append(type("Manifest", (), json.loads(path.read_text()))())
            validation = validate_manifest_inventory(manifests)
            self.assertFalse(validation.valid)
            self.assertIn(
                "laravel declares unsupported composition cli-worker + laravel; run: python tools/governance/template_scaffold.py doctor-composition --overlays cli-worker laravel",
                validation.errors,
            )


if __name__ == "__main__":
    unittest.main()
