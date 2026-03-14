# Codex Session Evidence Interpretation Model

## Purpose

This canon defines how governed Codex session evidence must be interpreted in
`codex-governance-os`.

It exists so session truth can be reconstructed deterministically from the
canonical Layer 6 evidence surfaces without allowing registry metadata, ledger
records, lifecycle observations, or runtime context to compete with the
authoritative lifecycle model.

## Scope

This canon governs interpretation of session evidence drawn from:

- `docs/contracts/codex-session-state-machine-canon.md`
- `docs/governance/codex-session-registry.md`
- `docs/governance/codex-session-ledger.md`
- `docs/governance/codex-session-lifecycle-observation-discipline.md`
- `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`

This canon does not govern:

- runtime instrumentation or event collection
- creation of new event schemas
- replacement of the repository-wide
  `docs/governance/governance-evidence-interpretation-canon.md`
- replacement of the state-machine canon, registry, ledger, observation
  discipline, or runtime-boundary canon

## Governing Authority

Authority for this canon is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/governance-evidence-interpretation-canon.md`
5. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
6. `docs/contracts/codex-session-state-machine-canon.md`
7. `docs/governance/codex-session-registry.md`
8. `docs/governance/codex-session-ledger.md`
9. `docs/governance/codex-session-lifecycle-observation-discipline.md`
10. `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`
11. `docs/governance/codex-session-reconstruction-rules.md`
12. this canon
13. generated pipeline artifacts and later runtime evidence records

This canon applies the repository-wide evidence-interpretation doctrine to
Layer 6 session-governance surfaces without overriding the higher authorities.

## Interpretation Surfaces

### State Machine Authority

The state-machine canon defines authoritative lifecycle meaning:

- canonical state names
- allowed transitions
- prohibited transitions
- lifecycle distinctions such as handoff completion, resumption, closure
  preparation, and closure

The state machine is the primary authority for lifecycle semantics.

### Session Registry

The session registry defines canonical session identity and current
state-summary meaning.

The registry establishes:

- `session_id`
- session existence and indexing
- summary lifecycle status
- summary admission, activation, continuity, and verdict fields

The registry is authoritative for session identity and indexed summary state,
but it does not redefine lifecycle semantics independently of the state
machine.

### Session Ledger

The session ledger defines canonical durable event-recording meaning.

The ledger establishes:

- ordered governed event evidence
- event-linked state transitions
- admission, activation, resume, and continuity evidence
- supporting evidence references

The ledger records what was observed or recorded as having happened, but it
does not create new lifecycle semantics outside the state machine.

### Lifecycle Observation

The lifecycle-observation canon defines how lifecycle signals are normalized
into canonical registry and ledger meaning.

Lifecycle observation is interpretive and reconstructive. It must defer to the
state machine, registry, and ledger rather than acting as an independent truth
surface.

### Runtime Boundary Evidence

The runtime-boundary canon defines what runtime-originating evidence may be
admissible and how it must map back into canonical session fields.

Runtime evidence is supporting context unless and until it has been normalized
into canonical Layer 6 meaning.

## Canonical Rules

1. `session_id` remains the canonical identity anchor for all session evidence
   interpretation.
2. Lifecycle meaning must be interpreted first through the state-machine canon.
3. Ledger evidence is authoritative for durable recorded session events within
   the scope of what the ledger actually records.
4. Registry evidence is authoritative for session existence, indexing, and
   current summary fields, but it must not be interpreted as a replacement for
   event history.
5. Lifecycle-observation evidence may normalize and explain session
   progression, but it must not redefine lifecycle states, create a parallel
   event system, or outrank ledger evidence.
6. Runtime evidence is admissible only when it remains within the runtime
   boundary and can be mapped back into canonical session fields.
7. Interpretation must never invent lifecycle transitions, state meanings, or
   continuity claims that are not supported by canonical evidence surfaces.
8. Where evidence is partial or conflicting, session truth must remain
   fail-closed and bounded rather than smoothed into a stronger narrative than
   the evidence supports.

## Evidence Authority Precedence

When interpreting governed session truth, evidence precedence is:

1. state-machine authority for lifecycle meaning
2. ledger evidence for durable event history
3. registry evidence for identity and current summary state
4. lifecycle-observation normalization
5. runtime-boundary supporting context

This precedence does not replace repository-wide authority ordering. It defines
how admissible Layer 6 session evidence is interpreted once the relevant
surfaces are already in scope.

## Evidence Admissibility

Session evidence is admissible when it is:

- produced by a canonical Layer 6 governance surface
- recorded in the session ledger
- recorded in the session registry
- derived through the lifecycle-observation canon from canonical evidence
- admitted as supporting runtime context through the runtime-boundary canon

Evidence is not admissible for session-truth interpretation when it:

- originates outside the canonical session-governance surfaces without an
  admissible mapping path
- depends on a runtime-native identifier that cannot be mapped back to
  `session_id`
- implies lifecycle semantics not defined by the state machine
- exists only as narrative summary without canonical support

## Conflict Resolution

If session evidence appears to conflict:

1. interpret lifecycle meaning through the state-machine canon first
2. prefer durable ledger evidence over registry summaries when evaluating what
   happened over time
3. treat registry summaries as current indexed state, not as a replacement for
   ledger event history
4. use lifecycle-observation discipline only to normalize or interpret signals
   that remain consistent with the higher Layer 6 surfaces
5. use runtime context only as supporting evidence that does not displace
   canonical Layer 6 surfaces

If the conflict cannot be resolved through this precedence, the session claim
must be treated as unresolved or insufficiently supported rather than
authoritatively reconstructed.

## Session Narrative Reconstruction

A governance observer should reconstruct governed session truth by:

1. identifying the session through `session_id` in the registry
2. gathering applicable ledger entries for the session
3. interpreting lifecycle transitions through the state-machine canon
4. using lifecycle-observation normalization to clarify admissible session
   progression where needed
5. consulting runtime-boundary evidence only as supporting context that maps
   back into canonical fields
6. preserving any insufficiency, ambiguity, or restriction that remains after
   interpretation

The resulting narrative is governance-observable session truth, not a claim of
full runtime capture.

Operational reconstruction of that narrative should follow
`docs/governance/codex-session-reconstruction-rules.md`.

## Allowed Behaviors

- interpreting session lifecycle meaning through the state machine first
- using ledger evidence as the durable record of session activity
- using registry evidence to anchor session identity and current summary state
- using lifecycle-observation discipline to normalize admissible signals
- using runtime evidence as supporting context when canonical mapping exists
- failing closed when evidence is insufficient or conflicting

## Prohibited Behaviors

- treating registry summaries as a substitute for lifecycle semantics
- treating ledger events as authority to redefine the state machine
- treating lifecycle observation as an independent runtime authority
- treating runtime context as superior to canonical Layer 6 surfaces
- inventing missing transitions or continuity claims from narrative pressure
- claiming complete runtime reconstruction when the evidence remains partial

## Compliance Signals

Compliance is indicated when:

- session interpretation starts from `session_id` and the state machine
- registry, ledger, observation, and runtime-boundary roles remain distinct
- evidence precedence is explicit and inspectable
- conflicts fail closed instead of being normalized away
- session narratives remain bounded by the evidence actually recorded

## Ambiguity Handling

- If the registry shows a session exists but the ledger is absent or partial,
  the repository may acknowledge session existence without overclaiming full
  lifecycle reconstruction.
- If the ledger records events whose implications are ambiguous, interpretation
  must defer to state-machine meaning rather than narrative convenience.
- If runtime evidence suggests activity but cannot be mapped back into
  canonical fields, it should be treated as non-authoritative supporting
  context or excluded from session-truth claims.

## Governance Implications

- Future verification lanes can audit session reconstruction consistency
  against one explicit Layer 6 interpretation model.
- Future runtime-support lanes can distinguish admissible supporting context
  from authoritative session-governance evidence.
- Session registry, ledger, observation, and runtime-boundary surfaces can
  evolve without collapsing their distinct roles.

## Non-Goals

This canon does not:

- create a runtime evidence engine
- replace the repository-wide evidence-interpretation canon
- replace the session state machine, registry, ledger, observation canon, or
  runtime-boundary canon
- guarantee complete retrospective reconstruction of all sessions
