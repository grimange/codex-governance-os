# Registry Verification

Inspected surface:

- [pipeline-registry.md](/home/ramjf/python-projects/codex-governance-os/docs/pipelines/registry/pipeline-registry.md)

Verification findings:

- pipeline `104` is present in the active registry: `PASS`
- pipeline `104` title matches the active pipeline definition: `PASS`
- pipeline `104` records the canonical pipeline definition path: `PASS`
- pipeline `104` records the canonical artifact-bundle path: `PASS`
- pipeline `105` is now registered for active-lane discoverability: `PASS`

Restrictions:

- the current canonical pipeline registry does not record a `registry id`
  column, so the `105` lane’s requested registry-id check is not directly
  verifiable from the registry surface alone: `RESTRICTED`
- the current canonical pipeline registry does not record a `classification`
  column, so the `105` lane’s requested classification check is not directly
  verifiable from the registry surface alone: `RESTRICTED`
