---
pipeline_id: "003"
title: "Discover Contract Candidates and Authority Surfaces"
status: active
category: governance
stage: discovery
objective: "Discover contract candidates, subsystem boundaries, and authority surfaces that require explicit canonical governance."
depends_on: ["001", "002"]
outputs: ["docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/"]
success_criteria: ["Contract candidates are inventoried.", "Authority surfaces are classified.", "Recommendations and a discovery ledger are recorded."]
governance_mode: fail-closed
execution_mode: advisory-then-enforcing
restrictions: ["Treat this lane as conditional for small repositories.", "Do not guess missing authority boundaries."]
non_claims: ["Does not author canonical contracts.", "Does not remediate implementation drift."]
classification: governance.discovery
authority: repo-governance
autonomy: advisory-only
problem_statement: "Architecture doctrine alone is too broad for downstream audits and remediation unless explicit contract candidates and authority surfaces are discovered."
scope: "Inventory repository surfaces, discover subsystem boundaries, classify authority, assess contract risk, and publish recommendations."
inputs: ["Architecture doctrine", "Repository evidence", "Existing contract and governance documents"]
entry_conditions: ["Architecture doctrine exists and contract discovery is materially useful for the repository."]
exit_conditions: ["Contract candidates, authority surfaces, and follow-on recommendations are recorded."]
validation: ["Inspect the discovery matrix, ledger, and verification artifacts."]
rollback: "Restore the prior lane definition from version control if template migration introduces semantic drift."
---

# Discover Contract Candidates and Authority Surfaces

## Purpose

Discover where explicit canonical contracts should exist and which repository surfaces currently act as authoritative, derived, compatibility-only, legacy, or ambiguous sources of truth.

## Problem Statement

Without systematic contract discovery, downstream governance risks treating implicit rules and accidental implementation patterns as if they were already governed.

## Objectives

- inventory repository surfaces relevant to contract discovery
- identify subsystem boundaries and authority surfaces
- assess drift, contract gaps, and risk
- publish recommendations and a durable discovery ledger

## Scope

In scope: discovery scope definition, taxonomy design, surface inventory, subsystem boundary analysis, authority analysis, contract-candidate matrix, risk assessment, and supporting-surface updates.

Out of scope: contract authoring, remediation, or verification of implementation against a contract.

## Preconditions

- architecture doctrine exists
- repository evidence is inspectable
- contract discovery is justified by subsystem or authority-surface complexity

## Execution Steps

1. Publish the discovery summary and taxonomy boundaries.
2. Inventory repository surfaces and discover subsystem boundaries.
3. Analyze authority surfaces, existing contracts, and drift risk.
4. Produce the candidate matrix, recommendations, discovery ledger, and supporting-surface updates.
5. Verify installation and record the final verdict.

Universal skills:

- `repository-discovery`
- `contract-candidate-discovery`

## Expected Outputs

- artifact bundle under `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/`
- contract-candidate matrix and authority-surface analysis
- durable discovery recommendations and ledger

## Verification Method

- inspect the candidate matrix, crosswalk, and risk assessment artifacts
- confirm supporting-surface updates and ledger publication
- confirm the final verdict reflects the recorded discovery state

## Restrictions

- keep the lane conditional for repositories where explicit contract discovery is not yet warranted
- do not elevate ambiguous evidence into canonical contract boundaries

## Non-Claims

- does not establish a canonical contract by itself
- does not guarantee every future subsystem needs contracting

## Final Verdict

Use a bounded discovery verdict such as `CONTRACT_CANDIDATES_DISCOVERED` or an explicitly restricted equivalent.
