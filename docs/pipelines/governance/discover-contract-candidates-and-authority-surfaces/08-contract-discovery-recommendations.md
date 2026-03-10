# Contract Discovery Recommendations

## Recommended Roadmap

1. Author the `Pipeline Registry Integrity Contract` first.
   Reason: it closes an active governance gap with immediate audit and routing value.

2. Author the `Contract Root Stewardship Contract` next.
   Reason: it prevents `docs/contracts/` from becoming an ad hoc dumping ground before substantive contracts exist.

3. Author the `Pipeline Artifact Interpretation Contract`.
   Reason: the repository already depends heavily on generated artifacts, and their authority limits should be explicit.

4. Verify whether the `Governance Authority Contract` and architecture doctrine are already sufficient as canonical surfaces.
   Reason: they may need normalization rather than replacement.

5. Defer product-domain subsystem contracts until real implementation surfaces appear.
   Reason: no repository evidence supports API, event, persistence, or runtime subsystem contracts yet.

## Document Actions

- promote `docs/governance/architecture-doctrine.md` as the primary supporting authority for contract work
- keep `AGENTS.md` and `.codex/AGENTS.md` as governance-supporting surfaces rather than moving contract content into them
- do not author speculative contracts for backend, frontend, or runtime layers
- consider normalizing status labels in active pipeline definitions so descriptive text matches operational state

## Instability Notes

- The lifecycle progression contract remains somewhat unstable until remediation, verification, and promotion pipelines become active.
- Contract authoring should stay bounded to governance-surface needs until the repository contains more than governance documents.
