# Codex Pipeline — Discover Contract Candidates and Authority Surfaces

**Pipeline ID**: 003  
**Category**: governance  
**Stage**: discovery  
**Status**: PROPOSED

## Purpose

Discover the repository’s contract candidates and authority surfaces from implementation, documentation, runtime structure, and architecture doctrine evidence.

This pipeline identifies where explicit subsystem contracts should exist, what they should govern, and which repository surfaces currently appear authoritative, derived, compatibility-only, legacy, or ambiguous.

It transforms a repository with architecture doctrine into a repository with a structured contract discovery map suitable for contract authoring, audit, remediation, and verification pipelines.

---

## Why This Pipeline Exists

Architecture doctrine defines the high-level rules of the system, but downstream governance requires more specific contract surfaces.

Without explicit contract discovery, repositories often suffer from:

- undocumented subsystem boundaries
- unclear source-of-truth ownership
- competing lifecycle vocabularies
- implementation drift hidden behind compatibility layers
- implicit rules that are never made auditable
- contract authoring done ad hoc instead of systematically

This pipeline identifies where explicit contracts are needed and what authority surfaces they must govern.

---

## Universal Skill References

- `repository-discovery`
  Use for surface inventory and evidence separation.
- `contract-candidate-discovery`
  Use for taxonomy definition, subsystem boundary analysis, candidate ranking, and recommendation design.

# Phase 00 — Pipeline Summary

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/00-pipeline-summary.md`

## Required Contents

Document:

- repository under review
- architecture doctrine status
- contract discovery objective
- expected classes of contract candidates
- expected authority-surface outputs
- principal governance risk if contract discovery is not performed

The summary must classify the repository’s current contract maturity as one of:

- contract-uninitialized
- contract-emergent
- partially contracted
- contract-fragmented
- contract-oriented but incomplete

---

# Phase 01 — Discovery Scope and Contract Taxonomy

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/01-scope-and-contract-taxonomy.md`

## Required Work

Define the discovery scope and the candidate contract taxonomy that will be used for the repository.

The artifact must identify:

### In Scope

- subsystem boundaries
- state authority boundaries
- runtime orchestration boundaries
- external interface boundaries
- event contracts
- command contracts
- lifecycle/state transition contracts
- persistence/state-store contracts
- API/request-response contracts
- compatibility-layer boundaries
- UI/backend authority boundaries where relevant

### Out of Scope

This pipeline does not:

- remediate implementation
- verify live runtime behavior unless required by local doctrine
- author final subsystem contracts in full
- declare contract closure
- promote any candidate contract to canonical status automatically
- replace architecture doctrine

### Contract Taxonomy

The artifact must define the contract classes used for discovery, such as:

- architecture doctrine contract
- subsystem responsibility contract
- runtime orchestration contract
- lifecycle/state contract
- identity contract
- persistence/state-store contract
- interface/API contract
- event publication contract
- projection/UI consumption contract
- compatibility/deprecation contract

The taxonomy may be tailored to the repository but must be explicit.

---

# Phase 02 — Repository Surface Inventory for Contract Discovery

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/02-surface-inventory.md`

## Required Work

Use the `repository-discovery` skill to produce a structured inventory of repository surfaces relevant to contract discovery.

The inventory must include, where present:

- core service modules
- controllers/handlers
- domain services
- state stores
- queues/workers
- runtime lifecycle handlers
- event emitters/consumers
- frontends/projection layers
- persistence adapters
- API surfaces
- configuration surfaces that affect behavior
- compatibility bridges
- legacy modules
- governance docs and draft contract docs

Each surface should be recorded with:

- path or location
- role in system behavior
- apparent responsibility
- likely governing contract class
- confidence level
- whether the surface appears canonical, derived, compatibility-only, legacy, or ambiguous

The inventory must separate code evidence from document claims.

---

# Phase 03 — Subsystem Boundary Discovery

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/03-subsystem-boundary-discovery.md`

## Required Work

Use the `contract-candidate-discovery` skill to identify the major subsystems that likely require explicit contracts.

For each subsystem candidate, record:

- subsystem name
- purpose
- inputs
- outputs
- owned state or resources
- lifecycle or responsibility boundary
- upstream dependencies
- downstream consumers
- likely contract need
- current documentation state

A subsystem is a strong contract candidate when it has one or more of the following:

- distinct authority boundary
- owned state
- orchestration responsibility
- externally visible interface
- event publication responsibility
- compatibility behavior
- high change risk
- repeated ambiguity in repository behavior or docs

This phase must distinguish between:

- real subsystem boundaries
- implementation modules that are not true governance boundaries

---

# Phase 04 — Authority Surface Analysis

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/04-authority-surface-analysis.md`

## Required Work

Identify and classify the authority surfaces relevant to contract design.

For each major surface, classify it as one of:

- canonical authority
- likely authority candidate
- descriptive only
- derived/projection
- compatibility layer
- legacy residual
- unresolved ambiguity

Authority surfaces may include:

- backend services
- runtime state stores
- databases
- Redis/state cache layers
- event streams
- UI stores
- API contracts
- docs that appear normative
- legacy adapters that still influence behavior

The analysis must answer:

- where truth appears to originate
- which layers are allowed to author state
- which layers only project or consume state
- which documents likely define intended behavior
- where authority conflicts exist
- where contract boundaries are required to prevent drift

This phase must remain evidence-based and must not promote surfaces to canonical authority without justification.

---

# Phase 05 — Contract Candidate Matrix

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/05-contract-candidate-matrix.md`

## Required Work

Use the `contract-candidate-discovery` skill to create the central matrix of candidate contracts.

Each candidate row should include:

- candidate contract name
- governing scope
- affected subsystem(s)
- contract class
- primary authority surface
- supporting authority surfaces
- principal risks if undocumented
- current status
- recommended next action

Suggested status values:

- missing
- partially implied
- draft exists
- fragmented
- likely canonical but undocumented
- documented but stale
- already canonical

Suggested next actions:

- author new contract
- audit existing contract
- normalize fragmented surfaces
- verify canonical candidate
- defer pending architecture clarification

This matrix is the primary planning surface for future contract pipelines.

---

# Phase 06 — Existing Contract and Document Crosswalk

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/06-existing-contract-crosswalk.md`

## Required Work

Crosswalk discovered contract candidates against existing governance documents.

The crosswalk must determine for each candidate whether:

- no relevant document exists
- a draft or partial document exists
- multiple fragmented documents exist
- a likely authoritative contract already exists
- a stale document conflicts with implementation evidence
- a descriptive document is being mistaken for a contract

For each matched document, record:

- document path
- claimed scope
- actual usefulness
- apparent authority level
- whether it is suitable for audit
- whether remediation or replacement is required

This phase prevents redundant contract creation and exposes false authority.

---

# Phase 07 — Drift, Gaps, and Contract Risk Assessment

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/07-drift-gaps-and-risk-assessment.md`

## Required Work

Assess the governance risk associated with missing or ambiguous contracts.

Record risk items such as:

- undocumented authoritative state model
- incompatible lifecycle vocabularies between layers
- event contracts implied only by code
- interface contracts missing despite external consumption
- identity rules split across multiple modules
- compatibility layer behavior not bounded by doctrine
- stale contract drafts misguiding audits
- UI/authored truth conflicting with backend/runtime authority

Each item must include:

- description
- evidence
- affected subsystem
- likely contract class
- risk severity
- likely downstream consequence if left unresolved

Severity levels:

- LOW
- MODERATE
- HIGH
- BLOCKING

---

# Phase 08 — Contract Discovery Recommendations

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/08-contract-discovery-recommendations.md`

## Required Work

Use the `contract-candidate-discovery` skill to translate the discovery results into explicit next-step governance recommendations.

Recommendations should include:

- which contract should be authored first
- which contract candidates require audit before authoring
- which existing documents should be promoted, normalized, split, or retired
- which authority ambiguities must be resolved before contract authoring
- whether any candidate is too unstable for immediate canonicalization

The recommendations must prioritize based on:

- governance risk
- blast radius
- centrality to architecture doctrine
- dependency ordering
- auditability value
- remediation sequencing needs

This phase should propose a bounded contract-authoring roadmap.

---

# Phase 09 — Contract Discovery Ledger

## Output Artifact

`docs/governance/contract-discovery-ledger.md`

## Required Work

Author a durable governance ledger that records the repository’s discovered contract candidates and their current status.

The ledger must be written as an operational governance surface, not a temporary note.

It should include:

- contract candidate inventory
- status
- primary authority surface
- recommended next action
- notes on ambiguity or fragmentation where relevant

This ledger becomes the planning surface for future contract pipelines.

---

# Phase 10 — Supporting Surface Updates

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/10-supporting-surface-updates.md`

## Required Work

Update supporting governance surfaces as needed so contract discovery is visible and usable.

This may include:

- linking the contract discovery ledger from `AGENTS.md`
- linking it from `.codex/AGENTS.md`
- adding it to governance index docs
- recording it in the pipeline registry notes
- referencing it from architecture doctrine if appropriate

This phase must record:

- what was updated
- why
- what was intentionally left unchanged
- whether stale references remain

---

# Phase 11 — Verification of Contract Discovery Installation

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/11-contract-discovery-verification.md`

## Required Work

Verify that contract discovery outputs now exist as explicit and usable governance surfaces.

Verification must confirm:

- the contract candidate matrix exists
- the contract discovery ledger exists
- authority surfaces are classified explicitly
- key subsystem candidates are recorded
- crosswalk against existing documents was performed
- risk items are documented rather than hidden
- recommendations are actionable for downstream pipelines

This verification evaluates discovery completeness and usability, not full correctness of every future contract decision.

---

# Phase 12 — Promotion Decision

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/12-promotion-decision.md`

## Required Work

Decide whether the repository now has a sufficient contract discovery map to support downstream contract governance work.

Allowed decisions:

- PROMOTE
- PROMOTE_WITH_OBSERVATIONS
- REQUIRES_REFINEMENT
- BLOCKED

### PROMOTE
Use when contract candidates, authority surfaces, and recommendations are clear enough to support authoring and audit pipelines.

### PROMOTE_WITH_OBSERVATIONS
Use when the discovery map is usable but bounded ambiguity remains.

### REQUIRES_REFINEMENT
Use when discovery outputs exist but are too incomplete or too weakly justified for safe downstream use.

### BLOCKED
Use when repository ambiguity is too severe to responsibly identify contract candidates without additional discovery or runtime evidence.

The decision must cite the governing reasons.

---

# Phase 13 — Final Verdict

## Output Artifact

`docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/13-final-verdict.md`

## Allowed Verdicts

- CONTRACT_DISCOVERY_ESTABLISHED
- CONTRACT_DISCOVERY_ESTABLISHED_WITH_OBSERVATIONS
- CONTRACT_DISCOVERY_REQUIRES_REFINEMENT
- CONTRACT_DISCOVERY_BLOCKED

The final verdict must summarize:

- contract discovery outcome
- contract maturity level
- major candidate contract areas
- principal unresolved authority risks
- next valid pipeline stage

---

# Required Deliverables

This pipeline is not complete unless it produces:

- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/00-pipeline-summary.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/01-scope-and-contract-taxonomy.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/02-surface-inventory.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/03-subsystem-boundary-discovery.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/04-authority-surface-analysis.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/05-contract-candidate-matrix.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/06-existing-contract-crosswalk.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/07-drift-gaps-and-risk-assessment.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/08-contract-discovery-recommendations.md`
- `docs/governance/contract-discovery-ledger.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/10-supporting-surface-updates.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/11-contract-discovery-verification.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/12-promotion-decision.md`
- `docs/pipelines/governance/discover-contract-candidates-and-authority-surfaces/13-final-verdict.md`

---

# Execution Rules

## Evidence First
Do not invent contract candidates from preference alone. Derive them from repository evidence, architecture doctrine, and repeated behavioral boundaries.

## Authority Must Be Classified
Each major surface must be explicitly classified instead of being treated informally.

## No Silent Canonicalization
This pipeline discovers candidate contracts. It does not silently make them canonical.

## Fragmentation Must Be Named
If authority is split across files, layers, or vocabularies, record that fragmentation explicitly.

## Planning Output Must Be Actionable
The candidate matrix and ledger must be concrete enough to drive authoring, audit, remediation, and verification pipelines.

---

# Recommended Next Pipelines

After successful completion, the next valid stage is typically one or more of:

- `004--author-canonical-contract-for-highest-priority-subsystem.md`
- `005--audit-existing-contract-surfaces-against-repository-reality.md`
- `006--normalize-fragmented-contract-authority-surfaces.md`
- `007--audit-implementation-against-architecture-doctrine.md`

If the highest-priority contract area is highly ambiguous, an additional discovery or runtime evidence pipeline may be required before authoring.

---

# Completion Standard

This pipeline is complete only when the repository has moved from:

**architecture-governed but contract-ambiguous**

to:

**architecture-governed with explicit contract candidate and authority discovery surfaces**
