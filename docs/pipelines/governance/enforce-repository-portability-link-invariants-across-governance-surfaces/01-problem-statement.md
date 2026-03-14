# Problem Statement

The repository had already demonstrated that workstation-local filesystem links
can leak into governed markdown surfaces and remain invisible until a later
verification lane inspects them. Pipeline `108` remediated the targeted Layer 6
defect cluster, but it left the underlying repository-wide policy gap open.

Pipeline `109` closes that gap by establishing a canonical Repository
Portability Link Invariant, aligning remaining canonical surfaces that still
used machine-local links, and defining how future verification and admission
work should treat this defect class.
