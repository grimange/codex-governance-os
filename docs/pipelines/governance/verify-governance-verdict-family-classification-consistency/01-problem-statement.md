# Problem Statement

Pipeline 146 verifies that the verdict-family canon introduced in Pipeline 145
classifies every recorded ledger verdict consistently and deterministically.

This verification has four required outcomes:

- extract all final verdict strings from the centralized ledger,
- verify one-family classification per canonical rule,
- confirm legacy verdicts are explicitly bounded as `OTHER`,
- confirm analytics verdict-family totals match the canonical ledger recomputation.

The preflight check in `python tools/governance/preflight.py` is also required
as part of this verification lane.
