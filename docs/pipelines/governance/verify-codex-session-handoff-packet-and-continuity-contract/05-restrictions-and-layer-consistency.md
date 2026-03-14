# Restrictions And Layer Consistency

Lower-layer consistency preserved:

- Layer 3 evidence-bounded verification posture is preserved
- Layer 5 handoff discipline remains explicit and restriction-preserving
- Layer 6 session orchestration remains documentation-level and subordinate to
  lower-layer authority
- the session registry and execution ledger remain authoritative for identity
  and event truth

Restrictions recorded by this verification:

- pipeline `096` names different canonical paths for the contract and template
  than the paths deliberately established in pipeline `095`
- pipeline `096` expects registry fields that the current pipeline registry
  schema does not encode
- pipeline `096` names different artifact filenames for the `095` bundle than
  the artifact names used by the executed establishment lane

These restrictions do not invalidate the established contract. They indicate
verification-body drift relative to the executed canonical repository state.

Result: `LAYER_CONSISTENCY_VERIFIED_WITH_DOCUMENTATION_DRIFT_RESTRICTIONS`
