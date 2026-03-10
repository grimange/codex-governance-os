# Implementation Drift Assessment

| Drift Category | Description | Contract Rule Violated | Implementation Evidence | Subsystem Affected | Severity |
|----------------|-------------|------------------------|-------------------------|--------------------|----------|
| authority drift | operational activation of `005` is not reflected in the registry even though the registry is the canonical activation state surface | every active pipeline must have a corresponding registry entry | this audit is executing `005`, but registry content ends at `004` | pipeline registry activation state | HIGH |
| lifecycle drift | activation-to-registration transition is not recorded in the same governed change set | registry updates must occur no later than the same change set that activates a pipeline | no registry row exists for `005` during its execution | governance lifecycle tracking | HIGH |
| interface drift | discoverability interface does not expose the full active governance set | audits should determine active governance coverage from the registry | active `005` must be inferred from execution context rather than registry state | registry consumer interface | MODERATE |
| compatibility drift | active pipelines still use `PROPOSED` vocabulary in their definitions | proposed text does not excuse omission and should not obscure active use | `001`, `003`, `004`, and `005` retain `PROPOSED` text despite active or operational use | lifecycle vocabulary | MODERATE |
| undocumented behavior | operational reality can still outrun published registry state | active use must be explicitly represented rather than inferred from artifacts alone | prior artifacts and current audit both rely on inference when registry lags | governance auditability | MODERATE |

## Assessment

No blocking evidence shows the subsystem is structurally broken. The dominant drift is discipline drift: the repository has the right authorities and schema, but active use still outpaces canonical publication.
