# Drift Detection Revalidation

Pipeline `035` revalidated drift protection with three simulated divergences:

## Case A

- temporary contract document removes `django + monorepo`
- runtime still supports it
- expected outcome: `CONTRACT_DRIFT_DETECTED`

## Case B

- runtime temporarily admits `service + monorepo`
- contract does not list it
- expected outcome: `CONTRACT_DRIFT_DETECTED`

## Case C

- a manifest temporarily declares `service + monorepo`
- contract still rejects it
- expected outcome: `CONTRACT_DRIFT_DETECTED`

All three were detected successfully.
