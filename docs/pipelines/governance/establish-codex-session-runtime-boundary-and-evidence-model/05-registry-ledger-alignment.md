# Registry Ledger Alignment

Alignment changes made by this lane:

- `docs/governance/codex-session-registry.md` now states that future runtime
  implementations must map runtime-native identity back to the canonical
  `session_id`
- `docs/governance/codex-session-ledger.md` now includes
  `evidence_reference` and defines how runtime-native event evidence must map
  back to canonical ledger fields rather than replacing them
- `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
  now references the runtime-boundary canon directly

No state-machine semantics or admission rules were changed.
