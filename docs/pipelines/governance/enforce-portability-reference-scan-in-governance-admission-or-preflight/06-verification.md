# Verification

Verification checks run:

1. executed the portability scan logic against active governed surfaces
2. executed the governance preflight command and confirmed it delegates to the
   portability scan
3. verified that the scan returns success on the current repository state
4. verified through unit tests that a machine-local markdown link is
   classified as a blocking violation
5. verified through unit tests that literal rule examples are classified as
   allowed exceptions
6. verified through unit tests that the preflight command returns non-zero when
   a violation exists in the scanned repo root

Verification outcome:

- deterministic portability scan logic exists: `PASS`
- governance preflight entrypoint exists and runs the scan: `PASS`
- the current repository passes the active-surface scan without violations:
  `PASS`
- new machine-local live links are classified as blocking violations: `PASS`
- explicit exception classes prevent the expected false positives: `PASS`

Restriction note:

- the enforcement gate is established at the documented preflight entrypoint
  rather than through an always-on background admission system
