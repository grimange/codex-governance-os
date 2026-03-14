# Problem Statement

Pipeline `029` made the composition contract executable, but the failure surface was still optimized for enforcement rather than diagnosis.

Operators and agents needed a deterministic way to answer:

- what overlay set was actually evaluated
- why it was supported or rejected
- which certified alternatives are closest to the rejected request

Pipeline `030` adds that explainability layer without widening the certified contract.
