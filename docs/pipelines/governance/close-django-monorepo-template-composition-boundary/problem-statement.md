# Problem Statement

The original composition matrix treated `django + monorepo` as fail-closed because the scaffold had no deterministic answer for Django service placement inside a repository root owned by the monorepo overlay.

Pipeline `033` closes that gap by defining a canonical nested placement and aligning contract, manifests, scaffold realization, enforcement, doctor output, and verification coverage around that structure.
