# From reference frames to routing

Stephen D. Bartlett, Terry Rudolph and Robert W. Spekkens, *Reference frames, superselection rules, and quantum information*, **Reviews of Modern Physics 79**, 555–609 (2007). [Journal record](https://doi.org/10.1103/RevModPhys.79.555) · [arXiv v3](https://arxiv.org/abs/quant-ph/0610030v3).

| Review section | What it supplies for the five-path bond |
| --- | --- |
| II.B–C | Turning an unknown phase into an average over phase rotations and identifying the sectors that survive |
| III.A.1 | Encoding a qubit in the location of one excitation across two local modes |
| III.C.1–2 | The loss of usable entanglement on an isolated single-particle link and the activation permitted by combining links |
| III.C.3 | Interpreting entanglement conditioned on a locally measured number sector |

The section labels follow the journal and v3's original text. Read them alongside the [network model](../science/model.md) and the [worked milestones](MILESTONES.md).

## From one party to a whole graph

In the review's phase-reference setting, photon number generates phase rotations. The network carrier can be any system with the specified occupation encoding and common phase action. Each end of a link has one mode, which can be empty or hold the link's excitation. A laboratory with several incident links counts all its occupied modes. The project's $`N_v`$ is the operator for that laboratory's total count. An unknown angle $`\theta_v`$ multiplies each pattern with count $`n`$ by the same phase $`e^{i n \theta_v}`$.

The project supplies one independent local angle per vertex and applies it to every mode at that vertex. Two patterns with the same counts at *every* laboratory keep their relative phase after averaging. The two patterns in which a laboratory's single excitation occupies either of two modes are the dual-rail qubit of the review. On a network, many global occupations can share one complete count record. The project indexes those occupations by directing each edge toward the end that holds its excitation. The graph's indegree vector is then the quantum measurement's charge record.

## From activation to a routing probability

Place five independent two-hop paths between Alice and Bob. Each path has one intermediate laboratory measuring its total count without resolving which incident mode is occupied. A count of one leaves two compatible occupations. A measurement in their sum-and-difference basis removes that intermediate label, leaving an endpoint excitation with a correctable sign.

Alice and Bob pool these outputs and read their total counts. A sector with at least one active excitation at each endpoint has two or more coherent placements. A local measurement and decoding extract a dual-rail Bell pair. This is where the review's activation mechanism becomes a routing protocol. The [parallel-path proof](../science/parallel-paths.md) counts these favorable sectors and proves optimality. The [graph proof](../science/graph.md) describes the general obstruction. The [lattice construction](../science/scale-and-robustness.md) uses many successfully activated bonds as well as the classical messages needed to find and connect them.

The review supplies the phase and encoding foundations. The network's routing theorem, exact pooled success probability and lattice construction follow from the project proofs. The [scientific account](../science/README.md) points to those arguments and their attribution.

[Start at M01](MILESTONES.md#m01-an-excitation-on-one-link) · [Learning route](README.md)
