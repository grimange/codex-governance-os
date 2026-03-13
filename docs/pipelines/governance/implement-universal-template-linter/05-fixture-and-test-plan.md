# Fixture And Test Plan

## Added Fixtures

- `tests/governance/fixtures/lint/valid-pipeline-template.md`
- `tests/governance/fixtures/lint/invalid-universal-rule-template.md`
- `tests/governance/fixtures/lint/normalized-skill-template.md`

## Added Coverage

- valid fixture passes as-is
- invalid fixture blocks with placeholder, portability, and semantics findings
- normalization fixture returns `NORMALIZED_AND_VALID`
- repo-wide fixture lint output is deterministic
- CLI JSON output works
- legacy scaffold tests still pass
- registry tests now exercise admission integration through the governed lint decision
