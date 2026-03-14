# Canon Consistency Checks

Verification findings:

- the canon distinguishes `SESSION_INITIALIZED`, `SESSION_ADMITTED`, and
  `SESSION_ACTIVE`: `PASS`
- the state machine now records `SESSION_INITIALIZED -> SESSION_ADMITTED ->
  SESSION_ACTIVE` as the canonical activation entry path: `PASS`
- resumed sessions re-enter through `SESSION_RESUMED -> SESSION_ADMITTED`
  rather than activating directly: `PASS`
- registry and ledger surfaces can represent admission status, activation
  status, fail-closed reason, and first admitted action: `PASS`
- first-action validation is explicit in the admission canon: `PASS`

Restrictions:

- pipeline `107` expects activation to explicitly produce a session ID, registry
  entry, and ledger execution record as a mandatory canon rule, but the current
  repository state establishes those surfaces as recordable evidence surfaces
  rather than stating automatic per-activation production as a canon invariant:
  `RESTRICTED`
