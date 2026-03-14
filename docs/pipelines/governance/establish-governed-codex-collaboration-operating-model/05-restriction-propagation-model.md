# Restriction Propagation Model

The established Layer 5 model makes restriction propagation explicit.

Recorded rules:

- any role that identifies a restriction must propagate it downstream
- downstream roles must preserve the restriction rather than reinterpret it
- final verdicts must include relevant restrictions explicitly
- later summaries must not silently erase unsupported, ambiguous, or
  stale-sensitive boundaries

This preserves the fail-closed behavior required by Layers 0 through 3 and
keeps the Layer 4 role model from being interpreted as a license to smooth over
restrictions during handoffs.
