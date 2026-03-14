# Weak Continuity Scenario

`scenario_id`: `continuity.weak.partial-artifact-link`

Participating sessions:

- `session_gamma`
- `session_delta`

Admissible evidence:

- one governed artifact continuation reference from `session_delta` back to an
  output of `session_gamma`

Expected classification:

- `WEAK_CONTINUITY`

Boundary validation:

- at least one admissible cross-session link is present
- evidence is insufficient for full continuity verification strength
- strict per-session `session_id` isolation remains intact

Prohibited reasoning patterns:

- treating a single weak link as equivalent to a full predecessor-successor
  chain
- filling the remaining evidence gap through narrative assumption
