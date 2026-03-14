# Problem Statement

Layer 6 session governance already defines the evidence surfaces and
interpretation precedence required for governed session truth.

What remained implicit was the deterministic operational method for
reconstructing one bounded session narrative from those surfaces.

Pipeline `121` closes that gap by establishing one reconstruction procedure
that:

- anchors on `session_id`
- collects durable ledger evidence
- applies lifecycle-observation normalization only where admissible
- interprets lifecycle meaning through the state-machine canon
- admits runtime context only through bounded runtime-boundary rules
- fails closed when evidence is partial, conflicting, or insufficient
