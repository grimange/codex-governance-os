# CLI Surface

Pipeline 162 exposes the governance self-inspection command:

```bash
python tools/governance/inspect_governance_state.py
```

Expected CLI behavior:

- scans the canonical governance introspection and capability surfaces
- regenerates `docs/governance/governance-system-state.json`
- reports governance artifact inconsistencies when detected
- exits non-zero when drift is found

This CLI does not change governance capability definitions or maturity scoring
models.
