# Remediation Design

Pipeline 178 adds two hardening layers:

## Target Consensus Enforcement

Added:

- `validate_governance_target_consensus()`

This function requires the roadmap target to match:

- the first remediation entry
- the first blocker
- the gap and maturity classification for that domain

Violation result:

- `GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION`

## Ambiguous Candidate Detection

Added:

- `detect_ambiguous_governance_surface_candidates()`

This function rejects alternate-named candidates using suffix patterns such as:

- `-copy`
- `-backup`
- `-old`
- `-temp`
- `-draft`

Violation result:

- `AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED`
