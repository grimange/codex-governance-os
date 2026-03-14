# Verification Plan

Verification criteria:

1. the active repository scan remains clean
2. a controlled machine-local markdown link in a governed surface is detected
   as a violation
3. `python tools/governance/preflight.py` returns non-zero when that violation
   exists
4. removing the violation restores zero violations and a successful preflight
5. rule examples, scan definitions, and preserved evidence remain classified as
   non-violations

Verification method:

- run `python tools/governance/portability_scan.py scan-active --output json`
  in the live repository
- run `python tools/governance/preflight.py` in the live repository
- create a temporary governed fixture repo root with a controlled violation
- run the same commands against that temporary repo root
- remediate the temporary violation and rerun both commands
