# Negative-Path Test Matrix

| Case | Mutation method | Expected result | Restoration method |
| --- | --- | --- | --- |
| Positive control | none | normal authoritative output with snapshot provenance | none |
| Missing snapshot | temporarily move `governance-state-snapshot.json` out of place | fail closed with no normal output and no snapshot recreation | restore original snapshot file |
| Structurally invalid snapshot | replace snapshot with bounded invalid JSON structure missing required fields | fail closed with invalid snapshot error | restore original snapshot file |
| Canonical mismatch | mutate roadmap without regenerating snapshot | fail closed with snapshot mismatch error | restore original roadmap file |
| Already drifted snapshot | set `drift_detected` to `true` in snapshot | fail closed with drift-detected error | restore original snapshot file |
| Restoration control | restore canonical snapshot and canonical roadmap | normal authoritative output restored | not applicable |
