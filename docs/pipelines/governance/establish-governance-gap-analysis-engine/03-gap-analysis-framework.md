# Gap Analysis Framework

Pipeline 153 uses the following framework for capability diagnosis:

1. Identify a governance capability area that materially influences maturity.
2. Anchor the capability to canonical repository evidence.
3. Classify the capability using one normalized coverage state.
4. Record a maturity blocker only when the capability gap materially limits
   higher maturity classification.
5. Preserve diagnostic boundaries by excluding speculative future features.

Interpretation rules:

- `fully implemented`
  - canonical surfaces and governed operating rules are already established
- `partially implemented`
  - meaningful capability exists, but major parts remain absent
- `emerging capability`
  - bounded scaffolding exists, but operating capability is incomplete
- `not implemented`
  - no canonical repository evidence establishes the capability as current truth
- `intentionally out of scope`
  - the capability is deliberately excluded by governance design
