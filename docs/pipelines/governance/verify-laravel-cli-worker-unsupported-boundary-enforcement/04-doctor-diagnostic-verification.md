# Doctor Diagnostic Verification

The doctor surface returns the exact explicit-boundary classification required by pipeline `041`.

Verified command:

```bash
python tools/governance/template_scaffold.py doctor-composition --overlays laravel cli-worker --output json
```

Verified diagnostic properties:

- explicit unsupported classification through `reason_code: explicitly-rejected`
- specific contract reason through `rejection_reason: missing Laravel worker composition contract`
- contract provenance through `decision_source: docs/contracts/universal-template-composition-contract.md`
- no fallback to generic reasons such as unknown incompatibility or absent manifest inventory
