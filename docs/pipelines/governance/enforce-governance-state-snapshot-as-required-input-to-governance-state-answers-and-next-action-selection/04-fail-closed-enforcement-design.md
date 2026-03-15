# Fail-Closed Enforcement Design

Pipeline 182 adds explicit fail-closed enforcement for the next-action selector.

Blocked conditions:

- snapshot file missing
- snapshot manifest structurally invalid
- snapshot hashes no longer match canonical governance surfaces
- snapshot manifest already records `drift_detected: true`
- canonical governance surface authority checks fail for roadmap, gaps,
  remediation plan, maturity surface, or state surface

Current machine-readable failure family:

- `MISSING_CANONICAL_GOVERNANCE_SURFACE`
- `INVALID_GOVERNANCE_STATE_SNAPSHOT`
- `GOVERNANCE_STATE_SNAPSHOT_MISMATCH`
- `GOVERNANCE_STATE_SNAPSHOT_DRIFT_DETECTED`
- existing canonical input authority and consensus violations

Normal authoritative selector output is emitted only when snapshot enforcement
passes.
