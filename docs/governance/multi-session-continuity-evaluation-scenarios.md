# Multi-Session Continuity Evaluation Scenarios

## Purpose

This canon defines the canonical scenario fixtures used to evaluate the
multi-session continuity verification stack in `codex-governance-os`.

It exists so the continuity model and evidence harness can be exercised through
deterministic, inspectable, and boundary-preserving scenarios rather than
through ad hoc examples or implicit reasoning.

## Scope

This canon governs:

- the canonical scenario set used to exercise multi-session continuity
  evaluation
- the minimum fields each scenario must declare
- the expected harness-internal continuity classification for each scenario
- the prohibited reasoning patterns that each scenario is designed to expose

This canon does not govern:

- replacement of the multi-session continuity verification model
- replacement of the multi-session continuity evidence harness
- replacement of single-session reconstruction doctrine
- runtime execution, replay, or automated session reconstruction
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
10. `docs/governance/multi-session-continuity-evidence-harness.md`
11. this canon
12. generated pipeline artifacts and later runtime evidence records

This canon provides bounded scenario fixtures for the established continuity
stack without overriding the higher continuity, handoff, or single-session
authorities.

## Scenario Purpose

The canonical scenario set exists to validate that multi-session continuity
evaluation:

- accepts admissible explicit cross-session evidence
- applies the minimum evidence threshold consistently
- classifies continuity strength deterministically
- preserves strict `session_id` isolation
- rejects continuity claims based on prohibited implicit reasoning

## Required Scenario Structure

Every canonical scenario must declare:

- `scenario_id`
- participating `session_id` values
- admissible cross-session evidence, if any
- expected harness-internal continuity classification
- prohibited reasoning patterns that must remain inadmissible
- governance boundary conditions being exercised

Scenario fixtures must remain fully inspectable from repository state and
must not depend on unstated narrative assumptions.

## Canonical Scenario Set

### Verified Continuity Scenario

This scenario exercises a valid continuity chain backed by strong explicit
evidence.

Required characteristics:

- one explicit predecessor-successor relationship
- one governance artifact continuation reference
- expected classification of `VERIFIED_CONTINUITY`

### Weak Continuity Scenario

This scenario exercises continuity with partial but admissible evidence.

Required characteristics:

- at least one admissible cross-session evidence link
- insufficient evidence for full continuity verification strength
- expected classification of `WEAK_CONTINUITY`

### No Continuity Scenario

This scenario exercises bounded independence between sessions.

Required characteristics:

- distinct `session_id` values
- no admissible cross-session evidence
- expected classification of `NO_CONTINUITY`

### Boundary Violation Scenario

This scenario exercises prohibited cross-session reasoning.

Required characteristics:

- attempted continuity inference without admissible evidence
- prohibited reasoning such as topic similarity or chronology
- expected failure classification of `SESSION_BOUNDARY_VIOLATION`

## Canonical Rules

1. Scenario fixtures must preserve strict per-session `session_id` boundaries.
2. Scenario fixtures must exercise only the continuity model and evidence
   harness already established in higher canons.
3. Scenario fixtures must not merge multiple sessions into one reconstructed
   state.
4. Expected classifications must remain consistent with
   `docs/governance/multi-session-continuity-evidence-harness.md`.
5. Prohibited reasoning patterns must remain explicit whenever a scenario is
   designed to expose invalid continuity claims.
6. Scenario fixtures must stay deterministic, inspectable, and reusable for
   later verification pipelines.
7. This canon must not introduce new continuity outcome types, runtime
   behavior, or governance mutation authority.

## Allowed Behaviors

- defining deterministic fixtures that exercise explicit continuity evidence
- recording the expected continuity classification for each fixture
- exposing boundary-violating reasoning patterns through controlled scenarios
- reusing scenario fixtures in later verification pipelines

## Prohibited Behaviors

- inferring continuity from chronology, similarity, or narrative pressure
- merging session event timelines across distinct `session_id` values
- treating scenario fixtures as replacements for live governance evidence
- introducing runtime replay, execution simulation, or governance mutation
  through this canon

## Compliance Signals

Compliance is indicated when:

- the canonical scenario set covers verified, weak, none, and
  boundary-violating continuity conditions
- each scenario declares explicit session identifiers and evidence conditions
- expected classifications align with the evidence harness
- prohibited reasoning patterns remain visible and bounded
- scenario fixtures remain distinct from single-session reconstruction

## Relationship To Existing Doctrine

This canon is subordinate to the multi-session continuity verification model
and the multi-session continuity evidence harness.

Doctrine responsibilities remain distinct:

- the continuity verification model defines what continuity verification is
- the continuity evidence harness defines how continuity evidence is evaluated
- this canon defines reusable scenario fixtures used to exercise that stack

## Non-Goals

This canon does not:

- implement runtime continuity validation
- replace the continuity evidence harness
- replace the single-session reconstruction stack
- authorize session merging or aggregate reconstructed state
