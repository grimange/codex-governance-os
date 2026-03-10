# Contract Compliance Matrix

| Contract Rule | Implementation Surface | Status | Evidence | Notes |
|---------------|------------------------|--------|----------|-------|
| active pipelines must appear exactly once in the registry | `docs/pipelines/registry/pipeline-registry.md`, `docs/pipelines/governance/005--audit-implementation-against-canonical-contract.md` | non-compliant | registry lists `000` through `004`; current work is executing `005` | active `005` is absent |
| each registry entry must include ID, name, status, category, and path | `docs/pipelines/registry/pipeline-registry.md` | compliant | registry table exposes all required columns | interface shape is correct |
| registry entries must point to real pipeline definition files | `docs/pipelines/registry/pipeline-registry.md`, registered pipeline files | compliant | `000` through `004` resolve to existing definitions | no stale references found |
| registry ID must match definition ID or filename | registry rows `000` through `004` and corresponding files | compliant | row IDs align with filenames | no mismatch detected |
| registry records discoverability only and must not redefine procedure | doctrine, contract, registry | compliant | registry contains summary metadata only | no procedural override behavior found |
| `PROPOSED` or draft text does not excuse omission once active | contract, active definition `005` | non-compliant | `005` definition says `PROPOSED` and is still operationally active during this run | contract rule is explicit |
| placeholder category directories must not be registered as active pipelines | registry and `docs/pipelines/` tree | compliant | registry contains concrete pipeline files only | no placeholder misregistration found |
| registry updates must occur in the same governed change set as activation | current execution context and registry contents | non-compliant | `005` is active now without registry update in the same change set | timing discipline failed |
| audits should be able to determine active coverage from the registry | registry plus prior audit artifacts | partially compliant | registry exposes active `000` through `004`, but `005` requires contextual inference | discoverability is incomplete, not collapsed |
| duplicate entries for one active pipeline are prohibited | registry | compliant | no duplicate IDs or paths found | no duplicate-entry defect present |
