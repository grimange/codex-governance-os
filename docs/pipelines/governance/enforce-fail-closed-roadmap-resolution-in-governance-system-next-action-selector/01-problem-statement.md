# Problem Statement

Pipeline 173 proved that the next-action selector was deterministic on canonical
state but unsafe on invalid roadmap input.

When `recommended_next_target` was corrupted, the selector still regenerated a
canonical next-action surface and exited successfully. Pipeline 174 repairs that
control-plane defect by enforcing fail-closed roadmap resolution.
