# Deterministic Generation Rules

Pipeline 170 preserves deterministic generation through these rules:

- identical maturity, gap, and remediation-plan inputs must produce identical
  roadmap output
- stage ordering follows remediation-plan dependency order
- stage grouping is derived from remediation strategy only
- no random prioritization is permitted
- no unsupported pipeline recommendation is introduced when remediation entries
  already record uncertainty
