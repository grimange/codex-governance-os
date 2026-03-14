# Authority Precedence Model

Pipeline `118` establishes the following Layer 6 session-evidence
interpretation precedence:

1. state-machine authority for lifecycle semantics
2. ledger evidence for durable event history
3. registry evidence for session identity and current indexed summary state
4. lifecycle-observation normalization
5. runtime-boundary supporting context

This precedence is subordinate to repository-wide authority ordering and the
global governance evidence-interpretation canon.

The resulting model prevents:

- ledger events from redefining lifecycle meaning
- registry summaries from replacing event history
- lifecycle observation from becoming a parallel authority
- runtime context from displacing canonical Layer 6 surfaces
