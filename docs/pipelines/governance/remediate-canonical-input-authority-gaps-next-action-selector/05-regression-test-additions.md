# Regression Test Additions

Pipeline 178 extends
`tests/governance/test_governance_system_next_action.py` with:

- target consensus violation coverage
- ambiguous `-copy` candidate detection coverage

The existing suite also continues to cover:

- invalid roadmap target
- missing roadmap target
- missing canonical surface
- remediation-plan mismatch
- gap mismatch
- same-name shadow surface detection
