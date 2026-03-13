---
lane: 024
title: Migrate Core Governance Lanes To Universal Templates
status: proposed
classification: governance.foundation
stage: implementation
authority: repo-governance
autonomy: advisory-only
created_at: 2026-03-14
updated_at: 2026-03-14
problem_statement: Core governance lanes were authored before a stable universal template existed, so lane structure, evidence expectations, and execution semantics are inconsistent across the foundation set.
objective: Normalize the core governance lanes onto a universal template so admission, routing, verification, and autonomous governance behavior can operate against a predictable lane contract.
scope: Foundational governance lanes that define repo governance behavior, lane execution semantics, evidence recording, routing, admission, and state progression.
out_of_scope: Rewriting the substantive governance decisions inside each lane, changing repository code unrelated to lane normalization, or introducing lane-specific execution logic that cannot be expressed through the universal template.
inputs: Existing core governance lane markdown files, current governance registry expectations, lane admission rules, routing behavior, and canonical template requirements.
outputs: Normalized core lane files using the universal template, a migration matrix, compatibility notes, verification evidence, and a final verdict.
prerequisites: A defined universal template contract exists or is established within this lane before migration is applied.
entry_conditions: Core governance lanes are present in the repository and at least one of them materially deviates from the target universal template contract.
exit_conditions: Targeted lanes conform to the universal template, preserve prior intent, satisfy admission requirements, and are verified against registry and routing expectations.
validation: Each migrated lane passes structural review, governed frontmatter checks, and dry-run or live admission checks without introducing semantic drift.
risk_level: medium
rollback: Restore prior lane files from version control and retain the migration matrix to identify which template changes caused incompatibility.
success_signal: The core governance lane set becomes structurally uniform enough that future lanes can inherit one template family rather than bespoke formatting rules.
---

# 024 -- Migrate Core Governance Lanes To Universal Templates

## Purpose

This lane establishes a controlled migration of the core governance lane set from historically inconsistent markdown contracts into a universal template model. The intent is not to rewrite governance policy. The intent is to make the policy executable, verifiable, and reusable under one structural contract.

Without this migration, later governance capabilities such as safe routing, admission gates, autonomous execution, multi-agent specialization, percentage-based maturity scoring, and architecture advisory remain partially fragile because the lane corpus itself is inconsistent.

## Why this lane exists

Early governance lanes are usually authored while the governance system is still being discovered. That is useful for exploration, but it leaves behind a foundation layer with mixed structures such as:

- inconsistent frontmatter keys
- unclear authority and autonomy boundaries
- variable output expectations
- weak entry and exit conditions
- inconsistent naming for validation and final verdict sections
- lane-local formatting that blocks reliable tooling

A universal template solves this by making each lane legible to both humans and governed tooling.

## Goals

1. Normalize the most important governance lanes first.
2. Preserve lane intent while standardizing structure.
3. Make the lane set compatible with current and future admission tooling.
4. Reduce bespoke parser logic and operator guesswork.
5. Prepare the repository for scalable governance authoring.

## Target lane families

The migration should prioritize the governance lanes that define or influence the rest of the system:

1. governance rules and constitutional lanes
2. routing and next-valid-action lanes
3. admission and normalization lanes
4. evidence and verification lanes
5. autonomous loop and governance state lanes
6. multi-agent orchestration lanes
7. status, maturity, and reporting lanes

If the repository already has a numbered subset recognized as canonical core lanes, that subset is the default migration target.

## Universal template requirements

Each migrated lane should conform to one canonical template family with the following minimum sections or equivalent governed fields:

### Governed frontmatter

Every migrated lane should carry single-line scalar frontmatter that is safe for deterministic parsing. The frontmatter should identify at least:

- lane number
- title
- status
- classification
- stage
- authority source
- autonomy boundary
- problem statement
- objective
- scope
- inputs
- outputs
- entry conditions
- exit conditions
- validation method
- rollback note

### Canonical body structure

Each migrated lane should contain:

1. purpose
2. problem or context
3. scope and exclusions
4. required inputs
5. required outputs or artifact bundle
6. execution procedure
7. acceptance criteria
8. verification method
9. failure or rollback handling
10. final expected verdict form

The exact wording can vary, but the semantic contract should remain stable.

## Migration principles

### 1. Preserve semantics

Migration is structural first. A lane should not change its substantive policy or claims unless the prior wording is internally contradictory or impossible to execute.

### 2. Prefer normalization over reinvention

If an existing section maps imperfectly to the universal template, normalize the section rather than replacing its intent with newly invented content.

### 3. Fail closed on ambiguity

If a legacy lane is too ambiguous to migrate cleanly, the migration record should mark it as restricted rather than silently guessing.

### 4. Record compatibility gaps

Every migration should note whether the lane was:

- valid as is
- normalized without semantic change
- normalized with bounded clarification
- restricted pending operator review

### 5. Keep lane numbering stable

The migration should not renumber historical lanes. The value is continuity plus better structure, not historical erasure.

## Execution plan

### Step 1: Inventory the core lane set

Build a migration matrix listing each target lane and its current state:

- lane number
- current title
- current status
- current structural defects
- current semantic ambiguity level
- migration priority

### Step 2: Define the universal template baseline

Freeze the exact target template contract before modifying the lanes. This prevents template drift during migration.

### Step 3: Perform lane-by-lane normalization

For each targeted lane:

- preserve the original lane identity
- rewrite frontmatter into canonical governed form
- reshape the body into the universal template
- preserve prior intent and dependencies
- remove formatting that breaks deterministic parsing

### Step 4: Record migration decisions

For every lane, write a brief compatibility note describing:

- what changed structurally
- what remained semantically unchanged
- whether any bounded clarification was required
- whether any restriction remains open

### Step 5: Verify admission and routing compatibility

Run the applicable governance checks so the migrated lane corpus is proven usable by the system, not just prettier for humans.

### Step 6: Publish the final migration verdict

Conclude with a repository-level assessment stating whether the core governance set is now template-normalized, normalized with restrictions, or still partially heterogeneous.

## Required artifacts

This lane should produce a structured artifact bundle under a directory name derived from the lane title. Recommended bundle:

1. `01-problem-statement.md`
2. `02-core-lane-inventory.md`
3. `03-universal-template-contract.md`
4. `04-migration-matrix.md`
5. `05-compatibility-notes.md`
6. `06-verification.md`
7. `07-final-verdict.md`

If the repository uses a different but already-governed artifact naming convention, preserve that convention.

## Acceptance criteria

This lane is complete when all of the following are true:

- the core governance lane set is explicitly identified
- the universal template baseline is documented
- each targeted lane is either migrated or explicitly restricted
- migration decisions are traceable lane by lane
- admission-facing structure is deterministic
- verification confirms the migrated lane set is compatible with governance tooling
- the final verdict states the real repository status without overstating completeness

## Verification guidance

Verification should be evidence-backed and should prefer repository-native governance commands where available. Suitable checks include:

- registry dry-run or sync dry-run
- lane preflight validation
- lane admission validation
- routing validation against migrated lanes
- deterministic frontmatter parsing checks
- evidence presence checks for required artifact files

If some validation commands do not yet exist in the repository, verification should still document the highest available evidence rather than inventing success claims.

## Final verdict format

The final verdict should use a bounded result label, such as one of the following:

- CORE_GOVERNANCE_LANES_MIGRATED_TO_UNIVERSAL_TEMPLATES
- CORE_GOVERNANCE_LANES_MIGRATED_TO_UNIVERSAL_TEMPLATES_WITH_RESTRICTIONS
- CORE_GOVERNANCE_LANES_PARTIALLY_MIGRATED_TEMPLATE_GAPS_REMAIN
- UNIVERSAL_TEMPLATE_BASELINE_DEFINED_BUT_MIGRATION_NOT_COMPLETE

## Risks and controls

### Risk: semantic drift during normalization
Control: require lane-by-lane compatibility notes and preserve original lane identity.

### Risk: template drift while migration is underway
Control: freeze the target universal template contract before editing the lane set.

### Risk: false confidence from formatting-only success
Control: require admission, routing, or equivalent governance verification after migration.

### Risk: historical lanes are too inconsistent to normalize cleanly
Control: allow bounded restriction status instead of forcing a misleading claim of completion.

## Follow-on value

Once the core lanes are migrated to universal templates, the governance OS becomes easier to scale across repositories, stacks, and specialized sub-agents. It also becomes substantially easier to:

- author new lanes safely
- compare repositories consistently
- compute maturity from governed evidence
- support autonomous next-valid execution
- package governance OS as a reusable framework

## Recommended next lanes

The most natural follow-on work after this lane is:

1. verify the migrated core governance lane set against the admission and routing system
2. register or refresh the normalized lane definitions in the pipeline registry
3. extend the same universal template migration pattern to non-core or domain-specific lane families

