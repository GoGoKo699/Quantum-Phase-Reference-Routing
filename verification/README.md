# Reproduce the finite calculations

Run from the repository root with Python 3.10 or later. The checks use the standard library.

```bash
python3 verification/run_all.py
```

Expected output

```text
orientation charge sectors verified: 40397
parallel-path cases verified: 120
serial test cases verified: 2
strict graph bound: 3/16, exact optimum: 1/8
endpoint pooling charge sectors verified: 10
mesh threshold and four repetition decoders verified
```

The orientation enumerator tests every simple graph on two to five labeled vertices. It groups orientations by indegree, checks the strongly connected component partition within every group and verifies factorization by counting the Cartesian product of component choices. The parallel-path test compares the exact rational formula with the orientation characterization for paths of lengths one to three, with one to four paths. It also checks two series examples.

The strict example checks the sector multiplicities and the terminal eigenvalue that enters the conversion bound. The five-path pooling test counts the diagonal measurement effects and outcome labels. The loss cutoff is bracketed using rational values, and the phase-repetition decoder is checked by enumerating error strings at four odd block sizes.

The [graph](../science/graph.md), [parallel-path](../science/parallel-paths.md), and [robustness](../science/scale-and-robustness.md) proofs establish the general statements. These calculations test finite witnesses and do not simulate optical hardware.
