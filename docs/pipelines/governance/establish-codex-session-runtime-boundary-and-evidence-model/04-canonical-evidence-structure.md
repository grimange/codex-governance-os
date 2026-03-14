# Canonical Evidence Structure

Minimum runtime-compatible evidence structure established by the new canon:

- canonical session identity through `session_id`
- registry-compatible state summary through fields such as `start_date`,
  `admission_status`, `activation_status`, `lifecycle_status`, and
  `primary_scope`
- ledger-compatible ordered event history through fields such as `session_id`,
  `event`, `event_date`, `from_state`, `to_state`, and `evidence_reference`

The model is intentionally compatibility-oriented:

- runtime implementations may emit richer native telemetry
- governed recording must normalize that telemetry back to the canonical Layer 6
  field and state model
