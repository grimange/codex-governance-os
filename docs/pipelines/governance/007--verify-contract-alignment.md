---
pipeline_id: "007"
title: "Verify Contract Alignment"
status: active
category: governance
stage: verification
objective: "Verify that implementation now aligns with the governing contract after remediation."
depends_on: ["005", "006"]
outputs: ["docs/pipelines/governance/verify-contract-alignment/"]
success_criteria: ["Verification criteria are extracted.", "Implementation is reinspected.", "Residual risk and final verdict are recorded."]
governance_mode: fail-closed
execution_mode: advisory-then-enforcing
restrictions: ["Run only after a contract and remediation evidence exist.", "Do not collapse residual uncertainty into a false pass."]
non_claims: ["Does not author the original contract.", "Does not replace remediation work."]
classification: governance.verification
authority: repo-governance
autonomy: advisory-only
problem_statement: "Remediation changes are not complete governance work until alignment with the governing contract is explicitly verified."
scope: "Extract verification criteria, reinspect implementation, evaluate behavior, update compliance status, and record residual risk."
inputs: ["Canonical contract", "Pipeline 005 audit findings", "Pipeline 006 remediation artifacts", "Optional tests or runtime evidence"]
entry_conditions: ["A governing contract exists and remediation work is ready for explicit verification."]
exit_conditions: ["Alignment findings, residual risk, and final verdict are explicitly recorded."]
validation: ["Inspect verification artifacts and compliance updates.", "Confirm evidence supports the final verdict."]
rollback: "Restore the lane definition from version control if template migration introduces semantic drift; repository rollback is handled by remediation controls, not this verification lane."
---

# Verify Contract Alignment

## Purpose

Verify that subsystem implementation now conforms to the canonical contract after remediation.

## Problem Statement

Without explicit verification, remediation cannot be considered complete and contract alignment remains an unproven claim.

## Objectives

- extract the contract-alignment criteria that must now hold
- reinspect implementation and relevant behavior
- update compliance status and assess residual risk
- publish an evidence-backed verification verdict

## Scope

In scope: verification-criteria extraction, implementation reinspection, behavioral verification, compliance update, residual-risk assessment, verification summary, and promotion guidance.

Out of scope: original contract authoring or new remediation planning beyond residual-risk notes.

## Preconditions

- canonical contract exists
- remediation work is complete enough to inspect
- evidence sources such as tests, runtime checks, or documentation are available as applicable

## Execution Steps

1. Publish the verification summary and extract verification criteria.
2. Reinspect implementation and evaluate relevant behavior against the contract.
3. Update compliance status, assess residual risk, and publish the verification summary.
4. Record promotion guidance and the final verdict.

Universal skills:

- `contract-alignment-verification`

## Expected Outputs

- artifact bundle under `docs/pipelines/governance/verify-contract-alignment/`
- updated contract-alignment assessment and residual-risk notes
- explicit verification verdict and promotion recommendation

## Verification Method

- inspect verification criteria, reinspection artifacts, and compliance updates
- confirm residual-risk statements are explicit
- confirm the final verdict is evidence-backed

## Restrictions

- do not claim full alignment without evidence
- do not substitute verification for missing remediation

## Non-Claims

- does not guarantee the contract is optimal
- does not eliminate the need for future audits if implementation changes again

## Final Verdict

Use a bounded verification verdict such as `CONTRACT_ALIGNMENT_VERIFIED` or an explicitly restricted equivalent.
