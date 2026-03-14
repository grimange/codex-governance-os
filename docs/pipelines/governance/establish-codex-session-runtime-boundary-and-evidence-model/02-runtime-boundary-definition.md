# Runtime Boundary Definition

The new canonical runtime-boundary authority is
`docs/governance/codex-session-runtime-boundary-and-evidence-model.md`.

The boundary it defines is:

- documentation-governed session truth remains authoritative in doctrine,
  contracts, pipeline artifacts, the session registry, and the execution ledger
- future runtime implementations may emit live session evidence only if that
  evidence maps back to the canonical Layer 6 meanings
- runtime evidence may support governed truth, but it must not redefine
  `session_id`, lifecycle semantics, admission ordering, or registry/ledger
  authority
