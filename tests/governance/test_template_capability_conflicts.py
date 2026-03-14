from __future__ import annotations

import dataclasses
import unittest

from tools.governance.template_scaffold import list_scaffold_manifests
from tools.templates.composition_contract import validate_capability_composition


class TemplateCapabilityConflictTests(unittest.TestCase):
    def test_framework_conflict_returns_cross_framework_taxonomy(self) -> None:
        manifests = list_scaffold_manifests()
        result = validate_capability_composition(manifests, ["django", "laravel"])
        self.assertFalse(result.supported)
        self.assertEqual("explicitly-rejected", result.reason_code)
        self.assertEqual("cross-framework-application-collision", result.conflict_code)

    def test_worker_conflict_returns_worker_model_taxonomy(self) -> None:
        manifests = list_scaffold_manifests()
        result = validate_capability_composition(manifests, ["laravel", "cli-worker"])
        self.assertFalse(result.supported)
        self.assertEqual("explicitly-rejected", result.reason_code)
        self.assertEqual("worker-model-collision", result.conflict_code)

    def test_runtime_conflict_returns_runtime_ownership_taxonomy(self) -> None:
        manifests = list_scaffold_manifests()
        adjusted = []
        for manifest in manifests:
            if manifest.template_name == "service":
                adjusted.append(
                    dataclasses.replace(
                        manifest,
                        composition_role="worker",
                        provides=manifest.provides + ("python-runtime",),
                    )
                )
            else:
                adjusted.append(manifest)
        result = validate_capability_composition(adjusted, ["service", "python-package"])
        self.assertFalse(result.supported)
        self.assertEqual("capability-conflict", result.reason_code)
        self.assertEqual("runtime-ownership-collision", result.conflict_code)

    def test_package_application_role_collision_is_classified(self) -> None:
        manifests = list_scaffold_manifests()
        result = validate_capability_composition(manifests, ["service", "python-package"])
        self.assertFalse(result.supported)
        self.assertEqual("capability-role-conflict", result.reason_code)
        self.assertEqual("package-application-role-collision", result.conflict_code)

    def test_workspace_orchestration_collision_is_classified(self) -> None:
        manifests = list_scaffold_manifests()
        adjusted = []
        for manifest in manifests:
            adjusted.append(manifest)
            if manifest.template_name == "monorepo":
                adjusted.append(
                    dataclasses.replace(
                        manifest,
                        template_name="workspace-topology",
                    )
                )
        result = validate_capability_composition(adjusted, ["monorepo", "workspace-topology"])
        self.assertFalse(result.supported)
        self.assertEqual("capability-conflict", result.reason_code)
        self.assertEqual("workspace-orchestration-collision", result.conflict_code)


if __name__ == "__main__":
    unittest.main()
