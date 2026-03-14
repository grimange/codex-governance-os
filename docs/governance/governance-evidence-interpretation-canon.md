# Governance Evidence Interpretation Canon

## Purpose

This doctrine defines the canonical Layer 0 rules for interpreting governance
evidence in this repository.

It exists so governance claims, verdicts, restrictions, and verification
outcomes are supported by explicit repository-wide interpretation rules rather
than distributed convention alone.

## Scope

This canon governs how evidence is interpreted across:

- doctrine under `docs/governance/`
- contracts under `docs/contracts/`
- pipeline definitions under `docs/pipelines/`
- generated pipeline artifact bundles
- canonical governance tooling under `tools/governance/` and `tools/templates/`
- governance test results under `tests/governance/`
- registry-backed and matrix-backed governance truth surfaces

This canon does not change runtime behavior. It governs interpretation of
repository evidence and the minimum support required for governance claims.

## Evidence Categories

### Authoritative Evidence

Authoritative evidence may directly support a governance claim when it is valid,
in scope, and drawn from a canonical repository surface.

Typical authoritative evidence includes:

- canonical version-controlled governance documents in their governing roots
- required artifact files present in governed output locations
- recorded verification command results from canonical governance tools
- passing governance tests scoped to the claim being made
- canonical registry declarations where registry authority applies
- canonical matrix declarations where matrix authority applies
- canonical runtime validation or doctor outputs for a governed domain
- final verdict files, but only as the decision record for evidence that is
  also present elsewhere in the bundle or repository state

### Supporting Evidence

Supporting evidence may strengthen or contextualize a claim but must not stand
alone when stronger authoritative evidence is required.

Typical supporting evidence includes:

- implementation notes
- capability or compatibility analysis
- partial inventories
- transition notes
- explanatory summaries that point back to authoritative evidence

### Narrative Or Descriptive Material

Narrative or descriptive material explains repository state but does not, by
itself, prove governance truth.

Typical narrative material includes:

- status summaries
- roadmap notes
- recommendations
- design rationale not paired with repository proof
- prose explanation of results already established elsewhere

### Non-Evidence

Non-evidence must never be treated as proof of repository truth.

Examples include:

- future intent without execution evidence
- uncited claims
- stale or superseded summaries
- placeholder surfaces with no governing authority
- optimistic interpretation that exceeds the recorded scope of proof

## Interpretation Rules

### Evidence Must Be Scoped

Evidence is authoritative only for the claim it actually supports.

- a test proving one composition boundary does not prove the entire matrix
- a verification artifact for one pipeline run does not prove all future runs
- a registry row proves pipeline activation, not implementation correctness
- a matrix declaration proves certified status only where the matrix is the
  canonical surface for that domain

### Evidence Must Respect Authority Order

Evidence may support a claim only within the repository's established authority
order.

- repository state outranks summaries about repository state
- governing doctrine outranks lower-order descriptive notes
- pipeline definitions outrank their generated artifact summaries
- artifacts record execution evidence but do not override higher-authority
  governing documents

### Verdicts Must Be Evidence-Backed

A final verdict is authoritative as the recorded decision surface only when it
is backed by valid supporting evidence in canonical repository state.

A verdict file must not stand alone as proof if:

- the required artifact bundle is incomplete
- the claimed verification result is absent
- the cited command or test result is not recorded
- the claim exceeds the scope of the evidence recorded

### Narrative Must Not Override Verification

Narrative explanation, recommendation, or summary must not override:

- recorded passing or failing verification results
- canonical registry or matrix truth
- explicit contract restrictions
- explicit fail-closed boundaries
- higher-authority doctrine or constitutional interpretation

### Restrictions Must Be Preserved

If the evidence proves only a bounded claim, the governance record must preserve
that restriction explicitly.

The repository must not interpret:

- bounded verification as universal support
- provisional or partial implementation as certified completion
- missing evidence as implied success

### Tool Output Requires Canonical Context

Tool output is authoritative only when the tool is part of canonical governance
truth for the domain being claimed.

- canonical governance tool output may directly support the relevant claim
- ad hoc scripts or one-off commands may be supporting evidence, but not
  automatically authoritative

## Claim Support Rules

### Establishment Claims

An establishment claim requires evidence that the governed surface now exists
and is installed in the correct canonical locations.

Minimum support normally includes:

- the created or updated governing document, contract, registry, or matrix
- required artifact bundle outputs for the establishment lane
- explicit statement of the established scope and any restrictions

### Verification Claims

A verification claim requires evidence that a governed verification procedure
was actually executed and recorded.

Minimum support normally includes:

- the executed verification command or test procedure
- the recorded result
- a direct tie between the result and the scoped claim

### Restriction Claims

A restriction claim requires evidence that the boundary is explicitly recorded
and that the repository does not silently treat the restricted state as
supported.

Minimum support normally includes:

- the governing restriction statement in a canonical surface
- supporting verification or runtime evidence that the boundary fails closed or
  remains bounded

### Blocked Claims

A blocked claim requires evidence that a required prerequisite is absent,
conflicted, or insufficient.

Minimum support normally includes:

- the missing or conflicting prerequisite
- the specific reason the claim cannot be established or verified
- any explicit bounded next step, if one exists

### Stability Or Non-Drift Claims

A stability or non-drift claim requires evidence that canonical surfaces remain
aligned after a prior establishment or verification event.

Minimum support normally includes:

- re-executed verification against the governing surfaces
- evidence that the canonical decision remains unchanged
- preservation of previously declared restrictions

## Evidence Insufficiency And Conflict Rules

### Insufficient Evidence

Evidence is insufficient when it does not support the full scope of the claim
being made.

When evidence is insufficient, the repository must:

- narrow the claim
- record the missing evidence explicitly
- avoid promoting the outcome beyond what is actually proven

### Conflicting Evidence

Evidence conflicts when two surfaces appear to support incompatible conclusions.

When evidence conflicts, interpretation must follow authority order first.
If authority order does not resolve the conflict completely, the claim must be
treated as unresolved until governance explicitly reconciles the surfaces in
version control.

### Missing Evidence

Silence is not proof.

If a required verification result, artifact, or governing update is absent, the
repository must not infer success from surrounding narrative or intent.

## Compliance Signals

Evidence interpretation is being followed correctly when:

- final verdicts cite or summarize concrete evidence rather than replacing it
- verification lanes record executed commands or test outcomes explicitly
- restrictions remain visible when evidence is only partial
- narrative summaries do not outrank governing runtime or verification surfaces
- later lanes can audit earlier claims without relying on unstated assumptions

## Non-Goals

This canon does not:

- automate evidence collection by itself
- replace subsystem-specific contracts
- redefine the repository authority hierarchy
- certify that any particular lane has sufficient evidence without inspecting
  that lane's actual artifacts
