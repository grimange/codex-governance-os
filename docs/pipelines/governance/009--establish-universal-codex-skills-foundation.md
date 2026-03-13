---
pipeline_id: "009"
title: "Establish Universal Codex Skills Foundation"
status: active
category: governance
stage: foundation
objective: "Author the universal skill taxonomy, standards, and discovery surfaces required for reusable Codex operation."
depends_on: ["008"]
outputs: ["docs/pipelines/governance/establish-universal-codex-skills-foundation/"]
success_criteria: ["Universal skill doctrine and taxonomy are authored.", "Core reusable skills are established.", "Verification and final verdict are recorded."]
governance_mode: fail-closed
execution_mode: advisory-then-enforcing
restrictions: ["Keep the skills foundation domain-agnostic.", "Do not replace architecture doctrine or subsystem contracts with skills."]
non_claims: ["Does not create all project-specific skills.", "Does not establish a full autonomous marketplace."]
classification: governance.foundation
authority: repo-governance
autonomy: advisory-only
problem_statement: "A governance template with doctrine and pipelines still remains operationally thin if common Codex behaviors are not captured as reusable governed skills."
scope: "Establish the universal skill taxonomy, standards, directory structure, core skill set, supporting integrations, and verification surfaces."
inputs: ["Governance doctrine foundation", "Repository governance structure", "Reusable behavior inventory"]
entry_conditions: ["Doctrine foundation exists and reusable operational behavior is ready to be normalized into skills."]
exit_conditions: ["Universal skill framework, supporting docs, and verification artifacts are published."]
validation: ["Inspect authored skill surfaces and integration artifacts.", "Confirm the final verdict matches the installed skill foundation."]
rollback: "Restore prior skill and lane state from version control if normalization introduces semantic drift."
---

# Establish Universal Codex Skills Foundation

## Purpose

Establish the reusable universal Codex skills foundation that future repositories can inherit and extend without rebuilding common operational behavior from scratch.

## Problem Statement

Without reusable skills, common Codex behaviors must be re-explained per repository, which fragments orchestration and weakens governed reuse.

## Objectives

- inventory reusable behavior worth turning into skills
- define the universal skill taxonomy and standards
- author the core universal skill set and discovery surfaces
- integrate the skills foundation into supporting governance materials

## Scope

In scope: behavior inventory, taxonomy design, skill selection, structure design, authoring standard, invocation standard, skill authoring, discovery surfaces, supporting integration, override model, and verification.

Out of scope: project-specific skills, domain-specific runtime prompts, or replacement of architecture doctrine and contracts.

## Preconditions

- doctrine foundation exists
- reusable behaviors can be identified from repository evidence
- skill publication under the canonical skill roots is available

## Execution Steps

1. Publish the pipeline summary and reusable-behavior inventory.
2. Design the skill taxonomy, select core skills, and define structure.
3. Author the skill standards, invocation rules, core skills, and discovery surfaces.
4. Integrate supporting surfaces, define override behavior, verify the foundation, and record promotion guidance and final verdict.

Universal skills:

- `repository-discovery`
- `skill-creator`

## Expected Outputs

- artifact bundle under `docs/pipelines/governance/establish-universal-codex-skills-foundation/`
- universal skill doctrine and core skill surfaces
- discovery, integration, and override-model documentation

## Verification Method

- inspect the authored standards, skills, and supporting-surface integrations
- confirm the universal skills index and invocation rules are published
- confirm the final verdict is explicit and evidence-backed

## Restrictions

- keep the skills foundation generic and reusable
- do not encode one domain or runtime stack as universal skill law

## Non-Claims

- does not create every future specialist skill
- does not make project-local overrides unnecessary

## Final Verdict

Use a bounded skills-foundation verdict such as `UNIVERSAL_CODEX_SKILLS_FOUNDATION_ESTABLISHED` or an explicitly restricted equivalent.
