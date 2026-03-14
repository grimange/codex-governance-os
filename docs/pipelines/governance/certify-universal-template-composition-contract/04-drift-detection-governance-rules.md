# Drift Detection Governance Rules

- Any change to overlay compatibility in `tools/governance/template_scaffold.py` must update `docs/contracts/universal-template-composition-contract.md`.
- Any change to `docs/codex/templates/manifests/*.json` that widens or narrows composition support must update the contract and affected docs in the same change set.
- `docs/codex/templates/README.md` and `docs/governance/template-scaffold-contract.md` must remain aligned with the certified matrix.
- `tests/governance/test_template_composition_matrix.py` must enumerate every certified supported combination.
- Governance verification must keep representative fail-closed combinations so rejection behavior remains explicit.
- A future lane may extend the certified matrix only after verification evidence proves the new combinations.
