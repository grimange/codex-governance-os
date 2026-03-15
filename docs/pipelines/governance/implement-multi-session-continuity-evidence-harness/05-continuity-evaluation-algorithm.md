# Continuity Evaluation Algorithm

The implemented algorithm follows this deterministic sequence:

1. Load canonical scenario fixtures from the established governance path.
2. Parse each scenario into explicit sessions, evidence, boundaries, and
   expected classifications.
3. Derive evidence families for each scenario from the documented evidence
   strings.
4. Fail boundary-violating scenarios closed before continuity-strength
   promotion.
5. Classify no-evidence scenarios as `NO_CONTINUITY`.
6. Classify predecessor-plus-artifact-continuation scenarios as
   `VERIFIED_CONTINUITY`.
7. Classify remaining admissible-evidence scenarios as `WEAK_CONTINUITY`.
8. Map the evaluated state to a machine verdict such as
   `VALID_CONTINUITY_CHAIN`, `MISSING_BRIDGE_EVIDENCE`, or
   `SESSION_ISOLATION_VIOLATION`.

The harness exits non-zero if evaluated results do not match the canonical
scenario expectations.
