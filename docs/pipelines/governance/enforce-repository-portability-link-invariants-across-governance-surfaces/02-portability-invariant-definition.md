# Portability Invariant Definition

The canonical Repository Portability Link Invariant is now established in
`docs/governance/governance-safety-invariants-canon.md`.

Invariant summary:

- canonical governance and repository-entry surfaces must not use
  machine-local absolute filesystem references as live links, canonical
  references, navigation paths, or doctrinal pointers
- forbidden live reference families include `/home/...`, `/Users/...`,
  `C:\...`, `file://...`, and `~/...`
- portable repository references must use document-relative links,
  repository-relative paths, or intentional external URLs
- historical evidence may preserve old path forms when documenting a past
  defect, but those mentions are not approval for future canonical use
- literal examples that describe forbidden patterns are allowed when they are
  not functioning as live links or repository navigation
