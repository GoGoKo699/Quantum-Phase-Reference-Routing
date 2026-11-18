# The exact success probability on parallel paths

Let the graph consist of $`k`$ paths from $`A`$ to $`B`$, with no shared interior vertices and with disjoint edges. Path $`i`$ has $`\ell_i`$ edges. An optional direct edge is a path of length one. Under the [charge-sector graph model](graph.md), the optimal one-batch probability of producing one exact encoded Bell pair is

```math
\begin{aligned}
a_i &= 2^{1-\ell_i},\\
P^*(G;A,B)
&= 1-2\prod_{i=1}^{k}(1-a_i/2)
     +\prod_{i=1}^{k}(1-a_i).
\end{aligned}
```

The impossibility part permits arbitrary local processing and classical communication under the twirled input. The attaining circuit uses only fixed-charge local processing. It consumes one raw state per elementary edge per batch, including failed batches.

## Why the upper bound has this form

An orientation contains a directed path from $`A`$ to $`B`$ if and only if one complete path is consistently oriented from $`A`$ to $`B`$. A directed walk can be shortened to a simple directed path, and every interior vertex of the graph is on just one path. The same statement holds with $`A`$ and $`B`$ exchanged. The terminals share a strongly connected component exactly when there is at least one consistently oriented path each way.

Path $`i`$ is consistently oriented forward with probability $`2^{-\ell_i}=a_i/2`$, backward with the same probability, and neither with probability $`1-a_i`$. These three-way outcomes are independent across paths by edge disjointness. The displayed expression follows by inclusion–exclusion for the probability that both directions occur, and the [general graph criterion](graph.md#conditional-graph-criterion) makes it an upper bound.

## The local protocol

**Identify active paths.** An internal node measures the total excitation count on its two path modes, keeping coherence between its two one-excitation patterns. It broadcasts the count. A path is active if all its internal counts are one. Its two possible orientations then run consistently in opposite directions. An inactive path has exactly one orientation compatible with its internal counts. An internal count of zero or two fixes both adjacent edges, and the known counts recursively determine the remaining edges in each direction. For a direct edge the active criterion is vacuous.

**Erase the orientation information at the helpers.** Every helper on an active path measures in the following basis of its one-excitation space and broadcasts the sign.

```math
\left\{ \frac{|10\rangle+|01\rangle}{\sqrt{2}},
        \frac{|10\rangle-|01\rangle}{\sqrt{2}}\right\}.
```

A known sign correction on one endpoint mode per path removes the product of those signs. The paths each have one endpoint excitation delocalized between $`A`$ and $`B`$, with only the common endpoint node phases unresolved. Inactive path modes can be ignored since their occupation is fixed by public internal counts. To see why none of the helper steps needs the unknown node phases, start with fixed phase values before averaging. The states on distinct paths factor at each fixed phase. At an active helper, its two patterns have equal charge and therefore pick up the same phase. The helper record probabilities are independent of the phases, and correction leaves the usual same-node phase on each of a terminal's active modes.

**Pool the active paths.** Let $`r`$ be the number of active paths, and measure the total charge $`K`$ on the active path modes at $`A`$. The conditional terminal state is

```math
|\Psi_{r,K}\rangle =
\binom{r}{K}^{-1/2}
\sum_{\substack{S\subseteq\{1,\ldots,r\}\\ |S|=K}}
|S\rangle_A\,|\overline{S}\rangle_B .
```

Here $`|S\rangle`$ denotes the occupation pattern with exactly the modes in $`S`$ occupied. The phase $`K\phi_A+(r-K)\phi_B`$ is common to every term and has no effect. If $`K=0`$ or $`K=r`$, the state is a product. If $`0<K<r`$, it has uniform Schmidt rank at least two and yields an exact encoded Bell pair deterministically by the next step. The entire protocol succeeds exactly on the sectors containing some active orientation in each direction. The success probability therefore equals the upper bound.

### A charge-preserving endpoint measurement

Use a local measurement at $`A`$ with a label for each adjacent pair of distinct $`K`$-subsets $`\{S,T\}`$, where adjacency means exchanging one occupied path for one unoccupied path. For each pair use the following measurement operator on the known charge sector.

```math
M_{\{S,T\}}=
\frac{|S\rangle\langle S|+|T\rangle\langle T|}
     {\sqrt{K(r-K)}} .
```

Each subset has precisely $`K(r-K)`$ adjacent subsets. Consequently these operators satisfy $`\sum_{\{S,T\}}M_{\{S,T\}}^\dagger M_{\{S,T\}}=I`$ on that sector, and the two surviving terms have equal amplitude. The label is sent to $`B`$. At both nodes, the occupations outside the two exchanged paths agree between the two terms and can be set aside. The two exchanged modes have exactly one excitation per terminal, supplying the dual-rail pair directly, up to a local logical basis choice. The measurement preserves local charge, and the basis change on the two output modes is also charge-preserving.

For a finite implementation, the measurement can be realized with a number-invariant outcome register: coherently write a uniform superposition of the unordered edges incident to the occupation pattern in the $`K`$-subset adjacency graph, then measure that register. The map is an isometry because the occupation pattern itself is retained. This describes the local instrument at fixed $`r,K`$. Hardware gate counts and storage budgets require an explicit synthesis and noise model.

## Consequences

For $`k`$ equal paths with $`\ell`$ edges, $`a=2^{1-\ell}`$. Along a sequence in which $`\ell\to\infty`$ and $`ka\to\lambda`$, the success probability tends to

```math
\left(1-e^{-\lambda/2}\right)^2.
```

Constant success probability bounded away from zero and one can be achieved with $`\Theta(2^\ell)`$ paths. For comparison, a fixed partition into disjoint pairs of paths that attempts the all-one ring sector independently on each resulting ring succeeds with probability

```math
1-\left(1-2^{1-2\ell}\right)^{\lfloor k/2\rfloor}.
```

This specified fixed pairing uses $`\Theta(4^\ell)`$ paths to reach the same probability scale. The improvement comes from keeping the active paths available until the endpoint charge outcome can certify a pool with both orientations.

When every path has two edges, $`a=1/2`$. Four paths give $`55/128`$ and five give $`285/512`$. Thus five paths cross the square-lattice independent bond threshold of one half. A circuit that treats each five-path gadget as a distinct mode set can therefore use the exact local conversion as the input to ordinary bond percolation and encoded entanglement swapping. [Kesten, *The Critical Probability of Bond Percolation on the Square Lattice Equals 1/2*](https://doi.org/10.1007/BF01197577).

The two-raw-state activation on a pair of laboratories comes from the standard local-number superselection setting. The parallel-path formula uses that mechanism after active-path detection and optimizes over all one-batch vertex-local protocols in the stated graph model. The final percolation construction uses the established idea of combining independent successful local conversions into long-distance routes. [Wiseman and Vaccaro, *The entanglement of indistinguishable particles shared between two parties*](https://doi.org/10.1103/PhysRevLett.91.097902). [Acín, Cirac and Lewenstein, *Entanglement percolation in quantum networks*](https://doi.org/10.1038/nphys549).
