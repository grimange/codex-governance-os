# Repository Evidence Inventory

## Code Evidence

| Surface | Evidence | Classification | Notes |
|---------|----------|----------------|-------|
| Application implementation | none present | ambiguous / unresolved | No backend, frontend, service, worker, or infrastructure code exists in tracked repository content. |
| `.gitignore` | tracks repository ignore policy | descriptive but non-authoritative | Relevant only as an operational support file; not an architecture authority surface. |

## Documentation Evidence

| Surface | Evidence | Classification | Notes |
|---------|----------|----------------|-------|
| `AGENTS.md` | repository constitution with mission, authority order, pipeline model, artifact standards, and routing rules | canonical authority | Highest repository-local governance authority after repository state. |
| `.codex/AGENTS.md` | Codex operating instructions referencing constitution and doctrine | likely authority candidate | Operational surface for agents; subordinate to constitution and doctrine. |
| `docs/governance/architecture-doctrine.md` | bootstrap doctrine installed by pipeline 000 | likely authority candidate | Exists as doctrine, but only captured initialization-baseline principles before this pipeline. |
| `docs/pipelines/governance/000--initialize-governed-project.md` | canonical initialization workflow | canonical authority | Governs repository bootstrap expectations. |
| `docs/pipelines/governance/001--discover-existing-architecture-and-establish-doctrine.md` | discovery/doctrine workflow being executed | likely authority candidate | Proposed pipeline definition that becomes operational through execution and registration. |
| `docs/pipelines/governance/initialize-governed-project/*.md` | execution artifacts for pipeline 000 | descriptive but non-authoritative | Durable evidence of initialization, but subordinate to the governing docs. |
| `docs/pipelines/registry/pipeline-registry.md` | registry of active pipelines | likely authority candidate | Canonical activation surface for pipelines, but does not override a pipeline definition. |
| `docs/contracts/.gitkeep` | placeholder contracts root | descriptive but non-authoritative | Establishes location only. |
| `docs/modernization/.gitkeep` | placeholder modernization root | descriptive but non-authoritative | Establishes location only. |

## Operational Evidence

| Surface | Evidence | Classification | Notes |
|---------|----------|----------------|-------|
| `docs/pipelines/registry/pipeline-registry.md` | registry status model for pipeline activation | likely authority candidate | Operational governance signal, not implementation runtime. |
| Repository folder layout | clear segregation of governance, contracts, modernization, and pipeline artifacts | inferred architecture | The current system is structured as a documentation-backed governance surface. |

## Legacy / Drift Indicators

| Surface | Evidence | Classification | Notes |
|---------|----------|----------------|-------|
| bootstrap doctrine | initialization-era doctrine uses generic minimal language | compatibility layer | Useful baseline, but insufficient as the long-term architecture authority once discovery occurs. |
| pipeline 001 status | specification marked `PROPOSED` while being used operationally | ambiguous / unresolved | Requires supporting governance update so discoverability matches usage. |
| empty domain roots | `docs/contracts/` and `docs/modernization/` contain only placeholders | ambiguous / unresolved | Reserved surfaces exist without active domain content. |

## Evidence Distinctions

- Evidence of actual behavior: the repository currently behaves as a governance-document system with a constitution, doctrine, pipeline definitions, execution artifacts, and a registry.
- Descriptive claims: the bootstrap doctrine and proposed pipeline text describe intended governance patterns.
- Inferred architecture: the repository's implemented architecture is documentation-first governance rather than application runtime logic.
- Unresolved ambiguity: whether pipeline 001 is formally active and how future non-governance implementation should revise this doctrine.
