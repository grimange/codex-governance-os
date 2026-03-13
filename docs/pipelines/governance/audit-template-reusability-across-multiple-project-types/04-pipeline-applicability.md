# Pipeline Applicability

| pipeline | backend service | frontend app | CLI tool | infrastructure automation | library or SDK | mixed monorepo |
|----------|-----------------|--------------|----------|---------------------------|----------------|----------------|
| 000 initialize governed project | universal | universal | universal | universal | universal | universal |
| 001 discover architecture and establish doctrine | universal | universal | universal | universal | universal | universal |
| 002 audit governance readiness | universal | universal | universal | universal | universal | universal |
| 003 discover contract candidates and authority surfaces | universal | optional early, universal once boundaries grow | optional early | universal | universal once API/package boundaries matter | universal |
| 004 author canonical contract | universal once a priority subsystem exists | optional | optional | universal | universal once a bounded public surface exists | universal |
| 005 audit implementation against canonical contract | universal once a contract exists | optional | optional | universal | universal once a contract exists | universal |
| 006 remediate implementation drift against contract | universal once drift exists | optional | optional | universal | universal once drift exists | universal |
| 007 verify contract alignment | universal once remediation occurs | optional | optional | universal | universal once remediation occurs | universal |

## Findings

- Pipelines `000` through `002` are genuinely baseline pipelines for all archetypes.
- Pipelines `003` through `007` are not backend-only; they become relevant whenever a repository has bounded canonical surfaces worth contracting.
- The pipeline catalog uses optionality rather than incompatibility. That is the right model for universality.
