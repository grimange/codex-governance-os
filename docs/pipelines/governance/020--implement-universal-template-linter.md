---
id: "020"
title: "Implement Universal Template Linter"
status: "proposed"
phase: "implementation"
layer: "governance"
kind: "codex-pipeline"
slug: "implement-universal-template-linter"
registry_id: "governance.templates.implement-universal-template-linter"
owner: "codex"
objective: "Create a universal template linting capability that validates repository governance templates, pipeline templates, rule templates, evidence templates, and sub-agent templates against a shared canonical contract before they are admitted or reused."
context: |
  codex-governance-os is moving toward reusable, repo-agnostic governance assets.
  As the number of templates grows, the system needs a deterministic way to verify
  that every template conforms to canonical structure, naming, metadata, required
  sections, safety boundaries, and portability expectations. Without this, template
  drift will spread invalid frontmatter, missing sections, inconsistent placeholders,
  unsafe assumptions, and repo-specific leakage into future pipelines.
problem_statement: |
  The repository needs a universal template linter that can inspect any governed
  template and determine whether it is structurally valid, portable, safe to reuse,
  and aligned with the governance operating model. The linter must fail closed,
  emit actionable diagnostics, and become the canonical gate for template admission,
  normalization, and ongoing template quality verification.
why_now:
  - "Universal templates are becoming a core reuse mechanism for codex-governance-os."
  - "Template drift would multiply defects across future pipelines and sub-agents."
  - "A linter is required before large-scale template standardization can be trusted."
  - "Governance OS needs machine-checkable portability and structure guarantees."
triggers:
  - "A new governed template is introduced."
  - "An existing template is edited."
  - "A pipeline attempts to consume a template."
  - "A repository-wide template quality audit is requested."
preconditions:
  - "Canonical template classes are defined or can be discovered from repository conventions."
  - "The governance toolchain can read template files from known locations."
  - "The linter can produce deterministic machine-readable and human-readable output."
inputs:
  - "Template files under docs/governance/templates/, docs/codex/templates/, or other declared docs-root template surfaces."
  - "Canonical template contract definition for each supported template class."
  - "Existing governance rules for frontmatter, naming, safety, and evidence structure."
  - "Repository path allowlist / denylist for portable template validation."
outputs:
  - "A universal template linting command exposed through the governance toolchain."
  - "A canonical rule set for template validity."
  - "Structured lint results with severity, rule id, path, and remediation guidance."
  - "A template-admission decision: VALID_AS_IS, NORMALIZED_AND_VALID, or BLOCKED."
  - "Verification artifacts proving the linter detects valid, invalid, and edge-case templates."
scope:
  includes:
    - "Governed pipeline templates"
    - "Governed rule templates"
    - "Governance evidence bundle templates"
    - "Sub-agent specialization templates"
    - "Prompt / instruction templates intended for governed reuse"
    - "Shared frontmatter and section contract enforcement"
    - "Portability checks for repo-specific leakage"
    - "Placeholder integrity and unresolved-token checks"
    - "Machine-readable output for future automation"
  excludes:
    - "Semantic correctness of downstream code generated from a template"
    - "Automatic repair beyond explicitly safe normalization steps"
    - "Evaluation of business-domain truth outside template structure and governance rules"
    - "Cross-repository publishing or package distribution"
non_goals:
  - "Do not invent missing business content inside templates."
  - "Do not silently rewrite templates beyond approved normalization rules."
  - "Do not treat stylistic preference as a blocking defect unless canonically defined."
  - "Do not allow repo-specific implementation details to become universal defaults."
canonical_template_classes:
  - name: "pipeline-template"
    required_elements:
      - "governed frontmatter"
      - "canonical title"
      - "objective"
      - "problem statement"
      - "scope"
      - "inputs"
      - "outputs"
      - "execution steps"
      - "verification"
      - "final outcome / completion criteria"
  - name: "rule-template"
    required_elements:
      - "rule identifier"
      - "purpose"
      - "authority / source hierarchy"
      - "enforcement logic"
      - "allowed behavior"
      - "blocked behavior"
      - "evidence expectations"
  - name: "evidence-template"
    required_elements:
      - "artifact inventory"
      - "verification method"
      - "decision vocabulary"
      - "traceability fields"
  - name: "sub-agent-template"
    required_elements:
      - "specialization purpose"
      - "entry conditions"
      - "decision boundaries"
      - "tool boundaries"
      - "handoff rules"
      - "evidence / reporting output"
  - name: "instruction-template"
    required_elements:
      - "purpose"
      - "safe invocation boundary"
      - "inputs"
      - "expected outputs"
      - "failure handling"
policy_requirements:
  - id: "UTL-001"
    rule: "Every governed template must declare a recognized template class."
    severity: "error"
  - id: "UTL-002"
    rule: "Every governed template must contain canonical frontmatter keys required by its class."
    severity: "error"
  - id: "UTL-003"
    rule: "Titles, identifiers, and slugs must match canonical naming conventions."
    severity: "error"
  - id: "UTL-004"
    rule: "Required sections must appear exactly once unless the class contract explicitly allows repetition."
    severity: "error"
  - id: "UTL-005"
    rule: "Templates must not contain unresolved placeholder tokens unless explicitly declared as allowed placeholders."
    severity: "error"
  - id: "UTL-006"
    rule: "Templates must not hard-code repo-specific paths, branch names, project names, secrets, or environment assumptions when marked universal."
    severity: "error"
  - id: "UTL-007"
    rule: "Templates must not contain contradictory status metadata or mixed draft/final semantics."
    severity: "error"
  - id: "UTL-008"
    rule: "Safe normalizations may fix whitespace, canonical heading format, scalar formatting, and known frontmatter normalization defects."
    severity: "warning"
  - id: "UTL-009"
    rule: "The linter must return deterministic results for identical file content."
    severity: "error"
  - id: "UTL-010"
    rule: "Every lint failure must include actionable remediation text."
    severity: "error"
normalization_policy:
  safe_normalizations:
    - "trim trailing whitespace"
    - "insert canonical top heading when missing and derivable"
    - "normalize single-line scalar frontmatter formatting"
    - "normalize line endings"
    - "sort or reformat known non-semantic metadata only where canonically defined"
  prohibited_normalizations:
    - "inventing missing objective or scope text"
    - "rewriting template meaning"
    - "silently removing unsafe content without recording it"
    - "guessing placeholders or business-specific values"
lint_decision_model:
  valid_as_is: "Template fully conforms without mutation."
  normalized_and_valid: "Only approved safe normalization was required before passing."
  blocked: "Template violates one or more blocking rules or requires semantic author intervention."
implementation_plan:
  - step: "Define canonical template taxonomy"
    detail: |
      Create a machine-readable registry of supported template classes and their
      required metadata, headings, placeholders, and portability constraints.
  - step: "Define lint rule catalog"
    detail: |
      Implement a stable rule vocabulary with rule ids, severity, remediation text,
      and deterministic matching logic.
  - step: "Build parser and classifier"
    detail: |
      Parse frontmatter, headings, placeholder tokens, and file structure; then
      classify each template into a supported canonical class or fail closed.
  - step: "Implement portability checks"
    detail: |
      Detect hard-coded repo names, implementation paths, project-specific secrets,
      environment assumptions, and non-universal references when a template claims
      portability or universality.
  - step: "Implement safe normalization layer"
    detail: |
      Apply only approved syntactic repairs and record every mutation in lint output.
  - step: "Expose governance CLI surface"
    detail: |
      Add commands such as gov.py lint-template <path>, gov.py lint-templates,
      and optional JSON output for automation.
  - step: "Create fixture suite"
    detail: |
      Add passing, failing, and edge-case template fixtures to prove rule coverage,
      deterministic behavior, and fail-closed handling.
  - step: "Wire admission integration"
    detail: |
      Ensure template-consuming lanes or future generators can require a PASS or
      NORMALIZED_AND_VALID result before template use.
  - step: "Document operator workflow"
    detail: |
      Record how maintainers run the linter, interpret output, remediate defects,
      and approve canon changes safely.
acceptance_criteria:
  - "A canonical template rule catalog exists and is versioned in the repository."
  - "The linter can classify and validate all supported governed template classes."
  - "The linter emits deterministic text and JSON results."
  - "Blocking defects are fail-closed and non-semantic defects may normalize safely."
  - "Portability leakage is detected for templates marked universal."
  - "Fixture-based tests prove valid, invalid, and normalized cases."
  - "At least one verification lane demonstrates integration with governance admission or template consumption."
verification:
  automated_checks:
    - "Unit tests for parser, classifier, rule evaluation, normalization, and decision model"
    - "Fixture tests for each template class"
    - "Golden-output tests for deterministic lint result formatting"
    - "CLI invocation tests for single-template and repo-wide linting"
  manual_checks:
    - "Review sample universal templates for false positives and false negatives"
    - "Confirm repo-specific leakage detection catches known anti-patterns"
    - "Confirm safe normalization does not mutate semantic content"
  evidence_artifacts:
    - "01-problem-statement.md"
    - "02-template-taxonomy.md"
    - "03-rule-catalog.md"
    - "04-linter-design.md"
    - "05-fixture-and-test-plan.md"
    - "06-verification.md"
    - "07-final-verdict.md"
risks:
  - risk: "Overly strict lint rules block useful template evolution."
    mitigation: "Separate blocking semantic errors from advisory style warnings and version canon changes deliberately."
  - risk: "Overly weak lint rules allow drift to continue."
    mitigation: "Use fixture regressions derived from real template failures and portability defects."
  - risk: "Universal portability checks produce false positives."
    mitigation: "Make universal mode explicit and maintain allowlists for approved neutral references."
  - risk: "Normalization becomes silent semantic rewriting."
    mitigation: "Restrict normalization to enumerated syntax-only repairs and record all changes."
dependencies:
  - "Canonical frontmatter and lane admission conventions"
  - "Governance CLI / toolchain entrypoint"
  - "Repository rule set for governed documents"
future_follow_on_pipelines:
  - "Verify Universal Template Linter"
  - "Register Universal Template Canon and Admission Gate"
  - "Implement Universal Template Generator Against Linted Canon"
  - "Detect and Repair Template Drift Across Repository"
final_outcome:
  success_state: "UNIVERSAL_TEMPLATE_LINTER_IMPLEMENTED_AND_READY_FOR_GOVERNED_ADMISSION"
  partial_state: "UNIVERSAL_TEMPLATE_LINTER_IMPLEMENTED_WITH_COVERAGE_GAPS"
  failure_state: "UNIVERSAL_TEMPLATE_LINTER_BLOCKED_OR_NON_DETERMINISTIC"
---

# 020 -- Implement Universal Template Linter

## Purpose

Implement a canonical linting capability for universal governance templates so the
repository can safely standardize and reuse templates without spreading invalid
metadata, missing structure, unsafe assumptions, or repo-specific leakage.

## Operator Intent

This pipeline establishes the enforcement layer that answers a simple question:
can this template be trusted as a universal governed asset?

A successful implementation gives the Governance OS a reusable admission gate for
pipeline templates, rules, evidence packs, sub-agent definitions, and other
structured governance artifacts.

## Expected Result

After this lane is complete, the repository should have a deterministic universal
template linter that:

1. classifies template type,
2. validates canonical structure,
3. detects portability and placeholder defects,
4. applies only safe normalizations,
5. emits machine-readable diagnostics, and
6. returns a governed admission decision.

## Execution Notes

The implementation should remain fail-closed. When the linter is uncertain about
a template class, required section, or portability status, it should block rather
than guess.

The linter should be designed as a governance primitive, not as a one-off helper.
That means its rules, outputs, and decisions must be stable enough to support
future automation, autonomous governance loops, and template-driven generation.

## Completion Condition

This pipeline is complete when the universal template linter exists, is tested,
produces deterministic decisions, and can be used as the canonical validation gate
for governed reusable templates.
