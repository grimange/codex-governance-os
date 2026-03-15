# Verification Scope

Verification criteria restated from Pipeline `137`:

- Evidence surface presence: `134`, `135`, and `136` must each expose canonical
  governance pipeline definitions and final verdict artifacts.
- Artifact consistency: the executed artifact bundles used in the continuity
  chain must include final verdict files.
- Registry alignment: the canonical pipeline registry must include the executed
  pipelines required by the reconstruction scenario.
- Deterministic session reconstruction: the repository must support a bounded
  reconstruction chain `134 -> 135 -> 136` using registry order, artifact
  bundles, and final verdict artifacts only.
- Governance tool compatibility: repository governance verification tooling must
  be checked against actual repository surfaces rather than assumed tool names.

Classification model used in this lane:

- `VERIFIED`: criterion satisfied directly from repository evidence
- `VERIFIED_WITH_RESTRICTIONS`: criterion satisfied, but the lane body contains
  wording drift relative to repository truth
- `FAILED`: criterion contradicted by repository evidence
- `UNVERIFIABLE`: criterion names a surface not present in the repository
