# Exception Classification Rules

The enforcement scan classifies non-violation matches explicitly.

Allowed exception classes:

- `rule_example`: a forbidden-pattern token appears inside inline code that is
  explaining the rule rather than acting as a link
- `scan_definition`: a forbidden-pattern token appears inside a fenced code
  block used to define scan criteria or examples
- `historical_evidence`: a forbidden-pattern token appears inside preserved
  artifact bundles for pipelines `108`, `109`, or `110`

Fail-closed rule:

- any match that is not explicitly classified as one of the allowed exception
  classes is treated as a `violation`
