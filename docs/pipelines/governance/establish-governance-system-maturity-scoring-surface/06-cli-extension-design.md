# CLI Extension Design

Pipeline 164 extends the existing self-inspection CLI with:

```bash
python tools/governance/inspect_governance_state.py maturity
```

CLI behavior:

1. Reuse the governance state inspection logic.
2. Fail closed if state inspection detects inconsistencies.
3. Compute maturity domains from the capability registry and deterministic
   domain mapping.
4. Regenerate `docs/governance/governance-system-maturity.json`.

This extension does not change maturity scoring models outside the new
system-level maturity surface.
