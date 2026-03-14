# Problem Statement

Pipelines `098` through `101` established continuity enforcement, schema
normalization, and registry discipline for governed Codex sessions, but they
left lifecycle state semantics distributed across multiple Layer 6 surfaces.

The repository had:

- session orchestration doctrine
- session identity and event-recording surfaces
- handoff continuity rules
- normalized field and registry path discipline

The repository did not yet have one canonical state machine defining the
authoritative lifecycle states, allowed transitions, invalid transitions, and
the distinction between handoff completion and resumption. Pipeline `102`
establishes that canon and aligns the active Layer 6 surfaces to it.
