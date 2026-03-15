# Regression Results

Executed command:

```bash
python -m unittest discover -s tests/governance -p "test_*.py"
```

Observed result:

- `Ran 135 tests in 7.574s`
- `OK`

Interpretation:

- the current regression suite passes
- however, the suite does not yet cover the authority gaps exposed in the
  Scenario 4 and Scenario 5 manual verification cases
