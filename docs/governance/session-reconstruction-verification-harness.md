# Session Reconstruction Verification Harness

## Purpose

This canon defines the governance verification harness for reconstructed Codex
session narratives in `codex-governance-os`.

It exists so governance observers can verify that a reconstructed session
narrative is deterministic, evidence-backed, subordinate to the Layer 6
interpretation hierarchy, state-machine conformant, and fail-closed when
evidence is incomplete or contradictory.

## Scope

This canon governs:

- verification of reconstructed governed session narratives
- doctrine-level checks applied to reconstructed session outputs
- classification of reconstruction outcomes as `VERIFIED`,
  `VERIFIED_WITH_RESTRICTIONS`, or `FAILED`
- fail-closed handling when reconstruction evidence is missing, conflicting, or
  ambiguous

This canon does not govern:

- reconstruction of session narratives itself
- runtime instrumentation or event collection
- creation of new evidence schemas
- replacement of the state-machine canon, registry, ledger, lifecycle
  observation doctrine, runtime-boundary canon, interpretation model, or
  reconstruction rules

## Governing Authority

Authority for this canon is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/governance-evidence-interpretation-canon.md`
5. `docs/governance/governance-safety-invariants-canon.md`
6. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
7. `docs/governance/codex-session-evidence-interpretation-model.md`
8. `docs/governance/codex-session-reconstruction-rules.md`
9. `docs/contracts/codex-session-state-machine-canon.md`
10. `docs/governance/codex-session-registry.md`
11. `docs/governance/codex-session-ledger.md`
12. `docs/governance/codex-session-lifecycle-observation-discipline.md`
13. `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`
14. this canon
15. generated pipeline artifacts and later runtime evidence records

This canon verifies reconstructed narratives under the existing Layer 6 session
authorities without overriding them.

## Verification Surfaces

The verification harness may evaluate reconstructed session narratives only
against these canonical Layer 6 surfaces:

- `docs/governance/codex-session-reconstruction-rules.md`
- `docs/governance/codex-session-evidence-interpretation-model.md`
- `docs/contracts/codex-session-state-machine-canon.md`
- `docs/governance/codex-session-registry.md`
- `docs/governance/codex-session-ledger.md`
- `docs/governance/codex-session-lifecycle-observation-discipline.md`
- `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`

No additional surface is authorized by this canon as an independent authority
for reconstructed session truth.

## Harness Model

The verification harness validates the output of the operational reconstruction
procedure defined in
`docs/governance/codex-session-reconstruction-rules.md`.

Where reconstruction evaluation is prepared as a formal case input, case
structure should follow
`docs/governance/session-reconstruction-case-verification-model.md`.

Where evidence is assembled for those cases, packaging should follow
`docs/governance/session-reconstruction-evidence-packaging-standard.md`.

The harness does not reconstruct the session itself. It verifies whether a
claimed reconstructed narrative:

- is anchored to canonical `session_id`
- is supported by admissible canonical evidence
- preserves Layer 6 authority precedence
- conforms to the canonical lifecycle state machine
- preserves ambiguity, insufficiency, and restrictions when the evidence does
  not support a stronger claim

## Canonical Rules

1. Verification must begin from the canonical `session_id` used by the
   reconstructed narrative.
2. Every lifecycle claim in the reconstructed narrative must be traceable to
   admissible canonical evidence surfaces.
3. The harness must evaluate lifecycle meaning through the state-machine canon
   before considering registry summaries, lifecycle observation, or runtime
   context.
4. The harness must treat ledger evidence as the durable event-history surface
   for determining what was recorded as having happened.
5. The harness must treat registry evidence as authoritative for session
   identity and indexed summary state, but not as a substitute for event
   history.
6. Lifecycle-observation evidence may clarify admissible progression, but it
   must remain interpretive and subordinate to the state machine, ledger, and
   registry.
7. Runtime-derived context may support verification only when it remains within
   the runtime boundary and maps back into canonical session fields.
8. If the available evidence permits more than one materially different valid
   narrative, verification must fail rather than choose one implicitly.
9. If required evidence is missing, contradictory, or outside admissible
   authority, verification must fail closed rather than smooth the gap away.

## Verification Checks

### Evidence Anchoring

The reconstructed session must anchor on canonical `session_id` from the
registry, and all cited evidence must correspond to that session identity.

### Ledger Consistency

All events used by the reconstructed narrative must be supported by ledger
evidence or by admissible normalization that does not invent ledger history.

### State-Machine Conformance

All lifecycle movement claimed by the reconstructed narrative must conform to
the canonical states and allowed transitions defined by
`docs/contracts/codex-session-state-machine-canon.md`.

### Evidence Precedence Compliance

Interpretation of session evidence must follow
`docs/governance/codex-session-evidence-interpretation-model.md` and must not
invert the authority order between state-machine, ledger, registry,
observation, and runtime-boundary surfaces.

### Observation Subordination

Lifecycle-observation signals may explain or normalize progression, but they
must not override ledger evidence or state-machine meaning.

### Runtime Boundary Compliance

Runtime-derived signals may add supporting context only when admitted through
the runtime-boundary canon. They must not redefine lifecycle truth or create
authoritative events absent from canonical surfaces.

### Deterministic Narrative Verification

The harness must confirm that the evidence set supports one bounded
governance-observable narrative. If ambiguity remains such that multiple valid
reconstructions exist, verification must fail.

## Output Classification

The harness must produce one governance result:

- `VERIFIED`
  - the reconstructed narrative is evidence-backed, deterministic, fully
    anchored, and conformant to all applicable verification checks
- `VERIFIED_WITH_RESTRICTIONS`
  - the reconstructed narrative is valid and deterministic, but bounded
    insufficiency or partial evidence remains explicit without contradicting
    canonical authority
- `FAILED`
  - the reconstructed narrative violates evidence anchoring, ledger integrity,
    state-machine conformance, evidence precedence, observation subordination,
    runtime-boundary compliance, or deterministic fail-closed behavior

`VERIFIED_WITH_RESTRICTIONS` is allowed only when restrictions are explicit and
the remaining evidence still supports one bounded narrative. It must not be
used to excuse invented events, invalid transitions, unresolved precedence
violations, or unresolved ambiguity.

## Allowed Behaviors

- verifying reconstructed session narratives against canonical Layer 6
  evidence surfaces
- classifying partial but still bounded narratives as
  `VERIFIED_WITH_RESTRICTIONS`
- failing closed when evidence is incomplete, contradictory, or ambiguous
- preserving distinct authority roles for state-machine, ledger, registry,
  observation, and runtime-boundary surfaces

## Prohibited Behaviors

- reconstructing a session narrative implicitly as part of harness evaluation
- accepting registry summary fields as a substitute for missing event history
- accepting invented lifecycle transitions not supported by canonical evidence
- allowing lifecycle observation to override ledger evidence
- allowing runtime context to displace canonical Layer 6 authorities
- treating ambiguous or contradictory evidence as verified truth

## Compliance Signals

Compliance is indicated when:

- the reconstructed narrative is anchored to canonical `session_id`
- every lifecycle claim can be traced to admissible canonical evidence
- lifecycle meaning remains subordinate to the state-machine canon
- ledger, registry, observation, and runtime-boundary roles remain distinct
- ambiguity and insufficiency are preserved explicitly instead of normalized
  away
- the harness remains doctrine-level and introduces no runtime behavior

## Ambiguity Handling

- If a reconstructed narrative is valid but only partially evidenced, the
  harness may return `VERIFIED_WITH_RESTRICTIONS` only when the restrictions
  are explicit and the bounded narrative remains unique.
- If evidence conflicts and precedence resolves the conflict cleanly, the
  harness may verify the resulting bounded narrative.
- If evidence conflicts and precedence does not resolve the conflict, the
  harness must return `FAILED`.

## Governance Implications

- Future verification lanes can evaluate reconstructed session narratives
  against one explicit Layer 7 verification target.
- Reconstruction drift can be classified more precisely as anchoring failure,
  invented history, precedence violation, invalid lifecycle movement, or
  unresolved ambiguity.
- Layer 6 reconstruction doctrine becomes operationally auditable without
  introducing runtime instrumentation.

## Non-Goals

This canon does not:

- implement a runtime verification engine
- create a new session evidence source
- replace the operational reconstruction procedure
- prove that every future reconstructed narrative will be correct without
  evidence inspection
