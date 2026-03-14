# Session Lifecycle Model

The execution ledger now defines the canonical session lifecycle events:

- `SESSION_STARTED`
- `SESSION_CONTEXT_ALIGNED`
- `SESSION_TASK_ASSIGNED`
- `SESSION_EXECUTION_STARTED`
- `SESSION_EXECUTION_COMPLETED`
- `SESSION_VERIFICATION_COMPLETED`
- `SESSION_CLOSED`

The registry complements those events with lifecycle status values:

- `STARTED`
- `CONTEXT_ALIGNED`
- `TASK_ASSIGNED`
- `EXECUTING`
- `EXECUTION_COMPLETED`
- `VERIFICATION_COMPLETED`
- `CLOSED`

Handoff traceability is preserved through explicit fields for:

- origin session
- target session
- objective
- constraints
- expected outputs

Mutation scope is also made explicit so overlapping structural work can be
serialized under the Layer 6 doctrine.
