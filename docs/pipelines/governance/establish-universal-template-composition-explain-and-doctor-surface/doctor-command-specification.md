# Doctor Command Specification

## Command

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays <overlay...> --output json
```

## Behavior

- normalizes the requested overlay set
- validates the composition through the canonical contract module
- prints structured diagnostics
- exits `0` when supported and `1` when unsupported

## Integration

- scaffold rejection messages now reference the exact doctor command to rerun
- manifest inventory drift messages reference the doctor surface for the rejected pair
- template listing inherits the same diagnostics because it reuses manifest inspection validation
