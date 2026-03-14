# Forbidden Pattern Scan Results

Patterns scanned:

- `/home/`
- `/Users/`
- `C:\`
- `file://`
- `~/`

## Active Governed Surface Scan

Deterministic scan across active governed surfaces found:

- no machine-local live markdown links in canonical doctrine, contracts, entry
  surfaces, registry, or active pipeline definitions outside literal pattern
  examples: `PASS`

Observed non-link literal examples in active surfaces:

| file | pattern family | classification | reason |
|------|----------------|----------------|--------|
| `docs/governance/governance-safety-invariants-canon.md` | `/home/...`, `/Users/...`, `file://...`, `~/...` | literal example | doctrine defines forbidden patterns rather than using them as links |
| `.codex/AGENTS.md` | `/home/...`, `/Users/...`, `C:\...`, `file://...`, `~/...` | literal example | agent instructions describe prohibited path families |
| `docs/pipelines/governance/108--remediate-non-portable-filesystem-links-in-canonical-governance-surfaces.md` | `/home/`, `/Users/`, `file://` | literal example | remediation lane definition names defect patterns and scope |
| `docs/pipelines/governance/109--enforce-repository-portability-link-invariants-across-governance-surfaces.md` | `/home/*`, `/Users/*`, `file://*`, `~/...` family | literal example | invariant lane definition names forbidden pattern families |
| `docs/pipelines/governance/110--verify-non-portable-filesystem-references-were-remediated-and-no-longer-exist-in-governed-repository-surfaces.md` | `/home/`, `/Users/`, `file://`, `~/` | literal example | verification lane definition names the scan criteria |

## Historical Artifact Bundle Scan

Observed preserved evidence in historical bundles:

| file family | classification | reason |
|-------------|----------------|--------|
| `docs/pipelines/governance/remediate-non-portable-filesystem-links-in-canonical-governance-surfaces/` | historical evidence | remediation bundle intentionally records prior defect patterns and replacements |
| `docs/pipelines/governance/enforce-repository-portability-link-invariants-across-governance-surfaces/` | historical evidence | invariant bundle intentionally records forbidden patterns and enforcement language |

No remaining matches in the inspected `107` verification bundle function as
machine-local live links.
