# Problem Statement

Pipeline `130` established the multi-session continuity verification model and
Pipeline `131` verified that it preserves strict session boundaries.

What remained implicit was the evidence harness used to evaluate continuity
claims across those independently verified sessions.

Pipeline `132` closes that gap by establishing one doctrine-level evidence
harness that:

- bounds admissible cross-session evidence types
- requires a minimum explicit continuity threshold
- preserves strict `session_id` isolation
- prevents implicit cross-session inference
- keeps multi-session continuity separate from single-session reconstruction
