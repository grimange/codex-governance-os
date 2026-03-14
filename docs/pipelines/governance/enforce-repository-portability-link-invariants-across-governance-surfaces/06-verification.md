# Verification

Verification checks run:

1. inspected `docs/governance/governance-safety-invariants-canon.md` for an
   explicit Repository Portability Link Invariant
2. inspected `docs/governance/architecture-doctrine.md`, `.codex/AGENTS.md`,
   and `README.md` for invariant discoverability
3. normalized the remaining machine-local links found in active canonical
   doctrine surfaces
4. ran deterministic scans across active canonical governance surfaces and
   active pipeline definitions, excluding literal pattern-definition examples
   in pipelines `108` and `109`
5. confirmed pipeline `108` remains consistent with the new invariant
6. confirmed pipeline `109` is registered with canonical definition and
   artifact bundle paths

Verification results:

- the Repository Portability Link Invariant exists in canonical doctrine:
  `PASS`
- the invariant is discoverable from architecture and agent entry surfaces:
  `PASS`
- active canonical doctrine and repository-entry surfaces do not retain
  machine-local live links after this lane's alignment: `PASS`
- active pipeline definitions outside the literal pattern-definition examples in
  pipelines `108` and `109` do not retain forbidden machine-local link forms:
  `PASS`
- pipeline `108` remediation remains valid under the new invariant: `PASS`
- pipeline `109` is registered canonically: `PASS`

Restrictions:

- historical pipeline artifact bundles still contain machine-local links as
  preserved evidence of earlier defects
- this lane establishes the rule and scan model, not an automated blocking
  mechanism
