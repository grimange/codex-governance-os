# Problem Statement

Pipeline `107` verification artifacts exposed workstation-local absolute
filesystem links under `/home/...` inside active Layer 6 governance surfaces and
their linked verification records. Those links are non-portable across clone
locations, users, and operating systems, and they leak local filesystem layout
into canonical repository documentation.

Pipeline `108` is limited to bounded documentation remediation. It normalizes
in-scope markdown references to portable relative links, aligns the active
`107` lane definition with the repository's true canonical state-machine path,
and preserves the historical restriction semantics recorded by the `107`
verification bundle.
