# CLI Extension Design

Pipeline 172 extends the governance inspection CLI with:

```bash
python tools/governance/inspect_governance_state.py next-action
```

CLI behavior:

1. Load the advancement roadmap.
2. Load the remediation plan.
3. Resolve the highest-priority roadmap target against remediation truth.
4. Emit `docs/governance/governance-system-next-action.json`.

The selector fails closed if roadmap or remediation inputs are inconsistent.
