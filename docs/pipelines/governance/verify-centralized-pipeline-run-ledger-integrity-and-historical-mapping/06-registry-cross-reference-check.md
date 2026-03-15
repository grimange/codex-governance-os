# Registry Cross-Reference Check

Registry surface inspected:

- `docs/pipelines/registry/pipeline-registry.md`

Verified registry conditions:

- the registry header states that it is the canonical discoverability surface
  for active governance lanes: `VERIFIED`
- the registry header points to `docs/governance/pipeline-run-ledger.md` as the
  authoritative centralized execution-history surface: `VERIFIED`
- Pipeline `139` is registered with the canonical artifact bundle path:
  `VERIFIED`
- no registry text contradicts the ledger's current latest recorded run:
  `VERIFIED`

Supplemental repository check:

- `python tools/governance/preflight.py` returned `decision: PASS` and
  `violations: 0`

Overall registry cross-reference result:

- registry and ledger are aligned for current repository truth: `VERIFIED`
