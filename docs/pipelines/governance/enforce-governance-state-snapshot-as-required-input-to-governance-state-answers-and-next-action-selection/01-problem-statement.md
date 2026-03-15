# Problem Statement

Pipeline 181 verified the governance snapshot mechanism, but verification alone
left a structural bypass: authoritative governance-state consumers could still
read canonical source surfaces directly and return normal answers without first
binding themselves to the verified snapshot envelope.

Pipeline 182 closes that gap by making the snapshot a required input for normal
authoritative governance-state consumption and by forcing the next-action
selector to fail closed when that dependency is missing, invalid, mismatched, or
already marked drifted.
