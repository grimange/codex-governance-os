# Boundary Diagnosis

The prior rejection of `service + monorepo` came from the lack of:

- a canonical nested service directory
- ownership boundaries between monorepo root and service subtree
- manifest metadata for nested service placement
- deterministic scaffold rules for generic services in a monorepo

The selected resolution is:

- monorepo owns repository root and shared root-level directories
- service owns `services/service-app/`
- governance surfaces stay at repository root
