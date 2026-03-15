# Problem Statement

Pipelines 176 through 179 hardened canonical input authority for the governance
next-action selector, but selector decisions still lacked an immutable snapshot
identifier for the exact governance-state surfaces used at decision time.

Without a deterministic snapshot manifest, the system cannot prove that two
selector runs evaluated the same canonical governance state or distinguish clean
re-execution from cross-surface drift.
