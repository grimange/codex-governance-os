# Registry Normalization Plan

Mutation class:

- editorial clarification

Minimal scoped update:

- keep the existing registry table shape unchanged
- update only the `089` row
- preserve the existing canonical pipeline definition path in the `path` cell
- add the canonical artifact-bundle directory path explicitly in the same `path`
  cell

Why this is the narrowest safe change:

- it closes the exact restriction recorded by pipeline `090`
- it avoids inventing a new global registry column without broader governance
  evolution work
- it preserves the registry's discoverability role rather than redefining
  pipeline semantics
- it avoids touching unrelated entries

No doctrinal update is required because the change clarifies discoverability and
traceability for one active lane without altering Layer 5 meaning.
