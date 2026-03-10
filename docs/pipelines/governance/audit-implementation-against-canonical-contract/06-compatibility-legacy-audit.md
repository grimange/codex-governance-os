# Compatibility And Legacy Surface Audit

| Item | Evidence | Subsystem Affected | Governance Risk | Remediation Likelihood |
|------|----------|--------------------|-----------------|------------------------|
| descriptive `PROPOSED` labels remain in active pipeline definitions | `001`, `003`, `004`, and `005` definitions still advertise `PROPOSED` while registry history and operational use show activity | lifecycle vocabulary and audit interpretation | moderate | high |
| registry completeness discipline has historically lagged operational use | earlier audit artifacts document the same issue first for `002`; current audit finds the pattern again for `005` | registry activation tracking | high | high |
| downstream lifecycle definitions exist without proven operational activation | `006` and `007` are present as concrete definitions but have no registry entry and no direct evidence of active execution in this audit | future registry scope boundary | low | moderate |
| generated artifacts are used to infer activation when registry state is incomplete | previous audits and contract-authoring artifacts record activation mismatches | discoverability and audit effort | moderate | high |

## Assessment

- The main legacy behavior is not obsolete code but a documentation-era habit of treating `PROPOSED` labels and delayed registry updates as tolerable transitional states.
- That compatibility behavior is explicitly constrained by the contract now and should no longer be treated as primary behavior.
- No deprecated code modules or compatibility adapters exist outside the documentation surfaces themselves.
