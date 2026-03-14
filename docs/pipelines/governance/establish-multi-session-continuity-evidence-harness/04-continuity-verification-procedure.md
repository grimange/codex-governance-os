# Continuity Verification Procedure

The evidence harness defines this deterministic procedure:

1. verify each in-scope session independently through the single-session stack
2. discover candidate cross-session evidence links
3. validate those links against the allowed evidence types
4. classify continuity evidence strength as:
   - `NO_CONTINUITY`
   - `WEAK_CONTINUITY`
   - `VERIFIED_CONTINUITY`

These classifications support the continuity model and do not replace the
top-level governance outcomes.
