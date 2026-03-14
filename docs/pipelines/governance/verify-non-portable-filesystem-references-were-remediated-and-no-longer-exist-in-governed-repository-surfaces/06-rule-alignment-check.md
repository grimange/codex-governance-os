# Rule Alignment Check

Repository Portability Link Invariant alignment:

- the invariant exists in `docs/governance/governance-safety-invariants-canon.md`: `PASS`
- `docs/governance/architecture-doctrine.md` routes canonical reference behavior through that invariant: `PASS`
- `.codex/AGENTS.md` instructs operators to treat machine-local live links as portability violations: `PASS`
- `README.md` exposes the portability rule at the repository entry surface: `PASS`
- pipeline `108` remediation remains consistent with the invariant's allowance
  for historical evidence and literal examples: `PASS`

Residual interpretive boundary:

- this repository now has a doctrine-level and verification-level invariant,
  but it still does not claim an automated admission gate or lint blocker for
  new violations
