# Interface And Interaction Audit

## Registry Entry Interface

| Interface Rule | Status | Evidence | Notes |
|----------------|--------|----------|-------|
| each registry entry includes ID, name, status, category, and path | compliant | current registry table includes all required columns | structure is valid |
| registry path references resolve to real pipeline files | compliant | each registered path `000` through `004` exists | no broken links found |
| registry ID must match filename-implied pipeline ID | compliant | registered IDs align with file naming | interface integrity is intact for existing rows |
| registry must expose active operational surfaces | non-compliant | `005` is an active interaction surface but is not published through the registry interface | discoverability interface is incomplete |

## Interaction Semantics

| Interaction Surface | Status | Evidence | Notes |
|---------------------|--------|----------|-------|
| constitution -> registry obligation | compliant | `AGENTS.md` requires registration for active pipelines | obligation is explicit |
| local operating instructions -> registry discipline | compliant | `.codex/AGENTS.md` repeats the requirement and names the registry contract | local operating rules align with contract |
| contract -> registry implementation | partially compliant | contract rules are explicit, but current registry state does not yet reflect active `005` | implementation lags the interface expectation |
| pipeline execution -> discoverability publication | non-compliant | current audit execution has not produced same-change-set registry representation | hidden activation is the primary interface defect |

## Hidden Or Undocumented Side Effects

- Operational use can currently outrun registry publication, forcing later audits to reconstruct activation from artifacts and user requests.
- `PROPOSED` status text in active definitions acts as a compatibility-era description rather than an authoritative interface field, which is allowed by the contract but still increases interpretation cost.
