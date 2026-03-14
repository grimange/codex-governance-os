# Evidence Model Consistency

## Session Identifier

- The runtime-boundary canon states that the canonical identity for a governed
  runtime session remains `session_id`.
- Runtime-native handles are allowed only as supporting evidence and must map
  deterministically back to `session_id`.
- The session registry still defines `session_id` as the canonical identifier
  surface and requires runtime-native identity to map back to that field.
- The execution ledger still records `session_id` as the canonical event
  linkage field and requires runtime evidence to map into canonical ledger
  fields rather than replacing them.

## Session Registry

- The registry remains the canonical session identity and state-summary
  surface.
- The runtime-boundary canon requires future runtime implementations to
  populate registry-compatible meaning for `session_id`, `start_date`,
  `admission_status`, `activation_status`, `lifecycle_status`, and
  `primary_scope`.
- Registry lifecycle status values remain sourced from the canonical
  state-machine canon.

## Execution Ledger

- The ledger remains the canonical governed event-recording surface.
- The runtime-boundary canon requires ordered event history that maps to at
  least `session_id`, `event`, `event_date`, `from_state`, `to_state`, and
  `evidence_reference`.
- The ledger already defines `evidence_reference` and requires runtime-native
  telemetry to map back into canonical ledger fields rather than displacing
  them.

## Classification

- canonical session identity preserved: `VERIFIED`
- registry authority preserved: `VERIFIED`
- ledger authority preserved: `VERIFIED`
- deterministic runtime evidence mapping defined: `VERIFIED`
