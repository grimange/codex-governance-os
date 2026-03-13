from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_registry import RegistryError, load_registry


class TemplateRegistryTests(unittest.TestCase):
    def test_default_registry_loads(self) -> None:
        registry = load_registry()
        self.assertIn("pipeline", registry.templates)
        self.assertIn("laravel", registry.overlays)

    def test_duplicate_aliases_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "registry.yaml"
            path.write_text(
                json.dumps(
                    {
                        "schema_version": "1.0.0",
                        "governance_mode": "fail-closed",
                        "execution_mode": "advisory-then-enforcing",
                        "universal_core": {},
                        "overlays": [],
                        "templates": [
                            {
                                "family": "pipeline",
                                "version": "1.0.0",
                                "required_sections": ["Purpose"],
                                "optional_sections": [],
                                "required_frontmatter": ["pipeline_id"],
                                "normalization_aliases": {"pipeline_id": ["id"]},
                                "output_path_pattern": "x",
                                "validator": "v",
                                "scaffold": "s",
                                "compatible_overlays": []
                            },
                            {
                                "family": "verification",
                                "version": "1.0.0",
                                "required_sections": ["Purpose"],
                                "optional_sections": [],
                                "required_frontmatter": ["id"],
                                "normalization_aliases": {"id": ["id"]},
                                "output_path_pattern": "x",
                                "validator": "v",
                                "scaffold": "s",
                                "compatible_overlays": []
                            }
                        ]
                    }
                )
            )
            with self.assertRaises(RegistryError):
                load_registry(path)


if __name__ == "__main__":
    unittest.main()
