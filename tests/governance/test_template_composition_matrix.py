from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_registry import RegistryError
from tools.governance.template_scaffold import realize_repository_scaffold
from tools.templates.composition_contract import explain_template_composition


class TemplateCompositionMatrixTests(unittest.TestCase):
    def test_supported_composition_matrix_realizes_expected_surfaces(self) -> None:
        cases = (
            ("base-only", [], {"docs/governance", "tools/templates"}),
            ("scheduler-plus-django", ["scheduler", "django"], {"backend", "config", "apps", "scheduler", "scheduler/schedule.py", "scheduler/scheduler_runtime.py", "manage.py", "project/settings.py", "project/urls.py", "project/asgi.py", "project/celery.py", "project/scheduler.py"}),
            ("django-plus-monorepo", ["django", "monorepo"], {"apps/backend/django-service/manage.py", "apps/backend/django-service/project/settings.py", "packages", "services", "shared"}),
            ("service-plus-monorepo", ["service", "monorepo"], {"services/service-app/src", "services/service-app/tests", "services/service-app/pyproject.toml", "services/service-app/README.md", "services/service-app/service_entrypoint", "packages", "services", "shared"}),
            ("node-typescript-service-plus-monorepo", ["node-typescript-service", "monorepo"], {"package.json", "packages", "services", "shared"}),
            ("cli-worker-plus-monorepo", ["cli-worker", "monorepo"], {"bin", "jobs", "worker", "packages", "services", "shared"}),
            ("cli-worker-plus-monorepo-plus-python-package", ["cli-worker", "monorepo", "python-package"], {"bin", "jobs", "worker", "packages", "services", "shared", "src", "tests", "docs"}),
            ("scheduler-plus-cli-worker", ["scheduler", "cli-worker"], {"scheduler", "scheduler/schedule.py", "scheduler/scheduler_runtime.py", "bin", "jobs", "worker"}),
            ("scheduler-plus-laravel", ["scheduler", "laravel"], {"app", "bootstrap", "routes", "config", "scheduler", "scheduler/schedule.py", "scheduler/scheduler_runtime.py", "app/Console/Kernel.php", "app/Console/Commands", "routes/console.php", "config/scheduler.php"}),
            ("scheduler-plus-monorepo", ["scheduler", "monorepo"], {"scheduler", "scheduler/schedule.py", "scheduler/scheduler_runtime.py", "packages", "services", "shared"}),
            ("scheduler-plus-python-package", ["scheduler", "python-package"], {"scheduler", "scheduler/schedule.py", "scheduler/scheduler_runtime.py", "src", "tests", "docs"}),
            ("scheduler-plus-cli-worker-plus-monorepo", ["scheduler", "cli-worker", "monorepo"], {"scheduler", "scheduler/schedule.py", "scheduler/scheduler_runtime.py", "bin", "jobs", "worker", "packages", "services", "shared"}),
            ("scheduler-plus-cli-worker-plus-python-package", ["scheduler", "cli-worker", "python-package"], {"scheduler", "scheduler/schedule.py", "scheduler/scheduler_runtime.py", "bin", "jobs", "worker", "src", "tests", "docs"}),
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

    def test_explicitly_rejected_pairs_retain_canonical_reasons(self) -> None:
        cases = (
            (["laravel", "cli-worker"], "missing Laravel worker composition contract"),
            (["laravel", "django"], "cross-framework application collision"),
        )

        for overlays, expected_reason in cases:
            with self.subTest(overlays=overlays):
                explanation = explain_template_composition(overlays)
                self.assertFalse(explanation.supported)
                self.assertEqual("explicitly-rejected", explanation.reason_code)
                self.assertEqual(expected_reason, explanation.rejection_reason)


if __name__ == "__main__":
    unittest.main()
