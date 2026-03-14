# Enforcement Design

The repository now treats machine-local filesystem links as portability
violations when they appear as live references in active governed surfaces.

Enforcement posture established by this lane:

1. canonical doctrine defines the invariant and the forbidden pattern families
2. architecture and agent entry surfaces route future operators to that
   invariant
3. deterministic scans can verify active canonical surfaces by searching for
   forbidden patterns while excluding historical artifact bundles and literal
   pattern-definition examples
4. future verification lanes may use the invariant as a conformance target
5. future admission or lint gates may block new portability violations, but
   this lane does not claim that automated blocking already exists

Boundaries:

- this lane establishes the rule and discoverability model
- this lane does not claim repository-wide historical cleanup
- this lane does not introduce runtime path rewriting or automatic admission
  enforcement
