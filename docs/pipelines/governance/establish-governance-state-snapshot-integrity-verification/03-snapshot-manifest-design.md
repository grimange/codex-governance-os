# Snapshot Manifest Design

Pipeline 180 introduces a deterministic machine-readable manifest with these
fields:

- `generated_by`
- `snapshot_version`
- `snapshot_id`
- `previous_snapshot_id`
- `drift_detected`
- `surfaces`

`snapshot_id` is derived by concatenating the ordered canonical surface hashes
with newline separators and hashing that canonical string with SHA256.

Initial canonical snapshot:

- `snapshot_id`: `6f7f70632592360b7e35c29590f71782944138010b51dd1ef4b3e9654852dc80`
