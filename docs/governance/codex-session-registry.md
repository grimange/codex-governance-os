# Codex Session Registry

## Purpose

This registry defines the canonical recording surface for governed Codex
sessions interacting with `codex-governance-os`.

It exists to preserve auditable session identity, ownership, parent-child
relationship context, lifecycle status, and closure outcomes for governed
workstreams. It is a documentation-level governance surface, not a runtime
session manager.

## Scope

This registry governs:

- canonical session identifiers
- session classification
- orchestrator and parent-session relationships
- lifecycle state recording
- final verdict recording for governed sessions
- compatibility expectations for future runtime session evidence mapped into
  registry meaning
- lifecycle observation summaries normalized from later runtime evidence

This registry does not:

- prove runtime enforcement of every session event
- create live session-state infrastructure
- authorize autonomous session spawning or delegation

## Governing Authority

Authority for this registry is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
5. this registry
6. generated pipeline artifacts referencing session execution

This registry records session truth without overriding higher-order doctrine.

## Session Identifier Model

Each governed session must use the identifier format:

`CS-YYYYMMDD-###`

Examples:

- `CS-20260314-001`
- `CS-20260314-002`

Identifier rules:

- the date component records the session start date in repository-local
  execution context
- the numeric suffix is a zero-padded sequence for that date
- identifiers must be unique within the repository registry
- identifiers must remain stable once recorded

## Supported Session Types

Supported session types include:

- `architecture-session`
- `pipeline-authoring-session`
- `pipeline-execution-session`
- `verification-session`
- `governance-audit-session`
- `analysis-session`

Additional session types may be introduced later through governed evolution
work if repository evidence requires them.

## Registry Fields

Each registry entry should record:

- `session_id`
- `session_type`
- `orchestrator_session`
- `parent_session`
- `start_date`
- `closure_date`
- `handoff_packet`
- `predecessor_handoff_packet`
- `admission_status`
- `activation_status`
- `admission_failure_reason`
- `resume_status`
- `preserved_restrictions`
- `first_admitted_action`
- `first_successor_action`
- `lifecycle_status`
- `continuity_status`
- `final_verdict`
- `primary_scope`

Field intent:

- `orchestrator_session` identifies the controlling workstream session
- `parent_session` identifies the immediate upstream session when the entry
  reflects a handoff or subordinate execution
- `handoff_packet` identifies the canonical continuity artifact when one is
  required at session close
- `predecessor_handoff_packet` identifies the predecessor packet used when the
  session is a resumed successor
- `admission_status` records whether the session passed the admission gate
- `activation_status` records whether governed execution actually became active
- `admission_failure_reason` records the fail-closed reason when admission does
  not succeed
- `resume_status` records whether resumed continuity was claimed and admissible
- `preserved_restrictions` records the restriction set that survived the
  boundary
- `first_admitted_action` records the first action validated at admission time
- `first_successor_action` records the first governed action required of a
  resumed successor
- `continuity_status` records whether continuity requirements were satisfied
- `primary_scope` records the main governed surface the session affects

## Lifecycle Status Values

Canonical lifecycle status values are defined by
[codex-session-state-machine-canon.md](../contracts/codex-session-state-machine-canon.md).

Allowed lifecycle status values are:

- `SESSION_INITIALIZED`
- `SESSION_ADMITTED`
- `SESSION_ACTIVE`
- `SESSION_HANDOFF_PENDING`
- `SESSION_HANDOFF_COMPLETED`
- `SESSION_RESUMED`
- `SESSION_CLOSURE_PENDING`
- `SESSION_CLOSED`

Allowed continuity status values are:

- `NOT_REQUIRED`
- `REQUIRED_PENDING`
- `SATISFIED`
- `VIOLATION_RECORDED`

Allowed resume status values are:

- `NOT_APPLICABLE`
- `RESUME_CLAIMED_PENDING`
- `RESUME_ADMISSIBLE`
- `RESUME_INADMISSIBLE`

Allowed admission status values are:

- `PENDING_REVIEW`
- `ADMITTED`
- `NOT_ADMITTED`
- `PENDING_EVIDENCE`
- `REJECTED`

Allowed activation status values are:

- `NOT_ACTIVE`
- `ACTIVE`
- `BLOCKED`

These values summarize current state at the registry level. Detailed event
history belongs in
[codex-session-ledger.md](codex-session-ledger.md).

## Recording Rules

- every governed session should have at most one registry entry
- registry entries should be updated deterministically rather than replaced by
  narrative summaries
- closure state should remain explicit instead of implied
- lifecycle_status must use the canonical Layer 6 state-machine names
- parent and orchestrator relationships must not contradict the execution
  ledger
- when continuity evidence is required, the registry entry should reference the
  handoff packet before closure is treated as complete
- admission and activation outcomes should be explicit rather than inferred
- resumed successors should reference `predecessor_handoff_packet` and record
  imported `preserved_restrictions` and `first_successor_action`
- future runtime implementations must map runtime-native identity back to the
  canonical `session_id` rather than replacing registry identity with a native
  runtime handle
- future lifecycle observations must map into canonical registry fields such as
  `start_date`, `closure_date`, `admission_status`, `activation_status`, and
  `lifecycle_status` rather than introducing parallel registry aliases
- future runtime evidence may enrich registry support records, but canonical
  registry meaning must remain centered on the existing field set

## Initial Registry State

The canonical registry begins as an empty governed surface until repository
work chooses to record specific sessions through a later governed lane.

| session_id | session_type | orchestrator_session | parent_session | start_date | closure_date | handoff_packet | predecessor_handoff_packet | admission_status | activation_status | admission_failure_reason | resume_status | preserved_restrictions | first_admitted_action | first_successor_action | lifecycle_status | continuity_status | final_verdict | primary_scope |
|------------|--------------|----------------------|----------------|------------|--------------|----------------|----------------------------|------------------|-------------------|--------------------------|---------------|------------------------|----------------------|------------------------|------------------|-------------------|---------------|---------------|

## Explicit Restrictions

This registry is bounded.

It does not claim:

- complete historical reconstruction for past unrecorded sessions
- automatic synchronization with runtime session tooling
- proof of live multi-session enforcement
- authority beyond the Layer 6 doctrine it serves

## Non-Goals

This registry does not:

- replace pipeline artifact bundles
- define handoff-event sequencing in full detail
- authorize concurrent structural mutation
