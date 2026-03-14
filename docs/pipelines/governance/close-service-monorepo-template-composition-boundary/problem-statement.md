# Problem Statement

After `django + monorepo` was closed, the remaining structurally plausible unsupported boundary was `service + monorepo`.

The missing piece was not policy ambiguity but deterministic nested placement for a generic service inside a monorepo.

Pipeline `036` closes that gap by defining a canonical service placement model and aligning the full composition subsystem around it.
