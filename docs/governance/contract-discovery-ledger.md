# Contract Discovery Ledger

## Purpose

This ledger records the repository's discovered contract candidates, their apparent authority surfaces, and the next governance action required for each. It is the durable planning surface for future contract pipelines.

## Candidate Inventory

| Contract Candidate | Status | Primary Authority Surface | Recommended Next Action | Notes |
|--------------------|--------|---------------------------|-------------------------|-------|
| Governance Authority Contract | partially implied | `AGENTS.md` | verify canonical candidate | Constitution and doctrine already cover much of this, but the repository may later want a more explicit cross-surface contract statement. |
| Pipeline Orchestration Contract | partially implied | `docs/pipelines/governance/*.md` | author new contract | Cross-pipeline orchestration rules are distributed across definitions rather than consolidated. |
| Pipeline Registry Integrity Contract | already canonical | `docs/contracts/pipeline-registry-integrity-contract.md` | audit existing contract | Canonical contract authored through pipeline `004`; registry must now remain aligned with it. |
| Pipeline Artifact Interpretation Contract | partially implied | `docs/governance/architecture-doctrine.md` | author new contract | Artifact evidence is central to governance and should have explicit interpretation rules. |
| Contract Root Stewardship Contract | missing | `docs/contracts/` | author new contract | Needed before substantive contracts accumulate under the contracts root. |
| Placeholder And Compatibility Handling Contract | partially implied | `docs/governance/architecture-doctrine.md` | audit existing contract | The doctrine already covers part of this space, but normalization may still help. |
| Lifecycle Progression Contract | fragmented | governance pipeline catalog | normalize fragmented surfaces | Sequencing exists, but later lifecycle stages are not yet active. |

## Current Maturity

Contract maturity is emergent. The repository has strong governance authorities and a clear architecture doctrine, but most contract surfaces are still implied rather than explicitly authored as contracts.

## Ambiguity Notes

- No product-domain subsystem contracts should be authored until repository evidence shows real implementation boundaries.
- Placeholder roots and proposed status labels remain governance ambiguity sources until normalized.
