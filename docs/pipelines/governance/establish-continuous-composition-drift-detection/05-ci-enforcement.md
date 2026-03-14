# CI Enforcement

The repository now has a single governance command suitable for CI enforcement:

```bash
python tools/governance/template_scaffold.py verify-composition-matrix
```

This command checks:

- supported matrix parity
- explicit rejection parity
- canonical rejection reasons
- manifest compatibility parity
- contract drift status

CI integration is therefore reduced to invoking this command alongside the governance test suite. The command is deterministic and returns a non-zero exit on any detected drift.
