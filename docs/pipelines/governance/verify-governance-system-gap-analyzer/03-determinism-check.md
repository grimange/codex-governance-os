# Determinism Check

Pipeline 167 executed the `gaps` CLI twice on unchanged repository state and
recorded the JSON hash after each run.

Observed hash after run 1:

- `defaee0474b06f929de5e8481ea1365f6a685c792adbc208fa4dd95690e8c525`

Observed hash after run 2:

- `defaee0474b06f929de5e8481ea1365f6a685c792adbc208fa4dd95690e8c525`

Result:

- repeated execution produced identical output
- deterministic regeneration of `docs/governance/governance-system-gaps.json`
  is verified
