# Scan Detection Results

Live repository result:

- `python tools/governance/portability_scan.py scan-active --output json`
  returned zero violations and only allowed exceptions

Controlled-violation result:

- the temporary governed fixture produced one violation:
  `docs/governance/controlled-violation.md:1:7 [POSIX_HOME] [bad](/home/example-user/project/file.md)`
- the scan output included the offending file, line, column, pattern, and
  excerpt

Remediated-fixture result:

- after replacing the violating content with `# Clean doctrine`, rerunning the
  same scan returned zero violations
- `SCAN_AFTER_REMEDIATION_EXIT=0`
