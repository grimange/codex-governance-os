from __future__ import annotations

import dataclasses
import unittest

from tools.governance.template_scaffold import list_scaffold_manifests
from tools.templates.composition_contract import (
    load_template_capability_registry,
    validate_capability_composition,
    verify_capability_matrix_preservation,
)


class TemplateCapabilityCompositionTests(unittest.TestCase):
    def test_capability_registry_loads_expected_roles(self) -> None:
        registry = load_template_capability_registry()
        self.assertIn("runtime-environment", registry.capabilities)
        self.assertIn("framework", registry.roles)
        self.assertIn("topology", registry.roles["framework"])

    def test_capability_resolution_preserves_supported_matrix_entries(self) -> None:
        manifests = list_scaffold_manifests()
        for pair in (
            ["django", "scheduler"],
            ["laravel", "monorepo"],
            ["laravel", "scheduler"],
            ["service", "monorepo"],
            ["cli-worker", "python-package"],
            ["cli-worker", "monorepo", "python-package"],
            ["scheduler", "cli-worker"],
            ["scheduler", "monorepo"],
            ["scheduler", "python-package"],
            ["scheduler", "cli-worker", "monorepo"],
            ["scheduler", "cli-worker", "python-package"],
        ):
            result = validate_capability_composition(manifests, pair)
            self.assertTrue(result.supported, msg=f"expected supported pair: {pair}")
            self.assertEqual("certified-multi-overlay", result.reason_code)

    def test_capability_resolution_preserves_explicit_rejections(self) -> None:
        manifests = list_scaffold_manifests()
        cases = (
            (["laravel", "cli-worker"], "worker-model-collision", "missing Laravel worker composition contract"),
        )
        for overlays, expected_code, expected_reason in cases:
            with self.subTest(overlays=overlays):
                result = validate_capability_composition(manifests, overlays)
                self.assertFalse(result.supported)
                self.assertEqual("explicitly-rejected", result.reason_code)
                self.assertEqual(expected_code, result.conflict_code)
                self.assertEqual(expected_reason, result.rejection_reason)

    def test_capability_roles_block_generic_incompatible_pair(self) -> None:
        manifests = list_scaffold_manifests()
        result = validate_capability_composition(manifests, ["service", "python-package"])
        self.assertFalse(result.supported)
        self.assertEqual("capability-role-conflict", result.reason_code)
        self.assertEqual("package-application-role-collision", result.conflict_code)
        self.assertEqual("composition roles collide: package vs service-host", result.rejection_reason)

    def test_required_capabilities_are_enforced(self) -> None:
        manifests = list_scaffold_manifests()
        adjusted = []
        for manifest in manifests:
            if manifest.template_name == "universal-base":
                adjusted.append(
                    dataclasses.replace(
                        manifest,
                        provides=("governance-foundation",),
                    )
                )
            else:
                adjusted.append(manifest)
        result = validate_capability_composition(adjusted, ["cli-worker", "monorepo"])
        self.assertFalse(result.supported)
        self.assertEqual("missing-required-capability", result.reason_code)
        self.assertIn("runtime-environment", result.rejection_reason)

    def test_capability_preservation_matches_live_certified_matrix(self) -> None:
        report = verify_capability_matrix_preservation(list_scaffold_manifests())
        self.assertTrue(report.valid, msg="\n".join(report.errors))


if __name__ == "__main__":
    unittest.main()
