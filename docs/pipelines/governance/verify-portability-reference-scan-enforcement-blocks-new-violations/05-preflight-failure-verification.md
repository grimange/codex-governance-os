# Preflight Failure Verification

Live repository result:

- `python tools/governance/preflight.py` returned `PASS`

Controlled-violation result:

- `python tools/governance/preflight.py --repo-root <tmp>` returned
  `BLOCKED`
- the output reported the portability-reference check and the offending file:
  `docs/governance/controlled-violation.md:1:7 [POSIX_HOME]`

Exit-code evidence:

- `PREFLIGHT_WITH_VIOLATION_EXIT=1`

This demonstrates that the canonical preflight entrypoint fails closed when a
new machine-local live link enters the governed scan scope.
