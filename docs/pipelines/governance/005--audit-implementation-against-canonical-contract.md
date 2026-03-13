# Codex Pipeline — Audit Implementation Against Canonical Contract

Pipeline ID: 005  
Category: governance  
Stage: audit  
Status: PROPOSED

---

# Purpose

Audit the repository implementation against a canonical subsystem contract to determine whether implementation behavior conforms to the contract’s authority model, lifecycle rules, state ownership rules, and interface expectations.

This pipeline evaluates contract compliance and identifies implementation drift.

It produces an evidence-based audit report but does not modify code or contracts.

This pipeline is conditional on a repository already having a canonical contract that is materially important to enforce.

---

# Why This Pipeline Exists

A canonical contract defines the intended behavior of a subsystem.

However, implementation may diverge from the contract due to:

- legacy behavior
- incomplete modernization
- undocumented compatibility layers
- developer assumptions
- accidental drift
- partial migrations
- outdated implementation patterns

Without systematic contract audits:

- contracts become decorative
- implementation becomes the real authority
- drift accumulates silently
- remediation pipelines lack evidence
- verification pipelines cannot determine closure

This pipeline ensures that contracts remain operational governance surfaces.

---

# Inputs

Required inputs:

- canonical subsystem contract  
- architecture doctrine  
- subsystem evidence artifacts from Pipeline 004  

Optional inputs:

- contract discovery ledger  
- prior governance audit artifacts  
- runtime inspection artifacts  

---

## Universal Skill References

- `implementation-contract-audit`
  Use for contract-scope extraction, implementation surface discovery, compliance analysis, drift classification, and audit-summary generation.

# Phase 00 — Pipeline Summary

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/00-pipeline-summary.md

The summary must document:

- repository under review
- subsystem contract under audit
- contract authority level
- subsystem scope
- audit objective
- expected audit coverage

---

# Phase 01 — Contract Scope Extraction

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/01-contract-scope-extraction.md

Use the `implementation-contract-audit` skill to extract from the canonical contract:

- subsystem scope
- lifecycle rules
- authority model
- source-of-truth rules
- state ownership
- command semantics
- event semantics
- interface rules
- compatibility boundaries

This phase converts contract language into **audit criteria**.

---

# Phase 02 — Implementation Surface Discovery

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/02-implementation-surface-discovery.md

Use the `implementation-contract-audit` skill to discover implementation surfaces relevant to the contract.

Possible surfaces include:

- service classes
- controllers
- handlers
- lifecycle orchestrators
- persistence layers
- state stores
- event publishers
- event consumers
- API interfaces
- configuration surfaces
- compatibility adapters

Each discovered surface must include:

- path
- responsibility
- relationship to subsystem
- authority classification

---

# Phase 03 — Authority Model Audit

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/03-authority-model-audit.md

Use the `implementation-contract-audit` skill to evaluate whether implementation obeys the contract authority model.

The audit must determine:

- whether source-of-truth ownership matches the contract
- whether state mutations occur in allowed layers
- whether projections are treated as authoritative
- whether command boundaries are respected
- whether lifecycle authority is consistent with doctrine

Findings must include:

- compliant behavior
- partial compliance
- authority violations
- ambiguous authority surfaces

---

# Phase 04 — Lifecycle and State Compliance Audit

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/04-lifecycle-state-compliance-audit.md

Audit lifecycle and state rules defined in the contract.

Evaluate:

- lifecycle state transitions
- state creation rules
- state mutation rules
- state termination rules
- lifecycle event publication
- lifecycle vocabulary consistency

Identify:

- missing lifecycle transitions
- undocumented states
- conflicting lifecycle definitions
- state mutations outside allowed boundaries

---

# Phase 05 — Interface and Interaction Audit

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/05-interface-interaction-audit.md

Evaluate whether implementation respects interface rules defined by the contract.

Audit:

- command interfaces
- API boundaries
- event publication semantics
- event consumption semantics
- request/response expectations
- integration surfaces

Identify violations such as:

- interface misuse
- undocumented side effects
- incompatible message structures
- hidden state mutations

---

# Phase 06 — Compatibility and Legacy Surface Audit

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/06-compatibility-legacy-audit.md

Evaluate compatibility and legacy behavior relative to the contract.

Identify:

- legacy modules influencing canonical behavior
- compatibility layers incorrectly treated as primary behavior
- deprecated behavior still active
- legacy lifecycle vocabulary

Each item must record:

- evidence
- subsystem affected
- governance risk
- remediation likelihood

---

# Phase 07 — Contract Compliance Matrix

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/07-contract-compliance-matrix.md

Use the `implementation-contract-audit` skill to produce a structured matrix mapping contract rules to implementation evidence.

Example structure:

| Contract Rule | Implementation Surface | Status | Evidence | Notes |
|---------------|-----------------------|--------|---------|------|

Status values:

- compliant
- partially compliant
- non-compliant
- ambiguous
- unverified

This matrix is the primary evidence surface for remediation pipelines.

---

# Phase 08 — Implementation Drift Assessment

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/08-implementation-drift-assessment.md

Use the `implementation-contract-audit` skill to identify implementation drift relative to the contract.

Drift categories include:

- authority drift
- lifecycle drift
- state ownership drift
- interface drift
- compatibility drift
- undocumented behavior

Each drift item must include:

- description
- contract rule violated
- implementation evidence
- subsystem affected
- severity

Severity levels:

LOW  
MODERATE  
HIGH  
BLOCKING

---

# Phase 09 — Audit Findings Summary

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/09-audit-findings-summary.md

Summarize:

- compliant areas
- partial compliance
- major violations
- ambiguous surfaces
- legacy influence

The summary must clearly state the **overall compliance posture**.

---

# Phase 10 — Promotion Decision

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/10-promotion-decision.md

Possible outcomes:

PROMOTE  
PROMOTE_WITH_REMEDIATION_REQUIRED  
REQUIRES_REMEDIATION  
BLOCKED

PROMOTE only when implementation substantially conforms to the contract.

---

# Phase 11 — Final Verdict

Output artifact:

docs/pipelines/governance/audit-implementation-against-canonical-contract/11-final-verdict.md

Allowed verdicts:

IMPLEMENTATION_CONTRACT_COMPLIANT  
IMPLEMENTATION_PARTIALLY_COMPLIANT  
IMPLEMENTATION_DRIFT_DETECTED  
IMPLEMENTATION_CONTRACT_VIOLATION

The final verdict must summarize:

- subsystem audited
- compliance level
- major drift areas
- remediation urgency
- recommended next pipeline

---

# Required Deliverables

This pipeline is not complete unless it produces:

- pipeline summary
- contract scope extraction
- implementation surface discovery
- authority model audit
- lifecycle/state compliance audit
- interface interaction audit
- compatibility legacy audit
- contract compliance matrix
- drift assessment
- audit findings summary
- promotion decision
- final verdict

---

# Execution Rules

Audit must remain evidence-based.

Implementation must not be modified during the audit.

Contract interpretation must align with architecture doctrine.

Legacy behavior must be identified explicitly rather than ignored.

Ambiguity must be recorded instead of silently resolved.

---

# Recommended Next Pipelines

After an implementation audit, the next stage is typically:

006--remediate-implementation-drift-against-contract.md

or if compliance is high:

007--verify-contract-alignment.md

---

# Completion Standard

This pipeline is complete only when implementation compliance relative to the canonical contract is explicitly documented and remediation decisions are supported by evidence.
