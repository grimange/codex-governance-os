# Verification Plan

Verification for Pipeline 184 should confirm:

1. `python tools/governance/inspect_governance_state.py authoritative-state`
   emits the canonical answer surface successfully on valid snapshot state.
2. repeated execution on unchanged snapshot state produces identical output.
3. required snapshot provenance fields are present.
4. embedded `recommended_next_action` matches the authoritative selector
   contract.
5. snapshot mutation changes the answer surface.
6. snapshot restoration restores the original answer.
7. invalid or drifted snapshot conditions fail closed rather than returning a
   normal authoritative state answer.
