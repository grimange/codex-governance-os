# Handoff Discipline

Layer 6 requires an explicit handoff record whenever responsibility moves
between sessions.

Required handoff content:

1. current objective
2. completed work
3. remaining tasks
4. active constraints and restrictions
5. expected outputs

Handoff rules established:

- handoffs must be inspectable rather than implied
- lower-layer restrictions must survive the handoff unchanged
- downstream sessions may continue scoped work but may not reinterpret their
  authority more broadly than what was handed off
- undocumented session forks are prohibited

This discipline strengthens continuity without changing the Layer 5
collaboration meaning already established.
