# Evidence And Authority Analysis

## Evidence

- `AGENTS.md` states that pipeline registration is mandatory for active pipelines.
- `docs/pipelines/registry/pipeline-registry.md` exists as the canonical registry surface.
- the governance readiness audit found that active pipeline `002` was missing from the registry.
- contract discovery identified registry integrity as the highest-priority missing contract.

## Current Authority Status

- the registry is a likely authority candidate for pipeline activation discoverability
- without an explicit contract, registry completeness rules are implied rather than fully codified
- higher authority for meaning still comes from the constitution and doctrine

## Observed Drift

- active pipelines `002`, `003`, and now `004` are present in repository practice but absent from the registry
- some pipeline definitions still carry descriptive `PROPOSED` labels while being used operationally

## Why A Canonical Contract Is Justified Now

- the subsystem already exists as an operational governance surface
- the risk is concrete and already observed in prior audit work
- the contract can be tightly scoped and verified from repository state
