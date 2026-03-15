# CLI Execution Results

## Clean Execution 1

Command:

```bash
python tools/governance/inspect_governance_state.py
```

Observed result:

- regenerated `docs/governance/governance-system-state.json`
- reported `No governance artifact inconsistencies detected.`

## Clean Execution 2

Command:

```bash
python tools/governance/inspect_governance_state.py
```

Observed result:

- regenerated `docs/governance/governance-system-state.json`
- reported `No governance artifact inconsistencies detected.`

## Post-Restore Execution

Command:

```bash
python tools/governance/inspect_governance_state.py
```

Observed result:

- regenerated `docs/governance/governance-system-state.json`
- reported `No governance artifact inconsistencies detected.`
