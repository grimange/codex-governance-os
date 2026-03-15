# Problem Statement

Pipeline 161 established canonical governance system state surfaces, but those
surfaces are still manually maintained.

Manual maintenance leaves governance state exposed to drift between repository
truth, capability tracking, and machine-readable introspection outputs.

Pipeline 162 implements a self-inspection engine so the repository can derive
its governance system state automatically from canonical evidence surfaces.
