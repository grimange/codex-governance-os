# Codex Pipeline — Establish Universal Codex Skills Foundation

Pipeline ID: 009
Category: governance
Stage: foundation
Status: PROPOSED

---

# Purpose

Establish a reusable universal Codex skills foundation for the template repository by authoring the generic skill surfaces, skill taxonomy, invocation rules, and integration guidance needed for deterministic multi-project Codex operation.

This pipeline creates the canonical skill framework that future projects can inherit and extend without rebuilding baseline skills from scratch.

The resulting skills foundation must remain domain-agnostic and reusable across software repositories with different architectures, languages, and business domains.

---

# Why This Pipeline Exists

A governance template with pipelines and doctrine can still remain operationally thin if it lacks reusable skills.

Without a universal skills foundation:

- common Codex behaviors must be re-explained per project
- orchestration becomes inconsistent across repositories
- specialist execution quality varies by repo
- reusable project bootstrapping is weaker
- skills drift into project-specific prompts instead of governed reusable assets

This pipeline solves that by creating the universal skill layer for the template repository.

---

# Objectives

This pipeline must establish a reusable skills foundation that includes, at minimum:

- universal skill taxonomy
- skill authoring standard
- skill invocation standard
- skill directory structure
- core generic skill set
- supporting governance integration for skill discovery and reuse

The universal skills foundation must support future repositories without assuming a specific domain such as telecom, SaaS, infrastructure, or AI applications.

---

# Out of Scope

This pipeline does not:

- create project-specific skills
- create telecom-specific or domain-specific runtime skills
- create private business-logic instructions
- replace repository architecture doctrine
- replace subsystem contracts
- generate a full autonomous agent marketplace
- encode language-specific implementation rules as universal law unless they are truly generic

This is a universal skill-foundation pipeline, not a project specialization pipeline.

---

# Inputs

Required inputs:

- current template repository governance doctrine
- `AGENTS.md`
- `.codex/AGENTS.md` if present
- governance lifecycle doctrine
- pipeline artifact standard
- pipeline naming standard
- governance terminology
- current pipeline catalog

Optional inputs:

- existing reusable prompt fragments
- existing task templates
- prior skill experiments
- repository README or contributor guidance

---

# Phase 00 — Pipeline Summary

## Output Artifact

`docs/pipelines/governance/establish-universal-codex-skills-foundation/00-pipeline-summary.md`

## Required Work

Document:

- repository under review
- universal-skills objective
- current skill maturity
- expected skill-foundation outputs
- expected value for future projects

The summary must classify the current skill state as one of:

- no skill foundation
- informal skill usage
- partially reusable skill set
- fragmented skill surfaces
- already skill-oriented

---

# Phase 01 — Existing Reusable Behavior Inventory

## Output Artifact

`docs/pipelines/governance/establish-universal-codex-skills-foundation/01-existing-reusable-behavior-inventory.md`

## Required Work

Inventory existing reusable behaviors already present in the template repository.

Inspect for reusable logic embedded in:

- `AGENTS.md`
- `.codex/AGENTS.md`
- governance doctrine docs
- existing pipelines
- README or contributor docs
- template setup guidance
- repeated pipeline execution patterns

Examples of reusable behavior candidates may include:

- discovery behavior
- audit behavior
- contract authoring behavior
- remediation planning behavior
- verification behavior
- registry hygiene behavior
- governance document authoring behavior
- bootstrap behavior

Each candidate must be classified as:

- strong universal skill candidate
- reusable but not yet normalized
- project-specific and not universal
- duplicated guidance
- incomplete
- stale

This phase must identify what logic already exists but is scattered.

---

# Phase 02 — Universal Skill Taxonomy Design

## Output Artifact

`docs/pipelines/governance/establish-universal-codex-skills-foundation/02-universal-skill-taxonomy-design.md`

## Required Work

Define the universal skill taxonomy that the template repository will support.

The taxonomy must organize skills into clear reusable classes.

Suggested top-level classes include:

- discovery skills
- audit skills
- doctrine-authoring skills
- contract-authoring skills
- remediation-design skills
- verification skills
- registry and catalog skills
- template/bootstrap skills
- governance hygiene skills

For each class, define:

- its purpose
- what kinds of tasks belong in it
- what must remain outside it
- whether it is universal or should stay project-local

The taxonomy must remain generic enough for future projects.

---

# Phase 03 — Universal Skill Selection

## Output Artifact

`docs/pipelines/governance/establish-universal-codex-skills-foundation/03-universal-skill-selection.md`

## Required Work

Select the initial set of universal skills to create.

At minimum, the pipeline should consider skills such as:

- repository discovery skill
- governance readiness audit skill
- architecture doctrine authoring skill
- contract candidate discovery skill
- canonical contract authoring skill
- implementation audit skill
- remediation planning skill
- contract verification skill
- pipeline registry reconciliation skill
- template bootstrap skill

For each selected skill, record:

- skill name
- skill purpose
- why it is universal
- why it belongs in the template
- expected users
- expected invocation contexts

The selected initial set must be bounded and realistic.

---

# Phase 04 — Skill Directory and Structure Design

## Output Artifact

`docs/pipelines/governance/establish-universal-codex-skills-foundation/04-skill-directory-and-structure-design.md`

## Required Work

Define the canonical directory structure for universal Codex skills.

The design must specify:

- where skills live
- how skill files are named
- how supporting examples or templates are stored
- how skill metadata is represented
- how future projects extend or override universal skills safely

A recommended structure may resemble:

- `skills/`
- `skills/discovery/`
- `skills/audit/`
- `skills/contracts/`
- `skills/remediation/`
- `skills/verification/`
- `skills/governance/`
- `skills/bootstrap/`

The design must also define the shape of an individual skill package, including:

- skill instruction file
- optional examples
- optional checklists
- optional output templates

---

# Phase 05 — Skill Authoring Standard

## Output Artifact

`docs/governance/skill-authoring-standard.md`

## Required Work

Author the canonical skill authoring standard.

This document must define:

- what a skill is
- what a universal skill is
- required sections in a skill definition
- how a skill declares scope
- how a skill declares inputs
- how a skill declares outputs
- how a skill declares boundaries and non-goals
- how examples should be written
- how skills must avoid domain-specific assumptions unless explicitly local

Required sections for a skill should normally include:

- purpose
- when to use
- when not to use
- inputs
- procedure
- outputs
- boundaries
- failure modes
- example invocation
- expected artifacts or deliverables if relevant

This standard must make skills consistently authorable and auditable.

---

# Phase 06 — Skill Invocation Standard

## Output Artifact

`docs/governance/skill-invocation-standard.md`

## Required Work

Author the canonical skill invocation standard.

This document must define:

- how Codex decides a skill is applicable
- how a skill is referenced from pipelines or governance docs
- precedence between universal skills and project-local skills
- how conflicts are resolved
- when local override is allowed
- how not to invoke overly broad skills
- when to decompose work across multiple skills
- how orchestrator behavior relates to skills

The standard must explicitly define:

- universal skill first-use conditions
- local-skill override conditions
- conflict resolution order
- anti-duplication rules

This document is essential for making the skill foundation operational.

---

# Phase 07 — Universal Skill Authoring

## Output Artifact

`docs/pipelines/governance/establish-universal-codex-skills-foundation/07-universal-skill-authoring.md`

## Required Work

Author the initial universal skill set into the repository.

At minimum, the pipeline must create the selected initial skills in their governed locations.

Each created skill must comply with the skill authoring standard.

Each skill must remain generic and reusable.

Examples of candidate skill file identities may include:

- `skills/discovery/repository-discovery-skill.md`
- `skills/audit/governance-readiness-audit-skill.md`
- `skills/doctrine/architecture-doctrine-authoring-skill.md`
- `skills/contracts/contract-candidate-discovery-skill.md`
- `skills/contracts/canonical-contract-authoring-skill.md`
- `skills/audit/implementation-contract-audit-skill.md`
- `skills/remediation/implementation-drift-remediation-skill.md`
- `skills/verification/contract-alignment-verification-skill.md`
- `skills/governance/pipeline-registry-reconciliation-skill.md`
- `skills/bootstrap/governed-project-bootstrap-skill.md`

The exact names may vary, but the resulting set must be coherent and reusable.

---

# Phase 08 — Skill Index and Discovery Surface Authoring

## Output Artifact

`docs/governance/universal-skills-index.md`

## Required Work

Author the canonical index for the universal skill foundation.

This document must include:

- skill taxonomy overview
- list of available universal skills
- short description of each skill
- intended use cases
- relationship between universal skills and project-local skills
- guidance for future extension

The index must be written as an operational discovery surface, not a temporary note.

---

# Phase 09 — Supporting Surface Integration

## Output Artifact

`docs/pipelines/governance/establish-universal-codex-skills-foundation/09-supporting-surface-integration.md`

## Required Work

Integrate the universal skills foundation into the repository’s operational governance surfaces.

This phase must update, as needed:

- `AGENTS.md`
- `.codex/AGENTS.md`
- governance index docs
- template README
- bootstrap guidance
- future-pipeline guidance surfaces

The integration must ensure:

- universal skills are discoverable
- future projects understand how to inherit them
- local project extensions are clearly separated from universal skills

This phase must record:

- what was updated
- what references were added
- what was intentionally left unchanged
- whether stale embedded skill guidance remains elsewhere

---

# Phase 10 — Override and Extension Model Design

## Output Artifact

`docs/pipelines/governance/establish-universal-codex-skills-foundation/10-override-and-extension-model.md`

## Required Work

Define how future projects extend the universal skills foundation safely.

This phase must define:

- what stays universal
- what must be project-local
- how local skills override universal skills
- how naming collisions are prevented
- how projects add domain-specific skills without polluting the template
- how deprecated universal skills are handled

The extension model must preserve template cleanliness while allowing real project specialization.

---

# Phase 11 — Skill Foundation Verification

## Output Artifact

`docs/pipelines/governance/establish-universal-codex-skills-foundation/11-skill-foundation-verification.md`

## Required Work

Verify that the universal skills foundation is installed and operational.

Verification must confirm:

- skill taxonomy exists
- skill authoring standard exists
- skill invocation standard exists
- initial skill set exists
- skills are generic and reusable
- universal skills index exists
- supporting surfaces reference the skills appropriately
- extension and override model is defined

This phase verifies installation and operational readiness, not whether every future skill is perfect.

---

# Phase 12 — Promotion Decision

## Output Artifact

`docs/pipelines/governance/establish-universal-codex-skills-foundation/12-promotion-decision.md`

## Required Work

Decide whether the universal skills foundation is suitable to serve as the template repository’s canonical reusable skill layer.

Allowed decisions:

- PROMOTE
- PROMOTE_WITH_OBSERVATIONS
- REQUIRES_NORMALIZATION
- BLOCKED

### PROMOTE
Use when the skills foundation is coherent, reusable, integrated, and safe for future multi-project inheritance.

### PROMOTE_WITH_OBSERVATIONS
Use when the foundation is operational but bounded cleanup remains.

### REQUIRES_NORMALIZATION
Use when skills exist but duplication, ambiguity, or weak invocation rules still prevent safe reuse.

### BLOCKED
Use when skill scope, overlap, or structure is too inconsistent to support a reliable reusable foundation.

---

# Phase 13 — Final Verdict

## Output Artifact

`docs/pipelines/governance/establish-universal-codex-skills-foundation/13-final-verdict.md`

## Allowed Verdicts

- UNIVERSAL_CODEX_SKILLS_FOUNDATION_ESTABLISHED
- UNIVERSAL_CODEX_SKILLS_FOUNDATION_ESTABLISHED_WITH_OBSERVATIONS
- UNIVERSAL_CODEX_SKILLS_FOUNDATION_REQUIRES_NORMALIZATION
- UNIVERSAL_CODEX_SKILLS_FOUNDATION_BLOCKED

The final verdict must summarize:

- skills established
- standards established
- degree of integration success
- extension readiness for future projects
- remaining normalization needs
- next valid pipeline stage

---

# Required Deliverables

This pipeline is not complete unless it produces:

- `docs/pipelines/governance/establish-universal-codex-skills-foundation/00-pipeline-summary.md`
- `docs/pipelines/governance/establish-universal-codex-skills-foundation/01-existing-reusable-behavior-inventory.md`
- `docs/pipelines/governance/establish-universal-codex-skills-foundation/02-universal-skill-taxonomy-design.md`
- `docs/pipelines/governance/establish-universal-codex-skills-foundation/03-universal-skill-selection.md`
- `docs/pipelines/governance/establish-universal-codex-skills-foundation/04-skill-directory-and-structure-design.md`
- `docs/governance/skill-authoring-standard.md`
- `docs/governance/skill-invocation-standard.md`
- `docs/pipelines/governance/establish-universal-codex-skills-foundation/07-universal-skill-authoring.md`
- the initial universal skill files in their governed locations
- `docs/governance/universal-skills-index.md`
- `docs/pipelines/governance/establish-universal-codex-skills-foundation/09-supporting-surface-integration.md`
- `docs/pipelines/governance/establish-universal-codex-skills-foundation/10-override-and-extension-model.md`
- `docs/pipelines/governance/establish-universal-codex-skills-foundation/11-skill-foundation-verification.md`
- `docs/pipelines/governance/establish-universal-codex-skills-foundation/12-promotion-decision.md`
- `docs/pipelines/governance/establish-universal-codex-skills-foundation/13-final-verdict.md`

---

# Execution Rules

## Universal Means Domain-Agnostic
Do not encode telecom-specific, SaaS-specific, or project-specific behavioral assumptions into the universal skill layer.

## Normalize Reusable Logic
If reusable execution logic already exists in pipelines or governance docs, normalize it into skills rather than duplicating it.

## Skills Must Stay Bounded
Avoid creating vague mega-skills that try to solve every possible problem.

## Invocation Rules Are Mandatory
A skill library without invocation law is incomplete and unsafe.

## Local Extension Must Remain Possible
The resulting system must allow future projects to add local skills without polluting the universal foundation.

---

# Recommended Next Pipelines

After successful completion, the next valid stage is typically one of:

- `010--normalize-template-pipelines-to-reference-universal-skills.md`
- `011--author-governed-project-bootstrap-surface-for-skill-inheritance.md`
- `012--audit-universal-skill-reusability-across-template-scenarios.md`

If current pipelines still embed substantial reusable behavior inline, normalization should usually come next.

---

# Completion Standard

This pipeline is complete only when the repository has moved from:

**governance-capable but skill-fragmented**

to:

**governance-capable with a reusable universal Codex skills foundation**