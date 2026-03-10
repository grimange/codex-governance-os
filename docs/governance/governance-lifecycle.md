# Governance Lifecycle

## Purpose

This doctrine defines the standard lifecycle used for governed repository work so pipelines can share one sequencing model instead of restating lifecycle rules independently.

## Standard Lifecycle Stages

The default governed lifecycle is:

1. initialization
2. discovery
3. doctrine or contract establishment
4. audit
5. remediation
6. verification
7. promotion

Not every repository must execute every stage for every change, but any stage that is used must be justified by repository evidence and recorded explicitly.

## Expected Stage Order

- Initialization establishes the minimum governance surface for repositories that are not yet governance-capable.
- Discovery establishes what currently exists before stronger doctrine, contracts, or audits are authored.
- Doctrine or contract establishment turns important discovered rules into canonical authority surfaces.
- Audit compares current state against the relevant authority surface.
- Remediation changes repository state to address identified drift.
- Verification confirms whether the remediated state now satisfies the governing authority.
- Promotion records whether the outcome is acceptable for downstream reliance.

Default expectation: do not audit before the governing doctrine or contract exists, do not remediate before drift has been identified, and do not promote remediation closure without verification unless a higher-authority exception is recorded.

## Dependency Rules

- Discovery normally precedes architecture doctrine or subsystem contract authoring unless the repository already has sufficient canonical evidence.
- Contract authoring depends on architecture understanding when subsystem boundaries or authority model details are architecture-sensitive.
- Audits depend on an existing canonical target such as a doctrine or contract.
- Remediation depends on documented audit findings, discovery findings, or an equivalent higher-authority drift statement.
- Verification depends on the existence of the change or state being verified.
- Promotion depends on the evidence produced by the relevant upstream stage.

## Allowed Deviations

Deviation from the default lifecycle is allowed when:

- the repository already contains the required authority surface
- the work is a bounded correction to an existing canonical document
- a stage would be redundant and the reason is recorded explicitly
- a higher-authority governance surface authorizes a narrower path

When deviation occurs, the governing pipeline or artifact bundle must record what was skipped, why it was skipped, and why the remaining sequence is still safe.

## Promotion Role

Promotion is not the same as authoring, auditing, or verification. It is the explicit decision about whether downstream work may rely on the result.

If a pipeline includes promotion, the decision must be recorded separately from analysis and separately from the final verdict summary.

## Downstream Pipeline Rule

Future pipelines should reference this lifecycle doctrine for baseline sequencing expectations and only add narrower lifecycle rules when the pipeline needs stricter ordering than the standard lifecycle provides.
