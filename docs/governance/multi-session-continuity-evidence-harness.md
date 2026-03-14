# Multi-Session Continuity Evidence Harness

## Purpose

This canon defines the governance evidence harness used to validate
multi-session continuity between independently verified Codex sessions in
`codex-governance-os`.

It exists so cross-session continuity claims are evaluated through one explicit
evidence-driven procedure that preserves strict `session_id` isolation, blocks
implicit continuity inference, and keeps multi-session continuity separate from
single-session reconstruction.

## Scope

This canon governs:

- allowed evidence types for multi-session continuity verification
- the minimum evidence threshold for continuity claims
- the deterministic procedure used to evaluate cross-session continuity
- bounded continuity classifications and failure classes
- governance boundary protections for cross-session evidence reasoning

This canon does not govern:

- reconstruction of any single session narrative
- replacement of the multi-session continuity verification model
- replacement of the single-session reconstruction verification stack
- runtime session replay or automated reconstruction engines
- session merging or aggregated reconstructed state
- governance mutation authority

## Governing Authority

Authority for this canon is ordered as follows:

1. version-controlled repository state
2. `AGENTS.md`
3. `docs/governance/architecture-doctrine.md`
4. `docs/governance/governance-evidence-interpretation-canon.md`
5. `docs/governance/governance-safety-invariants-canon.md`
6. `docs/governance/layer-6-codex-session-orchestration-and-handoff-discipline.md`
7. `docs/contracts/codex-session-handoff-packet-and-continuity-contract.md`
8. `docs/governance/codex-session-handoff-contract-and-resume-evidence-model.md`
9. `docs/governance/multi-session-continuity-verification-model.md`
10. `docs/governance/session-reconstruction-verification-harness.md`
11. `docs/governance/session-reconstruction-case-verification-model.md`
12. `docs/governance/session-reconstruction-evidence-packaging-standard.md`
13. `docs/contracts/codex-session-state-machine-canon.md`
14. `docs/governance/codex-session-registry.md`
15. `docs/governance/codex-session-ledger.md`
16. this canon
17. generated pipeline artifacts and later runtime evidence records

This canon operationalizes evidence evaluation under the continuity model
without overriding the higher continuity, handoff, and single-session
authorities.

## Harness Purpose

The multi-session continuity evidence harness provides the structured evidence
rules required to validate continuity relationships between independently
verified sessions.

The harness must ensure that cross-session continuity:

- requires explicit evidence
- preserves strict `session_id` isolation
- remains separate from single-session reconstruction
- is evaluated through a deterministic governance procedure

## Allowed Cross-Session Evidence Types

The harness admits only these evidence families for continuity validation.

### Explicit Session Predecessor Reference

Examples include:

- explicit predecessor-successor linkage in registry or ledger records
- explicit session-to-session relationship declarations in governed artifacts

### Governance Artifact Continuation

Examples include:

- later pipelines explicitly referencing artifacts from earlier sessions
- governed follow-up execution explicitly tied to prior verified session
  outputs

### Artifact Chain Evidence

Examples include:

- pipeline artifacts that reference earlier artifacts
- governance reports that reference previous verification outcomes

### Canonical Continuation Marker

Examples include explicit continuation markers such as:

- `continuation_of_session: <session_id>`

These markers are admissible only when they remain tied to governed evidence
surfaces rather than informal narrative alone.

## Continuity Evidence Threshold

Continuity between sessions requires minimum evidence conditions.

The minimum threshold is:

- at least one explicit cross-session evidence link between independently
  verified sessions

Stronger continuity support may include:

- predecessor reference
- artifact chain evidence
- governance lane continuation
- canonical handoff packet linkage

Continuity must not be inferred from:

- similar topics
- chronological proximity
- model memory assumptions
- conversational resemblance without governed evidence

## Continuity Verification Procedure

Continuity evaluation must follow this deterministic procedure.

### Step 1: Independent Session Verification

Each in-scope session must first pass single-session verification.

### Step 2: Evidence Discovery

Identify potential cross-session evidence links using admissible governed
surfaces.

### Step 3: Evidence Validation

Confirm that each candidate link matches one of the allowed evidence types and
does not exceed session-boundary rules.

### Step 4: Continuity Determination

Classify the continuity result as one of:

- `NO_CONTINUITY`
- `WEAK_CONTINUITY`
- `VERIFIED_CONTINUITY`

These are harness-internal continuity classifications used to determine the
strength of the evidence relationship. They do not replace the top-level
verification outcomes defined by the continuity model.

## Continuity Failure Classification

The harness must detect invalid continuity claims through these failure
classes:

- `CONTINUITY_CLAIM_WITHOUT_EVIDENCE`
- `AMBIGUOUS_SESSION_CONTINUITY`
- `SESSION_BOUNDARY_VIOLATION`
- `EVIDENCE_SCOPE_EXCEEDED`

These failure classes support bounded diagnosis of why a continuity claim did
not satisfy the evidence harness.

## Governance Boundary Protection

The harness must enforce the following boundaries.

### Session Isolation

A session is defined by canonical `session_id`.

Session event reconstruction must never cross session boundaries.

### Model Separation

The following verification layers must remain independent:

- single-session reconstruction
  - reconstructs and verifies events within one session
- multi-session continuity
  - evaluates relationships between independently verified sessions

### Evidence-Scoped Reasoning

Continuity claims must be based strictly on documented admissible evidence.

Implicit reasoning is disallowed.

## Outcomes

Top-level continuity verification outcomes remain aligned with the established
continuity model:

- `VERIFIED`
- `VERIFIED_WITH_RESTRICTIONS`
- `FAILED`

Harness-internal classifications such as `NO_CONTINUITY`, `WEAK_CONTINUITY`,
and `VERIFIED_CONTINUITY` provide evidence-strength interpretation within the
procedure and do not replace the top-level verification outcomes.

Canonical reusable fixtures for exercising those classifications are defined
by `docs/governance/multi-session-continuity-evaluation-scenarios.md`.

## Canonical Rules

1. Multi-session continuity evidence must be evaluated only between
   independently verified sessions.
2. Every in-scope session must retain its own canonical `session_id`.
3. Continuity claims must rely only on allowed explicit evidence types.
4. At least one explicit cross-session evidence link is required before a
   continuity claim can exceed `NO_CONTINUITY`.
5. Continuity must not be inferred from chronology, similarity, memory, or
   conversational resemblance alone.
6. The harness must classify continuity evidence deterministically using the
   procedure defined by this canon.
7. Failure classes must remain explicit when evidence is absent, ambiguous, or
   boundary-violating.
8. This harness must not merge session timelines, alter single-session
   reconstruction semantics, or introduce runtime continuity behavior.

## Allowed Behaviors

- validating explicit predecessor-successor linkage across verified sessions
- using governed artifact chains as admissible continuity evidence
- classifying continuity strength without replacing top-level verification
  outcomes
- failing continuity claims closed when evidence is absent or ambiguous

## Prohibited Behaviors

- inferring continuity from similar topics or chronology alone
- merging multiple sessions into one reconstructed state
- treating harness classifications as replacements for top-level verification
  outcomes
- introducing runtime replay or automated cross-session reconstruction through
  this canon
- granting the harness authority to mutate governance state

## Compliance Signals

Compliance is indicated when:

- explicit cross-session evidence types are bounded and inspectable
- the minimum continuity threshold is explicit
- session isolation remains strict through canonical `session_id`
- continuity reasoning remains evidence-scoped
- single-session and multi-session verification layers remain distinct
- failure classes identify absent, ambiguous, or boundary-violating evidence

## Governance Implications

- Multi-session continuity verification gains one explicit evidence harness.
- Cross-session claims can be audited for evidence sufficiency rather than
  inferred from narrative continuity.
- Future verification lanes can distinguish weak evidence from verified
  continuity without weakening session boundaries.

## Non-Goals

This canon does not:

- implement runtime continuity validation
- merge or replay sessions automatically
- replace the continuity verification model
- replace the handoff packet or handoff/resume authorities
