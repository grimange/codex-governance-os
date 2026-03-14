---
pipeline_id: "L0-00"
title: "Codex Pipeline — Scan Repository and Verify Layer 0 Governance Canon Gaps"
layer: "layer-0"
type: "verification"
status: "proposed"
purpose: "Scan the repository and determine what foundational Governance Canon capabilities already exist, what is partial, what is missing, and what should be implemented next before expanding Codex Behavior."
scope:
  includes:
    - governance canon vocabulary
    - authority hierarchy
    - evidence model
    - safety invariants
    - normalization boundary model
    - truth-source precedence
    - lifecycle/state canon
    - governed claim classification
  excludes:
    - implementing missing Layer 0 capabilities
    - modifying runtime behavior
    - modifying template composition logic
    - Git/PR operational governance
inputs:
  - repository tree
  - governance runtime files
  - governance docs
  - pipeline registry
  - existing verification artifacts
outputs:
  - "01-layer-0-scan-scope.md"
  - "02-layer-0-capability-inventory.md"
  - "03-layer-0-gap-matrix.md"
  - "04-layer-0-evidence-map.md"
  - "05-layer-0-missing-capabilities.md"
  - "06-layer-0-recommended-pipelines.md"
  - "07-verification.md"
  - "08-final-verdict.md"
success_criteria:
  - "Repository is scanned for explicit and implicit Layer 0 canon surfaces."
  - "Each Layer 0 capability is classified as ESTABLISHED, PARTIAL, MISSING, or UNCLEAR."
  - "Every classification is backed by file-path evidence."
  - "A recommended next-pipeline list is produced in dependency order."
  - "No implementation changes are made during this lane."
verification:
  - "Scan repository files and classify Layer 0 canon coverage."
  - "Verify whether canonical Layer 0 truth exists explicitly, implicitly, or not at all."
  - "Record evidence paths for every claim."
final_verdict_file: "08-final-verdict.md"
allowed_verdicts:
  - "LAYER_0_GOVERNANCE_CANON_GAPS_VERIFIED"
  - "LAYER_0_GOVERNANCE_CANON_PARTIALLY_ESTABLISHED"
  - "LAYER_0_GOVERNANCE_CANON_ALREADY_SUBSTANTIALLY_PRESENT"
---

# Codex Pipeline — Scan Repository and Verify Layer 0 Governance Canon Gaps

## 1. Problem Statement

`codex-governance-os` has active work in Layer 1 and Layer 2, and planned work in Layer 3. Before expanding Codex behavior, the repository should verify whether a proper **Layer 0 — Governance Canon** already exists explicitly, exists only implicitly across documents and code, or is materially missing.

This lane does not implement Layer 0. It verifies the current state and outputs a structured gap report for planning.

---

## 2. Objective

Produce an evidence-backed Layer 0 assessment that answers:

- What Layer 0 capabilities already exist?
- Which ones are only partial or implicit?
- Which ones are missing?
- What should be implemented next, in what order?

---

## 3. Canonical Layer 0 Capability Model

This lane evaluates the repository against the following Layer 0 capability domains.

### 3.1 Governance Canon Vocabulary
Canonical definitions for terms such as:

- pipeline
- lane
- establishment
- verification
- governed artifact
- authoritative
- evidence
- restriction
- normalization
- supported / unsupported boundary
- final verdict

### 3.2 Governance Authority Hierarchy
Explicit definition of which sources outrank others, such as:

- runtime execution truth
- registry truth
- verification artifact truth
- final verdict truth
- AI proposal vs executable authority

### 3.3 Governance Evidence Model
Explicit definition of what counts as proof, such as:

- tests
- verification logs
- artifact bundles
- required output files
- declared matrices
- canonical verdicts

### 3.4 Governance Safety Invariants
Non-negotiable fail-closed rules, such as:

- no silent semantic mutation
- no unverifiable success claim
- no hidden unsupported boundary
- no AI self-authorization
- no direct mutation of canonical state outside governed paths

### 3.5 Governance Normalization Boundary Model
Explicit boundary for what may be normalized automatically and what must block.

### 3.6 Governance Truth-Source Precedence
Explicit ordering of truth sources, such as:

- runtime truth over AI inference
- registry truth over narrative assumption
- evidence-backed verdict over summary text

### 3.7 Governance Lifecycle / State Canon
Explicit canonical lifecycle/state model for governance artifacts, lanes, and verdict-bearing outputs.

### 3.8 Governed Claim Classification Model
Explicit definitions for claim types, such as:

- established
- verified
- partial
- restricted
- unsupported
- blocked
- advisory

---

## 4. Required Scan Targets

Scan at minimum the following areas if present:

- `tools/governance/`
- `tools/pipelines/`
- `docs/governance/`
- `docs/pipelines/`
- `docs/pipelines/registry/`
- `docs/codex/`
- `docs/templates/`
- runtime entry files such as `gov.py`
- verification suites under `tests/` or equivalent
- registry and scaffold contracts
- instruction-routing documents
- README and contract docs that define canonical behavior

Also scan for implicit canon hidden inside:

- test assertions
- registry rules
- artifact naming conventions
- allowed verdict enumerations
- lane admission logic
- normalization logic
- dry-run / preflight classification logic

---

## 5. Classification Rules

Each Layer 0 capability must be classified using one of the following:

- **ESTABLISHED**  
  Explicitly defined, materially used, and evidenced in repository surfaces.

- **PARTIAL**  
  Present in some form, but incomplete, inconsistent, or only partially authoritative.

- **IMPLICIT_ONLY**  
  Observable through behavior, tests, or conventions, but not canonically defined.

- **MISSING**  
  No credible repository evidence of the capability.

- **UNCLEAR**  
  Possible traces exist, but evidence is insufficient to classify reliably.

Every classification must include:

- capability name
- classification
- evidence file paths
- brief reasoning
- blocker or risk if not established

---

## 6. Artifact Requirements

### 01-layer-0-scan-scope.md
Define:

- scan objective
- exact Layer 0 domains
- directories/files examined
- exclusions

### 02-layer-0-capability-inventory.md
Inventory each Layer 0 capability with:

- capability domain
- observed surfaces
- explicit vs implicit presence
- candidate authoritative files

### 03-layer-0-gap-matrix.md
Create a matrix like:

| Capability | Status | Evidence | Risk | Notes |
|---|---|---|---|---|
| Vocabulary | PARTIAL | `docs/...`, `tests/...` | semantic drift | definitions not centralized |

### 04-layer-0-evidence-map.md
Map every key claim to repository evidence paths.

### 05-layer-0-missing-capabilities.md
List only the missing or partial capabilities, with concise explanation of what is lacking.

### 06-layer-0-recommended-pipelines.md
Recommend the next Layer 0 pipelines in dependency order.

Suggested output sections:

- immediate must-have pipelines
- strong follow-up pipelines
- optional hardening pipelines

### 07-verification.md
Record:

- how the scan was performed
- which directories/files were inspected
- any constraints or uncertainty
- whether classifications are evidence-backed

### 08-final-verdict.md
Return one final verdict:

- `LAYER_0_GOVERNANCE_CANON_GAPS_VERIFIED`
- `LAYER_0_GOVERNANCE_CANON_PARTIALLY_ESTABLISHED`
- `LAYER_0_GOVERNANCE_CANON_ALREADY_SUBSTANTIALLY_PRESENT`

Include a concise summary:

- what exists
- what is partial
- what is missing
- what should be done next

---

## 7. Recommended Scan Heuristics

When scanning, treat Layer 0 as possibly existing in either of two forms:

### 7.1 Explicit Canon
Direct documents or code that clearly define canonical truth.

### 7.2 Emergent Canon
Rules inferred from:

- tests
- runtime validations
- registry constraints
- standard artifact bundles
- verdict schemas
- admission outcomes

If a capability exists only emergently, classify it as `IMPLICIT_ONLY` or `PARTIAL`, not `ESTABLISHED`.

---

## 8. Verification Questions the Lane Must Answer

The lane must explicitly answer:

1. Is there a single canonical vocabulary for governance terms?
2. Is authority precedence explicitly defined?
3. Is evidence formally distinguished from summary or interpretation?
4. Are fail-closed invariants explicitly documented?
5. Is normalization bounded by canon?
6. Is truth-source precedence defined?
7. Are lifecycle and claim classifications canonical?
8. Can Layer 3 be safely expanded without first formalizing Layer 0?

---

## 9. Expected Output Shape

The resulting report should be easy to paste back into ChatGPT and should include:

- a one-paragraph overall verdict
- a status table for all Layer 0 capability domains
- a short missing-capabilities list
- the top recommended next pipelines

---

## 10. Recommended Next Pipelines Template

If gaps are found, recommend pipelines in this order where relevant:

1. Establish Governance Canon Vocabulary
2. Verify Governance Canon Vocabulary
3. Establish Governance Authority Hierarchy
4. Verify Governance Authority Hierarchy
5. Establish Governance Evidence Model
6. Verify Governance Evidence Model
7. Establish Governance Safety Invariants
8. Verify Governance Safety Invariants
9. Establish Governance Normalization Boundary Model
10. Verify Governance Normalization Boundary Model
11. Establish Governance Truth-Source Precedence Model
12. Verify Governance Truth-Source Precedence Model

Optional additions if scan shows deeper gaps:

13. Establish Governance Lifecycle State Canon
14. Verify Governance Lifecycle State Canon
15. Establish Governed Claim Classification Model
16. Verify Governed Claim Classification Model

---

## 11. Execution Boundary

This lane is **verification-only**.

It must not:

- alter runtime code
- create or modify registry truth
- auto-implement missing Layer 0 canon
- rewrite docs except for the artifact bundle of this lane

It may only:

- inspect
- classify
- record evidence
- recommend next pipelines

---

## 12. Final Outcome

This pipeline is complete when the repository has an evidence-backed answer to:

> “What is missing in Layer 0 right now, based on the current repository state?”

That output can then be used to plan the actual Layer 0 establishment lanes.