# Session Runtime Model

Canonical runtime-session model established by this lane:

- a governed runtime session exists only after initialization, successful
  admission, active execution, and observable runtime evidence
- canonical identity remains `session_id`
- runtime-native handles may exist, but only as supporting evidence mapped back
  to `session_id`
- runtime lifecycle evidence must remain compatible with the existing state
  machine and admission canon

This keeps runtime compatibility subordinate to the existing Layer 6 canons
instead of creating a competing runtime-only truth model.
