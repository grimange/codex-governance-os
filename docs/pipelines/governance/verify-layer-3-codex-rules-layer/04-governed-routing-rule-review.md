# Governed Routing Rule Review

The Layer 3 canon explicitly requires Codex to:

1. classify requests
2. prefer governed routing when the repository already defines a governed path
3. route governance-truth changes through the appropriate lane or equivalent
   governed path
4. avoid implying mutation when work remains advisory
5. fail closed when the repository does not support the requested governance act

The canon also requires safe mutation behavior and evidence-bounded authorship,
which preserves the lower-layer restriction model rather than broadening it.

Restriction preserved by this verification:

- this lane verifies the rule definitions only
- it does not prove runtime enforcement of every Layer 3 behavior

Result: `ROUTING_RULES_VERIFIED_WITH_BOUNDARY`
