# Scenario Model Definition

The repository now has a canonical scenario doctrine at
`docs/governance/multi-session-continuity-evaluation-scenarios.md`.

Each canonical scenario fixture must declare:

- a stable `scenario_id`
- participating canonical `session_id` values
- explicit admissible cross-session evidence, if any
- the expected harness-internal continuity classification
- prohibited reasoning patterns that must remain inadmissible
- the governance boundary conditions being exercised

These fixtures exist to test the already-established continuity stack, not to
introduce new continuity semantics.
