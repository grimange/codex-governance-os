# Verification

## Commands Run

```bash
python -m unittest discover -s tests/governance -p 'test_*.py'
python tools/governance/template_lint.py lint-template tests/governance/fixtures/lint/valid-pipeline-template.md --family pipeline --output json
python tools/governance/template_lint.py lint-template tests/governance/fixtures/lint/invalid-universal-rule-template.md --output json
python tools/governance/template_lint.py lint-template tests/governance/fixtures/lint/normalized-skill-template.md --output json
python tools/governance/template_lint.py lint-templates --root tests/governance/fixtures/lint --output json
```

## Observed Outcomes

- valid fixture: `VALID_AS_IS`
- invalid fixture: `BLOCKED`
- normalization fixture: `NORMALIZED_AND_VALID`
- repo-wide fixture run: deterministic mixed output with one valid, one normalized, and one blocked case
- unit and integration tests: `Ran 18 tests ... OK`
- docs-root migration compatibility: linter behavior remained unchanged after template bodies moved to `docs/codex/templates/` and admitted registry state moved to `docs/governance/registries/templates/`

## Admission Integration

`tools/governance/template_registry.py` now uses the governed lint decision model during admitted-template validation, making the linter the canonical gate for registry-backed template admission.
