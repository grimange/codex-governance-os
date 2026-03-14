from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from tools.governance.template_scaffold import realize_repository_scaffold


def _hash_tree(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        if path.is_file():
            digest.update(b"file\0")
            digest.update(path.read_bytes())
        else:
            digest.update(b"dir\0")
    return digest.hexdigest()


class TripleOverlayDeterminismTests(unittest.TestCase):
    def test_certified_triple_overlay_scaffolds_are_deterministic(self) -> None:
        cases = (
            ["cli-worker", "monorepo", "python-package"],
            ["cli-worker", "monorepo", "scheduler"],
            ["cli-worker", "python-package", "scheduler"],
            ["laravel", "monorepo", "scheduler"],
        )

        for overlays in cases:
            with self.subTest(overlays=overlays):
                with tempfile.TemporaryDirectory() as left_tmp, tempfile.TemporaryDirectory() as right_tmp:
                    left_selection = realize_repository_scaffold(
                        "universal-base",
                        Path(left_tmp),
                        overlays=list(overlays),
                        include_optional=False,
                    )
                    right_selection = realize_repository_scaffold(
                        "universal-base",
                        Path(right_tmp),
                        overlays=list(overlays),
                        include_optional=False,
                    )

                    left_payload = json.loads(left_selection.read_text())
                    right_payload = json.loads(right_selection.read_text())

                    self.assertEqual(left_payload, right_payload)
                    self.assertEqual(
                        _hash_tree(Path(left_tmp)),
                        _hash_tree(Path(right_tmp)),
                    )


if __name__ == "__main__":
    unittest.main()
