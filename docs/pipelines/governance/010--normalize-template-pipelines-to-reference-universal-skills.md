---
pipeline_id: "010"
title: "Normalize Template Pipelines To Reference Universal Skills"
status: active
category: governance
stage: normalization
objective: "Normalize template pipelines so reusable behavioral logic is referenced through universal skills rather than duplicated inline."
depends_on: ["009"]
outputs: ["docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/"]
success_criteria: ["Pipeline behavioral logic is inventoried.", "Skill mappings and gaps are documented.", "Template pipelines are normalized and verified."]
governance_mode: fail-closed
execution_mode: advisory-then-enforcing
restrictions: ["Do not remove pipeline-specific artifact or verdict requirements.", "Do not treat decorative skill references as normalization success."]
non_claims: ["Does not create new universal skills unless justified by coverage gaps.", "Does not rewrite substantive governance policy unrelated to skill normalization."]
classification: governance.normalization
authority: repo-governance
autonomy: advisory-only
problem_statement: "After establishing the skills foundation, many pipelines still duplicate reusable behavior inline, which fragments maintenance and blocks consistent governed execution."
scope: "Inventory embedded pipeline behavior, map it to skills, normalize pipeline bodies, integrate skill invocation, and verify consistency."
inputs: ["Universal skills foundation", "Universal skills index", "Skill standards", "Template pipelines under governance"]
entry_conditions: ["Universal skills foundation exists and template pipelines still contain duplicated reusable behavior."]
exit_conditions: ["Targeted pipelines reference universal skills and the normalization evidence is recorded."]
validation: ["Inspect normalization artifacts and updated pipelines.", "Confirm verification and documentation updates are explicit."]
rollback: "Restore prior pipeline bodies from version control if normalization introduces semantic drift."
---

# Normalize Template Pipelines To Reference Universal Skills

## Purpose

Normalize template pipelines so reusable operational behavior is centralized in the universal skills layer rather than duplicated across individual pipelines.

## Problem Statement

If reusable logic remains embedded inline, pipelines become longer, behavior fragments across files, and updates must be repeated manually instead of inherited through skills.

## Objectives

- inventory reusable behavioral logic embedded in pipelines
- map that behavior to universal skills and detect coverage gaps
- normalize pipeline bodies to reference skills explicitly
- verify consistency, token-efficiency gains, and supporting-surface updates

## Scope

In scope: behavioral-logic inventory, skill mapping, gap detection, normalization plan, pipeline refactoring execution, skill-invocation integration, verification, and documentation/index updates.

Out of scope: unrelated policy rewrites or creation of unnecessary new skills.

## Preconditions

- universal skills foundation exists
- skill standards and discovery surfaces are available
- target pipelines still contain duplicated reusable behavior

## Execution Steps

1. Publish the pipeline summary and inventory embedded behavioral logic across template pipelines.
2. Map reusable logic to skills and detect any coverage gaps.
3. Design and execute the normalization plan for target pipelines.
4. Integrate skill invocation, assess consistency and efficiency, update documentation and indexes, and record promotion guidance and final verdict.

Universal skills:

- `repository-discovery`
- `pipeline-registry-reconciliation`

## Expected Outputs

- artifact bundle under `docs/pipelines/governance/normalize-template-pipelines-to-reference-universal-skills/`
- normalized pipeline bodies referencing universal skills
- verification and documentation/index updates

## Verification Method

- inspect the normalization artifacts and updated pipeline definitions
- confirm reusable behavior now points to the universal skills layer
- confirm the final verdict is explicit and evidence-backed

## Restrictions

- preserve pipeline-specific artifact and verdict requirements
- do not claim normalization if reusable behavior remains duplicated materially

## Non-Claims

- does not eliminate the need for future pipeline-specific changes
- does not replace the governance doctrine or artifact standards

## Final Verdict

Use a bounded normalization verdict such as `TEMPLATE_PIPELINES_NORMALIZED_TO_REFERENCE_UNIVERSAL_SKILLS` or an explicitly restricted equivalent.
