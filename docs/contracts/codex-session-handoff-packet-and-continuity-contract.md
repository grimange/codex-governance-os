# Codex Session Handoff Packet And Continuity Contract

## Purpose

This contract defines the canonical handoff packet and continuity rules for
governed Codex sessions in `codex-governance-os`.

It exists so session continuity remains explicit, inspectable, and
restriction-preserving when responsibility transfers between sessions or when a
governed workstream pauses across a boundary.

## Scope

This contract governs:

- the canonical handoff packet artifact family under `docs/codex/sessions/handoffs/`
- required handoff packet fields and sections
- continuity rules between upstream and downstream governed sessions
- relationship between handoff packets, the session registry, and the execution
  ledger

This contract does not govern:

- runtime orchestration enforcement
- automatic session creation or closure
- retrospective capture of all past sessions
- pipeline artifact structure outside handoff continuity concerns

## Governing Authority

Authority for this contract is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
5. `docs/governance/codex-session-registry.md`
6. `docs/governance/codex-session-ledger.md`
7. this contract
8. generated handoff packets and pipeline artifacts

This contract refines handoff continuity behavior without overriding the higher
session-governance surfaces.

Canonical lifecycle state meaning for handoff, resumption, and closure remains
governed by
[codex-session-state-machine-canon.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/codex-session-state-machine-canon.md).
Canonical handoff and resume admissibility meaning remains governed by
[codex-session-handoff-contract-and-resume-evidence-model.md](/home/ramjf/python-projects/codex-governance-os/docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md).

## Canonical Rules

1. The canonical handoff packet root is `docs/codex/sessions/handoffs/`.
2. Handoff packet filenames must use `codex-session-handoff-{session-id}.md`.
3. The `{session-id}` component must align with the canonical session
   identifier model or another later governed compatibility mapping.
4. A governed session must produce a handoff packet when responsibility
   transfers to another session or when the session closes after governance
   execution that requires continuity evidence.
5. A handoff packet must preserve current objective, completed work, remaining
   tasks, active constraints, and expected outputs.
6. A handoff packet must include authoritative close-state information about the
   affected workstream rather than speculative next-state claims.
7. Handoff packets supplement the session registry and execution ledger; they do
   not replace those surfaces as identity or event authorities.
8. Existing handoff packets are append-only records and must not be silently
   rewritten after downstream work has relied on them.
9. Downstream sessions should review the latest relevant handoff packet before
   continuing a handed-off workstream.
10. Session closure for an in-scope governed session is incomplete until the
    required handoff packet exists.
11. If an in-scope governed session closes without the required handoff packet,
    the execution ledger should record `SESSION_CONTINUITY_VIOLATION`.
12. A handoff packet is sufficient for `SESSION_HANDOFF_COMPLETED` only when it
    satisfies the minimum resume evidence model defined by the canonical
    handoff-and-resume doctrine.
13. A successor session must not claim `SESSION_RESUMED` unless it explicitly
    links to a valid predecessor handoff packet and satisfies the canonical
    resume admissibility rules.

## Required Packet Structure

Every canonical handoff packet must contain:

1. session identity
2. session objective
3. authoritative state at session close
4. mutation scope summary
5. governance evidence produced
6. restrictions and known limitations
7. recommended next pipeline or next governed path
8. mutation boundary for next session

Required field families include:

- `session_id`
- `handoff_packet_id`
- `source_session_id`
- `start_time`
- `end_time`
- `initiating_pipeline`
- `governance_layer`
- `execution_environment`
- `active_pipeline`
- `pipeline_stage`
- `registry_state`
- `governance_status`
- `lifecycle_state`
- `preserved_restrictions`
- `unsupported_boundaries`
- `evidence_references`
- `next_valid_action`
- `resume_admissibility_note`
- `successor_expectation`
- `open_risks`

## Allowed Behaviors

- creating a new handoff packet for a real session transfer
- creating a handoff packet as a required close artifact for an in-scope
  governed session
- recording bounded restrictions and incomplete work explicitly
- referencing existing pipeline artifacts, registry entries, and ledger fields
- leaving packet roots empty until a later lane records a real handoff packet,
  as long as the schema and canonical path exist

## Prohibited Behaviors

- treating a handoff packet as a replacement for the session registry
- treating a handoff packet as a replacement for the execution ledger
- modifying an existing handoff packet silently after downstream reliance
- omitting active restrictions during a handoff
- closing an in-scope governed session without the required handoff packet
- broadening authority through packet narrative alone
- claiming runtime orchestration guarantees from handoff documentation presence

## Compliance Signals

Compliance is indicated when:

- the canonical handoff packet root exists
- packet naming follows the canonical pattern
- required packet sections remain stable and inspectable
- downstream sessions can reconstruct scope, restrictions, and next-step
  boundaries from the latest handoff packet
- handoff lifecycle wording aligns with the canonical session state machine
- resumed continuity claims can be evaluated against explicit predecessor
  evidence and admissibility rules
- registry and ledger records remain authoritative alongside the handoff packet
- governed session closure records link to a handoff packet when the contract
  requires one

## Ambiguity Handling

- If a session ends without handing work to another session, a handoff packet is
  still required when the session is closing an in-scope governed execution
  that requires continuity evidence.
- If historical sessions predate this contract, their absence from the handoff
  packet root must be treated as unrecorded history, not as proof of
  non-existence.
- If a session identifier format in an older packet differs from the current
  canonical session identifier model, the difference must be reconciled through
  governed normalization rather than inferred away.

## Governance Implications

- Future verification and audit lanes can use this contract as the canonical
  target for handoff continuity review.
- Future remediation work can use this contract to identify missing sections,
  stale packet naming, or continuity drift.
- Session-governance work should continue treating the registry and ledger as
  identity and event authorities while using handoff packets as continuity
  evidence.

## Non-Goals

This contract does not:

- create runtime session-state software
- force retroactive packet generation for past sessions
- prove automatic continuity validation
- replace the Layer 6 doctrine or session-governance surfaces
