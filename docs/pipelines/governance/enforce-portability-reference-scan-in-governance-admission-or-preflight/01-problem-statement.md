# Problem Statement

Pipelines `108` through `110` proved that the repository can remediate and
verify portability defects, but they still left the repository dependent on
manual execution of those checks. Pipeline `111` closes that enforcement gap by
adding a deterministic scan and wiring it into a canonical governance preflight
command that fails closed on new machine-local path references.
