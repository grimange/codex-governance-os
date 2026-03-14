# Session Lifecycle

Layer 6 establishes the following governed session lifecycle:

1. session start
2. context alignment
3. task assignment
4. bounded execution
5. result consolidation
6. governance verification
7. session closure

Lifecycle implications:

- a session must align itself to current objective and lower-layer constraints
  before structural work
- bounded execution must preserve explicit ownership and expected outputs
- result consolidation occurs before closure so downstream verification can
  inspect a coherent record
- closure may not treat unverified structural output as complete

This lifecycle preserves the Layer 3 verification posture and Layer 5 evidence
preservation rules.
