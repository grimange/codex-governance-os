# Governance Execution Flow

The documented governed execution lifecycle now becomes:

1. session start
2. pipeline execution
3. artifact bundle creation
4. governance verification
5. handoff packet creation when continuity evidence is required
6. session registry and ledger update
7. session close

Failure handling:

- if a required packet is missing at close time, the execution ledger should
  record `SESSION_CONTINUITY_VIOLATION`
- closure reporting should keep that violation explicit

This is documented operational discipline, not proof of automated enforcement.
