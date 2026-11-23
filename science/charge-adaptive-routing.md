# Charge-adaptive Bell-pair extraction

A [charge record](model.md#why-the-charge-record-is-useful) leaves a uniform coherent superposition of consistent orientations. Learning the record gives the parties a choice of subsequent local measurements. This page gives an explicit choice in every eligible sector, examines graph-fixed helper policies, and tests charge-adaptive routing on a finite four-regular graph.

## Extracting a pair from two orientations

Fix a charge sector $`q`$ of positive probability. If the terminals share a strongly connected component, there are two orientations $`\omega,\omega'\in\Omega_q`$ with the following property. Form the subgraph of edges on which they disagree, ignoring isolated vertices. One connected component of this subgraph contains both terminals.

To find such a pair in principle, use the [proof of localizability](graph.md#a-local-measurement-gives-positive-success-inside-a-component), which gives a nonzero $`2\times2`$ minor of the formal terminal amplitude matrix $`M(z)`$. Expand it into signed products of orientations. Each term contains two different patterns at $`A`$ and two different patterns at $`B`$. If the terminals are in distinct disagreement components for a term, exchange the two orientations on the component containing $`B`$. Every vertex in that component has all its changed incident edges exchanged together, so both orientations retain their charges. The exchange leaves the product of helper coordinates unchanged, preserves the row assignments at $`A`$ and swaps the column assignments at $`B`$. It is a sign-reversing involution on terms whose disagreement components separate the terminals. The nonzero minor therefore contains a term with the required property.

After measuring and exchanging the charges, choose such a pair from the known fiber, for example by enumeration. Each vertex projects onto the span of its one or two patterns from that pair and reports acceptance. The measurements preserve fixed local charge. In a jointly accepting term a fixed edge has its original occupation. On a changed edge, the two incident vertices choose the same orientation label to keep one excitation on that edge. Thus each disagreement component makes one independent binary choice. If there are $`c`$ such components, exactly $`2^c`$ equal-amplitude orientations survive. The postselected state is the product of $`c`$ balanced two-pattern states and fixed occupations. The component containing both terminals gives the Bell pair by logical $`X`$ measurements at its helpers and a recorded phase correction. A fixed-charge isometry maps the two surviving patterns at each terminal to the dual-rail code.

The conditional success probability is
```math
\frac{2^c}{|\Omega_q|}\geq\frac{2}{|\Omega_q|}.
```
This quantifies an explicit circuit in every eligible sector. Its classical search can be expensive and its probability can be small. No hidden orientation sample is required.

## A restriction on graph-fixed pair measurements

Consider a four-regular graph with a tree ball of radius $`r\geq1`$ around $`A`$ that excludes $`B`$. Suppose every helper first projects onto a graph-fixed partition of its raw occupation basis into singleton patterns and pairs of equal charge. The protocol may use classical communication and arbitrary local operations after those projections. Under this restriction the one-batch Bell-pair success probability is at most
```math
4(5/8)^r.
```

The initial projections are diagonal, so sample a fair independent orientation to generate their outcome record. This is a way to analyze the probability of a record. A helper with a paired outcome has a binary choice between its sampled pattern and the alternative. Mark each port whose occupation changes under this choice. If both ends of an edge are marked, the corresponding helper choices must agree. If exactly one end is marked and the opposite helper port is fixed, the edge forces the paired helper to keep the reference pattern. The constraint propagates through the component of jointly marked edges. Terminal half-edge occupations are the complements of the incident helper bits, with no marked-edge constraints across the two laboratories. Fixing the local terminal charges can impose further constraints only on components incident to the respective terminal. If no unforced component is incident to both terminals, the sector after projection factors across a terminal-separating cut by assigning each exterior component to the terminal it touches or to either side if it touches neither. The cut depends on the projection record, and separability across it persists when averaging the terminal charges in that record. Such a record cannot yield a success branch.

A component that could touch both terminals must start at a marked port of a helper adjacent to $`A`$. At every helper reached along a marked edge, equal charge forces at least one additional port to be marked. Follow a deterministic choice of another marked port. Because the neighborhood is a tree, this walk moves outward until radius $`r`$ and encounters a fresh helper at every step. If it hits an unmarked incoming port of a helper, the component is forced. Conditional on the entering occupation bit, the other three bits at a new helper are independent and fair. Of the eight local patterns given that bit, at most one of weight one, at most one of weight three, and at most three of weight two can have a partner changing the entering bit. For weights one and three this follows because one side of the pairing has only one candidate for those weights, and extreme weights give no pair. Thus the conditional chance of a marked entering port is at most $`5/8`$. A union bound over the four starting ports proves the claim.

This bound tends to zero for distant terminals in the uniformly random four-regular bipartite ensemble, since the fixed-radius tree-ball event has probability tending to one for each $`r`$. Selecting the partitions using the complete observed charge vector, as in the two-orientation protocol, is outside the restriction. So are operations coherent across more than two patterns and adaptive measurements on links already fused.

## Adaptive fusion to a heralded frontier

In a rooted three-branching tree consider a helper with one parent link and $`k\leq3`$ heralded child links. Each link coherently shares an excitation between the helper and its remote endpoint, up to the endpoint phases. The identities of the remote endpoints can depend on earlier flags. Analyze the circuit at fixed arbitrary values of all node phases.

Write a local occupation pattern as a parent bit and a subset of occupied child modes. In each fixed-charge sector $`j`$, choose disjoint pairs $`(0,S),(1,T)`$ with $`T\subset S`$ and $`|S|=|T|+1`$. Measure the plus and minus vectors in each selected pair and the singleton vectors for the unpaired patterns. One possible choice is below. In the table, digits indicate child labels.

| Available child links | Paired subsets $`(S,T)`$ in each charge | Success |
| ---: | --- | ---: |
| $`0`$ | No pairs | $`0`$ |
| $`1`$ | $`j=1`$ has $`(1,\varnothing)`$ | $`1/2`$ |
| $`2`$ | $`j=1`$ has $`(1,\varnothing)`$. $`j=2`$ has $`(12,1)`$. | $`1/2`$ |
| $`3`$ | $`j=1`$ has $`(1,\varnothing)`$. $`j=2`$ has $`(12,1),(23,2),(13,3)`$. $`j=3`$ has $`(123,12)`$. | $`5/8`$ |

A paired outcome leaves the parent and the selected child endpoint with one coherently shared excitation. Their local occupations differ between the two alternatives, and all other remote modes have fixed occupations. Each paired outcome has a known correctable sign. The helper phase is common to both alternatives, and the outcome weights are phase independent. A singleton outcome fixes the parent partner's occupation so the next helper can ignore that mode.

Fuse from the leaves upwards. At fixed phases, disjoint subtrees give independent flags, and their probabilities are the same for every phase assignment. With $`u_t`$ as the probability of an available link from the end of a branch after $`t`$ fusion levels, the number of available children has binomial law with three trials and success probability $`u_t`$. The table gives
```math
u_0=1,\qquad
u_{t+1}=\tfrac32u_t-\tfrac32u_t^2+\tfrac58u_t^3,\qquad
\lim_{t\to\infty}u_t=\tfrac25.
```
The update is increasing on $`[0,1]`$ and its fixed points in that interval are zero and $`2/5`$. The sequence from one decreases and stays at least $`2/5`$.

The outcome chooses a frontier endpoint and provides an effective single-excitation link with the endpoints' unknown phases. It can participate in further phase-invariant processing. An exact encoded Bell pair at two predetermined endpoints requires an additional construction.

## Finite bounds on the complete bipartite graph

Take $`G=K_{4,4}`$ and distinct terminals of the same color. Four internally disjoint two-hop routes give unconditional probability $`55/128`$ by [path pooling](parallel-paths.md). The other edges may be left unused because the pooling measurements use disjoint modes and their success law is the same at any fixed node phases.

### A cut bound in each sector

For a vertex cut $`S\mid S^c`$, let $`C_S`$ be the orientation pattern of the crossing edges. In a sector $`q`$ the squared Schmidt coefficients across this cut equal $`\Pr(C_S=c\mid D=q)`$, where $`D`$ is the random full charge vector. Given the crossing pattern and the charges, the compatible internal orientations on the two sides form a Cartesian product. Different crossing patterns have orthogonal local occupations on each side. [Valence's cut identity](https://github.com/GoGoKo699/Entanglement-Valence-Threshold/blob/0e532750de184651381c4ed6db5836315c7e6670/science/entropy_identity.md#entanglement-across-an-arbitrary-cut)

Allowing collective quantum operations on each side of a terminal-separating cut relaxes the routing task. The bipartite single-copy conversion probability to a Bell pair is at most twice one minus the largest squared Schmidt coefficient, capped at one. Taking the strongest cut for each sector gives
```math
P^*(G;A,B)\leq\sum_q\Pr(D=q)
\min_{S\,:\,A\in S,\,B\notin S}
\min\!\left\{1,\,2\left[1-\max_c\Pr(C_S=c\mid D=q)\right]\right\}.
```
Every sector contributing to a successful branch must itself have that branch's pure Bell output. The inequality therefore also covers protocols that leave the initial charge unmeasured. [Vidal (1999)](https://doi.org/10.1103/PhysRevLett.83.1046)

Enumerating the 65,536 orientations and 64 terminal-separating cuts gives $`18{,}643/32{,}768`$. The simpler strongly connected component ceiling is $`20{,}801/32{,}768`$ on the same instance.

### A circuit using reported ring charges

Read and report the initial charge vector. Choose a simple ring and measure the number on its two local ring modes at each incident vertex. If every ring number is one, the ring state has two oriented alternatives and can supply an encoded pair between any two ring vertices. A nonunit ring number fixes both adjacent ring edges and hence the full ring orientation by propagation. In both cases the remaining state is the uniform fiber on the unmeasured edges with the recorded ring charges subtracted. In the successful branch the ring state factors from this residual fiber. All operations use local modes and classical reports.

Keep successful rings on disjoint raw edge sets. If a chain of accepted rings joins the terminals, extract the ring pairs and swap them. Otherwise choose another ring or pool available two-hop paths. A finite dynamic program on the residual graph, its fiber and the existing ring components evaluates this policy. For each candidate ring it partitions the orientations by the local ring numbers, evaluates the continuation on each outcome and adds their accepting orientation counts. The all-one branch carries both full ring orientations as well as the same residual fiber. Pooling counts residual sectors with a consistent two-hop path each way. Its operations commute with the initial number measurements, which allows this count to be made within each initial fiber.

The [exact finite checks](../verification/README.md#same-color-k44-routing-bounds) give the following bounds and attained probabilities.

| Measurement policy or upper bound | Probability |
| --- | ---: |
| Four-path pooling | $`55/128`$ |
| Best of pooling or a fixed choice of one or two rings after the initial charge record | $`443/1024`$ |
| Adaptive choice after every tested ring record, with pooling as a fallback | $`1809/4096`$ |
| Best relaxed cut in each sector | $`18{,}643/32{,}768`$ |

The adaptive policy accepts 28,944 of the 65,536 orientation weights, corresponding to a Bell-pair success probability of about 44.17%. The cut bound gives about 56.89%. These probabilities apply to this finite graph and do not characterize the large-graph optimum.

[Random four-regular graphs](degree-four-routing.md) · [Scientific account](README.md)
