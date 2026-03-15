---
pipeline: 182
title: Enforce Governance State Snapshot as Required Input to Governance State Answers and Next-Action Selection
status: proposed
authoring_type: pipeline
governance_layer: "Layer 6 — Governance State, Reporting, and Next-Action Surfaces"
classification:
  primary: enforcement
  secondary:
    - canonical-state
    - fail-closed
    - provenance
registry_id: governance.state.enforce-snapshot-required-input-for-state-answers-and-next-action-selection
depends_on:
  - 165
  - 180
  - 181
produces:
  - docs/pipelines/governance/enforce-governance-state-snapshot-as-required-input-to-governance-state-answers-and-next-action-selection/01-problem-statement.md
  - docs/pipelines/governance/enforce-governance-state-snapshot-as-required-input-to-governance-state-answers-and-next-action-selection/02-required-snapshot-dependency-model.md
  - docs/pipelines/governance/enforce-governance-state-snapshot-as-required-input-to-governance-state-answers-and-next-action-selection/03-canonical-consumer-boundary.md
  - docs/pipelines/governance/enforce-governance-state-snapshot-as-required-input-to-governance-state-answers-and-next-action-selection/04-fail-closed-enforcement-design.md
  - docs/pipelines/governance/enforce-governance-state-snapshot-as-required-input-to-governance-state-answers-and-next-action-selection/05-implementation-summary.md
  - docs/pipelines/governance/enforce-governance-state-snapshot-as-required-input-to-governance-state-answers-and-next-action-selection/06-verification.md
  - docs/pipelines/governance/enforce-governance-state-snapshot-as-required-input-to-governance-state-answers-and-next-action-selection/07-final-verdict.md
verdict_strings:
  - GOVERNANCE_STATE_SNAPSHOT_REQUIRED_INPUT_ENFORCED
  - GOVERNANCE_STATE_SNAPSHOT_REQUIRED_INPUT_ENFORCED_WITH_BOUNDARIES
---

# 182 — Enforce Governance State Snapshot as Required Input to Governance State Answers and Next-Action Selection

## 1. Purpose

Pipeline 181 verified that the governance state snapshot is deterministic on unchanged canonical surfaces, records the expected governed hashes, detects bounded drift, and feeds deterministic selector metadata. That verification is necessary but not sufficient.

The remaining gap is enforcement.

Without an explicit dependency rule, governance state reporting, maturity scoring, roadmap answering, advisor surfaces, and next-action selection can still silently bypass the verified snapshot and read raw canonical sources directly. That would weaken provenance, permit mixed-surface answers, and allow state claims that are not bound to the snapshot identity verified in Pipeline 181.

This pipeline closes that gap by making the governance state snapshot the required canonical input for governance state answers and next-action selection, with explicit fail-closed behavior when the snapshot is missing, stale, inconsistent, or drifted beyond allowed boundaries.

## 2. Problem Statement

The repository now has a verified snapshot generator and a deterministic selector contract, but there is still a structural risk:

- a reporting surface may answer from raw files rather than the snapshot envelope
- a selector may compute next action from repository truth that is not tied to the current `snapshot_id`
- maturity or consensus answers may mix snapshot-backed and direct-source reads
- missing or drifted snapshots may degrade silently instead of producing an explicit restricted result
- downstream consumers may emit governance conclusions without carrying snapshot provenance

This violates the governance operating model in four ways:

1. **Canonical truth bypass**  
   A verified canonical summary exists, but consumers are not yet required to use it.

2. **Provenance weakening**  
   Outputs can omit the specific `snapshot_id` and still appear authoritative.

3. **Drift ambiguity**  
   Consumers may answer during a drifted state without surfacing that the answer is restricted or degraded.

4. **Inconsistent state semantics**  
   Different surfaces can produce answers from different source moments, weakening consensus.

## 3. Target Outcome

After this pipeline, the repository must satisfy all of the following:

- `governance-state-snapshot.json` is the required canonical state envelope for governance state answers and next-action selection.
- Governance outputs that answer current state, maturity, consensus, or next recommended action must carry snapshot provenance.
- A consumer that requires current governed state must not silently bypass the snapshot and read raw canonical surfaces directly.
- Missing, stale, mismatched, or drifted snapshot inputs must produce an explicit fail-closed or bounded degraded result.
- Verification must prove that supported consumers derive their state answer from the snapshot contract rather than from ungoverned direct reads.

## 4. Scope

This pipeline covers:

- governance state reporting surfaces
- governance system next-action selection
- maturity and consensus answering surfaces
- architecture/governance advisor surfaces where they claim current governance state
- selector metadata propagation rules
- fail-closed behavior for snapshot absence or invalidity
- canonical documentation and tests for the dependency contract

This pipeline does **not** require:

- expanding the canonical snapshot input set beyond the governed surfaces already verified in Pipeline 181
- changing governance scoring semantics unrelated to snapshot dependency
- changing roadmap semantics beyond binding current-state answers to snapshot provenance
- adding autonomous execution behavior

## 5. Canonical Enforcement Doctrine

### 5.1 Snapshot as required state envelope

For any governed surface that answers one or more of the following:

- current governance state
- governance maturity or advancement state
- current consensus or readiness state
- next recommended governance action
- current blocker or progression state
- current architecture/governance advisory state tied to repository truth

the answer must be derived from a valid governance state snapshot or from a derivative surface that explicitly references the same snapshot.

### 5.2 Minimum provenance fields

Any supported output claiming current governance state must expose, directly or through referenced metadata, at minimum:

- `snapshot_id`
- snapshot generation time or equivalent timestamp already supported by the snapshot surface
- `snapshot_drift_detected`
- governance state consensus or equivalent state resolution field when applicable

If a consumer cannot provide these fields, it must not claim authoritative current governance state.

### 5.3 Direct-read restriction

A consumer may still inspect raw canonical surfaces only when one of these is true:

- it is itself the snapshot generator
- it is a verification harness explicitly testing parity or drift behavior
- it is a diagnostic surface clearly labeled as non-authoritative
- it is operating in a documented fallback mode that returns a bounded degraded result rather than a normal authoritative answer

Outside these cases, direct raw-surface state answering is disallowed.

### 5.4 Fail-closed rules

The system must not silently return a normal authoritative state answer when any of the following hold:

- snapshot file is missing
- snapshot file is unreadable
- snapshot manifest is structurally invalid
- required provenance fields are absent
- selector metadata is missing required snapshot linkage
- canonical source hashes no longer match the snapshot and drift is not explicitly surfaced
- the consumer requires authoritative current state but only non-snapshot direct reads are available

In these conditions, the consumer must:

- block, or
- return a bounded degraded result with explicit reason, or
- emit a restricted advisory answer that states the snapshot dependency failure

## 6. Implementation Requirements

Implement this pipeline by making the smallest additive changes necessary to establish explicit enforcement.

### 6.1 Canonical dependency model

Add or update repository documentation so that it explicitly states:

- which surfaces are authoritative governance state consumers
- that those consumers require snapshot-backed state
- what provenance fields they must propagate
- what fail-closed outcomes are allowed

Preferred documentation targets include existing governance doctrine, state/reporting contracts, and any next-action or maturity surface specifications already present in the repository.

### 6.2 Consumer binding

Update the supported consumer implementation surfaces so that they:

- load or resolve governance state from `governance-state-snapshot.json` or a derivative snapshot-backed surface
- carry the snapshot metadata into their outputs
- refuse to present authoritative current-state answers if the snapshot contract is not satisfied

### 6.3 Selector contract hardening

The next-action selector contract must guarantee that:

- selection output links to the active `snapshot_id`
- selector output surfaces whether snapshot drift is present
- selector output does not represent itself as authoritative current next action if the snapshot dependency is broken

### 6.4 Reporting and scoring boundary hardening

Where governance reporting or scoring surfaces answer the current state, they must either:

- consume the snapshot as their required canonical input, or
- explicitly document that they are historical/diagnostic and non-authoritative

### 6.5 Diagnostic and fallback semantics

If there are fallback or diagnostic tools that can inspect raw canonical sources, preserve them only if:

- they are clearly marked non-authoritative, and
- they cannot be confused with the normal current-state answer surface

## 7. Required Artifact Bundle

Create the artifact bundle under:

`docs/pipelines/governance/enforce-governance-state-snapshot-as-required-input-to-governance-state-answers-and-next-action-selection/`

with the following files:

### `01-problem-statement.md`
Capture the structural gap left after Pipeline 181 and why verification without enforced dependency is insufficient.

### `02-required-snapshot-dependency-model.md`
Define which governance surfaces require snapshot-backed state, what provenance fields are mandatory, and what boundaries apply.

### `03-canonical-consumer-boundary.md`
Inventory authoritative consumers versus diagnostic or verification-only consumers, including direct-read restrictions.

### `04-fail-closed-enforcement-design.md`
Describe the precise fail-closed or degraded behavior for missing, invalid, mismatched, or drifted snapshots.

### `05-implementation-summary.md`
Summarize the code/documentation/test changes that bind consumers to the snapshot contract.

### `06-verification.md`
Record the exact verification steps, outputs, and observed results.

### `07-final-verdict.md`
Record the final verdict string and any bounded restrictions that remain.

## 8. Verification Requirements

Verification must prove not only that the snapshot exists, but that consumers are actually bound to it.

At minimum, verify all of the following:

1. **Authoritative consumer provenance**  
   For each supported authoritative governance-state consumer, show that output includes the required snapshot linkage.

2. **No silent bypass in normal path**  
   Demonstrate that supported authoritative consumers do not silently return normal current-state answers when the snapshot dependency is missing or invalid.

3. **Selector linkage**  
   Verify that next-action selection remains tied to `snapshot_id` and drift metadata.

4. **Explicit degraded behavior**  
   Simulate or exercise at least one missing/invalid/drifted snapshot scenario and confirm that the output is blocked or explicitly degraded, not silently normal.

5. **Regression safety**  
   Run the relevant governance regression suite and confirm it passes with the new enforcement behavior.

6. **Boundary preservation**  
   Confirm that verification-only and diagnostic surfaces remain available only within their documented non-authoritative scope.

## 9. Suggested Verification Commands

Use the repository’s actual command surface where available. The following are representative and should be adapted to the existing toolchain:

```bash
python3 tools/governance/gov.py --format json state-snapshot
python3 tools/governance/gov.py --format json next-action
python3 tools/governance/gov.py --format json project-status
python3 -m unittest discover -s tests/governance -p 'test_*.py'
```

If the repository uses different commands for snapshot generation, reporting, selection, or scoring, use those actual commands and record them precisely.

Where safe and bounded, include a controlled negative-path verification by temporarily removing, corrupting, or mismatching the snapshot input and then restoring it, proving that authoritative consumers fail closed or degrade explicitly.

## 10. Implementation Guidance

Use additive hardening rather than broad refactoring.

Preferred change strategy:

- first document the dependency model
- then bind the small number of authoritative consumer paths
- then add negative-path tests
- then verify bounded diagnostic exceptions remain explicit

Do not introduce hidden fallback behavior that reconstructs a normal authoritative answer from raw sources when snapshot dependency fails. If a fallback exists, it must be visibly degraded and non-authoritative.

Do not broaden the canonical input set in this pipeline unless required to preserve current documented state semantics. If expansion becomes necessary, record it as a bounded follow-up rather than silently widening this pipeline.

## 11. Acceptance Criteria

This pipeline is complete when all of the following are true:

- authoritative governance state consumers are explicitly documented
- those consumers require snapshot-backed state
- required provenance fields are propagated
- normal-path answers cannot silently bypass the snapshot dependency
- missing/invalid/drifted snapshot scenarios produce explicit blocked or degraded behavior
- relevant tests pass
- the artifact bundle is complete
- the final verdict is recorded

## 12. Expected Verdict

Use one of the following final verdicts:

- `GOVERNANCE_STATE_SNAPSHOT_REQUIRED_INPUT_ENFORCED`
- `GOVERNANCE_STATE_SNAPSHOT_REQUIRED_INPUT_ENFORCED_WITH_BOUNDARIES`

Use the second verdict only if bounded exceptions remain explicit, documented, and non-authoritative.

## 13. Recommended Follow-up

After this pipeline, the ideal next lane is:

**183 — Verify Governance State Reporting and Next-Action Surfaces Fail Closed on Missing or Drifted Snapshot**

That verification lane should test the negative paths more aggressively and prove that all authoritative state-answering surfaces converge on the same snapshot-backed truth.
