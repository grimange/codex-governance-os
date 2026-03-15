# Verification

Verification is deferred to the dedicated follow-on verification pipeline.

Expected verification focus:

1. prove authoritative selector output includes required snapshot provenance
2. prove missing or invalid snapshot inputs fail closed
3. prove snapshot mismatch and pre-marked drift prevent normal selector output
4. prove regression safety for governance selector behavior
5. confirm direct-read exceptions remain bounded to non-authoritative or
   infrastructure-only usage
