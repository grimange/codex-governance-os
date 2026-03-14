# Drift Detection Revalidation

Pipeline `038` revalidated drift protection with three simulated divergences:

## Case A

- temporary contract document removes `service + monorepo`
- runtime still supports it
- expected outcome: `CONTRACT_DRIFT_DETECTED`

## Case B

- runtime temporarily admits `laravel + cli-worker`
- contract still rejects it
- expected outcome: `CONTRACT_DRIFT_DETECTED`

## Case C

- a manifest temporarily declares `laravel + cli-worker`
- contract still rejects it
- expected outcome: `CONTRACT_DRIFT_DETECTED`

All three were detected successfully.
