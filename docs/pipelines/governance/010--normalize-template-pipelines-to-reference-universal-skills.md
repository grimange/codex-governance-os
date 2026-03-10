# Codex Pipeline — Normalize Template Pipelines to Reference Universal Skills

Pipeline ID: 010
Category: governance
Stage: normalization
Status: PROPOSED

---

# Purpose

Normalize the template repository’s pipelines so they reference the universal Codex skills foundation instead of embedding reusable behavioral logic inline.

This pipeline improves maintainability, reduces token overhead, and ensures that reusable operational logic is centralized in the universal skills layer rather than duplicated across pipelines.

---

# Why This Pipeline Exists

After establishing the universal skills foundation, many pipelines may still contain embedded instructions that duplicate skill behavior.

Examples include:

- repository discovery procedures
- governance readiness audit patterns
- contract authoring instructions
- implementation audit procedures
- remediation planning logic
- verification workflows

If this logic remains embedded inside pipelines:

- pipelines become unnecessarily long
- reusable behavior becomes fragmented
- skills become decorative rather than operational
- updates must be applied across many pipelines

This pipeline moves reusable logic into the universal skills layer and converts pipelines to reference those skills.

---

# Inputs

Required inputs:

- universal skills foundation created in Pipeline 009
- `docs/governance/universal-skills-index.md`
- skill authoring standard
- skill invocation standard
- template pipelines `000` through latest pipeline

Optional inputs:

- existing reusable prompt fragments
- pipeline artifact standard
- governance lifecycle doctrine

---

# Phase 00 — Pipeline Summary

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/00-pipeline-summary.md`

## Required Work

Document:

- repository under review
- normalization objective
- pipelines evaluated
- expected token reduction
- expected governance improvement

The summary must classify the current pipeline skill usage as:

- skill-unaware
- partially skill-referenced
- skill-fragmented
- skill-consistent

---

# Phase 01 — Pipeline Behavioral Logic Inventory

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/01-pipeline-behavior-inventory.md`

## Required Work

Analyze pipelines in the repository and identify embedded reusable behavior.

For each pipeline, record:

- embedded operational logic
- repeated procedures
- discovery logic
- audit logic
- contract authoring instructions
- remediation planning instructions
- verification procedures

Each behavior must be classified as:

- already implemented as a universal skill
- reusable but not yet normalized
- pipeline-specific behavior
- duplicated across multiple pipelines
- candidate for skill extraction

This phase identifies normalization targets.

---

# Phase 02 — Skill Mapping Analysis

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/02-skill-mapping-analysis.md`

## Required Work

Map embedded pipeline behavior to existing universal skills.

For each identified behavior:

- identify the corresponding universal skill
- confirm that the skill covers the behavior
- record any gaps between pipeline behavior and skill capability
- identify pipelines that should reference the skill

Example mappings may include:

- repository discovery → `repository-discovery-skill`
- governance readiness audit → `governance-readiness-audit-skill`
- canonical contract authoring → `canonical-contract-authoring-skill`
- implementation audit → `implementation-contract-audit-skill`
- remediation planning → `implementation-drift-remediation-skill`
- verification → `contract-alignment-verification-skill`

The artifact must record which pipelines should reference which skills.

---

# Phase 03 — Skill Coverage Gap Detection

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/03-skill-coverage-gap-detection.md`

## Required Work

Identify cases where pipelines contain reusable logic that is not yet implemented as a universal skill.

For each gap:

- describe the missing skill capability
- identify pipelines affected
- assess whether the capability should become a new universal skill
- record recommended action

Possible actions:

- extend existing skill
- create new universal skill
- leave behavior pipeline-specific

No skill should be created automatically without justification.

---

# Phase 04 — Pipeline Normalization Plan

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/04-pipeline-normalization-plan.md`

## Required Work

Define the normalization strategy for the pipeline catalog.

The plan must specify:

- pipelines to modify
- sections of pipelines to replace with skill references
- expected reduction of inline instructions
- skill invocation format
- any pipelines intentionally left unchanged

Normalization must preserve:

- pipeline intent
- artifact expectations
- governance lifecycle alignment

---

# Phase 05 — Pipeline Refactoring Execution

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/05-pipeline-refactoring-execution.md`

## Required Work

Modify pipelines to reference universal skills.

Refactoring actions may include:

- removing duplicated procedural instructions
- replacing procedural blocks with skill references
- updating pipeline sections to invoke appropriate skills
- simplifying pipeline descriptions
- aligning pipeline behavior with skill invocation standard

Each modification must record:

- pipeline modified
- section modified
- skill referenced
- summary of change

---

# Phase 06 — Skill Invocation Integration

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/06-skill-invocation-integration.md`

## Required Work

Ensure pipelines correctly reference universal skills.

This phase must confirm:

- invocation syntax follows the skill invocation standard
- referenced skills exist
- pipelines do not invoke conflicting skills
- invocation context is clear
- pipelines still define outputs and artifact expectations

Skill invocation must remain explicit and unambiguous.

---

# Phase 07 — Token Efficiency Assessment

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/07-token-efficiency-assessment.md`

## Required Work

Evaluate token efficiency improvements.

This phase must estimate:

- average pipeline token reduction
- duplicated logic removed
- pipeline readability improvement
- expected reduction in future pipeline drift

The assessment must confirm that normalization improved maintainability.

---

# Phase 08 — Governance Consistency Verification

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/08-governance-consistency-verification.md`

## Required Work

Verify that normalization did not break governance behavior.

The verification must confirm:

- pipelines still follow governance lifecycle doctrine
- artifact expectations remain consistent
- skill references remain valid
- pipeline sequencing remains intact
- contract governance lifecycle still functions

This phase ensures normalization preserved operational integrity.

---

# Phase 09 — Documentation and Index Updates

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/09-documentation-updates.md`

## Required Work

Update documentation surfaces to reflect skill-based pipelines.

This phase may update:

- `AGENTS.md`
- `.codex/AGENTS.md`
- universal skills index
- governance lifecycle doctrine
- template README

Documentation must explain that pipelines now reference reusable skills.

---

# Phase 10 — Promotion Decision

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/10-promotion-decision.md`

Allowed decisions:

PROMOTE  
PROMOTE_WITH_OBSERVATIONS  
REQUIRES_ADDITIONAL_NORMALIZATION  
BLOCKED

PROMOTE when pipelines consistently reference universal skills and no critical embedded duplication remains.

---

# Phase 11 — Final Verdict

## Output Artifact

`docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/11-final-verdict.md`

Allowed verdicts:

PIPELINES_NORMALIZED_TO_UNIVERSAL_SKILLS  
PIPELINES_NORMALIZED_WITH_OBSERVATIONS  
PIPELINE_NORMALIZATION_INCOMPLETE  
PIPELINE_NORMALIZATION_BLOCKED

The final verdict must summarize:

- pipelines normalized
- skills referenced
- token efficiency improvement
- residual normalization needs
- next governance stage

---

# Required Deliverables

This pipeline is not complete unless it produces:

- `00-pipeline-summary.md`
- `01-pipeline-behavior-inventory.md`
- `02-skill-mapping-analysis.md`
- `03-skill-coverage-gap-detection.md`
- `04-pipeline-normalization-plan.md`
- `05-pipeline-refactoring-execution.md`
- `06-skill-invocation-integration.md`
- `07-token-efficiency-assessment.md`
- `08-governance-consistency-verification.md`
- `09-documentation-updates.md`
- `10-promotion-decision.md`
- `11-final-verdict.md`

---

# Execution Rules

## Skills Must Remain Authoritative

Reusable behavioral logic must live in the skills layer, not inside pipelines.

## Pipelines Must Stay Readable

Pipelines should reference skills without becoming cryptic or losing intent.

## Domain Neutrality Must Be Preserved

Normalization must not introduce domain-specific assumptions into universal pipelines.

## Skill References Must Be Valid

No pipeline may reference a skill that does not exist.

## Governance Lifecycle Must Remain Intact

Normalization must not change pipeline sequencing or governance behavior.

---

# Recommended Next Pipelines

After normalization, the next logical pipeline may include:

- `011--author-governed-project-bootstrap-surface-for-skill-inheritance.md`
- `012--audit-template-reusability-across-multiple-project-types.md`

These pipelines ensure that the template can be easily adopted across different project types.

---

# Completion Standard

This pipeline is complete when the repository transitions from:

pipelines with embedded reusable behavior

to:

pipelines referencing a centralized universal Codex skills foundation.