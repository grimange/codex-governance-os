# Existing Reusable Behavior Inventory

## Strong Universal Skill Candidates

- Repository discovery behavior
  Sources: `docs/pipelines/governance/000--initialize-governed-project.md`, `001--discover-existing-architecture-and-establish-doctrine.md`, `003--discover-contract-candidates-and-authority-surfaces.md`
  Classification: strong universal skill candidate.
- Governance readiness audit behavior
  Sources: `docs/pipelines/governance/002--audit-repository-governance-readiness.md`
  Classification: strong universal skill candidate.
- Architecture doctrine authoring behavior
  Sources: `docs/pipelines/governance/001--discover-existing-architecture-and-establish-doctrine.md`, `docs/governance/architecture-doctrine.md`
  Classification: strong universal skill candidate.
- Contract candidate discovery behavior
  Sources: `docs/pipelines/governance/003--discover-contract-candidates-and-authority-surfaces.md`, `docs/governance/contract-discovery-ledger.md`
  Classification: strong universal skill candidate.
- Canonical contract authoring behavior
  Sources: `docs/pipelines/governance/004--author-canonical-contract-for-highest-priority-subsystem.md`, `docs/governance/contract-writing-standard.md`
  Classification: strong universal skill candidate.
- Implementation audit behavior
  Sources: `docs/pipelines/governance/005--audit-implementation-against-canonical-contract.md`
  Classification: strong universal skill candidate.
- Remediation planning behavior
  Sources: `docs/pipelines/governance/006--remediate-implementation-drift-against-contract.md`
  Classification: strong universal skill candidate.
- Contract alignment verification behavior
  Sources: `docs/pipelines/governance/007--verify-contract-alignment.md`
  Classification: strong universal skill candidate.
- Pipeline registry hygiene behavior
  Sources: `docs/contracts/pipeline-registry-integrity-contract.md`, `docs/pipelines/registry/pipeline-registry.md`
  Classification: strong universal skill candidate.
- Governed project bootstrap behavior
  Sources: `docs/pipelines/governance/000--initialize-governed-project.md`, `AGENTS.md`, `.codex/AGENTS.md`
  Classification: strong universal skill candidate.

## Reusable But Not Yet Normalized

- Governance document authoring patterns
  Sources: pipeline artifact bundles and doctrine documents.
  Classification: reusable but not yet normalized.
- Promotion and final-verdict authoring patterns
  Sources: executed governance artifact bundles.
  Classification: reusable but not yet normalized.

## Duplicated Guidance

- Artifact numbering and closure logic are duplicated across multiple pipeline definitions.
- Lifecycle sequencing language is duplicated across doctrine and pipeline bodies.
- Contract-shape guidance is duplicated between pipeline `004` and the new contract-writing doctrine.

## Incomplete

- There is no governed in-repository universal skill directory yet.
- There is no canonical invocation rule for choosing between universal and project-local skills.
- There is no skills discovery index for future projects.

## Stale

- Future pipeline specifications `009` through `014` are still marked `PROPOSED` even where the repository is already using them as planned active governance surfaces.
- Skill logic presently lives in long-form pipeline prose instead of bounded reusable skill packages.

## Project-Specific And Not Universal

- None of the currently identified candidates are domain-specific in a way that blocks universalization because the repository still contains governance-template behavior rather than product-domain runtime behavior.

## Inventory Conclusion

The repository already contains enough repeated Codex operating behavior to justify a universal skill layer. The missing work is normalization, packaging, invocation law, and extension boundaries.
