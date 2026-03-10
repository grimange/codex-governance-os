---
name: canonical-contract-authoring
description: Author bounded canonical subsystem or governance contracts that follow the governed contract-writing standard and support downstream audit and verification.
---

# Canonical Contract Authoring

## Purpose

Turn a selected contract candidate into a durable canonical contract.

## When To Use

- after a contract candidate has been selected
- when a governance surface needs explicit operational rules
- when downstream audit and remediation work require a stable contract target

## When Not To Use

- when contract boundaries are still unclear
- when architecture discovery has not yet established enough evidence

## Inputs

- selected contract candidate
- architecture doctrine
- contract-writing standard
- supporting discovery evidence

## Procedure

1. define scope and authority boundaries
2. express canonical rules, allowed behaviors, and prohibited behaviors
3. define compliance signals and ambiguity handling
4. state governance implications and non-goals

## Outputs

- canonical contract under `docs/contracts/`
- supporting-surface update notes when applicable

## Boundaries

This skill authors one bounded contract. It does not perform the later audit or remediation stages.

## Failure Modes

- writing aspirational prose instead of operational rules
- overstating contract authority
- omitting auditable compliance signals

## Example Invocation

Use `canonical-contract-authoring` to author the highest-priority governance contract after candidate discovery.

## Expected Artifacts Or Deliverables

A canonical contract and the governance records needed to make it usable downstream.
