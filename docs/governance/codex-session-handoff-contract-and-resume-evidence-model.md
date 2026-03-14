# Codex Session Handoff Contract And Resume Evidence Model

## Purpose

This canon defines the governed meaning of session handoff and the minimum
evidence model required for valid resumed execution in `codex-governance-os`.

It exists so Layer 6 session continuity remains explicit, evidence-backed,
restriction-preserving, and fail-closed across session boundaries.

## Scope

This canon governs:

- the canonical meaning of governed session handoff
- the canonical meaning of governed session resume
- minimum required handoff-packet evidence for successor continuity
- predecessor-successor linkage requirements
- resume admissibility rules
- invalid handoff and resume cases
- Layer 6 surfaces that must preserve handoff and resume semantics

This canon does not govern:

- runtime session automation
- automatic handoff-packet generation
- database-backed session persistence
- lower-layer governance authority
- replacement of the existing session state-machine canon

## Governing Authority

Authority for this canon is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
5. `docs/contracts/codex-session-state-machine-canon.md`
6. `docs/contracts/codex-session-handoff-packet-and-continuity-contract.md`
7. `docs/governance/codex-session-registry.md`
8. `docs/governance/codex-session-ledger.md`
9. this canon
10. generated handoff packets and pipeline artifacts

This canon extends operational clarity for handoff and resume evidence without
overriding the state-machine canon or the higher Layer 6 doctrine.

## Canonical Rules

1. A governed handoff is explicit and must not be inferred from interruption,
   inactivity, abandonment, or memory reconstruction.
2. A valid handoff requires:
   - an identified source session
   - a bounded governed subject
   - a canonical current state aligned to the session state machine
   - preserved restrictions and unsupported boundaries
   - evidence references sufficient for reconstruction
   - a declared next valid action or bounded pending action
   - an explicit handoff-completion declaration
3. A handoff packet is the minimum continuity unit between sessions.
4. `SESSION_HANDOFF_COMPLETED` means the source session produced a valid
   successor-capable handoff packet and reached a governed resumable boundary.
5. `SESSION_HANDOFF_COMPLETED` does not mean a successor session already exists
   or has resumed execution.
6. `SESSION_RESUMED` is valid only when a successor session explicitly links to
   a valid predecessor handoff packet and adopts the governed scope and
   preserved restrictions.
7. A successor session must not claim resumed continuity unless all of the
   following are true:
   - a valid predecessor handoff packet exists
   - predecessor linkage is explicit
   - the resumed subject matches or strictly narrows predecessor scope
   - preserved restrictions are imported without silent weakening
   - unsupported boundaries remain explicit
   - evidence references are sufficient to reconstruct current truth
   - the next action is admissible under governing doctrine
   - unverified or pending claims are not upgraded into authoritative fact
8. If any required resume condition fails, the session must be interpreted as a
   fresh initiation, interrupted execution, incomplete handoff, or resume
   inadmissible pending evidence.
9. The repository must not collapse:
   - `SESSION_HANDOFF_COMPLETED` into `SESSION_RESUMED`
   - interrupted execution into handoff completion
   - new session initiation into resumed continuity
10. Registry and ledger surfaces that record continuity must be able to record:
    - predecessor-successor linkage
    - handoff packet reference
    - resume status
    - preserved restrictions
    - first successor action

## Required Resume Evidence Fields

The minimum governed resume evidence model includes:

- `handoff_packet_id`
- `source_session_id`
- `predecessor_registry_context`
- `handoff_created_at`
- `governed_subject`
- `current_state`
- `current_stage`
- `next_valid_action`
- `scope_boundary`
- `preserved_restrictions`
- `unsupported_boundaries`
- `open_dependencies`
- `authoritative_artifacts`
- `evidence_references`
- `last_verified_claims`
- `unverified_or_pending_claims`
- `resume_admissibility_note`
- `successor_expectation`
- `handoff_completion_declaration`

## Allowed Behaviors

- recording a handoff packet for a real governed session boundary
- treating a successor session as resumed only when predecessor evidence is
  explicit and admissible
- narrowing scope during resume when the narrowing remains bounded and explicit
- preserving restrictions, unsupported boundaries, and pending claims without
  weakening them
- failing continuity claims closed when evidence is incomplete

## Prohibited Behaviors

- claiming handoff completion without evidence references
- claiming resumed continuity without explicit predecessor linkage
- silently broadening scope across a resume boundary
- omitting preserved restrictions or unsupported boundaries from the handoff
  packet
- using raw memory, informal notes, or chat context alone as continuity proof
- upgrading uncertainty into fact during resume
- overstating runtime automation that the repository does not implement

## Compliance Signals

Compliance is indicated when:

- handoff and resume are described as distinct governed meanings
- required resume evidence fields are explicit and inspectable
- successor continuity claims remain linked to predecessor handoff evidence
- restrictions and unsupported boundaries survive session boundaries unchanged
- registry and ledger surfaces can record linkage, resume status, and successor
  first action
- entry surfaces reference the canon without implying runtime automation

## Ambiguity Handling

- If a session stops without a valid handoff packet, the repository should
  treat the state as interrupted, not implicitly handed off.
- If a successor session can plausibly reconstruct context from other evidence
  but lacks explicit predecessor linkage, it must not claim resumed continuity.
- If an older artifact predates this canon, it may remain historical evidence
  rather than a current violation, provided active authoritative surfaces use
  the canonical handoff and resume model.

## Governance Implications

- Future verification lanes can audit resume admissibility against one explicit
  evidence model.
- Future admission and closure lanes can distinguish valid continuity from
  unsupported restart behavior more precisely.
- Session registry, ledger, and handoff packet surfaces should use this canon
  to keep continuity claims evidence-backed and fail-closed.

## Non-Goals

This canon does not:

- create runtime continuity validation
- replace the state-machine canon
- replace the handoff packet contract as the packet-family definition
- prove that all historical session transfers were governed correctly
