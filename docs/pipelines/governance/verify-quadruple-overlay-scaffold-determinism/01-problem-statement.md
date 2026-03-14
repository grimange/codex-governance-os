# Problem Statement

Pipeline `074` admitted the first governed quadruple-overlay composition:
`cli-worker + monorepo + python-package + scheduler`.

That contract is not complete unless scaffold realization is deterministic
across repeated runs. This lane verifies that the certified quadruple produces
identical `scaffold-selection.json` payloads and identical generated tree
hashes when realized more than once.
