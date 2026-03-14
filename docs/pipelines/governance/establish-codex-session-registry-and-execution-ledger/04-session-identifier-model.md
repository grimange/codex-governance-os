# Session Identifier Model

Layer 6 session recording now uses the deterministic identifier format:

`CS-YYYYMMDD-###`

Model rules established:

- identifiers are unique within the repository registry
- the date component reflects session start date
- the numeric suffix is zero-padded and sequence-based for that date
- identifiers remain stable once recorded
- session artifacts may reference the identifier when a later governed lane
  chooses to record specific sessions

Example identifiers:

- `CS-20260314-001`
- `CS-20260314-002`

This identifier model improves reconstructability without implying that every
past session was historically captured.
