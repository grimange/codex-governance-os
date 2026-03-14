# Problem Statement

Layer 6 session governance already defines where governed session evidence
exists:

- the session state machine
- the session registry
- the session ledger
- lifecycle-observation normalization
- the runtime-boundary evidence model

What remained implicit was how those surfaces must be interpreted together when
reconstructing governed session truth.

Pipeline `118` closes that gap by establishing one Layer 6 session-evidence
interpretation model that preserves distinct authority boundaries and prevents
registry metadata, ledger history, lifecycle observations, or runtime context
from being misread as competing lifecycle truth.
