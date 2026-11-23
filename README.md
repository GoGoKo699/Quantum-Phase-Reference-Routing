# Quantum Phase Reference Routing

**Can distant nodes share a Bell pair when each node has an unknown local phase?** A single shared excitation on an edge loses its usable coherence when that edge is used alone. If all modes at a given node share the same phase, measurements of local excitation number can preserve interference between different routes. The resulting Bell pair is encoded in a fixed excitation sector at each endpoint.

For internally disjoint routes of lengths $`\ell_1,\ldots,\ell_k`$, one batch of edge states gives the exact optimal Bell-pair success probability

```math
P_{\rm opt}
=1-2\prod_{i=1}^k(1-a_i/2)+\prod_{i=1}^k(1-a_i),
\qquad a_i=2^{1-\ell_i}.
```

Intermediate nodes identify which paths have one excitation at every interior node. They measure within that fixed-number sector. The endpoints pool the surviving paths and use their total excitation counts to herald and extract the pair. The converse allows arbitrary adaptive local operations and classical communication on the twirled input.

Five two-hop paths give **285/512**. This exceeds the square-lattice bond percolation threshold. Replacing each square-lattice bond with such a gadget gives a positive distance-independent lower bound on ideal one-batch routing success with at most 20 supplied half-link modes per vertex. The model assumes ideal local control, storage and classical reports. Independent link phase errors can reduce the fidelity even when the flags remain reliable.

## Four modes per node

On uniformly random simple four-regular bipartite graphs, the probability of a charge sector that permits some Bell extraction converges to **50.596%** for two distinct same-color terminals. A local protocol on logarithmic-length cycles gives an inverse-polynomial lower bound with high probability over the graph. Whether the optimal success probability stays bounded away from zero remains open. On the finite same-color $`K_{4,4}`$ instance, a charge-adaptive circuit attains $`1809/4096`$, and a cut bound gives $`18643/32768`$ as an upper bound.

The same state also supports extensive entanglement between whole color classes when each class can process its modes jointly. A chain of four-regular blocks can have that extensive entanglement and exponentially weak routing between individual nodes. [Companion project · Entanglement Valence Threshold](https://github.com/GoGoKo699/Entanglement-Valence-Threshold)

| Question | Scientific account |
| --- | --- |
| What does each edge supply, and what does the herald certify? | [Model and output contract](science/model.md) |
| When can a charge sector connect the terminals? | [Graph criterion and converse](science/graph.md) |
| How do random four-regular graphs support routing? | [Sector probability and constructive lower bound](science/degree-four-routing.md) |
| What can a charge-adaptive instrument achieve? | [Local extraction and finite bounds](science/charge-adaptive-routing.md) |
| Why is path pooling optimal? | [Parallel-path protocol and success law](science/parallel-paths.md) |
| How do loss, phase drift and routing distance affect the result? | [Architecture and robustness](science/scale-and-robustness.md) |
| How does the result relate to earlier work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Which finite cases can I reproduce? | [Verification](verification/README.md) |

## Learn the project

The educational anchor is Bartlett, Rudolph and Spekkens, *Reference frames, superselection rules, and quantum information* (2007). Use the [reference-frame bridge](learning/BRS_BRIDGE.md) and the [30 milestones](learning/MILESTONES.md) to follow a five-path example from its input states to an encoded lattice bond. The milestones then relate this construction to routing and entanglement across cuts on other four-regular graphs.

## Purpose and contact

This repository records the scientific account and supports self-directed learning. For discussion or potential collaboration, contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
