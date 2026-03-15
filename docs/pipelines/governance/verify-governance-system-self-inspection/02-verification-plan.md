# Verification Plan

Pipeline 163 verification steps:

1. Execute `python tools/governance/inspect_governance_state.py`.
2. Re-run the CLI and compare the generated JSON hash to confirm deterministic
   output on unchanged repository state.
3. Introduce one temporary capability-status mismatch in the registry and
   confirm the CLI reports drift with a non-zero exit.
4. Restore the canonical registry state.
5. Re-run the CLI to restore the canonical JSON surface and confirm clean
   alignment.

Verification boundaries:

- no capability definitions are changed permanently
- no maturity scoring model is changed
- only the intended JSON regeneration is allowed as canonical output mutation
