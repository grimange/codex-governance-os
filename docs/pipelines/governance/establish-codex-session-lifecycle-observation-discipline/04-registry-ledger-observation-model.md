# Registry Ledger Observation Model

Pipeline `115` normalizes lifecycle observation into the canonical schema that
already exists.

Registry-compatible lifecycle observation must be able to support:

- `session_id`
- `start_date`
- `closure_date`
- `admission_status`
- `activation_status`
- `resume_status`
- `continuity_status`
- `lifecycle_status`
- `primary_scope`

Ledger-compatible lifecycle observation must be able to support:

- `session_id`
- `event`
- `event_date`
- `evidence_reference`
- `from_state`
- `to_state`
- admission, activation, resume, and continuity fields when applicable

This replaces the pipeline text's illustrative aliases such as
`current_state`, `session_start_time`, `session_end_time`, `timestamp`,
`event_type`, and `event_context` with the repository's canonical field names.
