# Regression Test Results

Executed command:

```bash
python -m unittest discover -s tests/governance -p "test_*.py"
```

Observed result:

- `Ran 135 tests in 7.598s`
- `OK`

Interpretation:

- the full governance regression suite passes
- the selector hardening and new authority-gap regression coverage hold under
  automated execution
