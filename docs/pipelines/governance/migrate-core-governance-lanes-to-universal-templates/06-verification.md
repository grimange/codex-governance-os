# Verification

## Commands Run

```bash
for f in docs/pipelines/governance/00{0..9}--*.md docs/pipelines/governance/010--*.md; do
  python tools/governance/template_lint.py lint-template "$f" --family pipeline --output json
done
python -m unittest discover -s tests/governance -p 'test_*.py'
```

## Expected Checks

- every migrated core lane parses as a governed pipeline document
- every migrated core lane contains the canonical required sections exactly once
- the normalized lane set does not regress existing governance tests
- registry discoverability remains explicit through the active pipeline catalog
