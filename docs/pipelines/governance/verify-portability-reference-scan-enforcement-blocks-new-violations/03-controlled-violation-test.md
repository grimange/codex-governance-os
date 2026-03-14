# Controlled Violation Test

Controlled fixture design:

- temporary repo root with governed-surface paths under `docs/governance/`
- temporary violating file:
  `docs/governance/controlled-violation.md`
- violating content:
  `[bad](/home/example-user/project/file.md)`

Detection result:

- `tools/governance/portability_scan.py scan-active --repo-root <tmp> --output json`
  reported one `POSIX_HOME` violation in
  `docs/governance/controlled-violation.md`
- the match was classified as `violation`, not as an allowed exception

Exit-code evidence:

- `SCAN_WITH_VIOLATION_EXIT=1`
