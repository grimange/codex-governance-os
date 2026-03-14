# Problem Statement

Pipeline `039` concluded that `laravel + cli-worker` should remain explicitly unsupported rather than be promoted into the certified composition matrix.

Pipeline `040` codifies that decision so the rejection is:

- explicit in policy
- visible in manifests and contract surfaces
- deterministic in doctor output
- protected by a dedicated governance regression test

The goal is to prevent accidental future admission through scaffold or manifest drift.
