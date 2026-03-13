# Docs And Manifest Matrix Consistency Report

## Surfaces Checked

- `docs/codex/templates/README.md`
- `docs/governance/template-scaffold-contract.md`
- `docs/codex/templates/manifests/*.json`
- `tools/governance/template_scaffold.py`

## Result

No mismatch detected after refreshing the top-level support documentation to state the verified composition matrix explicitly.

## Notes

- `node-typescript-service + cli-worker` is now supported in both manifest truth and scaffold behavior.
- explicit fail-closed examples in docs match actual rejected combinations.
- the pipeline registry path for pipeline `026` was corrected to match repository truth.
