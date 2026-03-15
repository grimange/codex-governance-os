# Verification Plan

Future verification of Pipeline 178 should confirm:

1. valid canonical state still produces deterministic selector output
2. changing the roadmap target to another known but non-consensus domain fails
   closed with `GOVERNANCE_RECOMMENDED_NEXT_TARGET_CONSENSUS_VIOLATION`
3. creating `*-copy.json` candidate surfaces fails closed with
   `AMBIGUOUS_GOVERNANCE_SURFACE_CANDIDATE_DETECTED`
4. canonical next-action output is not rewritten during these failures
5. the updated governance regression suite passes
