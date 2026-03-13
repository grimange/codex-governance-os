# Template Taxonomy

## Supported Template Classes

- `pipeline`
- `verification`
- `rule`
- `skill`
- `sub_agent`
- `instruction`
- `report`
- `evidence-pack`
- `decision`
- `remediation`

## Classification Sources

The linter now classifies templates from:

- explicit canonical `category` values when present
- `pipeline_id` presence for pipeline templates
- filename hints such as `pipeline`, `rule`, `skill`, `sub-agent`, `report`, and `instruction`
- required-section signatures as a fallback when the file shape is unambiguous

When classification remains uncertain, the linter blocks instead of guessing.
