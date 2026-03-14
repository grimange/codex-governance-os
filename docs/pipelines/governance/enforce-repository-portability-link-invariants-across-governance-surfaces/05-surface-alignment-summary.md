# Surface Alignment Summary

Aligned surfaces:

- `docs/governance/governance-safety-invariants-canon.md` now defines the
  Repository Portability Link Invariant and its historical-evidence boundary
- `docs/governance/architecture-doctrine.md` now routes canonical-reference
  behavior through that invariant
- `.codex/AGENTS.md` now instructs operators to treat machine-local live links
  as portability violations
- `README.md` now exposes the portability invariant at the repository entry
  surface
- `docs/governance/compound-composition-certification-ledger.md` and
  `docs/governance/template-scaffold-contract.md` were normalized to remove the
  remaining machine-local links from canonical governance doctrine
- `docs/pipelines/registry/pipeline-registry.md` now registers pipeline `109`

Pipeline `108` remains valid under this rule because its scoped remediation used
portable relative links and preserved historical restriction evidence instead of
rewriting it away.
