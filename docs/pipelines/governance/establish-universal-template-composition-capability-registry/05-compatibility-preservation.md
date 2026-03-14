# Compatibility Preservation

The capability model is additive, not a replacement authority.

Pipeline `050` adds a preservation check that compares capability-derived decisions against the certified matrix for every admitted two-overlay combination. That preservation report now runs as part of manifest inventory validation and therefore feeds the existing continuous verifier:

```bash
python tools/governance/template_scaffold.py verify-composition-matrix
```

This means the capability layer cannot silently broaden or narrow the governed matrix without surfacing deterministic drift errors.
