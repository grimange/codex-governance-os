---
pipeline_id: "005"
title: "Audit Implementation Against Canonical Contract"
status: active
category: governance
stage: audit
objective: "Audit implementation behavior against a canonical contract and classify concrete drift findings."
depends_on: ["004"]
outputs: ["docs/pipelines/governance/audit-implementation-against-canonical-contract/"]
success_criteria: ["Contract scope is extracted.", "Implementation evidence is audited.", "Compliance and drift findings are recorded with a bounded verdict."]
governance_mode: fail-closed
execution_mode: advisory-then-enforcing
restrictions: ["Run only when a materially important canonical contract exists.", "Do not mutate implementation during the audit."]
non_claims: ["Does not remediate drift.", "Does not rewrite the governing contract."]
classification: governance.audit
authority: repo-governance
autonomy: advisory-only
problem_statement: "Canonical contracts become decorative if implementation is never audited against their authority, lifecycle, and interface expectations."
scope: "Extract contract scope, audit implementation surfaces, classify drift, and publish evidence-backed audit findings."
inputs: ["Canonical contract", "Architecture doctrine", "Relevant implementation evidence", "Optional prior governance artifacts"]
entry_conditions: ["A canonical contract exists and is important enough to enforce."]
exit_conditions: ["Compliance matrix, drift assessment, audit summary, and final verdict are recorded."]
validation: ["Inspect audit artifacts and compliance matrix.", "Confirm findings map to contract evidence."]
rollback: "No repository rollback is expected because this lane is audit-only; restore the lane body from version control if needed."
---

# Audit Implementation Against Canonical Contract

## Purpose

Audit repository implementation against a canonical contract to determine whether implementation behavior conforms to the contract’s authority model, lifecycle rules, state ownership rules, and interface expectations.

## Problem Statement

Without systematic contract audits, implementation drift accumulates silently and implementation behavior can displace the contract as the real authority.

## Objectives

- extract the contract scope and audit criteria
- inventory implementation surfaces relevant to the contract
- audit authority, lifecycle, interface, and compatibility behavior
- publish a compliance matrix and drift findings

## Scope

In scope: contract-scope extraction, implementation discovery, authority audit, lifecycle/state audit, interface audit, compatibility audit, compliance matrix, drift assessment, and audit summary.

Out of scope: remediation, contract rewriting, or alignment verification after fixes.

## Preconditions

- canonical subsystem contract exists
- contract scope can be mapped to inspectable implementation evidence
- audit outputs can be published under the canonical artifact root

## Execution Steps

1. Publish the audit summary and extract contract scope.
2. Discover implementation surfaces relevant to the contract.
3. Audit authority, lifecycle/state, interface, and compatibility behavior.
4. Produce the compliance matrix, drift assessment, audit findings summary, promotion guidance, and final verdict.

Universal skills:

- `implementation-contract-audit`

## Expected Outputs

- artifact bundle under `docs/pipelines/governance/audit-implementation-against-canonical-contract/`
- contract compliance matrix and drift assessment
- evidence-backed audit findings summary

## Verification Method

- inspect the compliance matrix and drift findings
- confirm findings cite the governing contract and implementation evidence
- confirm the final verdict and promotion decision are explicit

## Restrictions

- do not mutate implementation during the audit
- do not overclaim compliance when evidence is partial

## Non-Claims

- does not remediate or verify closure
- does not treat the contract as correct merely because it exists

## Final Verdict

Use a bounded audit verdict such as `IMPLEMENTATION_AUDITED_AGAINST_CONTRACT` or an explicitly restricted non-compliance equivalent.
