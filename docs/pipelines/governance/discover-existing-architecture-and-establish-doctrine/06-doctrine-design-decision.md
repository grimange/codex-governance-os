# Doctrine Design Decision

## Decision

Adopt a governance-surface architecture doctrine in which the repository's canonical system is the version-controlled governance documentation and pipeline framework currently implemented.

## Why This Doctrine Was Chosen

- Repository evidence shows governance artifacts only; inventing backend, frontend, service, or persistence architecture would violate the pipeline's evidence-first rule.
- The constitution already establishes a strong authority hierarchy that the doctrine can refine for architecture use.
- Pipeline definitions and artifacts form a clear procedural and evidentiary model that downstream pipelines need to consume consistently.

## Architecture Principles

- repository state in version control is the canonical substrate
- constitutional and doctrinal documents define meaning before artifacts do
- pipeline definitions author expected procedure
- pipeline artifacts preserve evidence, not superseding authority
- placeholders reserve namespace but do not create architecture
- future implementation layers require explicit doctrinal revision

## Authority Precedence Decision

The doctrine adopts the repository constitution's order and refines it to distinguish between canonical authority, operational support surfaces, and descriptive outputs.

## System Truth Model

System truth is documentation-backed and file-backed, not runtime-backed. The repository currently has no evidenced runtime state authority outside tracked files.

## State Ownership Rules

- authoritative state is authored in tracked governance documents
- pipeline definitions own process expectations
- pipeline artifacts own run-specific evidence only
- the registry owns activation visibility, not process semantics

## Orchestration Ownership

Pipeline definitions own orchestration of governance work. Agents execute against those definitions and record outputs in pipeline artifact folders.

## Projection Rules

- summaries, verification records, and verdicts are projections of repository state and pipeline execution
- placeholders and empty directories are structural projections only
- no projected artifact may be treated as a stronger source of truth than the file it summarizes

## Compatibility-Layer Handling

Initialization-era doctrine language is preserved only insofar as it remains consistent with stronger evidence-based doctrine. Transitional or proposed surfaces must be called out explicitly instead of silently treated as canonical.

## Document Precedence Rules

- the constitution outranks doctrine
- doctrine outranks pipeline definitions on architecture interpretation
- registered pipeline definitions outrank generated artifacts
- descriptive notes without explicit elevation remain non-authoritative

## Terminology Normalization

Canonical terms for the current repository are constitution, doctrine, pipeline definition, registry, pipeline artifact, canonical, descriptive, and placeholder. Product-architecture terms remain non-canonical until implementation evidence exists.

## Residual Uncertainty

The repository may later gain product-domain code or operational infrastructure. When that happens, this doctrine must be reevaluated rather than assumed to still be sufficient.
