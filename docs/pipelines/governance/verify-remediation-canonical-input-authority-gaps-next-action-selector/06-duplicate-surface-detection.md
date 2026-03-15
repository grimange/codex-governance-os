# Duplicate Surface Detection

Injected candidates:

- `governance-system-advancement-roadmap-copy.json`
- `governance-system-advancement-roadmap-backup.json`
- `governance-system-advancement-roadmap-old.json`
- `governance-system-advancement-roadmap-draft.json`

Expected behavior:

- selector exits non-zero
- selector emits `AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED`
- selector does not rewrite canonical output

Observed behavior:

- selector exited `1`
- selector emitted the expected machine-readable error
- canonical next-action output hash remained unchanged

Result:

- alternate-named duplicate candidate detection is now verified
