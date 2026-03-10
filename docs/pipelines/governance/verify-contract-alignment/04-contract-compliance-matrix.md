# Contract Compliance Matrix

| Contract Rule | Status | Evidence | Notes |
|---------------|--------|----------|-------|
| every active pipeline appears exactly once in the registry | verified compliant | registry lists active pipelines `000` through `007`, including current pipeline `007` | no duplicate entries observed |
| each registry entry includes ID, name, status, category, and path | verified compliant | registry table columns and row data are complete | interface shape is correct |
| registry entries point to real pipeline definition files | verified compliant | every referenced path resolves to an existing file | no stale rows found |
| registry ID matches definition ID or filename | verified compliant | row IDs align with filenames `000` through `007` | identifier integrity holds |
| registry records discoverability only and does not redefine procedure | verified compliant | registry rows contain summary metadata only | authority boundary intact |
| `PROPOSED` text does not excuse omission once active | verified compliant | active pipeline `007` is registered despite its definition still saying `PROPOSED` | contract rule is satisfied |
| placeholder category directories are not registered as active pipelines | verified compliant | all rows reference concrete pipeline definition files | no placeholder misuse found |
| registry updates occur no later than the same governed change set as activation | verified compliant | current verification change set registers `007` while executing it | current active transition is published |
| audits can determine active governance coverage from the registry | verified compliant | current active governance sequence is visible directly from registry state | no contextual reconstruction required |
| duplicate entries are prohibited | verified compliant | one row per active pipeline ID | no duplication found |
