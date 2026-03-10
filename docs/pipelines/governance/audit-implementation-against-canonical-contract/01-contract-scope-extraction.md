# Contract Scope Extraction

## Subsystem Scope

The contract governs:

- `docs/pipelines/registry/pipeline-registry.md`
- active pipeline definitions under `docs/pipelines/`
- the relationship between registry state and pipeline activation
- governance work that depends on accurate active-pipeline discoverability

## Audit Criteria Derived From Contract

| Contract Area | Audit Criterion |
|---------------|-----------------|
| lifecycle rules | registry updates must occur no later than the same governed change set that activates a pipeline for operational use |
| authority model | the registry owns activation/discoverability state only and must not redefine substantive pipeline procedure |
| source-of-truth rules | version-controlled pipeline definitions and higher authorities remain primary; registry entries must resolve to real files and consistent IDs |
| state ownership | active-pipeline listing state belongs to `docs/pipelines/registry/pipeline-registry.md`; pipeline definitions own procedure |
| command semantics | governance work must register active pipelines; omission of an active pipeline is prohibited behavior |
| event semantics | activation creates an observable requirement for registry representation; registry silence is non-compliance, not neutrality |
| interface rules | each entry must include pipeline ID, name, status, category, and canonical path; path and ID must match the referenced definition |
| compatibility boundaries | placeholder directories are not active pipelines; `PROPOSED` text does not excuse omission once a pipeline is operationally active |

## Specific Rules To Test

1. Every active pipeline appears exactly once in the registry.
2. Every registry entry points to an existing pipeline definition.
3. Registered IDs match pipeline filenames.
4. Registry content does not treat placeholders or non-operative surfaces as active pipelines.
5. Registry state is used for discoverability only and does not override higher-order authorities.
6. Operational use of a pipeline triggers the registration obligation even if the pipeline body still says `PROPOSED`.
