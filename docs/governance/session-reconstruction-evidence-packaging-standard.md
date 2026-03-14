# Session Reconstruction Evidence Packaging Standard

## Purpose

This canon defines the governance standard for packaging evidence used in
session reconstruction verification in `codex-governance-os`.

It exists so governance observers organize reconstruction evidence through one
deterministic, inspectable, and governance-safe structure that preserves
explicit citations, stable ordering, and visible restrictions across
reconstruction cases.

## Scope

This canon governs:

- the canonical structure of a session reconstruction evidence package
- the minimum sections required when packaging evidence for a reconstruction
  case
- deterministic ordering of packaged evidence
- citation and restriction discipline for packaged reconstruction evidence

This canon does not govern:

- reconstruction of session narratives itself
- replacement of the session reconstruction case verification model
- replacement of the session reconstruction verification harness
- automated session replay or runtime reconstruction tooling
- multi-session evidence aggregation
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
10. `docs/governance/session-reconstruction-case-verification-model.md`
11. `docs/contracts/codex-session-state-machine-canon.md`
12. `docs/governance/codex-session-registry.md`
13. `docs/governance/codex-session-ledger.md`
14. `docs/governance/codex-session-lifecycle-observation-discipline.md`
15. `docs/governance/codex-session-runtime-boundary-and-evidence-model.md`
16. this canon
17. generated pipeline artifacts and later runtime evidence records

This canon defines how evidence is organized for reconstruction verification
without overriding the higher Layer 6 session authorities, the harness, or the
case model.

## Evidence Package Concept

A session reconstruction evidence package is the complete collection of
artifacts used to evaluate one session reconstruction case.

Each evidence package must correspond to one reconstruction case and therefore
must be anchored on one canonical `session_id`.

An evidence package is not:

- a multi-session continuity bundle
- a replacement reconstruction case
- a replacement verification harness
- a runtime execution artifact

Evidence packages must not combine evidence from multiple governed sessions
into one package.

## Evidence Package Identity

Every evidence package must declare:

- `session_id`
- package scope
- reconstruction objective
- evaluation timestamp
- evaluator context

`session_id` is the mandatory identity anchor for the evidence package.

## Required Evidence Sections

Every evidence package must contain the following sections.

### Source Session Evidence

This section records evidence directly derived from the reconstructed session.

Examples include:

- conversation excerpts
- execution summaries
- session reconstruction outputs
- assistant responses relevant to governance evaluation

Quoted source evidence must preserve original wording and structure.

### Governance Doctrine Citations

This section records governance documents used during reconstruction
evaluation.

Examples include:

- architecture doctrine
- Layer 6 orchestration doctrine
- session reconstruction verification harness canon
- session reconstruction case verification model canon

Each citation must reference a specific governed surface.

### Pipeline Artifact References

This section records pipeline artifacts referenced during reconstruction.

Examples include:

- artifact bundles
- verification logs
- final verdict files
- pipeline definition files

Each artifact reference must include its canonical repository path.

### Reconstruction Assumptions

If reconstruction requires inference because evidence is incomplete, this
section must record:

- reconstruction assumptions
- inference boundaries
- ambiguity markers

Assumptions must never be embedded implicitly in verification conclusions.

### Restriction Record

If limitations affect reconstruction evaluation, they must be recorded in a
dedicated restriction section.

Examples include:

- missing artifacts
- incomplete session history
- ambiguous citations
- repository working tree inconsistencies

Restrictions must remain visible, explicit, and traceable.

## Evidence Ordering Discipline

Evidence packages must use deterministic ordering.

The canonical ordering is:

1. case identity
2. source session evidence
3. governance doctrine citations
4. pipeline artifact references
5. reconstruction assumptions
6. restriction record

Evidence ordering must not vary arbitrarily across cases.

## Citation Discipline

Every packaged evidence item must reference a specific governed surface.

Acceptable citation targets include:

- governance doctrine files
- pipeline artifact bundles
- pipeline definitions
- verification logs

Quoted defect evidence may remain quoted and does not become live semantics
merely by being included in the package.

## Restriction Preservation

Restrictions must always be recorded explicitly when they affect reconstruction
evaluation.

Restrictions may include:

- incomplete artifact surfaces
- dirty working tree state
- reconstruction ambiguity
- unresolved citation references

Restrictions must never be silently absorbed into general narrative
explanation.

## Canonical Rules

1. Every evidence package must anchor on one canonical `session_id`.
2. An evidence package must not combine multiple sessions into one packaged
   evaluation surface.
3. Every evidence package must declare its package scope, reconstruction
   objective, evaluation timestamp, and evaluator context.
4. Every evidence package must contain the required sections defined by this
   canon.
5. Every packaged evidence item must cite a specific governed surface.
6. Evidence packages must preserve the canonical ordering defined by this
   canon.
7. Reconstruction assumptions and ambiguity markers must remain explicit and
   inspectable.
8. Restrictions affecting the package must be recorded in a dedicated visible
   section.
9. This packaging standard must not introduce a new evidence-precedence model,
   runtime reconstruction semantics, or governance mutation authority.

## Relationship To Existing Doctrine

This packaging standard does not replace existing session reconstruction
doctrine.

Its relationship is:

- the session reconstruction case verification model defines case structure
- this canon defines evidence organization for those cases
- the session reconstruction verification harness evaluates cases using the
  packaged evidence

Each doctrine remains distinct and subordinate to the shared Layer 6 authority
hierarchy.

## Allowed Behaviors

- packaging reconstruction evidence for one bounded session case
- preserving original wording in quoted source evidence
- citing governance doctrine and pipeline artifacts explicitly
- recording assumptions and restrictions in dedicated visible sections

## Prohibited Behaviors

- combining evidence from multiple sessions into one package
- hiding restrictions or assumptions in narrative-only prose
- omitting citation targets for packaged evidence
- introducing runtime replay or automated reconstruction behavior through this
  canon
- granting the packaging standard authority to mutate governance state

## Compliance Signals

Compliance is indicated when:

- every evidence package begins from canonical `session_id`
- required sections are present and inspectable
- evidence ordering is deterministic across cases
- doctrine and artifact citations are explicit
- restrictions remain visible rather than hidden
- the packaging standard remains subordinate to the case model, harness, and
  Layer 6 authorities

## Governance Implications

- Reconstruction evidence can be compared across cases more consistently.
- Citation boundaries and assumptions remain easier to audit.
- Future reconstruction verification lanes gain one explicit packaging target
  without becoming runtime evaluation systems.

## Non-Goals

This canon does not:

- implement automated session replay
- define a multi-session continuity evidence bundle
- replace the case model or verification harness
- authorize runtime tooling or mutation behavior
