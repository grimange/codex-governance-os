# Boundary Violation Scenario

`scenario_id`: `continuity.violation.implicit-cross-session-merge`

Participating sessions:

- `session_eta`
- `session_theta`

Admissible evidence:

- none supporting continuity

Invalid reasoning being exercised:

- topic similarity
- chronological proximity
- attempted cross-session event merging

Expected failure classification:

- `SESSION_BOUNDARY_VIOLATION`

Boundary validation:

- prohibited implicit continuity inference is rejected
- session event reconstruction must not cross `session_id` boundaries
- invalid relationship claims fail closed
