# Codex Session Execution Ledger

## Purpose

This ledger defines the canonical event-recording surface for governed Codex
session execution in `codex-governance-os`.

It exists to preserve traceable lifecycle events, mutation-scope declarations,
handoff relationships, and final closure outcomes for governed sessions. It is
an evidence surface, not a runtime event bus.

## Scope

This ledger governs:

- session lifecycle transition recording
- orchestrator and agent-role event attribution
- task and mutation-scope event recording
- handoff traceability
- final session execution outcome recording

This ledger does not:

- prove that every historical session event was captured
- create automatic event emission
- replace the session registry or pipeline artifacts

## Governing Authority

Authority for this ledger is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
5. `docs/governance/codex-session-registry.md`
6. this ledger
7. generated pipeline artifacts referencing session execution

## Lifecycle Events

The canonical lifecycle events are:

- `SESSION_STARTED`
- `SESSION_CONTEXT_ALIGNED`
- `SESSION_TASK_ASSIGNED`
- `SESSION_EXECUTION_STARTED`
- `SESSION_EXECUTION_COMPLETED`
- `SESSION_VERIFICATION_COMPLETED`
- `SESSION_HANDOFF_PACKET_CREATED`
- `SESSION_CLOSED`
- `SESSION_CONTINUITY_VIOLATION`

These events should be recorded in execution order for a governed session when
the repository chooses to record that session.

The canonical lifecycle states that these events move between are defined by
[codex-session-state-machine-canon.md](/home/ramjf/python-projects/codex-governance-os/docs/contracts/codex-session-state-machine-canon.md).

## Ledger Fields

Each ledger entry should record:

- `session_id`
- `event`
- `event_date`
- `from_state`
- `to_state`
- `orchestrator_session`
- `agent_role`
- `pipeline_executed`
- `task_scope`
- `mutation_scope`
- `handoff_packet`
- `handoff_from_session`
- `handoff_to_session`
- `predecessor_handoff_packet`
- `admission_status`
- `activation_status`
- `admission_failure_reason`
- `resume_status`
- `handoff_objective`
- `handoff_constraints`
- `handoff_expected_outputs`
- `preserved_restrictions`
- `first_admitted_action`
- `first_successor_action`
- `final_verdict`

Field intent:

- `from_state` and `to_state` identify the canonical lifecycle transition
  represented by the event when lifecycle movement is being recorded
- `mutation_scope` identifies the canonical surface or directory affected by
  the session event
- `pipeline_executed` identifies the governed lane associated with the session
  event when applicable
- `handoff_packet` identifies the continuity artifact created or expected for
  closure-related events
- `predecessor_handoff_packet` identifies the packet a resumed successor
  consumed when continuity is claimed
- `admission_status` records the admission-gate outcome represented by the
  event
- `activation_status` records whether the session became active or remained
  blocked
- `admission_failure_reason` records why admission failed closed when
  applicable
- `resume_status` records whether a resume claim was admissible or blocked
- handoff fields remain blank unless the event records an explicit handoff
- `preserved_restrictions` records the restriction set carried across the
  session boundary
- `first_admitted_action` records the first action validated before activation
- `first_successor_action` records the first governed action a resumed
  successor is expected to take
- `final_verdict` is normally populated on closure-oriented events

## Handoff Traceability Rules

If work transfers between sessions, ledger entries should preserve:

- origin session
- target session
- objective
- active constraints
- expected outputs

Handoff recording must remain consistent with the Layer 6 handoff discipline and
must not silently erase restrictions carried from upstream work.

If resumed continuity is claimed, the ledger should preserve explicit
predecessor packet linkage, resume-status interpretation, preserved
restrictions, and the first successor action rather than relying on narrative
summary alone.

If admission review occurs, the ledger should preserve admission status,
activation status, any fail-closed reason, and the first admitted action rather
than treating activation as implicit.

If a governed session closes without the required handoff packet, the ledger
should record `SESSION_CONTINUITY_VIOLATION` explicitly rather than smoothing
the gap away.

Lifecycle transition recording must not contradict the canonical state machine.
Events may add execution detail, but they must not imply an invalid lifecycle
movement such as reopening a closed session directly into active execution.

## Mutation Scope Rules

Every governed session that mutates repository state should declare a bounded
mutation scope such as:

- `docs/pipelines/governance`
- `docs/governance/architecture-doctrine.md`
- `docs/pipelines/registry/pipeline-registry.md`

If two sessions would claim overlapping mutation scopes, Layer 6 requires those
mutations to be serialized rather than performed concurrently.

## Initial Ledger State

The ledger begins as an empty canonical evidence surface until later governed
work records specific session events.

| session_id | event | event_date | from_state | to_state | orchestrator_session | agent_role | pipeline_executed | task_scope | mutation_scope | handoff_packet | predecessor_handoff_packet | admission_status | activation_status | admission_failure_reason | resume_status | handoff_from_session | handoff_to_session | handoff_objective | handoff_constraints | preserved_restrictions | handoff_expected_outputs | first_admitted_action | first_successor_action | final_verdict |
|------------|-------|------------|------------|----------|----------------------|------------|-------------------|------------|----------------|----------------|----------------------------|------------------|-------------------|--------------------------|---------------|----------------------|--------------------|-------------------|---------------------|------------------------|--------------------------|----------------------|------------------------|---------------|

## Explicit Restrictions

This ledger is bounded.

It does not claim:

- full retrospective capture of prior sessions
- automatic event generation from session tooling
- proof of runtime orchestration enforcement
- independent authority apart from the Layer 6 doctrine and session registry

## Non-Goals

This ledger does not:

- replace the session registry identity surface
- replace pipeline final verdict artifacts
- authorize runtime orchestration infrastructure
