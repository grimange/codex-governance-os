# Defect Summary

Verified defect from Pipeline 173:

- an invalid roadmap `recommended_next_target` did not cause selector failure
- the selector exited `0`
- the selector regenerated `docs/governance/governance-system-next-action.json`

Root cause:

- the selector recomputed roadmap truth instead of resolving against the
  canonical roadmap surface under verification

Risk:

- misleading canonical next-action output could be emitted from invalid roadmap
  state
