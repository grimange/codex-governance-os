# Codex Session Runtime Boundary And Evidence Model

## Purpose

This canon defines the runtime boundary and evidence model for governed Codex
sessions in `codex-governance-os`.

It exists so future runtime implementations can produce deterministic evidence
that remains compatible with the already established Layer 6 session doctrine,
state machine, registry, execution ledger, admission model, and handoff rules.

## Scope

This canon governs:

- the canonical boundary between documentation-governed session state and live
  runtime session execution
- minimum evidence expectations for a future runtime-governed session
- compatibility rules for mapping runtime-native identifiers and events into
  the canonical session registry and execution ledger
- runtime evidence integrity expectations for later implementations

This canon does not govern:

- implementation of a runtime session manager
- automatic event capture infrastructure
- database-backed session persistence
- replacement of the existing state-machine, admission, handoff, registry, or
  ledger authorities

## Governing Authority

Authority for this canon is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
5. `docs/contracts/codex-session-state-machine-canon.md`
6. `docs/governance/codex-session-admission-and-activation-rules.md`
7. `docs/governance/codex-session-registry.md`
8. `docs/governance/codex-session-ledger.md`
9. `docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md`
10. `docs/governance/codex-session-lifecycle-observation-discipline.md`
11. `docs/governance/codex-session-evidence-interpretation-model.md`
12. this canon
13. generated pipeline artifacts and later runtime evidence records

This canon clarifies runtime compatibility without overriding the higher Layer 6
session authorities.

## Runtime Boundary Definition

The Codex session runtime boundary is the point at which documented governance
state transitions into live governed session execution.

On the documentation-governance side of the boundary, the authoritative surfaces
remain:

- doctrine
- contracts
- pipeline definitions
- pipeline artifacts
- the session registry
- the execution ledger

On the runtime side of the boundary, a future implementation may produce:

- live session initialization
- admission and activation execution
- runtime-native event streams
- tool-execution traces
- termination or closure traces

The runtime side is subordinate to the documentation side. Runtime evidence may
instantiate or support the governed model, but it must not redefine the
canonical meanings already established by Layer 6 doctrine.

## Canonical Rules

1. A governed runtime Codex session exists only when:
   - a governed session instance is initialized
   - admission succeeds under the canonical admission doctrine
   - governed execution becomes active under the canonical state machine
   - observable runtime evidence is produced
2. The canonical identity for a governed runtime session remains `session_id`.
3. A future runtime implementation may use a native runtime handle or process
   identifier, but that native handle must be mapped deterministically to the
   canonical `session_id` rather than replacing it.
4. Runtime execution must not bypass `SESSION_ADMITTED` before
   `SESSION_ACTIVE`.
5. Runtime evidence must remain compatible with the canonical lifecycle states
   and allowed transitions defined by the session state-machine canon.
6. Runtime evidence must preserve the difference between:
   - initialization
   - admission
   - activation
   - execution activity
   - handoff or closure preparation
   - terminal closure
7. If a future runtime implementation cannot map its evidence back to the
   canonical `session_id`, lifecycle model, and evidence order deterministically,
   that implementation is not conformant to this canon.

## Minimum Runtime Evidence Model

Any future runtime implementation must be able to produce or reconstruct the
following governed evidence families:

### Canonical Session Identity

- `session_id`
- optional runtime-native session handle as supporting evidence only

### Registry-Compatible Session Record

The runtime implementation must be able to populate the canonical registry
meaning for at least:

- `session_id`
- `start_date`
- `admission_status`
- `activation_status`
- `lifecycle_status`
- `primary_scope`

### Ledger-Compatible Event History

The runtime implementation must be able to produce an ordered event history that
maps deterministically into the canonical execution ledger meaning for at least:

- `session_id`
- `event`
- `event_date`
- `from_state`
- `to_state`
- `evidence_reference`

Runtime-native event names may exist internally, but governed recording must
normalize or map them to the canonical ledger vocabulary rather than inventing a
parallel authoritative event model.

## Evidence Integrity Requirements

Runtime evidence integrity requires:

- immutable canonical `session_id` once the governed session is recognized
- deterministic ordering of recorded session events
- consistent mapping from runtime evidence into registry and ledger records
- evidence references that allow later inspection of the supporting runtime
  trace when one exists
- reconstructable lifecycle history for initialization, admission, activation,
  and closure-related state
- lifecycle observations that can be normalized through the canonical
  observation discipline when later runtime evidence exists

If evidence is partial, missing, or inconsistent, the repository must fail
closed rather than treating the runtime session as fully reconstructed.

## Registry And Ledger Compatibility Rules

- The session registry remains the canonical session identity and state-summary
  surface.
- The execution ledger remains the canonical governed event-recording surface.
- Lifecycle observations should be interpreted through
  `docs/governance/codex-session-lifecycle-observation-discipline.md` so
  runtime evidence maps into canonical registry and ledger meaning without
  creating competing field names or event schemas.
- Session evidence interpretation should follow
  `docs/governance/codex-session-evidence-interpretation-model.md` so runtime
  context remains subordinate to state-machine, ledger, registry, and
  observation authority.
- Runtime implementations must map native timestamps, handles, and event
  identifiers into the registry and ledger without replacing the canonical
  field names already established by governance doctrine.
- Runtime-native identifiers may be preserved as supporting evidence or
  references through later governed extension work, but they must not displace
  `session_id`.
- Runtime event histories may be richer than the canonical ledger vocabulary,
  but governed recording must keep the canonical summary deterministic and
  inspectable.

## Allowed Behaviors

- documenting a future-compatible runtime evidence model without implementing it
- requiring runtime implementations to normalize to canonical governance fields
- preserving documentation-first authority while allowing later runtime support
- recording compatibility notes for future runtime event systems

## Prohibited Behaviors

- treating runtime evidence as a higher authority than documented session
  doctrine
- replacing canonical `session_id` with a runtime-native identifier
- redefining lifecycle state meanings through runtime terminology alone
- claiming automatic runtime evidence production that the repository does not
  implement
- introducing a runtime manager or persistence engine through this canon

## Compliance Signals

Compliance is indicated when:

- the runtime boundary between documentation governance and live execution is
  explicit
- the canonical evidence model uses `session_id` and the existing registry and
  ledger surfaces
- runtime-compatible evidence requirements preserve admission and lifecycle
  ordering
- the canon does not overclaim present runtime implementation
- entry surfaces can route future runtime-boundary questions to this canon

## Ambiguity Handling

- If no runtime implementation exists, the repository remains compliant as long
  as the boundary and evidence model are documented clearly.
- If a future runtime system emits richer telemetry than the canonical ledger
  currently records, that telemetry may exist as supporting evidence while the
  governed summary remains mapped to canonical fields.
- If a future runtime system cannot distinguish admission from activation in a
  reconstructable way, the repository should treat the evidence as insufficient
  rather than silently smoothing the gap away.

## Governance Implications

- Future runtime implementations can be audited against one explicit Layer 6
  evidence-compatibility target.
- Future verification lanes can distinguish missing runtime implementation from
  non-conformant runtime evidence more precisely.
- The session registry and execution ledger can remain documentation-first
  authorities while still serving as the canonical targets for later runtime
  mapping.

## Non-Goals

This canon does not:

- create runtime orchestration software
- require event streaming, persistence, or background services
- replace the state-machine canon, admission doctrine, registry, or ledger
- guarantee that every real session will be recorded automatically today
