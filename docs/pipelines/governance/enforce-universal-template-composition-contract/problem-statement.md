# Problem Statement

Pipeline `028` published the canonical universal template composition contract, but enforcement still depended on scattered compatibility checks and verification lanes.

That left two gaps:

- unsupported compositions could still be requested outside the verification workflow
- manifest drift could remain latent until a human compared docs, tests, and JSON manually

Pipeline `029` closes those gaps by making the certified composition boundary executable at scaffold time and manifest-inspection time.
