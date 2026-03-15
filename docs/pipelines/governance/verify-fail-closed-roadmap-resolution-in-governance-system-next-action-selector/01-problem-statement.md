# Problem Statement

Pipeline 174 repaired the next-action selector so unresolved roadmap targets
should now fail closed instead of silently generating a valid-looking canonical
decision surface.

Pipeline 175 verifies that the repaired selector now behaves correctly on both
valid canonical state and invalid roadmap resolution scenarios.
