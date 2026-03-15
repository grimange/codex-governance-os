# CLI Extension Design

Pipeline 170 extends the governance inspection CLI with:

```bash
python tools/governance/inspect_governance_state.py advancement-roadmap
```

CLI behavior:

1. Load canonical maturity, gap, and remediation-plan surfaces.
2. Derive the current maturity snapshot.
3. Group remediation entries into ordered advancement stages.
4. Emit `docs/governance/governance-system-advancement-roadmap.json`.

The CLI remains deterministic and evidence-scoped.
