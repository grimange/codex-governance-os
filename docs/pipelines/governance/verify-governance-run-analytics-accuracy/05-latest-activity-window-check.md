# Latest Activity Window Check

The analytics latest-10 list in `docs/governance/pipeline-run-analytics.md` was compared against the canonical ledger tail.

Expected window from ledger (pipeline ids 132-141, oldest to newest):

- 132, 133, 134, 135, 136, 137, 138, 139, 140, 141

Analytics-reported window:

- 132, 133, 134, 135, 136, 137, 138, 139, 140, 141

Artifact bundles and verdict strings also matched exactly for each row.

Result: **PASS**
