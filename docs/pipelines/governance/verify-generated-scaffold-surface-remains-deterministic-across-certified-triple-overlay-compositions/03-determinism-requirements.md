# Determinism Requirements

Each certified triplet must be deterministic across repeated realization for:

- file presence
- directory structure
- file names
- file content
- scaffold selection payload content

No run-specific variance is allowed because scaffold generation is a governance
surface, not a best-effort convenience feature.
