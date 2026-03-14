# Remediation And Retest

Controlled remediation:

- removed the temporary violating markdown link from the fixture
- replaced the file content with non-violating governed text

Retest result:

- `python tools/governance/portability_scan.py scan-active --repo-root <tmp> --output json`
  returned zero violations
- `python tools/governance/preflight.py --repo-root <tmp>` returned `PASS`

Exit-code evidence:

- `PREFLIGHT_AFTER_REMEDIATION_EXIT=0`

This confirms that the enforcement gate is reversible through actual
remediation rather than requiring manual override.
