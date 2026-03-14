# Evidence Surface Alignment

## State Machine

- The interpretation model treats the state machine as the primary authority
  for lifecycle semantics.
- It does not define alternative lifecycle states or transitions.

## Session Ledger

- The interpretation model treats the ledger as authoritative for durable
  recorded event history within the scope of what the ledger actually records.
- It does not redefine the ledger as lifecycle authority.

## Session Registry

- The interpretation model preserves the registry as the canonical identity and
  indexed summary surface.
- It explicitly prohibits using registry summaries as a replacement for event
  history.

## Lifecycle Observation

- The interpretation model treats lifecycle observation as interpretive and
  reconstructive only.
- It keeps observation subordinate to the state machine, registry, and ledger.

## Runtime Boundary

- The interpretation model treats runtime evidence as supporting context only
  when it can map back into canonical session fields.
- It introduces no runtime instrumentation or event-system semantics.

## Classification

- state-machine alignment: `VERIFIED`
- ledger alignment: `VERIFIED`
- registry alignment: `VERIFIED`
- observation subordination: `VERIFIED`
- runtime-boundary alignment: `VERIFIED`
