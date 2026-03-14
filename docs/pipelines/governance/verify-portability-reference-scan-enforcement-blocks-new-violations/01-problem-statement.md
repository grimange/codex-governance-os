# Problem Statement

Pipeline `111` established a deterministic portability scan and wired it into a
canonical governance preflight command. Pipeline `112` must verify that this
enforcement behaves fail-closed against a newly introduced violation and
returns to a clean pass once the violation is removed.
