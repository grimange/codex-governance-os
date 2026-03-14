# Codex Session Lifecycle Observation Discipline

## Purpose

This canon defines how governed Codex session lifecycle transitions should be
observed and normalized into canonical governance evidence in
`codex-governance-os`.

It exists so future runtime-capable session implementations can produce
deterministic lifecycle observations that map back into the canonical session
state machine, session registry, and execution ledger without requiring one
specific runtime implementation.

## Scope

This canon governs:

- observation of meaningful governed session lifecycle transitions
- normalization of lifecycle observations into canonical registry and ledger
  meaning
- ordering discipline for lifecycle observation evidence
- minimum observation evidence needed to reconstruct governed session movement

This canon does not govern:

- runtime instrumentation frameworks
- logging, telemetry, or monitoring tool selection
- implementation of a live runtime observer
- replacement of the state-machine canon, registry, ledger, or runtime-boundary
  canon

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
9. `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`
10. `docs/governance/codex-session-evidence-interpretation-model.md`
11. this canon
12. generated pipeline artifacts and later runtime evidence records

This canon defines lifecycle-observation discipline without overriding the
higher Layer 6 authorities that already define lifecycle meaning and canonical
recording surfaces.

## Observation Model

Lifecycle observation is the governed act of detecting a meaningful session
lifecycle transition and recording enough evidence for that transition to be
reconstructed later.

Observation discipline exists so future runtime execution can be summarized
through canonical governance surfaces instead of inventing a parallel truth
model.

Observation does not create new lifecycle states. It records evidence about
movement through the lifecycle states already defined by the state-machine
canon.
Interpretation of that evidence should follow
`docs/governance/codex-session-evidence-interpretation-model.md`.

## Canonical Rules

1. Observed lifecycle movement must use the canonical lifecycle states defined
   by `docs/contracts/codex-session-state-machine-canon.md`.
2. The canonical identity for lifecycle observation remains `session_id`.
3. Lifecycle observation must preserve the distinction between:
   - initialization
   - admission
   - activation
   - meaningful governed execution
   - handoff preparation or completion when applicable
   - resumed continuity when applicable
   - closure preparation
   - terminal closure
4. Observation evidence must be normalized into canonical registry and ledger
   fields rather than recorded through a competing schema such as
   `current_state`, `session_start_time`, `event_type`, or other parallel
   surface-specific aliases.
5. Observation records must preserve deterministic ordering sufficient to show
   that invalid lifecycle movement did not occur.
6. Observation of active execution must not imply that admission was skipped or
   that an initialized or resumed session became active automatically.
7. If a future runtime implementation cannot map lifecycle observations back to
   canonical `session_id`, `lifecycle_status`, `event`, `event_date`,
   `from_state`, and `to_state`, that implementation is not conformant to this
   canon.

## Observation Families

The observation discipline recognizes the following canonical lifecycle
observation families:

- session initialization observation
- admission outcome observation
- activation observation
- meaningful execution observation
- handoff-related observation when continuity is in scope
- resumed-continuity observation when a successor session claims continuity
- closure-preparation observation
- terminal-closure observation
- continuity-violation observation when required lifecycle evidence is missing

These observation families are categories of evidence, not a replacement event
vocabulary. Canonical ledger recording must still use the existing ledger
surface and map observations into inspectable event history and state
transitions.

## Registry Observation Discipline

Lifecycle observation must be able to support the canonical registry meaning
for at least:

- `session_id`
- `start_date`
- `closure_date` when closure is observed
- `admission_status`
- `activation_status`
- `resume_status` when applicable
- `continuity_status` when applicable
- `lifecycle_status`
- `primary_scope`

The registry remains the canonical session identity and state-summary surface.
Observation discipline explains how lifecycle evidence populates that meaning;
it does not replace the registry with runtime-native state storage.

## Ledger Observation Discipline

Lifecycle observation must be able to support the canonical ledger meaning for
at least:

- `session_id`
- `event`
- `event_date`
- `evidence_reference`
- `from_state`
- `to_state`
- `admission_status` when applicable
- `activation_status` when applicable
- `resume_status` when applicable
- `handoff_packet` and related continuity fields when applicable

The ledger remains the canonical event-recording surface. Observation
discipline requires lifecycle evidence to map into ordered ledger-compatible
entries rather than into a runtime-only event stream with no canonical mapping.

## Ordering Rules

Observation ordering must remain consistent with the canonical state machine
and admission rules.

Examples of required ordering:

- initialization must be observable before admission
- admission must be observable before activation
- activation must be observable before meaningful active execution is treated
  as governed execution
- closure preparation must precede terminal closure
- resumed continuity must not erase the distinction between handoff completion,
  resumed status, renewed admission, and later activation

Observed ordering that contradicts the canonical state machine should be
treated as lifecycle drift or insufficient evidence rather than normalized away.

## Allowed Behaviors

- documenting a runtime-neutral observation discipline without implementing it
- requiring lifecycle observations to map to canonical registry and ledger
  fields
- allowing richer runtime telemetry so long as canonical mapping remains
  deterministic
- distinguishing insufficient observation evidence from proven lifecycle
  conformance

## Prohibited Behaviors

- introducing a competing lifecycle-state vocabulary through observation
  doctrine
- replacing canonical registry or ledger fields with runtime-local aliases
- treating observed execution as proof that admission or activation discipline
  was satisfied when the evidence cannot show it
- claiming that this canon implements runtime instrumentation, monitoring, or
  persistence
- collapsing handoff completion, resumed continuity, admission, and activation
  into one undifferentiated observed event

## Compliance Signals

Compliance is indicated when:

- lifecycle observation semantics remain subordinate to the state-machine,
  registry, ledger, and runtime-boundary canons
- canonical `session_id` remains the observation anchor
- registry and ledger mapping fields are explicit and inspectable
- ordering rules preserve the distinction between initialization, admission,
  activation, execution, and closure-related transitions
- the canon remains documentation-only and runtime-neutral

## Ambiguity Handling

- If no runtime implementation exists, the repository remains compliant as long
  as the observation discipline is explicit and compatible with the canonical
  Layer 6 surfaces.
- If a future runtime system emits richer lifecycle telemetry than the
  canonical ledger records directly, that telemetry may exist as supporting
  evidence as long as the governed summary maps back to canonical fields.
- If an observation can show activity but cannot reconstruct whether admission
  preceded activation, the evidence should be treated as insufficient rather
  than assumed valid.

## Governance Implications

- Future runtime-oriented verification lanes can evaluate whether lifecycle
  evidence is reconstructable without requiring one runtime stack.
- Future implementation work can distinguish observation compatibility from
  runtime instrumentation design.
- Registry and ledger surfaces remain authoritative even when later runtime
  evidence becomes richer.

## Non-Goals

This canon does not:

- create a runtime event observer
- require telemetry infrastructure
- replace the state-machine canon, registry, ledger, or runtime-boundary canon
- guarantee that every real lifecycle transition is recorded automatically
