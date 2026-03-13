# Bootstrap Model Compatibility

## Archetype Assessment

| archetype group | compatibility | notes |
|-----------------|---------------|-------|
| simple repositories | compatible with observations | The bootstrap guides allow selective downstream pipeline use, but the documentation density may feel heavy for very small projects. |
| single-package libraries | compatible | The model does not assume services or multiple deployable components. |
| CLI utilities | compatible with observations | Works structurally, though contract-oriented follow-on pipelines are often deferred until the tool matures. |
| frontend-only applications | compatible | The bootstrap guide and override model do not assume backend services or runtime infrastructure. |

## Assumption Review

- backend architecture assumed: no
- contract-heavy systems assumed: no, but later lifecycle phases become more visible than the smallest repositories may need initially
- runtime services assumed: no
- multi-component architecture assumed: no

## Findings

- `docs/bootstrap/governed-project-bootstrap.md` explicitly delays project-specific contracts and local skill overrides until discovery justifies them.
- `docs/bootstrap/local-override-model.md` allows specialization without forcing multi-service or infrastructure-heavy models.
- `docs/bootstrap/example-governed-repository-layout.md` includes optional local contract and local pipeline growth, which scales to larger systems without making them mandatory for smaller repositories.
