# Governance Tool Compatibility

## Executed Tool Checks

Command executed:

```text
python tools/governance/continuity_harness.py --run-scenarios --output json
```

Observed result:

- `decision: PASS`
- `scenario_count: 4`
- all scenarios matched their expected classifications or failure classes

Scenario outcomes:

- verified continuity scenario: `VALID_CONTINUITY_CHAIN`
- weak continuity scenario: `INCOMPLETE_SESSION_RECONSTRUCTION`
- no continuity scenario: `MISSING_BRIDGE_EVIDENCE`
- boundary violation scenario: `SESSION_ISOLATION_VIOLATION`

Command executed:

```text
python tools/governance/preflight.py
```

Observed result:

- `decision: PASS`
- `violations: 0`

## Compatibility Finding

Pipeline `137` names both of the following governance tools:

- `tools/governance/preflight.py`
- `tools/governance/gov.py`

Repository truth differs from the lane body:

- `tools/governance/preflight.py` exists and executes successfully
- `tools/governance/gov.py` does not exist in the repository
- repository evidence already records that this repository does not currently
  expose a single `gov.py`-style governance entry surface

Classification:

- preflight compatibility: `VERIFIED`
- `gov.py` compatibility expectation: `UNVERIFIABLE`
- overall tooling criterion: `VERIFIED_WITH_RESTRICTIONS`

The restriction reflects lane-definition drift relative to repository truth, not
a defect in the continuity harness implementation.
