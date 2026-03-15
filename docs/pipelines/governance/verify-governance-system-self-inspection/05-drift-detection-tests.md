# Drift Detection Tests

## Injected Drift Scenario

Temporary mismatch introduced:

- changed `Architecture Advisor` status in
  `docs/governance/governance-capability-registry.md`
  from `planned` to `in progress`

Reason:

- create a bounded mismatch against
  `docs/governance/governance-capability-progress.md`

## CLI Result

Observed output:

```text
Regenerated docs/governance/governance-system-state.json
Detected governance artifact inconsistencies:
- Capability status mismatch for 'Architecture Advisor': registry=in_progress, progress=planned
```

Observed behavior:

- CLI exited non-zero
- mismatch was reported explicitly
- no silent masking of drift occurred

## Restoration

- canonical registry state was restored immediately after the test
- the CLI was run again successfully to restore canonical JSON output
