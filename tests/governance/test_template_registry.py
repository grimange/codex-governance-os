from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import hashlib

from tools.governance.template_registry import (
    RegistryError,
    build_compiled_index,
    load_registry,
    load_template_entries,
    resolve_template,
)


class TemplateRegistryTests(unittest.TestCase):
    def test_default_registry_loads(self) -> None:
        registry = load_registry()
        self.assertIn("pipeline", registry.templates)
        self.assertIn("laravel", registry.overlays)
        self.assertIn("sub_agent", registry.templates)
        self.assertIn("report", registry.templates)

    def test_admitted_template_entries_load(self) -> None:
        entries = load_template_entries()
        self.assertIn("pipeline.universal.base", entries)
        self.assertIn("verification.universal.base", entries)

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

    def test_missing_body_file_blocks_admission(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            entry_dir = Path(tmp)
            entry_dir.mkdir(exist_ok=True)
            (entry_dir / "broken.yaml").write_text(
                json.dumps(
                    {
                        "template_id": "pipeline.test.broken",
                        "template_name": "Broken",
                        "template_family": "pipeline",
                        "template_kind": "base",
                        "version": "1.0.0",
                        "status": "active",
                        "authority_level": "canonical",
                        "description": "Broken",
                        "inputs_contract": {},
                        "outputs_contract": {},
                        "compatible_stacks": ["agnostic"],
                        "compatible_modes": ["design"],
                        "constraints": [],
                        "resolution_tags": ["broken"],
                        "file_path": "docs/codex/templates/does-not-exist.md",
                        "checksum_sha256": "deadbeef",
                        "admitted_at": "2026-03-14",
                        "admitted_by": "codex",
                        "supersedes": []
                    }
                )
            )
            with self.assertRaises(RegistryError):
                load_template_entries(entry_dir)

    def test_compiled_index_is_stable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            first = build_compiled_index(output_path=Path(tmp) / "first.json")
            second = build_compiled_index(output_path=Path(tmp) / "second.json")
            self.assertEqual(first, second)

    def test_exact_resolution_and_lifecycle_blocking(self) -> None:
        resolved = resolve_template(template_id="pipeline.universal.base")
        self.assertEqual("resolved", resolved.status)
        self.assertEqual("pipeline.universal.base", resolved.selected_template_id)

        with tempfile.TemporaryDirectory() as tmp:
            entry_dir = Path(tmp)
            entry_dir.mkdir(exist_ok=True)
            restricted_body = Path("docs/codex/templates/rules/safety.md")
            (entry_dir / "restricted.yaml").write_text(
                json.dumps(
                    {
                        "template_id": "rule.test.restricted",
                        "template_name": "Restricted",
                        "template_family": "rule",
                        "template_kind": "safety",
                        "version": "1.0.0",
                        "status": "restricted",
                        "authority_level": "canonical",
                        "description": "Restricted",
                        "inputs_contract": {},
                        "outputs_contract": {},
                        "compatible_stacks": ["agnostic"],
                        "compatible_modes": ["analysis"],
                        "constraints": [],
                        "resolution_tags": ["restricted"],
                        "file_path": "docs/codex/templates/rules/safety.md",
                        "checksum_sha256": hashlib.sha256(restricted_body.read_bytes()).hexdigest(),
                        "admitted_at": "2026-03-14",
                        "admitted_by": "codex",
                        "supersedes": []
                    }
                )
            )
            blocked = resolve_template(template_id="rule.test.restricted", entry_directory=entry_dir)
            self.assertEqual("blocked", blocked.status)
            self.assertIn("restricted", blocked.reason)

    def test_deprecated_and_archived_lifecycle_rules(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            entry_dir = Path(tmp)
            entry_dir.mkdir(exist_ok=True)
            body_path = Path("docs/codex/templates/pipelines/universal-base.md")
            checksum = hashlib.sha256(body_path.read_bytes()).hexdigest()
            (entry_dir / "deprecated.yaml").write_text(
                json.dumps(
                    {
                        "template_id": "pipeline.test.deprecated",
                        "template_name": "Deprecated",
                        "template_family": "pipeline",
                        "template_kind": "base",
                        "version": "1.0.0",
                        "status": "deprecated",
                        "authority_level": "canonical",
                        "description": "Deprecated",
                        "inputs_contract": {},
                        "outputs_contract": {},
                        "compatible_stacks": ["agnostic"],
                        "compatible_modes": ["design"],
                        "constraints": [],
                        "resolution_tags": ["deprecated"],
                        "file_path": "docs/codex/templates/pipelines/universal-base.md",
                        "checksum_sha256": checksum,
                        "admitted_at": "2026-03-14",
                        "admitted_by": "codex",
                        "supersedes": []
                    }
                )
            )
            blocked = resolve_template(template_id="pipeline.test.deprecated", entry_directory=entry_dir)
            self.assertEqual("blocked", blocked.status)
            allowed = resolve_template(
                template_id="pipeline.test.deprecated",
                allow_deprecated=True,
                entry_directory=entry_dir,
            )
            self.assertEqual("resolved", allowed.status)
            self.assertIn("deprecated", allowed.warnings[0])

            (entry_dir / "archived.yaml").write_text(
                json.dumps(
                    {
                        "template_id": "pipeline.test.archived",
                        "template_name": "Archived",
                        "template_family": "pipeline",
                        "template_kind": "verification",
                        "version": "1.0.0",
                        "status": "archived",
                        "authority_level": "canonical",
                        "description": "Archived",
                        "inputs_contract": {},
                        "outputs_contract": {},
                        "compatible_stacks": ["agnostic"],
                        "compatible_modes": ["design"],
                        "constraints": [],
                        "resolution_tags": ["archived"],
                        "file_path": "docs/codex/templates/pipelines/universal-base.md",
                        "checksum_sha256": checksum,
                        "admitted_at": "2026-03-14",
                        "admitted_by": "codex",
                        "supersedes": []
                    }
                )
            )
            archived = resolve_template(template_id="pipeline.test.archived", entry_directory=entry_dir)
            self.assertEqual("blocked", archived.status)
            self.assertIn("archived", archived.reason)

    def test_agnostic_fallback_requires_opt_in(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            entry_dir = Path(tmp)
            entry_dir.mkdir(exist_ok=True)
            body_path = Path("docs/codex/templates/pipelines/universal-base.md")
            checksum = __import__("hashlib").sha256(body_path.read_bytes()).hexdigest()
            (entry_dir / "agnostic.yaml").write_text(
                json.dumps(
                    {
                        "template_id": "pipeline.test.agnostic",
                        "template_name": "Agnostic",
                        "template_family": "pipeline",
                        "template_kind": "base",
                        "version": "1.0.0",
                        "status": "active",
                        "authority_level": "canonical",
                        "description": "Agnostic",
                        "inputs_contract": {},
                        "outputs_contract": {},
                        "compatible_stacks": ["agnostic"],
                        "compatible_modes": ["design"],
                        "constraints": [],
                        "resolution_tags": ["agnostic"],
                        "file_path": "docs/codex/templates/pipelines/universal-base.md",
                        "checksum_sha256": checksum,
                        "admitted_at": "2026-03-14",
                        "admitted_by": "codex",
                        "supersedes": []
                    }
                )
            )
            blocked = resolve_template(
                family="pipeline",
                kind="base",
                stack="django",
                mode="design",
                entry_directory=entry_dir,
            )
            self.assertEqual("blocked", blocked.status)
            resolved = resolve_template(
                family="pipeline",
                kind="base",
                stack="django",
                mode="design",
                allow_agnostic_fallback=True,
                entry_directory=entry_dir,
            )
            self.assertEqual("resolved", resolved.status)

    def test_duplicate_active_resolution_key_blocks_admission(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            entry_dir = Path(tmp)
            entry_dir.mkdir(exist_ok=True)
            body_path = Path("docs/codex/templates/pipelines/universal-base.md")
            checksum = hashlib.sha256(body_path.read_bytes()).hexdigest()
            shared = {
                "template_family": "pipeline",
                "template_kind": "base",
                "version": "1.0.0",
                "status": "active",
                "authority_level": "canonical",
                "description": "duplicate",
                "inputs_contract": {},
                "outputs_contract": {},
                "compatible_stacks": ["agnostic"],
                "compatible_modes": ["design"],
                "constraints": [],
                "file_path": "docs/codex/templates/pipelines/universal-base.md",
                "checksum_sha256": checksum,
                "admitted_at": "2026-03-14",
                "admitted_by": "codex",
                "supersedes": []
            }
            (entry_dir / "one.yaml").write_text(
                json.dumps(
                    {
                        **shared,
                        "template_id": "pipeline.test.one",
                        "template_name": "One",
                        "resolution_tags": ["one"]
                    }
                )
            )
            (entry_dir / "two.yaml").write_text(
                json.dumps(
                    {
                        **shared,
                        "template_id": "pipeline.test.two",
                        "template_name": "Two",
                        "resolution_tags": ["two"]
                    }
                )
            )
            with self.assertRaises(RegistryError):
                load_template_entries(entry_dir)


if __name__ == "__main__":
    unittest.main()
