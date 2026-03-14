# Problem Statement

The repository could already describe session lifecycle, handoff completion,
and resumed continuity, but it did not yet define when an existing or resumed
session is actually allowed to begin governed execution.

Pipeline `106` closes that gap by establishing explicit admission and
activation rules so initialization, admission, and active execution are no
longer treated as equivalent.
