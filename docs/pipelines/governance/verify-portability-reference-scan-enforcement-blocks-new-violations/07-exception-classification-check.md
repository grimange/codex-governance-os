# Exception Classification Check

Live repository scan evidence shows the enforcement logic does not misclassify:

- inline rule examples in `.codex/AGENTS.md` as violations
- forbidden-pattern lists in
  `docs/governance/governance-safety-invariants-canon.md` as violations
- indented scan-definition examples in pipelines `109`, `110`, `111`, and
  `112` as violations

Observed classifications:

- `rule_example`
- `scan_definition`

Historical evidence handling remains consistent with pipeline `111`:

- preserved evidence bundles are allowed by classification design and are not
  required to be rewritten for this verification lane
