# Capability Resolution

Capability evaluation is implemented in [composition_contract.py](/home/ramjf/python-projects/codex-governance-os/tools/templates/composition_contract.py).

The engine now verifies:

- required capabilities are present in the composed capability set
- conflicting capabilities are not introduced by sibling overlays
- composition roles remain mutually compatible
- explicit fail-closed boundaries keep their canonical rejection reasons

Scaffold realization now applies this capability evaluation in addition to the certified composition contract, so capability drift is rejected before repository surfaces are created.
