# When can two nodes share an encoded Bell pair?

Let $`G=(V,E)`$ be a finite undirected graph with two distinct terminals $`A,B`$. Each edge supplies a normalized single-excitation Bell state with one mode at each incident node. Separate nodes can communicate classically and act on their own modes within fixed-charge subspaces. For the upper bounds on success probability, take the node phases to be independently uniform, with the same phase on all modes at each node. The protocols also work for arbitrary fixed values of those unknown node phases.

In an occupation basis vector, orient each edge toward its occupied endpoint. For an orientation $`\omega`$, denote the vector of vertex indegrees by $`q(\omega)`$. Let $`\Omega_q`$ be the set of orientations with indegrees $`q`$, and write $`|\omega\rangle`$ for the corresponding joint occupation state. Number measurements reveal $`q`$. The twirled state and its conditional pure states are

```math
\rho_G = \sum_{q:\,|\Omega_q|>0}\frac{|\Omega_q|}{2^{|E|}}
|\Omega_q\rangle\langle\Omega_q|,
\qquad
|\Omega_q\rangle = \frac{1}{\sqrt{|\Omega_q|}}
\sum_{\omega\in\Omega_q}|\omega\rangle .
```

An arbitrary fixed node phase contributes a single common scalar phase in each sector, so conditioning on charges yields the same states. The orientation representation, equal-indegree cycle reversals and single-cycle localization on bipartite graphs are already used in [Entanglement Valence Threshold](https://github.com/GoGoKo699/Entanglement-Valence-Threshold/tree/e3217a7babf8448c77799747623294c3c05d8357/science). The underlying cycle-reversal equivalence is classical. [Gioan, *Enumerating degree sequences in digraphs and a cycle-cocycle reversing system*](https://doi.org/10.1016/j.ejc.2005.11.006).

## Conditional graph criterion

Fix a charge sector of positive probability. The terminals can obtain an exact encoded Bell pair with positive conditional probability if and only if they belong to the same strongly connected component in an orientation compatible with that sector. If $`\omega`$ is a uniformly random orientation, the optimal unconditional probability $`P^*(G;A,B)`$ therefore obeys

```math
P^*(G;A,B)\leq
\Pr_\omega\!\left[A,B\text{ belong to the same strongly connected component of }\omega\right].
```

### Factorization across strongly connected components

Take $`\omega,\omega'\in\Omega_q`$. In $`\omega`$, the set of edges reversed by $`\omega'`$ is a balanced directed subgraph, since each vertex gains and loses the same number of incoming edges. Every finite balanced directed subgraph decomposes into edge-disjoint directed cycles. Reverse them in turn. Each reversal preserves reachability because a traversed edge that was reversed can be replaced by the rest of that reversed cycle. The same reasoning applies to the reverse transformation. Consequently all orientations in $`\Omega_q`$ have the same strongly connected components.

Every edge between components is fixed throughout $`\Omega_q`$, since no such edge belongs to a directed cycle. The charge still required at each vertex after these fixed edges are removed is determined. For each component, its internal edge orientations are then constrained only by those remaining charges within that component. Joining any one admissible internal choice per component gives a valid global orientation, and this gives a bijection. The equal-amplitude state factorizes over the components, with each fixed external edge contributing product half-mode occupations.

If $`A,B`$ are in distinct components, the conditional state is separable across a cut that places them on opposite sides. Classical communication and local operations cannot create entanglement across that cut. This is true even if parties within each side could act jointly. Coherent access across different charge sectors is absent in $`\rho_G`$. For any heralded exact Bell-pair protocol, a success branch on $`\rho_G`$ has the same pure Bell output on each component of the mixture that contributes to that branch. This follows because a positive mixture can have rank-one support only if each nonzero positive summand has that support. An unsuccessful sector thus contributes zero to the overall success probability.

### A local measurement gives positive success inside a component

Suppose the terminals are in one strongly connected component. Any partition with $`A`$ and $`B`$ on opposite sides has an edge of that component crossing the cut. Such an edge lies on a directed cycle in $`\omega`$. Reversing that cycle produces a second orientation in the same sector. The mixed pair of left and right basis patterns obtained from these two orientations is absent from the support of the sector state. Specifically, the changed crossing edge would have either two excitations or none. In a product pure state across the cut, the support would be Cartesian. Therefore this sector state is entangled across every cut that separates the terminals.

Localization of bipartite pure entanglement by measuring other parties is known for genuinely multipartite pure states. The following argument gives a finite set of candidate projections for our fixed-charge spaces. [Zwerger et al., *Device-Independent Detection of Genuine Multipartite Entanglement for All Pure States*, Theorem 2](https://arxiv.org/abs/1809.02381).

Give each helper $`v`$ a vector $`z_v`$ of formal bra coordinates in a basis of its space. The unnormalized conditional terminal state has coefficient matrix $`M(z)`$, whose entries are polynomials of degree one in the coordinates of each helper. The row and column indices label the terminal bases.

Suppose all such projections give terminal states of Schmidt rank at most one. All $`2\times2`$ minors of $`M(z)`$ then vanish identically. Over the polynomial ring, divide a nonzero column by the greatest common divisor of its entries to obtain a primitive column $`u`$. Every column is proportional to $`u`$ over the fraction field. Writing its multiplier as a reduced fraction shows the denominator divides every entry of $`u`$ and must be a unit. Thus $`M=u v^{\mathsf T}`$ for a row of polynomial multipliers.

For each helper, the smallest and largest homogeneous degrees both add under multiplication of nonzero polynomials. Since each nonzero entry of $`M`$ has degree exactly one in that helper's coordinates, each nonzero factor entry is homogeneous in that group. Comparing to one fixed nonzero entry of the opposite factor shows that the factor degree is common to all its nonzero entries. The degrees of the two factors add to one, so each helper's coordinates occur in just one factor. Taking coefficients in $`M=u v^{\mathsf T}`$ now gives a pure product state across a cut, with the degree-one helpers from $`u`$ on $`A`$'s side and the rest on $`B`$'s. This contradicts entanglement across every terminal-separating cut.

Hence at least one minor is a nonzero polynomial. Its degree in each coordinate is at most two, so it is nonzero somewhere on the Cartesian grid with coordinate values in $`\{0,1,2\}`$. Indeed, a polynomial of individual degree at most two vanishing on this grid is zero by repeated univariate interpolation. Choose those local bras, normalize them and make each one an outcome of a fixed-charge projective measurement. The selected joint outcome has nonzero probability and gives Schmidt rank at least two. Projecting onto two nonzero Schmidt coefficients and applying a bipartite local filter gives a Bell pair with positive probability. Local fixed-charge unitaries, with local number-eigenstate auxiliary modes if required, can put this pair into dual-rail form. The grid provides a finite choice of bras and can grow exponentially with the size of the network.

## Criterion before measuring charges

The unconditional probability is positive exactly when there are two edge-disjoint undirected paths from $`A`$ to $`B`$.

If there are two such paths, orient them in opposite directions. Any completion of the orientation gives a sector in which the terminals are strongly connected. There is also a direct cycle protocol. The union of the two paths is connected and has even degree at every vertex. Decompose its edges into simple undirected cycles and choose a chain of cycles meeting successively in vertices from $`A`$ to $`B`$. This chain exists because the cycle intersection graph of the connected union is connected. On a ring of length $`\ell`$, the branch where every node has one excitation on its two ring modes has probability $`2^{1-\ell}`$ and retains only the two consistently directed cycles. The resulting fixed-charge superposition has one encoded qubit per ring node. Measuring logical $`X`$ at the other nodes of a ring gives an encoded Bell pair between the chain junctions. Each junction swaps its two encoded pairs locally. The cycles use disjoint edge resources, and their operations can act separately on the cycle mode sets even if some nodes are shared. All cycle accepts have strictly positive joint probability.

If there are fewer than two edge-disjoint paths, the edge form of Menger's theorem gives an undirected cut separating $`A`$ and $`B`$ with at most one edge. No orientation supplies both directed crossings, so the conditional criterion gives zero probability.

## The probability bound can be strict

Consider the five-edge graph with an orientation

```math
U\to V,\quad V\to A,\quad A\to U,\quad V\to B,\quad B\to U.
```

Its indegrees in order $`(U,V,A,B)`$ are $`(2,1,1,1)`$. This sector contains exactly three orientations, obtained by keeping the displayed orientation or reversing exactly one of the two directed triangles. The only directed cycles in the displayed orientation are those triangles, which share an edge, and the balanced-difference decomposition excludes any further orientations. All four vertices are strongly connected in this sector.

The occupation pattern at $`A`$ is the same in two of the orientations and different in the third. The cross terms vanish on tracing out the other sites, since they contain different complementary occupations on the modes paired with $`A`$. Its reduced density matrix has nonzero eigenvalues $`2/3`$ and $`1/3`$. Even if the other three laboratories were one quantum coalition, the optimal success probability across $`A|\{U,V,B\}`$ would be at most $`2(1-2/3)=2/3`$ by the single-copy bipartite pure-state conversion bound. [Vidal, *Entanglement of Pure States for a Single Copy*](https://doi.org/10.1103/PhysRevLett.83.1046).

That probability is achievable under separate local operations. At $`U`$, project onto the span of its occupation patterns for the two single-cycle reversals. Its original orientation has a third, orthogonal pattern, so this projection leaves the equal superposition of the two reversals and succeeds with probability $`2/3`$. Each of $`U,V`$ then measures logical $`X`$ on its own two-pattern space. Each remaining terminal has distinct local patterns in the two surviving terms, so correcting the recorded sign gives an encoded Bell pair.

In any orientation where $`A,B`$ share a strongly connected component, both must have indegree one, and $`U,V`$ must also be in the component as the two neighbors of $`A`$. Their degrees are three, so their indegrees must be one or two, summing to three. The only sectors to count are thus $`(2,1,1,1)`$ and its reversal $`(1,2,1,1)`$. Each sector has weight $`3/32`$ and conditional optimum $`2/3`$. The graph criterion gives an unconditional upper bound of $`3/16`$ while the exact optimal success probability is $`1/8`$.

[Continue to the exact parallel-path result](parallel-paths.md).
