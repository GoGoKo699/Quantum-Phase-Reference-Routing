# Routing on random four-regular bipartite graphs

A four-regular graph supplies four raw half-link modes per node. Can an ideal one-batch protocol use those modes to deliver an exact encoded Bell pair between distant, specified terminals? We consider uniformly random simple four-regular bipartite graphs with $`n`$ labeled vertices per color. Choose distinct terminals $`A,B`$ uniformly from one color class before the batch. By label symmetry, the same distribution of success probabilities holds for any two fixed distinct labels in that class.

The [graph criterion](graph.md#conditional-graph-criterion) identifies the charge records where local extraction is possible with positive probability. Draw a fair independent orientation $`\omega`$ to sample the law of the charge record. Define
```math
Q_n(G;A,B)=\Pr_\omega(A,B\text{ lie in the same strongly connected component}),
\qquad
P^*(G;A,B)\leq Q_n(G;A,B).
```
The orientation is an analysis variable. The protocol has the supplied graph, the charge record and its own measurement outcomes.

## Probability of an eligible sector

**Theorem.** Define
```math
x=\frac{\sqrt 5-1}{2},
\qquad
s=1-2x^4+(2x-1)^4.
```
Then $`Q_n(G;A,B)`$ converges in probability over the graph and terminal draw to $`s^2=0.505961279498\ldots`$. Its expectation has the same limit. In particular, for every $`\varepsilon\gt0`$, with probability tending to one over that draw,
```math
P^*(G;A,B)\leq s^2+\varepsilon.
```
The charge-sector criterion concerns positive success on each finite graph. The conditional probability of extracting a pair can decrease with graph size even in an eligible sector.

### Local upper bound

On the infinite four-regular tree, each branch independently fails to sustain an infinite outward directed path with probability $`x`$. The initial edge points outward with probability $`1/2`$. If it does, its three successor branches all fail with probability $`x^3`$. Extinction gives the smallest solution of $`x=(1+x^3)/2`$ on $`[0,1]`$, which is the value above. Inward paths obey the same recursion. Inward and outward survival on one branch are disjoint because they require opposite directions of its initial edge. Inclusion–exclusion over four independent branches gives $`1-2x^4+(2x-1)^4`$ as the probability that the root has both infinite arms.

For each fixed radius $`r`$, the two terminal balls are disjoint trees with probability tending to one. In the bipartite configuration model this follows by exposing a bounded number of stub matches. It holds after conditioning on simplicity because the probability of simplicity is bounded below. For this degree the probability tends to $`\exp(-9/2)`$, given by the absence of double edges in the configuration model. [McKay, Wormald and Wysocka (2004)](https://doi.org/10.37236/1819)

A common strongly connected component forces both an inward arm and an outward arm from each root to the boundary of its ball. Let $`s_r`$ be the probability of the two arms reaching radius $`r`$ at a single tree root. Conditional on a graph with these disjoint tree balls, edge orientations are independent, and the probability of the necessary event is $`s_r^2`$. Taking the large-graph limit first and then increasing $`r`$ yields $`\limsup_{n\to\infty}\mathbb E Q_n\leq s^2`$.

### Matching lower bound

Use the four-stub bipartite configuration model with a fair direction per edge. An equivalent sampler first draws $`K\sim\mathrm{Bin}(4n,1/2)`$, the number of edges directed left to right. Choose uniformly $`K`$ outbound left stubs and independently $`K`$ inbound right stubs. Match these two sets uniformly and match the remaining two sets uniformly. For any particular directed matching, multiplying the probability of $`K`$, the choices of stubs, and the two matchings gives $`2^{-4n}/(4n)!`$, the same probability as matching first and then orienting. On each side separately the stub directions are marginally independent fair bits. In particular the empirical vertex indegree law on both sides tends in probability to $`\mathrm{Bin}(4,1/2)`$. The two direction-compatible matchings stay uniform on their remaining stubs after partial exposure.

Expose the radius-$`r`$ balls around the terminals. For each terminal use separate forward and backward searches, initialized with the unpaired stubs that extend the corresponding directed arm from a vertex in the last generation of its ball. The forward search holds outbound stubs and the backward search holds inbound stubs. Require each of these four initial queues to have at least $`M`$ stubs. For fixed $`M`$ this event has probability approaching $`s^2`$ as $`r`$ increases after the large-graph limit. The two rooted graphs converge locally to disjoint trees, with the stubs one generation further than $`r`$ sampled from fair orientations. Away from the root, each directed arm grows as a branching process with offspring law $`\mathrm{Bin}(3,1/2)`$, whose generation size tends to infinity on survival.

Set $`m=\lfloor n^{2/3}\rfloor`$. Grow the four queues sequentially, stopping a queue once it reaches size $`m`$. Mark both initial balls as visited. In a forward step, select an outbound stub from the active queue, sample its uniform compatible inbound stub on the opposite side and add the unpaired outbound stubs of the sampled vertex if it is fresh. In a backward step, interchange inbound and outbound. Each step rejects previously visited vertices, including vertices encountered by earlier queues. A rejected match consumes the selected stub and adds no children.

As long as at most a fixed multiple of $`m`$ matches has been exposed, the empirical degree law gives conditional mean $`3/2-o(1)`$ for the number of added stubs, uniformly over such histories. A fresh forward sample is weighted by indegree, so the ratio is given asymptotically by
```math
\frac{\mathbb E[D(4-D)]}{\mathbb E[D]}=\frac32,
\qquad D\sim\mathrm{Bin}(4,1/2).
```
The backward ratio equals this by symmetry. Exposed, visited and rejected vertices remove only $`O(m)`$ bounded-degree stubs from pools of order $`n`$. The queue size changes by a value in $`[-1,2]`$ with conditional mean at least $`1/4`$ for sufficiently large $`n`$. For a fixed sufficiently small $`t\gt0`$, the exponential of minus $`t`$ times the queue size is therefore a supermartingale until exhaustion, hitting $`m`$, or a cap of $`C m`$ steps. This bounds exhaustion from size $`M`$ by $`e^{-tM}`$. For sufficiently large fixed $`C`$, bounded-increment martingale concentration bounds the probability of reaching the cap without either exhausting or hitting $`m`$ by $`o(1)`$.

An earlier search consumes a stub from a later fixed-size seed with probability $`O(m/n)`$. Each earlier grown queue loses an expected $`O(m^2/n)=o(m)`$ stubs to later searches. Thus with probability tending to one each grown queue still has $`m-o(m)`$ stubs after the four searches. These estimates are for fixed $`M,r`$ and $`C`$. The total failure probability at this stage, conditional on good seeds and the empirical law, is at most $`4e^{-tM}+o(1)`$.

Connect the forward queue of $`A`$ to the backward queue of $`B`$, and then the forward queue of $`B`$ to the backward queue of $`A`$. Select the majority color of stubs in each queue. If the colors of the two queues to be connected differ, try a fixed fraction of the selected outbound stubs for a direct match to the inbound pool. Each test succeeds with probability $`\Omega(m/n)`$ until the first connection. If the colors agree, use a two-edge path through a fresh intermediate vertex of the opposite color. An outbound test stub reaches a fresh vertex with an unused outgoing stub with probability bounded below, by the empirical degree law. Matching one such outgoing stub to the selected inbound pool then succeeds with probability $`\Omega(m/n)`$. In either case stop on unintended depletion of a fixed fraction of any reserved pool. Such depletion has probability $`o(1)`$ because the expected unintended consumption is $`O(m^2/n)`$. With $`\Theta(m)`$ trials available for each connection, the conditional probability of failing to make it is at most $`\exp[-\Omega(m^2/n)]+o(1)`$. Both connections together give a directed path in each direction between the terminals.

Conditioning the construction on simplicity preserves the $`o(1)`$ errors and multiplies the seed-extinction bound by at most a constant. The probability of the seed event itself still tends to its tree value because the neighborhoods are asymptotically trees and the orientations are fair conditional on the graph. Take the large-graph limit, increase $`r`$ for each fixed $`M`$, and then let $`M`$ grow. This gives $`\liminf_{n\to\infty}\mathbb E Q_n\geq s^2`$.

For convergence in probability, the deterministic bound $`Q_n\leq s_r^2`$ holds on the disjoint-tree-ball event. The expected deficit there is at most $`s_r^2-\mathbb E Q_n+o(1)`$. Apply Markov's inequality to this deficit for fixed $`r`$, then let $`r`$ grow so that $`s_r^2\to s^2`$.

## A local protocol with inverse-polynomial success

For some constant $`C_0\gt0`$, a graph-chosen fixed-charge protocol achieves
```math
P^*(G;A,B)\geq (2n)^{-C_0}
```
with probability tending to one over the graph and terminal draw. On that graph event the construction works for every pair of distinct terminals. The protocol requires neither extra edge states nor several batches.

To prove the graph part, suppose that a connected four-regular graph has edge expansion $`h\gt0`$, meaning every vertex set $`S`$ of size at most $`|V|/2`$ has at least $`h|S|`$ outgoing edges in the undirected graph. Growth of radius balls gives diameter $`O_h(\log |V|)`$. Choose a shortest terminal path $`P`$ with $`\ell=O_h(\log |V|)`$ edges and delete its edges. Every terminal-separating cut has even cardinality because the graph is even-regular. The path crosses each such cut an odd number of times. At least one cut edge survives, so the two terminals remain connected.

In the residual component containing both terminals, each terminal ball grows by at least one vertex per step until it reaches size $`2\ell/h+1`$ or saturates the component. If it saturates earlier the residual distance is already $`O_h(\ell)`$. Above that threshold and up to half the total graph, a ball has residual boundary at least $`h|S|-\ell\geq h|S|/2`$. Its size grows geometrically, since a newly reached vertex has degree at most four. Both terminal balls therefore meet after $`O_h(\log |V|)`$ steps. This gives a second logarithmic-length path edge-disjoint from $`P`$.

Now decompose the union of the two paths into edge-disjoint simple cycles and choose a chain of cycles meeting at vertices from $`A`$ to $`B`$. The [cycle protocol](graph.md#criterion-before-measuring-charges) yields a fixed-charge Bell pair on a ring of length $`\ell_i`$ with probability $`2^{1-\ell_i}`$. Different rings use disjoint raw states and the branch probabilities are independent even at shared laboratories, since the tests are separately invariant under each common phase. Upon joint success the junctions swap the pairs. The total ring length is $`O_h(\log |V|)`$, giving the stated lower bound on any graph with a fixed positive $`h`$. For the random ensemble, Brito, Dumitriu and Harris's bound on the second-largest adjacency eigenvalue gives a fixed gap below four with high probability, which implies such edge expansion. [Spectral gap theorem](https://doi.org/10.1017/S0963548321000249)

## A separation from color-coalition entanglement

The companion project studies the same state with collective processing allowed inside each color. Its degree-four theorem gives color-coalition entanglement at least $`8L\alpha_4-I_4`$ on each connected simple four-regular bipartite graph with $`8L`$ vertices, where $`\alpha_4\gt0`$ and $`I_4`$ are constants. [Entanglement Valence Threshold, degree-four bound](https://github.com/GoGoKo699/Entanglement-Valence-Threshold/blob/e3217a7babf8448c77799747623294c3c05d8357/science/degree_four.md#the-lower-bound)

To see how topology affects individual routing at that same degree, take a chain of $`L`$ copies of $`K_{4,4}`$. At each boundary choose one reserved edge from each neighboring block. Exchange their right endpoints so the two replacement edges cross the boundary. Reserve disjoint edges for the two boundaries of each interior block. This preserves connectivity, simplicity, bipartiteness and four-regularity. Choose terminals in the first and last blocks. To belong to the same strongly connected component their orientations must give one directed edge each way at every boundary. Each boundary passes this test with probability $`1/2`$ and the tests use disjoint edges. Thus
```math
P^*(G;A,B)\leq 2^{-(L-1)}.
```
This example has extensive color-coalition entanglement and exponentially small routing probability. The ensemble above separately addresses typical random topology. The [arbitrary-cut identity](https://github.com/GoGoKo699/Entanglement-Valence-Threshold/blob/0e532750de184651381c4ed6db5836315c7e6670/science/entropy_identity.md#entanglement-across-an-arbitrary-cut) explains which orientations contribute to entanglement across a terminal-separating cut.

## What remains open

The random-graph upper bound and inverse-polynomial protocol leave open whether $`P^*(G;A,B)`$ stays bounded away from zero under general separated-node local operations and classical communication. The limit of $`Q_n`$ quantifies the availability of eligible sectors. An answer about routing needs to control the probability of extraction within those sectors. The [charge-adaptive protocols](charge-adaptive-routing.md) give explicit finite examples and a restriction on graph-fixed helper measurements.

[Scientific account](README.md) · [Finite checks](../verification/README.md#same-color-k44-routing-bounds)
