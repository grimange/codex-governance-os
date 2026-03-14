# Layer 6 Codex Session Orchestration And Handoff Discipline

## Purpose

This doctrine defines the canonical Layer 6 session orchestration and handoff
discipline for Codex work inside `codex-governance-os`.

Layer 6 establishes how governed Codex work may be coordinated across multiple
sessions or bounded sub-agents without weakening the lower governance layers.
It defines documentation-level orchestration discipline, task ownership, and
handoff requirements. It does not establish a runtime orchestration engine,
automatic delegation, or autonomous multi-session control.

Canonical lifecycle state semantics for governed sessions are defined by
[codex-session-state-machine-canon.md](../contracts/codex-session-state-machine-canon.md).
Canonical handoff and resume evidence semantics are defined by
[codex-session-handoff-contract-and-resume-evidence-model.md](codex-session-handoff-contract-and-resume-evidence-model.md).
Canonical admission and activation semantics are defined by
[codex-session-admission-and-activation-rules.md](codex-session-admission-and-activation-rules.md).
Canonical runtime-boundary and runtime-evidence compatibility semantics are
defined by
[codex-session-runtime-boundary-and-evidence-model.md](codex-session-runtime-boundary-and-evidence-model.md).
Canonical lifecycle-observation normalization semantics are defined by
[codex-session-lifecycle-observation-discipline.md](codex-session-lifecycle-observation-discipline.md).
Canonical session-evidence interpretation semantics are defined by
[codex-session-evidence-interpretation-model.md](codex-session-evidence-interpretation-model.md).
Canonical session-reconstruction procedure semantics are defined by
[codex-session-reconstruction-rules.md](codex-session-reconstruction-rules.md).
Canonical session-reconstruction verification semantics are defined by
[session-reconstruction-verification-harness.md](session-reconstruction-verification-harness.md).
Canonical session-reconstruction case-structure semantics are defined by
[session-reconstruction-case-verification-model.md](session-reconstruction-case-verification-model.md).
Canonical session-reconstruction evidence-packaging semantics are defined by
[session-reconstruction-evidence-packaging-standard.md](session-reconstruction-evidence-packaging-standard.md).
Canonical multi-session continuity-verification semantics are defined by
[multi-session-continuity-verification-model.md](multi-session-continuity-verification-model.md).
Canonical multi-session continuity-evidence semantics are defined by
[multi-session-continuity-evidence-harness.md](multi-session-continuity-evidence-harness.md).
Canonical multi-session continuity-evaluation scenario semantics are defined by
[multi-session-continuity-evaluation-scenarios.md](multi-session-continuity-evaluation-scenarios.md).

## Scope

This canon governs:

- session orchestration discipline for governed workstreams
- bounded task ownership across sessions
- deterministic handoff content and sequencing
- session lifecycle expectations for governed execution
- serialization rules for structural mutation
- evidence preservation across session boundaries

This canon does not:

- prove runtime session orchestration enforcement
- require automatic session spawning or delegation
- replace Layer 0 through Layer 5 governance boundaries

## Layer Position

Layer 6 sits above:

- Layer 0 doctrine and safety canons
- Layer 1 interpretation canon
- Layer 2 execution surfaces
- Layer 3 Codex rules canon
- Layer 4 Codex role model
- Layer 5 collaboration operating model

All Layer 6 behavior remains subordinate to those lower layers.

## Definitions

### Codex Session

A bounded reasoning context executing governed repository work.

Examples:

- planning session
- implementation session
- verification session

### Codex Sub-Agent

A specialized reasoning unit used for a narrow governed task within a bounded
workstream.

Examples:

- pipeline authoring agent
- verification agent
- doctrine-alignment agent

### Session Orchestrator

The controlling session responsible for coordinating a governed workstream,
preserving shared context, and consolidating bounded outputs.

### Session Handoff

The explicit transfer of responsibility or next-step execution context from one
session to another.

## Governed Orchestration Model

The governance OS adopts a bounded hub-and-spoke orchestration model.

One orchestrator session may coordinate a workstream while other sessions or
sub-agents contribute scoped outputs. Coordination exists to preserve
determinism and evidence continuity. It does not create new authority, bypass
governed routing, or authorize uncontrolled concurrent mutation.

The orchestrator is responsible for:

- maintaining current objective and lower-layer constraints
- assigning bounded tasks and expected outputs
- preventing duplicate ownership of the same structural mutation
- consolidating outputs before verification and closure

Subordinate sessions must remain scoped to their assigned task and must not
expand their authority through coordination alone.

## Session Lifecycle

Every governed session should follow the canonical Layer 6 lifecycle state
machine.

Canonical states:

- `SESSION_INITIALIZED`
- `SESSION_ADMITTED`
- `SESSION_ACTIVE`
- `SESSION_HANDOFF_PENDING`
- `SESSION_HANDOFF_COMPLETED`
- `SESSION_RESUMED`
- `SESSION_CLOSURE_PENDING`
- `SESSION_CLOSED`

Canonical allowed transitions:

- `SESSION_INITIALIZED -> SESSION_ADMITTED`
- `SESSION_ADMITTED -> SESSION_ACTIVE`
- `SESSION_ACTIVE -> SESSION_HANDOFF_PENDING`
- `SESSION_HANDOFF_PENDING -> SESSION_HANDOFF_COMPLETED`
- `SESSION_HANDOFF_COMPLETED -> SESSION_RESUMED`
- `SESSION_RESUMED -> SESSION_ADMITTED`
- `SESSION_HANDOFF_COMPLETED -> SESSION_CLOSURE_PENDING`
- `SESSION_ACTIVE -> SESSION_CLOSURE_PENDING`
- `SESSION_CLOSURE_PENDING -> SESSION_CLOSED`

Operational interpretation:

1. initialize the governed session
2. pass admission review
3. enter active execution only after an admissible first action exists
4. either prepare and complete a handoff or enter closure preparation
5. close only after required verification and closure evidence exist

No governed session may treat unverified output as a completed structural
result, and no live lifecycle interpretation may contradict the canonical state
machine.

## Session Responsibility Rules

### Single Orchestrator

Only one orchestrator session may coordinate a single repository workstream at
a time.

### Explicit Task Ownership

Every task must identify:

- owner
- scope
- expected output artifact or result

### Serialized Structural Mutation

Multiple sessions may analyze concurrently, but structural mutation must be
serialized.

No two sessions may simultaneously:

- edit the same canonical file
- mutate the same governance surface
- change architecture doctrine concurrently

### Evidence Preservation

Session outputs that affect governed work must preserve evidence traceability in
the pipeline artifact bundle or other governing record.

### Verified Closure

Before a workstream is closed, the orchestrator must confirm that outputs have
passed the required verification posture for the lane.

### Handoff Enforcement At Session Close

When a governed session transfers responsibility or closes after mutating
governance state, it must produce a handoff packet in the canonical handoff
packet root before closure.

If the required packet is absent, the session should be treated as having a
continuity violation that must remain visible in the execution record.

## Handoff Discipline

A session handoff must include:

1. current objective
2. completed work
3. remaining tasks
4. active constraints and restrictions
5. expected outputs

Handoffs must be explicit, inspectable, and sufficient for a downstream session
to continue without silently reinterpreting authority or losing restrictions.

Where the continuity contract requires a packet, the handoff is not complete
until the packet exists and the downstream session can inspect it. Lifecycle
meaning for handoff completion and later resumption must follow the canonical
state machine rather than local narrative inference.

A resumed session must be able to point to explicit predecessor evidence,
preserved restrictions, and an admissible next action. Continuity claims fail
closed when that evidence is incomplete.

An initialized or resumed session must not activate merely because it exists or
can describe the work. Admission must succeed first, and the first active step
must be admissible under current doctrine and scope.

## Prohibited Behaviors

The following behaviors are prohibited:

- silent task reassignment
- hidden session forks affecting governed work
- uncontrolled concurrent structural edits
- undocumented handoffs
- skipping required verification
- closing a governed session that requires continuity evidence without a
  handoff packet
- broadening authority through orchestration language alone

## Governance Integration

Layer 6 depends on and preserves:

- Layer 3 request classification, governed routing, safe mutation, and bounded
  reporting rules
- Layer 4 role boundaries and specialization limits
- Layer 5 collaboration workflow, restriction propagation, and evidence
  preservation
- Governance Safety Invariants fail-closed and authority-preservation rules

## Explicit Restrictions

This first Layer 6 canon is bounded.

It does not claim:

- runtime multi-session orchestration enforcement
- automatic session spawning or delegation
- autonomous repository mutation across sessions
- session-state infrastructure beyond documented governance discipline
- authority beyond Layers 0 through 5

## Compliance Signals

Layer 6 is being followed correctly when:

- one orchestrator owns a governed workstream
- session ownership and outputs remain explicit
- structural mutation is serialized
- lifecycle movement follows the canonical Layer 6 state machine
- admission precedes active execution
- handoffs preserve objective, restrictions, and expected outputs
- resumed execution preserves predecessor linkage, restrictions, and admissible
  next action
- required handoff packets exist before governed closure
- verification still occurs before closure

## Non-Goals

This canon does not:

- create runtime orchestration software
- prove enforcement of session serialization automatically
- replace the Layer 5 collaboration model
- authorize uncontrolled multi-agent execution
