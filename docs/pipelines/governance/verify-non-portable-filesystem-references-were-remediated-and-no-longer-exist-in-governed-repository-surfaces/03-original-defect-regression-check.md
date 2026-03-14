# Original Defect Regression Check

Original defect lineage:

- pipeline `107` recorded the state-machine canon restriction using a portable
  relative link in
  `docs/pipelines/governance/verify-codex-session-admission-and-activation-rules/08-final-verdict.md`
- pipeline `108` inventory recorded the pre-remediation machine-local form as
  `/home/.../docs/contracts/codex-session-state-machine-canon.md`
- pipeline `108` normalized that reference to
  `../../../contracts/codex-session-state-machine-canon.md`

Regression result:

- the original machine-local state-machine path does not appear as a live link
  in the active `107` verification bundle: `PASS`
- the active `107` lane definition no longer misstates the state-machine canon
  path under `docs/governance/`: `PASS`
- the corrected reference is portable because it is document-relative and
  repository-local: `PASS`
