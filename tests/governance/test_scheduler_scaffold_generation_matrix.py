from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_registry import RegistryError
from tools.governance.template_scaffold import realize_repository_scaffold


class SchedulerScaffoldGenerationMatrixTests(unittest.TestCase):
    def test_certified_scheduler_compositions_generate_expected_surfaces(self) -> None:
        cases = (
            (
                "scheduler-only",
                ["scheduler"],
                {
                    "scheduler",
                    "scheduler/schedule.py",
                    "scheduler/scheduler_runtime.py",
                },
            ),
            (
                "scheduler-plus-cli-worker",
                ["scheduler", "cli-worker"],
                {
                    "scheduler",
                    "scheduler/schedule.py",
                    "scheduler/scheduler_runtime.py",
                    "bin",
                    "jobs",
                    "worker",
                },
            ),
            (
                "scheduler-plus-django",
                ["scheduler", "django"],
                {
                    "scheduler",
                    "scheduler/schedule.py",
                    "scheduler/scheduler_runtime.py",
                    "backend",
                    "config",
                    "apps",
                    "manage.py",
                    "project/settings.py",
                    "project/urls.py",
                    "project/asgi.py",
                    "project/celery.py",
                    "project/scheduler.py",
                },
            ),
            (
                "scheduler-plus-laravel",
                ["scheduler", "laravel"],
                {
                    "scheduler",
                    "scheduler/schedule.py",
                    "scheduler/scheduler_runtime.py",
                    "app",
                    "bootstrap",
                    "routes",
                    "config",
                    "app/Console/Kernel.php",
                    "app/Console/Commands",
                    "routes/console.php",
                    "config/scheduler.php",
                },
            ),
            (
                "scheduler-plus-monorepo",
                ["scheduler", "monorepo"],
                {
                    "scheduler",
                    "scheduler/schedule.py",
                    "scheduler/scheduler_runtime.py",
                    "packages",
                    "services",
                    "shared",
                },
            ),
            (
                "scheduler-plus-python-package",
                ["scheduler", "python-package"],
                {
                    "scheduler",
                    "scheduler/schedule.py",
                    "scheduler/scheduler_runtime.py",
                    "src",
                    "tests",
                    "docs",
                },
            ),
            (
                "scheduler-plus-cli-worker-plus-monorepo",
                ["scheduler", "cli-worker", "monorepo"],
                {
                    "scheduler",
                    "scheduler/schedule.py",
                    "scheduler/scheduler_runtime.py",
                    "bin",
                    "jobs",
                    "worker",
                    "packages",
                    "services",
                    "shared",
                },
            ),
            (
                "scheduler-plus-cli-worker-plus-python-package",
                ["scheduler", "cli-worker", "python-package"],
                {
                    "scheduler",
                    "scheduler/schedule.py",
                    "scheduler/scheduler_runtime.py",
                    "bin",
                    "jobs",
                    "worker",
                    "src",
                    "tests",
                    "docs",
                },
            ),
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
                    self.assertTrue(
                        expected.issubset(created),
                        msg=f"{case_name} missing expected generated surfaces",
                    )
                    self.assertEqual(sorted(overlays), payload["overlays"])

    def test_scheduler_generation_preserves_coexisting_overlay_surfaces(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            selection = realize_repository_scaffold(
                "universal-base",
                Path(tmp),
                overlays=["scheduler", "cli-worker", "monorepo"],
                include_optional=False,
            )
            payload = json.loads(selection.read_text())
            self.assertIn("scheduler/scheduler_runtime.py", payload["created_surfaces"])
            self.assertIn("bin", payload["created_surfaces"])
            self.assertIn("packages", payload["created_surfaces"])
            self.assertTrue((Path(tmp) / "scheduler/scheduler_runtime.py").is_file())
            self.assertTrue((Path(tmp) / "bin").is_dir())
            self.assertTrue((Path(tmp) / "packages").is_dir())

    def test_representative_unsupported_scheduler_compositions_fail_closed(self) -> None:
        cases = (
            ("scheduler-plus-service", ["scheduler", "service"]),
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
                    self.assertFalse((Path(tmp) / "scheduler").exists())


if __name__ == "__main__":
    unittest.main()
