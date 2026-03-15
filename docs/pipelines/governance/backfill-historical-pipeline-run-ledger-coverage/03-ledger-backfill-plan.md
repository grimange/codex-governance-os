# Ledger Backfill Plan

Backfill procedure used by Pipeline `141`:

1. scan `docs/pipelines/governance/*/07-final-verdict.md` for candidate executed bundles
2. resolve the corresponding pipeline definition and `registry_id` from repository truth
3. exclude any candidate lacking resolvable metadata instead of inferring it
4. sort validated historical candidates by artifact timestamp
5. insert the validated historical block ahead of the seeded `137`–`139` entries
6. append current continuation entries for `140` and `141` so the ledger remains operationally current
