# Forbidden Pattern Definition

The scan enforces the portability invariant against these pattern families:

- `/home/`
- `/Users/`
- `C:\`
- `file://`
- `~/`

Pattern interpretation:

- matches inside live markdown link targets are portability violations
- matches inside literal rule examples or fenced scan-definition blocks may be
  classified as allowed exceptions
- matches inside preserved historical artifact bundles may be classified as
  historical evidence rather than active-surface violations
