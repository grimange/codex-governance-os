# Doctrine Gap Analysis

## Lifecycle Doctrine Gap

- Missing or fragmented rule: standard governance stage ordering, deviation policy, and dependency rules between discovery, audit, contract authoring, remediation, verification, and promotion.
- Current location if partially present: implied by pipeline numbering and repeated sequencing language in pipelines `000` through `007`.
- Governance risk: future pipelines may redefine sequence inconsistently or skip required predecessor work without recording why.
- Downstream effect on pipelines: discovery, audit, remediation, and verification pipelines remain harder to align and harder to compare across repositories.
- Implementation priority: high.

## Pipeline Artifact Standard Gap

- Missing or fragmented rule: minimum artifact bundle structure, numbering rules, closure surfaces, exceptions handling, and evidence expectations.
- Current location if partially present: `AGENTS.md`, `.codex/AGENTS.md`, and artifact patterns already present in executed governance pipelines.
- Governance risk: artifact bundles may become uneven, closing evidence may be omitted, and later audits may need to infer whether a pipeline run was complete.
- Downstream effect on pipelines: token usage increases because each pipeline restates formatting and closure expectations.
- Implementation priority: high.

## Pipeline Naming Standard Gap

- Missing or fragmented rule: filename pattern, verb-first naming, category alignment, registry identity matching, and anti-collision rules.
- Current location if partially present: existing `NNN--slug.md` filenames, artifact directory names, and registry entries.
- Governance risk: future template growth could introduce naming collisions, ambiguous slugs, or registry drift.
- Downstream effect on pipelines: discovery and registration become less deterministic as the catalog expands.
- Implementation priority: medium-high.

## Contract Writing Standard Gap

- Missing or fragmented rule: required sections and writing expectations for canonical subsystem contracts.
- Current location if partially present: pipeline `004` and the existing registry-integrity contract.
- Governance risk: future contracts may vary in structure, omit authority semantics, or become difficult to audit and verify consistently.
- Downstream effect on pipelines: audit, remediation, and verification pipelines may need contract-specific interpretation work that should have been normalized.
- Implementation priority: high.

## Governance Terminology Gap

- Missing or fragmented rule: controlled operational meanings for recurring governance terms.
- Current location if partially present: `docs/governance/architecture-doctrine.md`, pipeline definitions, and existing artifacts.
- Governance risk: the same term may mean different things in different pipelines or future repositories.
- Downstream effect on pipelines: comparison, reuse, and auditability degrade because terminology must be reinterpreted from context.
- Implementation priority: medium-high.

## Justification Summary

Each doctrine document is needed because the repository already behaves as though these rules exist, but it still relies on scattered fragments and implied conventions. Installing the doctrine foundation converts that implicit law into explicit, reusable governance authority.
