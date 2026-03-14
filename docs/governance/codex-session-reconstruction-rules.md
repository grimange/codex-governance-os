# Codex Session Reconstruction Rules

## Purpose

This canon defines the deterministic rules for reconstructing governed Codex
session truth in `codex-governance-os`.

It exists so governance observers can derive one bounded, evidence-backed
session narrative from the canonical Layer 6 evidence surfaces without
inventing events, collapsing authority boundaries, or elevating runtime context
above documented governance truth.

## Scope

This canon governs:

- deterministic reconstruction of governed session narratives
- the ordered method used to collect and interpret admissible session evidence
- preservation of state-machine, ledger, registry, observation, and
  runtime-boundary roles during reconstruction
- fail-closed handling of incomplete or conflicting reconstruction evidence

This canon does not govern:

- runtime instrumentation or event collection
- creation of new event schemas
- replacement of the session evidence-interpretation model
- replacement of the state-machine canon, registry, ledger, observation
  doctrine, or runtime-boundary canon

## Governing Authority

Authority for this canon is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/governance-evidence-interpretation-canon.md`
5. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
6. `docs/governance/codex-session-evidence-interpretation-model.md`
7. `docs/contracts/codex-session-state-machine-canon.md`
8. `docs/governance/codex-session-registry.md`
9. `docs/governance/codex-session-ledger.md`
10. `docs/governance/codex-session-lifecycle-observation-discipline.md`
11. `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`
12. this canon
13. generated pipeline artifacts and later runtime evidence records

This canon operationalizes reconstruction under the existing Layer 6
interpretation model without overriding the higher authorities.

## Reconstruction Surfaces

Session reconstruction may rely only on the canonical Layer 6 evidence
surfaces:

- the session registry for identity and indexed summary state
- the session ledger for durable recorded event history
- the state-machine canon for lifecycle meaning and transition validity
- the lifecycle-observation doctrine for normalization of admissible signals
- the runtime-boundary canon for bounded supporting runtime context

No additional surface is authorized as independent session-truth authority by
this canon.

## Canonical Rules

1. Session reconstruction must anchor on canonical `session_id`.
2. Session reconstruction must follow the evidence precedence defined by
   `docs/governance/codex-session-evidence-interpretation-model.md`.
3. The registry identifies the session and provides indexed summary fields, but
   it must not be treated as a substitute for lifecycle event history.
4. The ledger is the durable event-evidence surface for reconstruction of what
   was recorded as having happened.
5. Lifecycle meaning must be interpreted through the state-machine canon rather
   than through event labels, summaries, or runtime-native terminology alone.
6. Lifecycle observation may normalize admissible signals and clarify
   progression, but it must not create new lifecycle authority or invent
   missing transitions.
7. Runtime context may assist reconstruction only when admitted through the
   runtime-boundary canon and mapped back into canonical session fields.
8. Reconstruction must preserve insufficiency, ambiguity, and restrictions
   explicitly when the evidence cannot support a stronger narrative.

## Reconstruction Process

### Step 1: Identify The Session

Locate the governed session through the registry using `session_id`.

Use the registry to establish:

- session identity
- session existence in canonical recording surfaces
- indexed summary fields that guide scoped evidence lookup

### Step 2: Collect Durable Evidence

Gather all applicable ledger entries associated with the identified
`session_id`.

Relevant evidence may include:

- start or initialization-oriented records
- admission and activation evidence
- execution and verification evidence
- handoff or continuity evidence when applicable
- closure or continuity-violation evidence when applicable

### Step 3: Normalize Admissible Signals

Apply lifecycle-observation normalization where additional admissible signals
clarify session progression.

Normalization may clarify:

- how recorded evidence maps into lifecycle movement
- whether activity implies admissible progression or only partial support
- whether observed signals remain insufficient for full reconstruction

Normalization must not override ledger evidence or state-machine meaning.

### Step 4: Interpret Lifecycle Meaning

Interpret all lifecycle movement through the state-machine canon.

This step determines:

- whether transitions are valid
- whether a claimed handoff, resumption, admission, activation, or closure path
  is consistent with canonical lifecycle semantics
- whether evidence implies drift, insufficiency, or bounded reconstruction

### Step 5: Admit Supporting Runtime Context

Consult runtime-boundary evidence only when it can be mapped back into
canonical session fields and used as supporting context.

Runtime context may clarify reconstruction but must not:

- redefine lifecycle meaning
- displace registry or ledger evidence
- create authoritative events that do not exist in canonical surfaces

### Step 6: Construct The Narrative

Construct one bounded governance-observable session narrative that:

- starts from canonical `session_id`
- reflects recorded ledger evidence
- respects state-machine lifecycle meaning
- incorporates normalized observation only where admissible
- preserves unresolved ambiguity, insufficiency, or restriction explicitly

The resulting narrative is the reconstructed governance-observable session
truth, not a claim of complete runtime capture.

## Reconstruction Invariants

### State-Machine Authority

Lifecycle semantics are determined by the state-machine canon only.

### Ledger Integrity

Reconstruction must not invent events absent from durable evidence.

### Registry Identity Authority

The registry remains the authoritative identity and index surface.

### Observation Subordination

Lifecycle observation remains interpretive and subordinate.

### Runtime Neutrality

Runtime context remains supporting and bounded.

## Conflict And Insufficiency Rules

If evidence conflicts, reconstruction must apply the precedence rules from the
session evidence-interpretation model.

If evidence remains insufficient after admissible interpretation,
reconstruction must:

- narrow the narrative
- preserve the insufficiency explicitly
- avoid inventing transitions, continuity, or closure certainty

If evidence cannot be reconciled within the canonical precedence model, the
reconstruction outcome must remain unresolved rather than authoritatively
completed.

## Allowed Behaviors

- reconstructing session narratives from canonical registry and ledger
  evidence
- using lifecycle observation to clarify admissible session progression
- using runtime context as bounded supporting evidence
- preserving ambiguity and insufficiency explicitly
- failing closed when reconstruction evidence is incomplete or conflicting

## Prohibited Behaviors

- constructing session truth without anchoring to `session_id`
- treating registry summaries as a replacement for event history
- inventing missing lifecycle transitions
- treating lifecycle observation as an independent event authority
- treating runtime context as authoritative lifecycle truth
- claiming complete reconstruction when evidence remains partial

## Compliance Signals

Compliance is indicated when:

- reconstruction begins with `session_id` and canonical evidence collection
- lifecycle interpretation defers to the state-machine canon
- ledger, registry, observation, and runtime-boundary roles remain distinct
- reconstructed narratives preserve evidence limits explicitly
- different observers following the canon should converge on the same bounded
  reconstruction outcome

## Ambiguity Handling

- If the registry identifies the session but the ledger is partial, the
  reconstruction may acknowledge the session while preserving partial-history
  status.
- If lifecycle observation suggests activity but ledger support is incomplete,
  the reconstruction should remain bounded rather than silently filled in.
- If runtime context cannot be mapped back into canonical fields, it must not
  influence authoritative reconstruction.

## Governance Implications

- Future verification lanes can audit whether session reconstruction remains
  deterministic across observers.
- Future runtime-support lanes can distinguish better between reconstruction
  assistance and authoritative session evidence.
- The Layer 6 model gains an explicit operational method for converting
  admissible evidence into one bounded narrative.

## Non-Goals

This canon does not:

- create a runtime reconstruction engine
- replace the session evidence-interpretation model
- replace the state-machine canon, registry, ledger, observation doctrine, or
  runtime-boundary canon
- guarantee that every historical session can be reconstructed completely
