# Session Reconstruction Case Verification Model

## Purpose

This canon defines the governance case model for evaluating individual
reconstructed Codex sessions in `codex-governance-os`.

It exists so governance observers use one deterministic, inspectable, and
governance-safe structure when preparing session reconstruction cases for
evaluation under the session reconstruction verification harness.

## Scope

This canon governs:

- the canonical structure of an individual session reconstruction verification
  case
- the minimum fields and evidence declarations required for case preparation
- the evaluation dimensions that a reconstruction case must expose for harness
  review
- explicit restriction recording for incomplete, ambiguous, or bounded case
  evidence

This canon does not govern:

- reconstruction of session narratives itself
- replacement of the session reconstruction verification harness
- automated runtime evaluation tooling
- multi-session continuity verification models
- mutation authority over governance artifacts

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
9. `docs/governance/session-reconstruction-verification-harness.md`
10. `docs/contracts/codex-session-state-machine-canon.md`
11. `docs/governance/codex-session-registry.md`
12. `docs/governance/codex-session-ledger.md`
13. `docs/governance/codex-session-lifecycle-observation-discipline.md`
14. `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`
15. this canon
16. generated pipeline artifacts and later runtime evidence records

This canon defines the structure of case inputs evaluated by the harness
without overriding the higher Layer 6 session authorities or the harness
itself.

## Reconstruction Case Concept

A session reconstruction case is one bounded evaluation package describing
whether a reconstructed session faithfully reflects the original governed
execution state for one canonical `session_id`.

A reconstruction case is not:

- a multi-session continuity record
- a replacement session narrative
- an alternative evidence-precedence model
- an automated runtime evaluation artifact

Each case must remain scoped to a single `session_id`. Cases must not merge
evidence from multiple governed sessions into one evaluation unit.

## Case Structure

### Case Identity

Every reconstruction case must declare:

- `session_id`
- reconstruction scope
- verification objective
- evaluation timestamp
- evaluator context

`session_id` is the mandatory identity anchor for the case.

### Reconstruction Scope

Every case must declare the bounded surfaces being reconstructed and evaluated.

Examples include:

- conversation history
- pipeline execution history
- governance artifact references
- interpretation decisions

Scope must be explicit enough to show what the case includes and excludes.

### Evidence Sources

Every case must declare all evidence used during reconstruction evaluation.

Evidence may include:

- conversation transcripts
- pipeline artifacts
- governance doctrine
- verification logs
- referenced governance documents

All evidence used by the case must be explicitly cited. Uncited evidence must
not influence the case outcome.

### Reconstruction Assumptions

If evidence gaps exist, the case must record:

- reconstruction assumptions
- inference boundaries
- ambiguity markers

Assumptions must remain explicit and inspectable. They must not be embedded
silently in the narrative or evaluation summary.

## Evaluation Dimensions

Each reconstruction case must expose the following evaluation dimensions.

### Structural Completeness

The case must show whether the reconstructed session includes all required
structural elements within its declared scope.

Examples include:

- referenced pipelines
- artifact bundles
- governance doctrine citations

### Citation Integrity

The case must show whether cited surfaces:

- exist
- correspond to the referenced governance documents
- maintain citation fidelity

### Authority Compliance

The case must show whether interpretation follows the Layer 6 authority
hierarchy and the session reconstruction verification harness without
introducing new precedence rules.

### Continuity Fidelity

The case must show whether the reconstructed session faithfully represents:

- pipeline order
- decision sequence
- governance outcomes

### Restriction Preservation

The case must show whether reconstruction limitations remain explicit as
restrictions rather than being hidden in narrative summary.

## Canonical Rules

1. Every reconstruction case must anchor on one canonical `session_id`.
2. A reconstruction case must declare its reconstruction scope before outcome
   evaluation occurs.
3. Every evidence source used by the case must be explicitly cited.
4. A reconstruction case must not combine evidence from multiple sessions into
   one evaluation unit.
5. A reconstruction case must record assumptions, inference boundaries, and
   ambiguity markers explicitly whenever the evidence is incomplete.
6. A reconstruction case must expose the required evaluation dimensions:
   structural completeness, citation integrity, authority compliance,
   continuity fidelity, and restriction preservation.
7. A reconstruction case must preserve restrictions explicitly rather than
   embedding them implicitly in narrative prose.
8. A reconstruction case must use only the bounded outcome model authorized by
   the session reconstruction verification harness.
9. A reconstruction case must not introduce a new evidence-precedence model,
   runtime execution semantics, or governance mutation behavior.

## Restriction Discipline

Restrictions must be recorded when:

- evidence is incomplete
- reconstruction assumptions are required
- repository state introduces ambiguity
- verification surfaces contain environmental inconsistencies
- citation boundaries cannot support stronger certainty

Restrictions must be:

- explicit
- inspectable
- tied to the affected case dimension
- preserved in the final evaluation summary

Restrictions must never be hidden inside general narrative wording or omitted
because the case still reaches a bounded result.

## Outcome Model

Reconstruction cases may produce only these outcomes:

- `VERIFIED`
- `VERIFIED_WITH_RESTRICTIONS`
- `FAILED`

These outcomes are defined and bounded by
`docs/governance/session-reconstruction-verification-harness.md`.

This canon does not authorize additional outcome types or softer narrative
classifications.

## Relationship To The Verification Harness

The session reconstruction verification harness performs evaluation.

This case model defines the required structure of evaluation inputs consumed by
that harness.

Where evidence is assembled for case evaluation, packaging should follow
`docs/governance/session-reconstruction-evidence-packaging-standard.md`.

Accordingly:

- the harness evaluates cases prepared through this model
- this model does not replace the harness
- this model does not change harness outcome rules
- this model does not create a second evaluation authority

## Allowed Behaviors

- preparing bounded reconstruction cases for one `session_id`
- explicitly citing evidence sources used by case evaluation
- preserving assumptions and ambiguity as explicit restrictions
- structuring case inputs so harness evaluation remains consistent across
  sessions

## Prohibited Behaviors

- combining multiple sessions into one reconstruction case
- hiding assumptions or restrictions in narrative-only prose
- introducing additional outcome types beyond the harness doctrine
- introducing runtime tooling or automated reconstruction behavior through this
  canon
- granting the case model authority to mutate governance state

## Compliance Signals

Compliance is indicated when:

- every case begins with canonical `session_id`
- case scope and objective are explicit
- evidence sources and assumptions are inspectable
- the required evaluation dimensions are present
- restrictions remain explicit rather than hidden
- the case model remains subordinate to the verification harness and Layer 6
  authorities

## Governance Implications

- Session reconstruction verification can be prepared through one canonical
  case structure instead of session-specific ad hoc formats.
- Restrictions and ambiguity can be compared across cases more consistently.
- The verification harness gains a deterministic input model without becoming
  a runtime evaluation system.

## Non-Goals

This canon does not:

- implement an automated reconstruction engine
- implement runtime evaluation tooling
- verify cross-session continuity chains
- replace the verification harness or reconstruction rules
