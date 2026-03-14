# Generation Exercise Plan

Generation coverage was added in [test_scheduler_scaffold_generation_matrix.py](/home/ramjf/python-projects/codex-governance-os/tests/governance/test_scheduler_scaffold_generation_matrix.py).

The suite verifies:

- scheduler-only generation
- every currently certified scheduler pair and triple generation path
- coexistence preservation for scheduler plus worker and topology surfaces
- explicit failure for representative unsupported scheduler combinations

The harness is matrix-shaped rather than bespoke so future certified scheduler compositions can be added by extending the case table.
