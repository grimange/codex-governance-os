# Compatibility Notes

## Preserved

- lane IDs `000` through `010`
- lane titles used by the pipeline registry
- original lane stage intent such as bootstrap, discovery, audit, remediation, verification, foundation, and normalization
- existing artifact bundle roots under `docs/pipelines/governance/<lane-slug>/`

## Normalized

- governed frontmatter was added to every migrated lane
- canonical universal pipeline sections were added uniformly
- restrictions, non-claims, and verification methods are now explicit in every core lane
- skill references are recorded in the normalized execution model where applicable

## Residual Notes

- the migration intentionally compresses older phase-heavy prose into a stable top-level lane contract
- historical artifact directories remain the durable evidence for prior execution detail
- no lane was marked restricted during this migration because each targeted lane could be normalized without unresolved structural ambiguity
