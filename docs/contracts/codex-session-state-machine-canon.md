# Codex Session State Machine Canon

## Purpose

This contract defines the canonical lifecycle state machine for governed Codex
sessions in `codex-governance-os`.

It exists so Layer 6 session-governance surfaces use one authoritative state
model for lifecycle meaning, transition validity, handoff completion,
resumption, and closure semantics.

## Scope

This contract governs:

- canonical lifecycle state names for governed Codex sessions
- allowed and invalid state transitions
- lifecycle meaning of handoff completion, resumption, closure preparation, and
  closure completion
- Layer 6 governance surfaces that record or interpret governed session state

This contract does not govern:

- runtime session-state infrastructure
- automatic orchestration enforcement
- lower-layer governance authority
- non-governed or purely ad hoc work sessions

## Governing Authority

Authority for this contract is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
5. `docs/governance/codex-session-registry.md`
6. `docs/governance/codex-session-ledger.md`
7. `docs/contracts/codex-session-handoff-packet-and-continuity-contract.md`
8. this contract
9. generated pipeline artifacts and handoff packets

This contract refines Layer 6 lifecycle semantics without overriding higher
session-governance surfaces.

## Canonical Rules

1. Governed session lifecycle state must be expressed using the canonical state
   names in this contract.
2. The canonical state set is:
   - `SESSION_INITIALIZED`
   - `SESSION_ADMITTED`
   - `SESSION_ACTIVE`
   - `SESSION_HANDOFF_PENDING`
   - `SESSION_HANDOFF_COMPLETED`
   - `SESSION_RESUMED`
   - `SESSION_CLOSURE_PENDING`
   - `SESSION_CLOSED`
3. `SESSION_INITIALIZED` means the governed session has been created and
   recognized but active execution has not yet begun.
4. `SESSION_ADMITTED` means the session passed the admission gate and is
   permitted to begin governed execution, but active execution has not yet
   started.
5. `SESSION_ACTIVE` means the session is actively executing governed work.
6. `SESSION_HANDOFF_PENDING` means the session is preparing a governed handoff
   and has not yet satisfied the required continuity packet and context
   transfer.
7. `SESSION_HANDOFF_COMPLETED` means the required handoff packet and continuity
   evidence are complete for the in-scope session.
8. `SESSION_RESUMED` means a successor governed session has accepted continuity
   evidence and resumed the governed workstream under that continuity context.
9. `SESSION_CLOSURE_PENDING` means the session is finalizing closure evidence
   and may not skip the required close discipline.
10. `SESSION_CLOSED` means the session is formally closed and may not re-enter
   active execution.
11. The canonical allowed transitions are:
    - `SESSION_INITIALIZED -> SESSION_ADMITTED`
    - `SESSION_ADMITTED -> SESSION_ACTIVE`
    - `SESSION_ACTIVE -> SESSION_HANDOFF_PENDING`
    - `SESSION_HANDOFF_PENDING -> SESSION_HANDOFF_COMPLETED`
    - `SESSION_HANDOFF_COMPLETED -> SESSION_RESUMED`
    - `SESSION_RESUMED -> SESSION_ADMITTED`
    - `SESSION_ACTIVE -> SESSION_CLOSURE_PENDING`
    - `SESSION_HANDOFF_COMPLETED -> SESSION_CLOSURE_PENDING`
    - `SESSION_CLOSURE_PENDING -> SESSION_CLOSED`
12. The following invalid transitions are explicitly prohibited:
    - `SESSION_CLOSED -> SESSION_ACTIVE`
    - `SESSION_INITIALIZED -> SESSION_CLOSED`
    - `SESSION_ACTIVE -> SESSION_INITIALIZED`
    - `SESSION_HANDOFF_COMPLETED -> SESSION_ACTIVE`
    - `SESSION_INITIALIZED -> SESSION_ACTIVE`
    - `SESSION_RESUMED -> SESSION_ACTIVE`
13. Handoff completion and resumption are distinct states and must not be
    collapsed into one lifecycle meaning.
14. Layer 6 governance surfaces that record lifecycle state must align with
    this canonical state machine instead of inventing parallel status models.

## Allowed Behaviors

- recording lifecycle status with the canonical state names
- recording event-oriented ledger evidence that maps cleanly to canonical state
  transitions
- requiring admission before active execution
- closing a session directly from `SESSION_ACTIVE` through
  `SESSION_CLOSURE_PENDING` when no governed handoff is being completed
- recording compatibility notes when older artifacts used earlier lifecycle
  labels
- using this canon as the verification target for future continuity, recovery,
  or resumption lanes

## Prohibited Behaviors

- reopening a session after `SESSION_CLOSED`
- bypassing `SESSION_ADMITTED` when moving from initialization or resumption
  into active execution
- skipping `SESSION_CLOSURE_PENDING` before closure
- treating `SESSION_HANDOFF_COMPLETED` as equivalent to resumed execution
- recording live Layer 6 lifecycle state through unofficial aliases or
  alternative status vocabularies
- claiming runtime orchestration enforcement from documentation alone

## Compliance Signals

Compliance is indicated when:

- Layer 6 surfaces name the canonical state set explicitly or reference this
  contract as the lifecycle authority
- allowed transitions are inspectable and deterministic
- invalid transitions are called out as governance findings or violations
- session registry and ledger semantics do not contradict the canonical state
  machine
- handoff and closure documents distinguish handoff completion from resumption

## Ambiguity Handling

- If an older artifact uses pre-canon lifecycle wording, that artifact may
  remain as historical evidence if active authoritative surfaces use the
  canonical state machine.
- If a surface needs event-level detail beyond the canonical states, it may add
  bounded event semantics as long as those events do not contradict the state
  machine.
- If a session closes without a required handoff packet, the continuity
  violation remains an execution finding, but the lifecycle state still must
  respect the canonical closure path.

## Governance Implications

- Future verification lanes can use this canon as the authoritative target for
  lifecycle-state and transition checks.
- Future recovery or resumption lanes can classify invalid session movement as
  state-machine drift rather than narrative inconsistency.
- Session-governance surfaces should use this canon to keep registry, ledger,
  handoff, and orchestration semantics aligned.

## Non-Goals

This contract does not:

- create a runtime session manager
- prove that every governed session will be recorded automatically
- replace the session registry, execution ledger, or handoff packet contract
- authorize state semantics outside Layer 6 governed Codex sessions
