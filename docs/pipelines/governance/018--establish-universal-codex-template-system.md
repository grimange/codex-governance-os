---
pipeline_id: "template.universal.establish-codex-template-system"
title: "Codex Pipeline — Establish Universal Codex Template System"
status: "proposed"
category: "governance"
stage: "design"
scope: "cross-repository"
objective: "Create a universal, governed template system for pipelines, rules, skills, verification lanes, evidence bundles, and execution contracts in codex-governance-os."
parent: null
depends_on: []
blocks: []
allowed_next:
  - "template.universal.implement-template-registry"
  - "template.universal.implement-template-linter"
  - "template.universal.implement-template-scaffold"
  - "template.universal.verify-template-conformance"
outputs:
  - "docs/governance/templates/README.md"
  - "docs/governance/templates/template-registry.yaml"
  - "docs/governance/templates/pipeline-template.md"
  - "docs/governance/templates/verification-template.md"
  - "docs/governance/templates/rule-template.md"
  - "docs/governance/templates/skill-template.md"
  - "docs/governance/templates/evidence-pack-template.md"
  - "docs/governance/templates/decision-template.md"
  - "docs/governance/templates/remediation-template.md"
  - "tools/governance/template_registry.py"
  - "tools/governance/template_lint.py"
  - "tools/governance/template_scaffold.py"
  - "tests/governance/test_template_registry.py"
  - "tests/governance/test_template_lint.py"
  - "tests/governance/test_template_scaffold.py"
success_criteria:
  - "Every governed document family has a canonical template."
  - "Templates separate required fields from optional fields."
  - "Templates support stack-specific overlays without changing the universal core."
  - "A linter can validate template conformance."
  - "A scaffold command can instantiate new governed artifacts from templates."
  - "Verification lanes can prove template completeness and conformance."
governance_mode: "fail-closed"
execution_mode: "advisory-then-enforcing"
---

# Codex Pipeline — Establish Universal Codex Template System

## 1. Purpose

Design and authorize a universal template system for `codex-governance-os` so future governed artifacts are created from one canonical structure instead of ad hoc document patterns.

This lane establishes the template architecture, registry model, validator expectations, scaffold behavior, overlay strategy, and verification boundary required to make template-driven governance durable across multiple stacks and repository types.

## 2. Problem Statement

`codex-governance-os` is evolving into a reusable governance substrate, but without a universal template layer the system risks:

- drift between pipeline files
- inconsistent frontmatter and artifact bundle structure
- repository-specific conventions leaking into universal governance
- weak portability across Laravel, Django, package, and tooling repositories
- brittle automation because similarly named artifacts are not structurally identical
- higher AI execution variance because governed documents are not shape-stable

A universal template system is needed so Codex can reliably author, lint, scaffold, verify, and migrate governed artifacts without losing consistency.

## 3. Objectives

This pipeline must:

- define the canonical template families used by `codex-governance-os`
- separate universal requirements from stack-specific overlays
- make template conformance machine-checkable
- make scaffold generation deterministic
- preserve fail-closed governance semantics
- enable future migration of existing lanes into a shared governed template model

## 4. Scope

This pipeline applies to the universal governance substrate, not to one application framework.

It must be valid for:

- Laravel repositories
- Django repositories
- generic Python repositories
- generic PHP repositories
- MCP and tooling repositories
- modernization programs
- governance-only repositories
- repository templates that embed governance behavior

## 5. Out of Scope

This lane does not yet:

- migrate every existing pipeline into the universal template system
- enforce the new templates repository-wide on day one
- introduce stack-specific behavior that weakens the universal core
- authorize unbounded auto-remediation of malformed artifacts
- replace project-local governance decisions that are stricter than the universal baseline

## 6. Required Design Principles

The universal template system must follow these principles:

1. Universal core first.
2. Overlays may extend but must not weaken the universal core.
3. Governed artifacts must remain deterministic and machine-checkable.
4. Verification evidence must always be producible.
5. Restrictions and non-claims must remain explicit.
6. Template changes must be versioned.
7. Breaking template changes require a verification lane before enforcement.
8. Template scaffolding must never silently invent authority or execution rights.

## 7. Template Families

The system must define canonical templates for at least the following families.

### 7.1 Pipeline Template

Used for executable, advisory, design, implementation, verification, and governance control lanes.

Required sections:

- frontmatter
- purpose
- problem statement
- objectives
- scope
- preconditions
- execution steps
- expected outputs
- verification method
- restrictions and non-claims
- final verdict shape

### 7.2 Verification Template

Used for `verify-*` lanes and evidence-backed closure checks.

Required sections:

- claim under test
- evidence sources
- verification commands
- pass conditions
- fail conditions
- residual risk
- final verdict

### 7.3 Rule Template

Used for codex rules and governance policies.

Required sections:

- rule name
- policy intent
- rationale
- enforcement level
- allowed behavior
- blocked behavior
- escalation path
- examples

### 7.4 Skill Template

Used for codex skill contracts and invocation boundaries.

Required sections:

- skill name
- purpose
- invocation conditions
- inputs
- outputs
- authority boundaries
- safety limits
- examples

### 7.5 Evidence Pack Template

Used for governed execution bundles and artifact directories.

Required sections:

- problem statement
- observed state
- analysis
- decision
- remediation or recommendation
- verification
- final verdict

### 7.6 Decision Template

Used for architecture and governance decisions.

Required sections:

- context
- options considered
- chosen decision
- rationale
- implications
- rollback or reversal conditions

### 7.7 Remediation Template

Used for corrective governance action.

Required sections:

- defect statement
- impact
- bounded remediation
- safety constraints
- validation plan
- completion conditions

## 8. Universal Core Schema

Every template family must support a common core contract.

Minimum universal fields:

- `id` or `pipeline_id`
- `title`
- `status`
- `category`
- `stage`
- `objective`
- `depends_on`
- `outputs`
- `success_criteria`
- `governance_mode`
- `execution_mode`
- `restrictions`
- `non_claims`

Notes:

- family-specific aliases may exist, but the universal registry must normalize them
- any overlay that removes a universal requirement is invalid
- optional fields must be clearly marked as optional, not merely omitted informally

## 9. Overlay Model

The template system must support three layers.

### 9.1 Universal Core

The immutable governance baseline shared by every repository.

### 9.2 Stack Overlay

Adds stack-aware expectations without changing or weakening the universal baseline.

Examples:

- `laravel`
- `django`
- `python-package`
- `php-package`
- `mcp-tools`
- `infrastructure`

### 9.3 Project Overlay

Adds repository-local conventions such as naming, directories, evidence-pack placement, or command patterns.

Rule:

Project overlays may extend the core but must not reduce required sections, reduce evidence obligations, or bypass fail-closed behavior.

## 10. Canonical Directory Design

Recommended structure:

```text
docs/
  governance/
    templates/
      README.md
      template-registry.yaml
      pipeline-template.md
      verification-template.md
      rule-template.md
      skill-template.md
      evidence-pack-template.md
      decision-template.md
      remediation-template.md
      overlays/
        laravel.yaml
        django.yaml
        python-package.yaml
        php-package.yaml
        mcp-tools.yaml

tools/
  governance/
    template_registry.py
    template_lint.py
    template_scaffold.py

tests/
  governance/
    test_template_registry.py
    test_template_lint.py
    test_template_scaffold.py
```

## 11. Implementation Plan

### Phase A — Define Template Registry

Create `docs/governance/templates/template-registry.yaml`.

The registry must define:

- template family
- version
- required sections
- optional sections
- required frontmatter fields
- normalization aliases
- output path expectations
- validator mapping
- scaffold mapping
- overlay compatibility

### Phase B — Author Canonical Templates

Create canonical markdown templates for each family.

Each template must visibly distinguish:

- `REQUIRED`
- `OPTIONAL`
- `GENERATED`
- `PROJECT_DEFINED`

### Phase C — Build Template Registry Loader

Create `tools/governance/template_registry.py`.

The loader must:

- parse the registry deterministically
- expose normalized template family definitions
- reject malformed or ambiguous registry entries
- detect duplicate identifiers or alias collisions

### Phase D — Build Template Linter

Create `tools/governance/template_lint.py`.

The linter must verify:

- required sections exist
- section order is canonical where mandated
- required frontmatter keys are present
- prohibited weakening is absent
- overlays do not remove universal requirements
- scaffolded artifacts pass template conformance

### Phase E — Build Template Scaffold Tool

Create `tools/governance/template_scaffold.py`.

The scaffold tool must:

- generate artifacts from a selected template family
- optionally apply one or more overlays
- inject canonical frontmatter
- materialize expected headings and placeholders
- generate deterministic output paths
- refuse ambiguous or invalid overlay combinations

### Phase F — Add Tests

Create tests that prove:

- the registry loads correctly
- every template is parseable
- scaffold output passes lint
- overlays inherit properly
- invalid weakening is blocked
- output remains deterministic across runs

### Phase G — Introduce Enforcement Safely

Adopt a two-step rollout:

1. advisory mode
2. enforcing mode after verification

No repository-wide hard enforcement should begin before a verification lane confirms the template system works across representative fixtures.

## 12. Expected Outputs

This design lane should authorize the creation of:

- universal template registry
- universal template family files
- registry loader
- template linter
- template scaffold tool
- tests for registry, lint, and scaffold behavior
- follow-up verification lanes
- migration lanes for existing governance artifacts

## 13. Preconditions

Before implementation starts, the repository should already have:

- an existing governed pipeline model
- normalized or mostly normalized lane structure
- stable artifact bundle conventions or an active effort to normalize them
- governance tooling entry points under `tools/governance/`

If some of these are incomplete, the lane may still proceed as a design lane, but enforcement should remain advisory.

## 14. Execution Steps

1. Define universal template families.
2. Specify the universal core schema.
3. Define overlay rules and anti-weakening constraints.
4. Design the registry format.
5. Design the linter requirements.
6. Design scaffold behavior and deterministic output rules.
7. Define safe rollout from advisory to enforcement.
8. Define verification requirements and follow-up lanes.

## 15. Verification Method

This design lane is considered complete when:

- the universal template families are clearly defined
- the universal core schema is explicit
- the overlay model is bounded and anti-weakening
- the registry, linter, and scaffold responsibilities are clearly separated
- follow-up implementation lanes are derivable without ambiguity
- at least one future verification lane is explicitly required before enforcement

## 16. Restrictions

This lane must not:

- silently rewrite all existing governance artifacts
- introduce overlays that weaken required evidence or safety fields
- allow project-local conventions to override universal fail-closed semantics
- claim full repository compliance before a verification lane proves it
- claim multi-stack safety without representative fixtures

## 17. Non-Claims

This design does not yet prove:

- that all existing lanes already conform to the future template system
- that scaffolded output is production-ready without testing
- that overlay inheritance is complete for every stack on first release
- that automatic migration can safely normalize every historical artifact

## 18. Suggested Follow-Up Pipelines

Recommended next sequence:

1. `188 -- Implement Universal Template Registry`
2. `189 -- Implement Universal Template Linter`
3. `190 -- Implement Universal Template Scaffold`
4. `191 -- Verify Universal Template Conformance Across Multi-Stack Fixtures`
5. `192 -- Migrate Core Governance Lanes To Universal Templates`
6. `193 -- Add Universal Overlay Packs For Supported Stacks`
7. `194 -- Verify Overlay Safety And Anti-Weakening Guarantees`

## 19. Final Verdict Shape

Allowed final verdict values:

- `UNIVERSAL_CODEX_TEMPLATE_SYSTEM_DESIGNED`
- `UNIVERSAL_CODEX_TEMPLATE_SYSTEM_DESIGNED_WITH_RESTRICTIONS`
- `UNIVERSAL_CODEX_TEMPLATE_SYSTEM_IMPLEMENTED`
- `UNIVERSAL_CODEX_TEMPLATE_SYSTEM_IMPLEMENTED_WITH_RESTRICTIONS`
- `UNIVERSAL_CODEX_TEMPLATE_SYSTEM_VERIFIED`
- `UNIVERSAL_CODEX_TEMPLATE_SYSTEM_VERIFIED_WITH_RESTRICTIONS`

## 20. Recommended Initial Verdict For This Lane

If this document is adopted as the canonical design lane, the expected immediate outcome is:

`UNIVERSAL_CODEX_TEMPLATE_SYSTEM_DESIGNED`

