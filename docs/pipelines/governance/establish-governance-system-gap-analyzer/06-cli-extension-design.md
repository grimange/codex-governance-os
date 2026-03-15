# CLI Extension Design

Pipeline 166 extends the governance inspection CLI with:

```bash
python tools/governance/inspect_governance_state.py gaps
```

CLI behavior:

1. Reuse state inspection and maturity derivation logic.
2. Fail closed to `BLOCKED_BY_DRIFT` when canonical state alignment fails.
3. Convert non-verified maturity domain classifications into explicit gap
   records.
4. Emit `docs/governance/governance-system-gaps.json`.

The CLI does not invent capabilities or normalize invalid domains.
