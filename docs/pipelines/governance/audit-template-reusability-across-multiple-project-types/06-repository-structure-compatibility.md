# Repository Structure Compatibility

| structure surface | small repos | backend repos | frontend repos | infra repos | libraries | monorepos | notes |
|-------------------|------------|---------------|----------------|-------------|-----------|-----------|-------|
| `docs/governance/` | compatible | compatible | compatible | compatible | compatible | compatible | Stable doctrine root across all archetypes. |
| `docs/contracts/` | compatible with optional use | compatible | compatible | compatible | compatible | compatible | Empty or sparse use is acceptable until contracts are warranted. |
| `docs/pipelines/` | compatible | compatible | compatible | compatible | compatible | compatible | Scales well because categories and artifact folders are explicit. |
| `skills/` | compatible | compatible | compatible | compatible | compatible | compatible | Universal skill library remains generic. |
| `docs/bootstrap/` | compatible with slight onboarding overhead | compatible | compatible | compatible | compatible | compatible | Useful as an adoption layer, though small repos may only use it once. |

## Findings

- The structure works for monorepos because doctrine, contracts, pipelines, and local skills can all grow by bounded scope.
- The structure also works for small repositories because unused roots can remain sparse without changing authority order.
- New-contributor understandability is decent, but the absence of a top-level README means first discovery still relies heavily on `AGENTS.md` and the pipeline catalog.
