# Drift Detection Mechanism

Continuous matrix verification is now exposed through:

```bash
python tools/governance/template_scaffold.py verify-composition-matrix
```

The implementation is shared between:

- [composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py)
  - loads the matrix snapshot
  - compares snapshot, runtime supported pairs, explicit rejections, reasons, and contract drift state
- [template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_scaffold.py)
  - exposes the verifier as a governance CLI command

Success output:

```text
composition-matrix: OK
no drift detected
```

Any mismatch now returns a non-zero exit and structured drift errors.
