---
pipeline_id: "000"
title: "Initialize Governed Project"
status: active
category: governance
stage: bootstrap
objective: "Install the minimum governance framework required for a repository to operate as a governed Codex project."
depends_on: []
outputs: ["docs/pipelines/governance/initialize-governed-project/"]
success_criteria: ["Baseline governance surfaces are installed.", "The pipeline registry is updated.", "Initialization artifacts and verdict are recorded."]
governance_mode: fail-closed
execution_mode: advisory-then-enforcing
restrictions: ["Do not infer product-domain architecture during bootstrap.", "Do not skip registry publication when the lane becomes active."]
non_claims: ["Does not establish subsystem contracts.", "Does not certify implementation readiness beyond governance bootstrap."]
classification: governance.foundation
authority: repo-governance
autonomy: advisory-only
problem_statement: "A repository cannot support reliable governed operation until its core governance surfaces, authority model, and registry structure exist."
scope: "Bootstrap the minimum governance constitution, doctrine roots, pipeline catalog, and verification surfaces required for governed execution."
inputs: ["Current repository state", "Repository constitution target", "Governed bootstrap skill guidance"]
entry_conditions: ["Repository is not yet fully governed or needs bootstrap normalization."]
exit_conditions: ["Governance baseline is installed and recorded.", "Registry discoverability is explicit."]
validation: ["Inspect installed governance surfaces.", "Confirm pipeline registration and initialization artifacts."]
rollback: "Restore prior repository state from version control if the bootstrap normalization introduces unintended structural drift."
---

# Initialize Governed Project

## Purpose

Convert a standard repository into a governed Codex repository by installing the minimum governance framework required for deterministic pipeline operation.

## Problem Statement

Without an explicit governance bootstrap, later lanes operate against missing authority surfaces, undocumented routing rules, and incomplete artifact structure.

## Objectives

- install the baseline governance surfaces
- establish the initial authority and documentation roots
- register the initialization lane as an active governance surface
- produce inspectable bootstrap artifacts and a bounded verdict

## Scope

In scope: governance constitution, docs-root pipeline structure, registry integration, installation planning, verification, and promotion recording.

Out of scope: architecture discovery, subsystem contracting, implementation audits, or repository-specific runtime design.

## Preconditions

- repository state is available for inspection
- the bootstrap target is documentation-first governance installation
- the registry surface can be updated in the same governed change set

## Execution Steps

1. Record the pipeline summary and bootstrap scope under `docs/pipelines/governance/initialize-governed-project/`.
2. Discover the current repository state and baseline governance gaps.
3. Design the governance structure and initialization plan.
4. Install the baseline governance surfaces and publish registry integration.
5. Verify the installed bootstrap surfaces.
6. Record the promotion decision and final verdict.

Universal skills:

- `governed-project-bootstrap`
- `repository-discovery`
- `pipeline-registry-reconciliation`

## Expected Outputs

- initialization artifact bundle under `docs/pipelines/governance/initialize-governed-project/`
- installed baseline governance surfaces such as `AGENTS.md`, `.codex/AGENTS.md`, `docs/governance/`, and `docs/pipelines/`
- updated `docs/pipelines/registry/pipeline-registry.md`

## Verification Method

- inspect the installed governance surfaces
- confirm the registry lists pipeline `000`
- confirm initialization artifacts, promotion notes, and final verdict exist

## Restrictions

- do not infer architecture or contracts during bootstrap
- do not treat bootstrap completion as proof of repository readiness for all later lanes

## Non-Claims

- does not author architecture doctrine
- does not audit implementation behavior

## Final Verdict

Use a bounded bootstrap verdict such as `GOVERNED_PROJECT_INITIALIZED` or an explicitly restricted equivalent.
