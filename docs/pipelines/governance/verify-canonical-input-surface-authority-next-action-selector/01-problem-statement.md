# Problem Statement

Pipeline 176 hardened the next-action selector with canonical input authority
checks for missing surfaces, shadow surfaces, and cross-surface consistency.

Pipeline 177 verifies whether that enforcement is complete enough to reject all
authority-violating scenarios while preserving deterministic valid-state
behavior.
