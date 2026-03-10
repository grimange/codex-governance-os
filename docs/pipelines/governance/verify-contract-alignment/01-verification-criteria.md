# Verification Criteria

| Contract Rule | Verification Evidence |
|---------------|-----------------------|
| every active pipeline has exactly one registry entry | inspect `docs/pipelines/registry/pipeline-registry.md` against currently operational pipelines `000` through `007` evidenced by repository use |
| each registry entry includes ID, name, status, category, and path | inspect registry table columns and row structure |
| registry entries point to real files | confirm referenced pipeline definitions exist under `docs/pipelines/governance/` |
| registry IDs match filename-implied IDs | compare each registry row to the referenced filename and header ID |
| registry records discoverability only | inspect registry content for summary metadata rather than procedural duplication |
| placeholder roots are not treated as active pipelines | inspect registry rows for concrete file references only |
| active use does not rely on `PROPOSED` text as an excuse for omission | confirm active current pipeline `007` is represented despite `PROPOSED` text in its definition |
| audits can determine active governance coverage from the registry | verify that the current governed workflow sequence is discoverable directly from registry state |

## Verification Scope Note

This verification treats currently executed pipeline `007` as operationally active under the contract's ambiguity-handling rules and therefore verifies it as part of the active set.
