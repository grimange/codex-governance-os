# Most-Specific Override Precedence Rule

Compound realization precedence is now centralized as a governance rule:

1. collect matching composition overrides for the selected overlay set
2. choose the highest-specificity matching override
3. reject same-specificity ambiguity fail-closed
4. never infer compound admission from lower-specificity pairwise rules alone

This rule is implemented in
[template_scaffold.py](/home/ramjf/python-projects/codex-governance-os/tools/governance/template_scaffold.py)
and reinforced by the new ledger drift checks in
[composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py).
