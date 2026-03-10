# Contract Scope And Boundaries

## In Scope

- activation semantics for governance pipelines
- required registry fields and referential integrity
- timing expectations for registry updates
- distinction between active pipelines and placeholder directories
- relationship between registry discoverability and higher-order governance authorities

## Out Of Scope

- phase logic inside any specific pipeline
- artifact content requirements beyond registry discoverability
- remediation, verification, or promotion rules for non-registry subsystems
- product-domain subsystem contracts

## Authority Boundaries

- the constitution and architecture doctrine remain higher authority than this contract
- this contract governs registry behavior and interpretation
- pipeline definitions remain the authoritative source for procedure, not the registry

## State Ownership Boundaries

- `docs/pipelines/registry/pipeline-registry.md` owns active-pipeline listing state
- pipeline definition files own pipeline procedure and identity
- generated artifacts may evidence usage, but do not own active-status truth

## Dependent Surfaces

- `AGENTS.md`
- `docs/governance/architecture-doctrine.md`
- `docs/governance/contract-discovery-ledger.md`
- active governance pipeline definition files
