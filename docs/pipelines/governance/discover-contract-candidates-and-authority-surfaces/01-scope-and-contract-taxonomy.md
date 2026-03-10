# Scope And Contract Taxonomy

## In Scope

- subsystem boundaries evidenced by governance documents and repository structure
- state authority boundaries between constitution, doctrine, registry, pipeline definitions, and generated artifacts
- governance orchestration boundaries expressed through pipeline definitions
- external interface boundaries represented by repository-facing governance surfaces
- lifecycle and state-transition contracts for pipeline execution evidence
- persistence and state-store contracts where repository files act as the state substrate
- compatibility-layer boundaries such as placeholders and bootstrap-era surfaces

## Out Of Scope

This pipeline does not:

- remediate implementation
- verify live runtime behavior beyond repository evidence
- author final subsystem contracts in full
- declare contract closure
- promote any candidate to canonical status automatically
- replace architecture doctrine

## Contract Taxonomy

| Contract Class | Meaning In This Repository |
|----------------|----------------------------|
| architecture doctrine contract | Governs architectural interpretation rules and authority ordering for repository structure. |
| governance authority contract | Governs constitution, doctrine, and agent-surface responsibilities and precedence. |
| pipeline orchestration contract | Governs how a pipeline definition drives required phases, outputs, and decisions. |
| pipeline artifact contract | Governs how execution artifacts are named, located, and interpreted relative to pipeline definitions. |
| registry integrity contract | Governs when a pipeline must appear in the registry and what the registry is allowed to assert. |
| contract-root stewardship contract | Governs the meaning and allowed use of `docs/contracts/` before substantive contracts exist. |
| compatibility and placeholder contract | Governs how placeholders, bootstrap surfaces, and proposed pipelines must be treated without over-promotion. |
| lifecycle progression contract | Governs sequencing from initialization to discovery, audit, remediation, verification, and promotion. |

## Scope Decision

Because the repository contains no application implementation, contract discovery is limited to governance-surface contracts and placeholder stewardship. Runtime APIs, event buses, UI boundaries, and persistence adapters remain out of scope until repository evidence establishes them.
