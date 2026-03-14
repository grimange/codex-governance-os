# Remediation Plan

1. Inventory workstation-local absolute path references across the Layer 6
   canonical docs, handoff packet README, and pipeline `107` verification
   bundle.
2. Separate pure link-portability defects from path-truth defects so the lane
   only changes representation where semantics must stay fixed.
3. Normalize markdown links to the nearest stable portable relative form.
4. Correct the active `107` lane definition so its `affects` path matches the
   canonical state-machine location under `docs/contracts/`.
5. Preserve the historical `107` restriction wording that records the prior
   path mismatch, while replacing the embedded absolute link with a portable
   relative link.
6. Register pipeline `108` and verify that the remediated in-scope surfaces no
   longer contain `/home/`, `/Users/`, `C:\`, or `file://` references.
