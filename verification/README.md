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
K4,4 fibers verified: 16145, SCC-positive: 4323
K4,4 SCC upper: 20801/32768, Vidal upper: 18643/32768, strict cut improvements: 2466
K4,4 fixed pooling lower: 55/128, charge-based ring-choice lower: 443/1024, adaptive ring lower: 1809/4096
```

The orientation enumerator tests every simple graph on two to five labeled vertices. It groups orientations by indegree, checks the strongly connected component partition within every group and verifies factorization by counting the Cartesian product of component choices. The parallel-path test compares the exact rational formula with the orientation characterization for paths of lengths one to three, with one to four paths. It also checks two series examples.

The strict example checks the sector multiplicities and the terminal eigenvalue that enters the conversion bound. The five-path pooling test counts the diagonal measurement effects and outcome labels. The loss cutoff is bracketed using rational values, and the phase-repetition decoder is checked by enumerating error strings at four odd block sizes.

The [graph](../science/graph.md), [parallel-path](../science/parallel-paths.md), and [robustness](../science/scale-and-robustness.md) proofs establish the general statements. These calculations test finite witnesses and do not simulate optical hardware.

## Same-color K4,4 routing bounds

[k44.py](k44.py) enumerates all 65,536 orientations and all 64 terminal-separating cuts. It computes the SCC bound, the strongest bipartite Vidal bound per charge sector, and the accepting weights of the fixed pooling, charge-based ring choice, and sequential adaptive ring circuits. It checks that a two-orientation disagreement component can connect the terminals in exactly the SCC-positive charge sectors of this graph.

The adaptive recurrence records the residual orientation fiber and the components already connected by successful ring measurements. Each outcome either fixes the measured ring orientation or keeps the two alternatives of a consistently oriented ring. The recurrence counts both alternatives and chooses the next operation from the known charge and measurement records. All bounds are exact rational numbers for this graph. The count fixes the success bounds of the stated protocols, while optimal success over all separated-node operations remains open.
