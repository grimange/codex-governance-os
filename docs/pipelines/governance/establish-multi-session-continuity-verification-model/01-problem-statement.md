# Problem Statement

Pipelines `124` through `129` established and verified the single-session
reconstruction verification stack.

What remained implicit was how continuity relationships between independently
verified sessions should be evaluated without collapsing their boundaries.

Pipeline `130` closes that gap by establishing one doctrine-level
multi-session continuity model that:

- preserves strict per-session `session_id` boundaries
- requires explicit cross-session continuity evidence
- evaluates continuity through bounded relationship dimensions
- preserves restrictions when continuity evidence is incomplete
- remains distinct from the single-session verification stack
