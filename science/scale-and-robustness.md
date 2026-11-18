# Layout, loss, and phase drift

A logical bond can be built between two laboratories by pooling parallel two-hop paths. If the raw link phases are common to all modes at each node, the bond is either heralded as an exact encoded Bell pair or declared unavailable. This gives an ordinary random routing graph. A differential phase between modes changes the fidelity of available bonds as well as what can be guaranteed along a route.

## A square mesh from two-hop paths

Replace each bond of a square lattice by five paths, each with its own intermediate node and two elementary edges. The [parallel-path optimum](parallel-paths.md) gives these success probabilities for four and five such paths, respectively.

```math
p_4=1-2(3/4)^4+(1/2)^4=55/128,\qquad
p_5=1-2(3/4)^5+(1/2)^5=285/512 .
```

Run the receiver once for each bond, using distinct modes for different bonds even where they share a terminal laboratory. For any fixed node phases, the raw states and receiver operations factor across these disjoint registers. Every success flag has a phase-independent probability, since the receiver uses fixed local charge sectors. Averaging over phases shared by several bonds therefore leaves their flags independent. A bond is open when it supplies an encoded Bell pair.

The bond percolation threshold on the square lattice is $`1/2`$. Let $`\theta(p)`$ be the probability that a site belongs to the infinite open cluster. When $`p>1/2`$, uniqueness and positive association give a probability at least $`\theta(p)^2>0`$ that two specified sites belong to the same infinite cluster. The standard percolation step then becomes a routing protocol. Use the open flags to choose a simple path, measure the two encoded qubits at every internal site in an encoded Bell basis, and use the announced outcomes to correct the output. Each such measurement acts within a fixed local charge sector. The network construction uses percolation once each effective bond can be activated from the phase-uncertain raw links. [Harris and Kesten threshold](https://sites.math.northwestern.edu/~auffing/papers/K12.pdf) · [Burton and Keane uniqueness](https://sites.math.northwestern.edu/~auffing/papers/BurtonKeane.pdf) · [Acín, Cirac and Lewenstein on entanglement percolation](https://arxiv.org/abs/quant-ph/0612167).

There is a finite version of this bound. Put the sites in the inner square of radius $`R`$ and use a square of radius $`2R`$ for the hardware, with distances measured in the underlying square lattice. If both sites join the infinite cluster of an extension of the same bond process and an open circuit surrounds the inner square in the annulus, their paths to infinity meet that circuit before leaving the hardware. The absence of such a circuit implies a radial path of dual closed edges in the annulus. Dual bonds are open with probability $`1-p<1/2`$, so subcritical exponential decay and a union bound over $`O(R)`$ inner-boundary sites bound the failure of the circuit event. The finite square thus supplies an exact encoded pair with probability at least

```math
\theta(p)^2 - C(p)R\,e^{-c(p)R}
```

for some positive constants when $`p>1/2`$. At $`p=285/512`$, the mean-field lower bound for Bernoulli percolation gives $`\theta(p)\ge 58/285`$. The statement is a one-batch probability bound for terminals in an expanding finite square. [Duminil-Copin and Tassion, sharpness of Bernoulli percolation](https://arxiv.org/abs/1502.03051).

For comparison, put all redundancy into $`k`$ internally disjoint paths of a common length $`\ell`$ between the terminals. If $`k2^{1-\ell}\to\lambda`$, the pooled success probability tends to $`(1-e^{-\lambda/2})^2`$. A prescribed disjoint pairing of the paths gives isolated cycles of length $`2\ell`$, with per-cycle success probability $`2^{1-2\ell}`$. Those independent cycles require $`\Theta(4^\ell)`$ paths for fixed success probability, while pooling requires $`\Theta(2^\ell)`$. The square layout places the redundancy around each local bond and uses bounded degree over increasing distances.

## Independently flagged whole-link loss

Suppose every raw edge independently survives with probability $`s`$. Flags are supplied independently of its quantum state, and a missing edge is deleted before local charge processing. This model treats the erased modes as absent, or removes them using the flags before measurement.

For a path of length $`\ell_i`$, its total activation probability is

```math
a_i=s^{\ell_i}2^{1-\ell_i}.
```

Conditioned on a deletion record, incomplete paths have surviving pieces that attach to the rest at at most one endpoint. None of these pieces lies on a directed cycle. They cannot increase the upper bound from the [charge-sector factorization](graph.md), and deleting them from the receiver leaves that bound attainable. The surviving path activation events are independent. Averaging the conditional optimum over the records therefore gives the same inclusion–exclusion formula with the new $`a_i`$.

For $`k`$ two-hop paths the bond probability becomes

```math
p_k(s)=1-2(1-s^2/4)^k+(1-s^2/2)^k .
```

For five paths, $`p_5(s)`$ is strictly increasing on $`0<s\le1`$. Its unique root at $`p_5(s)=1/2`$ is $`s\approx0.9555985166`$. Hence this mesh percolates for flagged loss below about **4.44% per raw edge**, with otherwise ideal links and operations. Four paths stay below the threshold even at unit raw survival. This is a threshold for the specified bond-by-bond architecture.

For any fixed $`s>0`$ one can choose a finite number of two-hop paths to exceed the same threshold. As $`s\to0`$, the necessary and sufficient width is $`\Theta(s^{-2})`$. For the upper bound, $`p_k(s)\ge1-2\exp(-ks^2/4)`$. For the lower bound, an open bond needs one active path each way. A union bound over ordered pairs of paths gives $`p_k(s)\le k(k-1)s^4/16`$. Increasing this width increases the number of raw modes stored at the terminals.

## Differential phase noise

Let each surviving edge have a residual phase $`\varphi_e`$ between its endpoint occupations in addition to the common node rotations. In the pooling measurement, the two selected endpoint occupation patterns differ by exchanging two active paths. The surviving coherence is therefore sensitive to the phase around the loop formed by those paths. With signs set by the chosen orientation convention, the relative phase is

```math
\Delta=\sum_{e\ \mathrm{on\ the\ loop}}\epsilon_e\varphi_e,
\qquad \epsilon_e\in\{-1,1\}.
```

The activation, helper sign, endpoint charge, and pair selection records have probabilities determined by occupations. At a helper on an activated path, the logical X outcome is uniform because opposite path orientations still occupy orthogonal endpoint states. At the terminal, the charge and the pair-selection effects are diagonal in the occupation basis. These facts allow averaging the unknown phases after conditioning on the herald and the selected loop.

For independent centered Gaussian residual phases, with variance $`\sigma_e^2`$ for edge $`e`$, the output visibility and Bell fidelity on that loop are

```math
v=\mathbb E[e^{i\Delta}]
  = \exp\!\left[-\tfrac12\sum_{e\ \mathrm{on\ the\ loop}}\sigma_e^2\right],
\qquad
F=\tfrac12(1+v).
```

The two eigenstates of this dephased logical pair are the two Bell phase labels, with phase error probability $`(1-v)/2`$. For two equal-length paths of $`\ell`$ edges and homogeneous residual variance $`\sigma^2`$, the visibility is $`e^{-\ell\sigma^2}`$. The two-hop gadget has $`v=e^{-2\sigma^2}`$. Its open probability remains $`p_k(s)`$, since opening observes occupations.

An encoded Bell measurement along a selected route combines the two incoming phase labels by their parity. After known measurement corrections, the phase label over the route is the parity of its bond phase errors. The effective errors are independent on edge-disjoint gadgets, even when the route is chosen using phase-independent flags. With $`m`$ open bonds on the route, the visibility and fidelity are therefore

```math
v_{\mathrm{route}}=\prod_{j=1}^{m}v_j,\qquad
F_{\mathrm{route}}
=\tfrac12\bigl(1+e^{-2m\sigma^2}\bigr)
\quad\text{for the homogeneous two-hop mesh.}
```

A fixed target $`F_*>1/2`$ in this direct swapping protocol requires $`2m\sigma^2\le-\log(2F_*-1)`$. Macroscopic connectivity by itself guarantees a route to swap. Its fidelity can still approach $`1/2`$ at any fixed positive residual variance.

There is also an exact-output obstruction for finite uses of full-rank edge noise. Suppose every surviving edge density is strictly positive on the two-dimensional span of its occupation alternatives. The raw product density, followed by the node twirl, then dominates a positive multiple of the identity on the common orientation space. This identity is a sum of product occupation projectors. Any completely positive accepted branch with positive probability on the raw density must also accept this separable component with positive probability, because both inputs have the same support. Local operations and classical communication preserve separability on that component. The accepted output therefore cannot be a pure entangled pair. This applies after conditioning on any whole-link deletion record and to any finite number of independent batches with full support. Uniformly random independent phases on all edges give the wholly diagonal, separable limiting case.

## Fixed-fidelity repair with charged repetitions

For independent differential phase errors across raw attempts and ideal encoded operations and storage, repeated batches can suppress the accumulation. The following phase-error repetition procedure uses the logical pair from the same gadget. Set $`v>0`$ to its visibility, and collect an odd number $`n`$ of independently heralded copies. Apply an encoded Hadamard on both ends of every copy to convert phase errors into bit errors. At each end use the first pair as the control of a local encoded CNOT into every other pair, then measure the targets in the computational basis. The XOR of the target measurements reveals each error label relative to the first pair's label. There are two consistent error strings and they are complements. Choose the lower-weight string, correct the first pair accordingly, and undo the Hadamards on it. All these operations act within fixed-charge logical registers.

The retained pair has a phase error exactly when a majority of the original phase labels were erroneous. For independent labels of mean $`(1-v)/2`$, its probability, averaged over the purification record, is bounded by

```math
\Pr(\text{residual phase error})\le e^{-n v^2/2}.
```

For a predetermined route of $`m`$ bonds with per-gadget success probability at least $`p>0`$, attempt every bond in each of $`T=\lceil2n/p\rceil`$ declared batches and store the first $`n`$ successes per bond. A binomial lower-tail bound gives failure probability at most $`e^{-n/4}`$ for any one bond. Declare a failure if any bond falls short. Conditional on enough successes, accepted copies retain their independently distributed phase errors. Purify one pair per bond and perform the route swaps. The probability of a heralded failure is at most $`m e^{-n/4}`$, and the conditional Bell infidelity is at most $`m e^{-nv^2/2}`$. To bound both by $`\delta`$, one can take the next odd integer at or above

```math
n \ge \max\{4,\,2/v^2\}\log(m/\delta).
```

For fixed $`p,v>0`$ and fixed gadget width, this uses $`O(m\log(m/\delta))`$ raw link attempts and $`O(\log(m/\delta))`$ stored modes per relay. This is a separate repeated-batch guarantee. Correlated phase drift across attempts, storage decoherence and faulty encoded gates require additional models.

## Modes, local operations, and messages

For a finite square with $`B`$ underlying bonds, one noiseless batch uses $`10B`$ elementary link states and $`20B`$ endpoint modes. An original lattice site has at most 20 raw half-link modes. Every added two-hop relay has two raw modes, and its number-preserving basis measurement reports one of vacuum, two excitations, or the two signs in the one-excitation subspace. It can send a two-bit result to each terminal. At an original site there are at most four distinct gadget registers.

For five paths, the endpoint charge has at most six values. The subsequent pair-selection measurement has at most 30 outcomes in any given sector. Indeed, the number of unordered adjacent pairs of $`K`$-subsets of $`r`$ active paths is $`\binom rK K(r-K)/2`$ with $`r\le5`$. The result can be sent in five bits once the active set and charge are known. The receiver can implement that measurement by coupling the fixed-charge modes to a register with 30 orthogonal labels of equal local charge, and measuring its label. Five dual-rail qubits suffice for such a register. This local workspace can be reused across incident bonds. The selected pair physically occupies the two modes whose labels were exchanged, with the same spectator occupation in the two alternatives. An encoded swap uses a number-preserving measurement on the four modes of two local dual-rail qubits, returns two classical bits, and consumes those local halves. Arbitrary fixed-charge local control is supplied; optical gates and detector hardware would need separate accounting.

A central controller with a shared bond ordering can collect one open bit per logical bond and find a route by graph search. It can send each selected relay its two neighboring directions, collect the two-bit swap outcomes, and send the endpoint corrections. This uses $`O(B+m)`$ payload bits for the route control plus the gadget records. If the controller is in the mesh and classical messages travel only between neighboring lattice sites, preassigned paths of length $`O(R)`$ give $`O((B+m)R)`$ payload bit-hops. This is an explicit centralized upper bound. The modes holding successful pairs must wait while flags, route instructions and corrections propagate. The distance-independent bound is on success probability per supplied batch. Clock time and generation rate also depend on preparing raw links, processing at each node and moving the classical messages.

For the repetition repair, each purification discards $`n-1`$ logical pairs by local measurement, uses an encoded CNOT into each of their halves on both sides, and exchanges their one-bit readouts. This adds $`O(mn)`$ local encoded operations and payload bits, while a relay stores at most $`2n`$ logical halves from its two route bonds before purification. Every raw link slot in the $`T`$ attempts is charged, including failed acquisitions.
