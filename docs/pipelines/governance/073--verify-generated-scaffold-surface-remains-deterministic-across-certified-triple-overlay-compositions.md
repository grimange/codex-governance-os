# 073 — Verify Generated Scaffold Surface Remains Deterministic Across Certified Triple Overlay Compositions

```yaml
pipeline_id: 073
registry_id: governance.templates.verify-generated-scaffold-determinism-triple-overlay
title: Verify Generated Scaffold Surface Remains Deterministic Across Certified Triple Overlay Compositions
stage: verification
lane_type: verification
governance_layer: L2_template_engine
authoritative_inputs:
  - docs/codex/templates/
  - docs/governance/template-scaffold-contract.md
  - tools/templates/
  - tests/governance/
expected_outputs:
  - docs/pipelines/governance/verify-generated-scaffold-surface-remains-deterministic-across-certified-triple-overlay-compositions/
classification: TEMPLATE_ENGINE_DETERMINISM_VERIFICATION
blocking: false
```

---

# 01 — Problem Statement

The Governance OS template engine supports **overlay-based scaffold composition**.
Previous pipelines verified deterministic generation for:

* base template
* single overlay compositions
* dual overlay compositions

However, once **three overlays compose simultaneously**, new risks appear:

1. overlay merge order instability
2. nondeterministic file generation
3. manifest resolution drift
4. cross-overlay file collision

Without verification, scaffold output could vary across runs.

Deterministic scaffolding is a **governance invariant** because:

* generated repositories must be reproducible
* template composition must behave predictably
* governance pipelines must operate on stable repository surfaces

Therefore this lane verifies that **certified triple overlay compositions produce identical repository scaffolds across repeated generations.**

---

# 02 — Certified Triple Overlay Composition Matrix

Only **governed overlay combinations** are allowed to participate in this verification.

Certified matrix examples:

| Composition                                           | Description                         |
| ----------------------------------------------------- | ----------------------------------- |
| node-typescript-service + cli-worker + monorepo       | multi-service monorepo scaffold     |
| cli-worker + python-package + monorepo                | mixed language workspace            |
| php-package + cli-worker + monorepo                   | PHP package with operational worker |
| node-typescript-service + cli-worker + python-package | service + worker + tooling          |

Each composition must satisfy:

* overlays individually certified
* composition allowed by template scaffold contract
* overlay merge order explicitly defined

---

# 03 — Determinism Requirements

A scaffold generation is deterministic when:

### File Surface

Generated files must be identical across runs.

No variation allowed in:

* file presence
* directory structure
* file names
* file counts

---

### File Content

File contents must remain identical across runs.

Specifically:

* dependency manifests
* configuration files
* generated scripts
* README scaffolds
* CI configuration

---

### Ordering Guarantees

The generator must ensure:

* deterministic overlay merge order
* deterministic manifest key ordering
* deterministic template variable rendering
* deterministic file write order

---

# 04 — Verification Method

The verification harness performs the following steps.

### Step 1 — Generate Scaffold

```
python tools/templates/generate_template.py \
  --overlay node-typescript-service \
  --overlay cli-worker \
  --overlay monorepo \
  --output /tmp/scaffold-run-1
```

Repeat generation:

```
python tools/templates/generate_template.py \
  --overlay node-typescript-service \
  --overlay cli-worker \
  --overlay monorepo \
  --output /tmp/scaffold-run-2
```

---

### Step 2 — Normalize Non-Deterministic Surfaces

Ignore expected variable values:

* timestamps
* random IDs
* generated secrets

Normalization step removes these values before comparison.

---

### Step 3 — Repository Diff

Compare scaffold directories:

```
diff -r scaffold-run-1 scaffold-run-2
```

Expected result:

```
no differences
```

---

### Step 4 — Repeat Across Matrix

Verification repeats for every certified triple overlay composition.

---

# 05 — Deterministic Scaffold Test Harness

A governance test must be added.

Example location:

```
tests/governance/test_template_triple_overlay_determinism.py
```

Example structure:

```python
class TripleOverlayDeterminismTest(unittest.TestCase):

    def test_node_cli_monorepo_deterministic(self):
        run1 = generate(["node-typescript-service", "cli-worker", "monorepo"])
        run2 = generate(["node-typescript-service", "cli-worker", "monorepo"])

        self.assertEqual(hash_tree(run1), hash_tree(run2))

    def test_cli_python_monorepo_deterministic(self):
        run1 = generate(["cli-worker", "python-package", "monorepo"])
        run2 = generate(["cli-worker", "python-package", "monorepo"])

        self.assertEqual(hash_tree(run1), hash_tree(run2))
```

---

# 06 — Drift Detection Boundaries

If any differences occur, the pipeline records:

* file drift
* content drift
* ordering drift
* overlay resolution drift

Example evidence artifact:

```
05-drift-report.md
```

This includes:

* file path differences
* content diffs
* root cause classification

---

# 07 — Verification Execution

Example execution commands:

```
python -m unittest discover -s tests/governance -p 'test_template_*.py'
```

Template generator sanity check:

```
python tools/templates/list_templates.py
```

Optional manual scaffold validation:

```
python tools/templates/generate_template.py --overlay node-typescript-service --overlay cli-worker --overlay monorepo
```

---

# 08 — Evidence Artifacts

The pipeline produces the following artifact bundle:

```
docs/pipelines/governance/
verify-generated-scaffold-surface-remains-deterministic-across-certified-triple-overlay-compositions/
```

Artifacts:

| File                                  | Purpose                      |
| ------------------------------------- | ---------------------------- |
| 01-problem-statement.md               | describes determinism risk   |
| 02-certified-triple-overlay-matrix.md | allowed overlay combinations |
| 03-determinism-requirements.md        | scaffold invariants          |
| 04-verification-method.md             | execution procedure          |
| 05-drift-report.md                    | recorded differences if any  |
| 06-test-harness.md                    | governance test description  |
| 07-verification.md                    | verification run log         |
| 08-final-verdict.md                   | final determination          |

---

# 09 — Final Verdict

Possible verdicts:

### Determinism Verified

```
TRIPLE_OVERLAY_SCAFFOLD_DETERMINISM_VERIFIED
```

Meaning:

* scaffold output identical across runs
* overlay merge order stable
* file surface deterministic

---

### Determinism Verified With Restrictions

```
TRIPLE_OVERLAY_SCAFFOLD_DETERMINISM_VERIFIED_WITH_RESTRICTIONS
```

Meaning:

* deterministic for certified matrix
* other compositions not supported

---

### Determinism Failed

```
TRIPLE_OVERLAY_SCAFFOLD_DETERMINISM_FAILED
```

Meaning:

* scaffold output varies across runs
* overlay ordering or template generation unstable

Remediation pipeline required.

---

# 10 — Governance Significance

This lane certifies that the **template engine remains deterministic even under complex overlay composition.**

Once verified:

* generated repositories are reproducible
* governance pipelines operate on stable repository surfaces
* multi-overlay scaffolds are safe for production template distribution

This establishes a key invariant for the **Governance OS Template Engine.**

```
```
