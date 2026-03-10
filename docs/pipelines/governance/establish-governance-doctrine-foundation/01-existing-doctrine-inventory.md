# Existing Governance Doctrine Inventory

## Canonical And Reusable

- `AGENTS.md`
  Classification: canonical and reusable.
  Doctrine fragments present: authority precedence, artifact expectations, routing rules, deterministic sequencing expectations.
- `docs/governance/architecture-doctrine.md`
  Classification: canonical and reusable.
  Doctrine fragments present: authority model, source-of-truth rules, artifact meaning, compatibility handling, terminology rules.
- `docs/contracts/pipeline-registry-integrity-contract.md`
  Classification: canonical and reusable for registry behavior.
  Doctrine fragments present: registry identity matching, active-pipeline discoverability, ambiguity handling for proposed versus active pipelines.

## Reusable But Informal

- `.codex/AGENTS.md`
  Classification: reusable but informal.
  Doctrine fragments present: operating expectations, repository routing guidance, requirement to treat doctrine and contracts as operational authority.
- Existing governance pipeline definitions `000` through `007`
  Classification: reusable but informal.
  Doctrine fragments present: repeated statements about phase numbering, summary/final-verdict expectations, lifecycle ordering between discovery, audit, remediation, verification, and promotion.

## Duplicated Across Multiple Surfaces

- Artifact durability and explicit verification/promotion requirements appear in `AGENTS.md`, `.codex/AGENTS.md`, and multiple pipeline definitions.
- Lifecycle sequencing language appears in `000`, `001`, `004`, `005`, `006`, and `007`, but no standalone lifecycle doctrine currently governs the sequence.
- Pipeline naming patterns are implemented by filename convention and artifact folders, but the naming law is implicit across the catalog rather than explicit in doctrine.
- Contract section expectations appear in `004--author-canonical-contract-for-highest-priority-subsystem.md` and in the existing registry contract, but there is no governing contract-writing standard for future subsystem contracts.

## Incomplete

- Lifecycle doctrine is incomplete: ordering is inferable from the catalog, but no canonical lifecycle document defines stages, dependencies, or allowed deviations.
- Artifact standard is incomplete: conventions exist in practice, but there is no doctrine that defines minimum bundle closure or exceptions handling.
- Naming standard is incomplete: pipeline filenames are consistent so far, but no doctrine defines collision, supersession, or registry identity rules across future additions.
- Terminology doctrine is incomplete: terms such as contract, drift, verification, promotion, and final verdict are used operationally without a controlled vocabulary document.

## Stale

- Several active pipeline definitions still carry `Status: PROPOSED`, which is a stale status signal relative to operational use and registry activation.
- Initialization-era references in earlier pipeline bodies still describe the governance baseline without access to doctrine-foundation documents that now need to exist as shared law.

## Missing

- `docs/governance/governance-lifecycle.md`
- `docs/governance/pipeline-artifact-standard.md`
- `docs/governance/pipeline-naming-standard.md`
- `docs/governance/contract-writing-standard.md`
- `docs/governance/governance-terminology.md`

## Inventory Conclusion

The repository already contains enough doctrinal fragments to normalize into a doctrine foundation, but the rules are currently scattered across the constitution, architecture doctrine, local agent instructions, and pipeline bodies rather than installed as a reusable doctrine set.
