# Governance Compatibility Model

## Compatibility Rules

- Compatible changes preserve current authority ordering and do not require adopters to rebuild their governance layout.
- Potentially incompatible changes include new mandatory files, changed pipeline meaning, removed doctrine surfaces, or changed registry semantics.
- Compatibility assessment must consider the framework's published archetypes: small repositories, libraries, CLI tools, frontend applications, backend services, and monorepositories.

## Evaluation Questions

1. Does the change alter authority interpretation?
2. Does the change add a mandatory adoption step?
3. Does the change require existing adopters to rename, move, or replace governance surfaces?
4. Does the change narrow domain neutrality?
5. Does the change make a previously optional pipeline effectively mandatory?

If any answer is yes, compatibility must be recorded explicitly and migration or deprecation handling should be considered.
