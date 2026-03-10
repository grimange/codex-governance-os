# Codex Pipeline — Discover Existing Architecture and Establish Doctrine

**Pipeline ID**: 001  
**Category**: governance  
**Status**: PROPOSED

## Purpose

Discover the repository’s current architecture from real implementation and documentation evidence, then establish an explicit canonical architecture doctrine for future governance, audit, remediation, verification, and promotion pipelines.

This pipeline converts an initialized governance-capable repository into a repository with documented architectural authority.

It is the first canonical architecture-discovery step after governance bootstrap.

---

## Why This Pipeline Exists

A repository can be governance-capable without yet being architecture-governed.

Initialization creates the governance scaffolding, but it does not determine:

- what layers are authoritative
- what data flows are canonical
- what subsystem boundaries exist
- where state truth lives
- what implementation patterns are intentional versus accidental
- what documents are authoritative versus stale or descriptive only

Without this pipeline, future audits and remediations risk operating against assumptions instead of explicit doctrine.

This pipeline establishes that doctrine.

---

# Phase 00 — Pipeline Summary

## Output Artifact

`docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/00-pipeline-summary.md`

## Required Contents

Document:

- repository under review
- discovery objective
- initial architecture-documentation state
- expected doctrinal outputs
- key risks if doctrine is absent or ambiguous

The summary must state whether the repository currently appears:

- undocumented
- partially documented
- documented but inconsistent
- documented with likely canonical authority already present

---

# Phase 01 — Scope and Discovery Boundaries

## Output Artifact

`docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/01-scope-and-boundaries.md`

## Required Work

Define the discovery boundary for this pipeline.

The artifact must explicitly identify:

### In Scope

- repository structure relevant to architecture
- implementation evidence
- existing governance and contract documents
- subsystem boundaries
- runtime/state authority candidates
- interface boundaries
- existing terminology and lifecycle vocabularies
- architecture diagrams or descriptive docs if present

### Out of Scope

This pipeline does not:

- remediate code
- rewrite implementation
- verify runtime behavior in production
- declare closure of architecture drift
- modernize legacy systems
- create subsystem contracts beyond architecture doctrine
- promote every existing document to canonical status automatically

This pipeline may identify contract candidates, but it does not author full subsystem contracts unless explicitly required by local governance doctrine.

---

# Phase 02 — Repository Evidence Discovery

## Output Artifact

`docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/02-repository-evidence-inventory.md`

## Required Work

Perform a structured inventory of repository evidence relevant to architecture.

The inventory should cover, where present:

- top-level application structure
- backend folders
- frontend folders
- services
- domain modules
- infrastructure modules
- event systems
- queues/workers
- data/state layers
- API boundaries
- docs/governance surfaces
- docs/contracts surfaces
- legacy folders
- generated or mirrored surfaces that may not be authoritative

The artifact must organize evidence into categories such as:

### Code Evidence
Implementation files, modules, service boundaries, runtime paths, lifecycle handlers, state writers/readers.

### Documentation Evidence
Architecture docs, README files, ADRs, governance docs, diagrams, contract drafts, subsystem notes.

### Operational Evidence
Config files, deployment patterns, runtime assumptions, event routing, infrastructure indicators.

### Legacy / Drift Indicators
Deprecated folders, legacy adapters, duplicate terminology, competing flows, stale docs, transitional patterns.

The inventory must distinguish between:

- evidence of actual behavior
- descriptive claims
- inferred architecture
- unresolved ambiguity

---

# Phase 03 — Architecture Mapping

## Output Artifact

`docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/03-architecture-mapping.md`

## Required Work

Produce a repository architecture map from the discovered evidence.

The mapping should identify:

- primary subsystems
- subsystem responsibilities
- boundary crossings
- core state stores
- orchestration layers
- authority layers
- projection layers
- external dependencies
- legacy compatibility layers if any

The artifact should answer questions like:

- What is the system made of?
- Which layer is the source of truth?
- Which layers consume and project state?
- Where does lifecycle orchestration happen?
- Which components author state, and which only reflect it?
- Which paths appear canonical versus compatibility-only?

The architecture map should include at least these sections:

### System Context
What kind of system this repository implements.

### Major Components
Named components and their responsibilities.

### State Authority Model
Where canonical state appears to live.

### Flow Model
How commands, runtime events, persistence, and UI projection appear to move.

### Dependency Model
Internal and external dependency relationships.

### Legacy and Compatibility Zones
Areas that appear transitional, mirrored, deprecated, or residual.

---

# Phase 04 — Authority and Source-of-Truth Analysis

## Output Artifact

`docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/04-authority-analysis.md`

## Required Work

Identify the most likely architecture authority structure currently present in the repository.

The artifact must evaluate:

- implementation authority versus document authority
- runtime truth versus UI truth
- persistent truth versus derived/cache truth
- command path versus event path
- canonical lifecycle vocabulary versus competing vocabularies
- direct state mutation versus projected state consumption

The output must explicitly classify each significant surface as one of:

- canonical authority
- likely authority candidate
- descriptive but non-authoritative
- compatibility layer
- legacy residual
- ambiguous / unresolved

This phase must not assume that existing documents are authoritative merely because they exist.

Authority must be justified by evidence.

---

# Phase 05 — Drift, Ambiguity, and Risk Assessment

## Output Artifact

`docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/05-drift-and-ambiguity-assessment.md`

## Required Work

Assess where the repository lacks clear doctrine or contains conflicting architectural signals.

Examples of drift or ambiguity include:

- multiple competing state authorities
- frontend-authored lifecycle truth conflicting with backend/runtime truth
- duplicate lifecycle vocabularies
- legacy adapters still active on canonical paths
- outdated documents contradicting live implementation
- multiple orchestration surfaces for the same responsibility
- mirrored state stores with unclear precedence
- compatibility layers treated as primary behavior

The artifact must record:

- ambiguity description
- affected subsystem
- evidence
- governance risk
- whether follow-up audit/remediation is likely required

Each drift item should be classified by severity:

- low
- moderate
- high
- blocking

---

# Phase 06 — Doctrine Design Decision

## Output Artifact

`docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/06-doctrine-design-decision.md`

## Required Work

Based on the prior evidence, define the architecture doctrine that should become canonical for this repository.

This is the central design decision phase.

The artifact must define:

- architecture principles
- authority precedence
- system truth model
- state ownership rules
- orchestration ownership
- projection rules
- compatibility-layer handling
- document precedence rules
- terminology normalization where needed

Typical doctrine questions include:

- Does backend or frontend author runtime truth?
- Is Redis/database/event stream/cache authoritative or derived?
- Is the UI allowed to author lifecycle state?
- Are legacy mirrors canonical or compatibility-only?
- What is the canonical logical identity model?
- What is the relationship between contract docs and implementation?

This phase must choose doctrine deliberately and explain the choice.

If uncertainty remains, it must be recorded explicitly rather than hidden.

---

# Phase 07 — Canonical Doctrine Authoring

## Output Artifact

`docs/governance/architecture-doctrine.md`

## Required Work

Author or replace the canonical architecture doctrine document using the results of discovery and doctrine design.

The doctrine must include, at minimum:

## Required Sections

### Purpose
Why this doctrine exists.

### Scope
What systems and layers it governs.

### Authority Precedence
Order of authority for architecture and implementation decisions.

### System Model
High-level statement of how the system is structured.

### Source of Truth
Where canonical runtime/business/system truth lives.

### Layer Responsibilities
What each major layer is allowed to do.

### State and Projection Rules
Which layers author state and which only project or consume.

### Compatibility and Legacy Rules
How transitional/legacy paths must be treated.

### Terminology Rules
Canonical vocabulary for lifecycle/state/components when ambiguity exists.

### Governance Implications
How future contracts, audits, remediations, and verifications must use this doctrine.

### Non-Goals
What the doctrine intentionally does not define.

The doctrine must be written as an authority surface, not as a brainstorming note.

---

# Phase 08 — Supporting Governance Surface Updates

## Output Artifact

`docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/08-supporting-surface-updates.md`

## Required Work

Update related governance surfaces as needed so the new doctrine is discoverable and operational.

This may include:

- updating `AGENTS.md` authority references
- updating `.codex/AGENTS.md`
- adding doctrine reference to pipeline registry notes
- recording architecture doctrine in governance index docs
- linking future pipeline routing to the new doctrine

This phase must record:

- what was updated
- why
- what was intentionally left unchanged
- whether any stale references remain

---

# Phase 09 — Verification of Doctrine Installation

## Output Artifact

`docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/09-doctrine-installation-verification.md`

## Required Work

Verify that the doctrine now exists as an explicit, discoverable, usable authority surface.

Verification must confirm:

- `docs/governance/architecture-doctrine.md` exists
- the doctrine reflects repository evidence rather than pure speculation
- the doctrine contains explicit authority precedence
- canonical architecture principles are documented
- supporting governance references are updated as needed
- major ambiguity areas are recorded, not hidden

This verification is about installation and adequacy of doctrine, not complete architectural correctness in production runtime conditions.

---

# Phase 10 — Promotion Decision

## Output Artifact

`docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/10-promotion-decision.md`

## Required Work

Decide whether the newly authored doctrine is suitable to serve as the repository’s canonical architecture authority.

Allowed decisions:

- PROMOTE
- PROMOTE_WITH_OBSERVATIONS
- REQUIRES_REFINEMENT
- BLOCKED

### PROMOTE
Use when doctrine is clear, evidence-based, internally coherent, and sufficient for downstream governance work.

### PROMOTE_WITH_OBSERVATIONS
Use when doctrine is usable and should become canonical, but some bounded ambiguities or follow-up audits remain.

### REQUIRES_REFINEMENT
Use when doctrine exists but is too incomplete, too vague, or too poorly grounded to safely govern future work.

### BLOCKED
Use when repository ambiguity is so severe that doctrine cannot responsibly be established without additional discovery or runtime evidence.

The decision must cite the reasoning.

---

# Phase 11 — Final Verdict

## Output Artifact

`docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/11-final-verdict.md`

## Allowed Verdicts

- ARCHITECTURE_DOCTRINE_ESTABLISHED
- ARCHITECTURE_DOCTRINE_ESTABLISHED_WITH_OBSERVATIONS
- ARCHITECTURE_DOCTRINE_REQUIRES_REFINEMENT
- ARCHITECTURE_DOCTRINE_BLOCKED

The final verdict must summarize:

- doctrine outcome
- architectural clarity level
- principal authority decision
- key residual risks
- next valid pipeline stage

---

# Required Deliverables

This pipeline is not complete unless it produces:

- `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/00-pipeline-summary.md`
- `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/01-scope-and-boundaries.md`
- `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/02-repository-evidence-inventory.md`
- `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/03-architecture-mapping.md`
- `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/04-authority-analysis.md`
- `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/05-drift-and-ambiguity-assessment.md`
- `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/06-doctrine-design-decision.md`
- `docs/governance/architecture-doctrine.md`
- `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/08-supporting-surface-updates.md`
- `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/09-doctrine-installation-verification.md`
- `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/10-promotion-decision.md`
- `docs/pipelines/governance/discover-existing-architecture-and-establish-doctrine/11-final-verdict.md`

---

# Execution Rules

## Evidence First
Do not invent architecture. Infer it from repository evidence and explicitly label uncertainty.

## Authority Must Be Justified
Documents are not automatically authoritative. Authority must be argued from consistency, scope, intent, and repository reality.

## Doctrine Must Be Usable
The result must be concrete enough to guide later contract, audit, remediation, and verification pipelines.

## Drift Must Be Named
Do not hide contradictions. Record them explicitly.

## No Silent Promotion of Legacy
Legacy and compatibility surfaces must not be treated as canonical unless justified by evidence and decision.

---

# Recommended Next Pipelines

After successful completion, the next valid stage is typically one or more of:

- `002--audit-repository-governance-readiness.md`
- `003--discover-contract-candidates-and-authority-surfaces.md`
- `004--audit-implementation-against-architecture-doctrine.md`

If significant drift is found, a remediation-planning pipeline may be more appropriate before broader audits.

---

# Completion Standard

This pipeline is complete only when the repository has moved from:

**governance-capable but architecture-ambiguous**

to:

**governance-capable with explicit canonical architecture doctrine**