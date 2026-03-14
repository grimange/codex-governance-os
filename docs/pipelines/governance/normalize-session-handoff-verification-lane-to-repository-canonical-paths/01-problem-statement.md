# Problem Statement

Pipeline `096` verified the handoff continuity contract with restrictions that
did not reflect a defect in the established contract itself. The restrictions
instead reflected verification-lane drift:

- stale canonical path assumptions for the contract and template
- registry expectations broader than the current registry schema
- expected artifact names that did not match the executed `095` bundle

This lane normalizes the verification definition so future runs of `096` match
repository truth directly.
