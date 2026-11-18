# Thirty milestones for phase-reference-independent routing

Alice and Bob want a usable Bell pair across one bond of a square lattice. Five paths connect them. Each has two links and its own intermediate helper. Start with the physical occupation pattern on one link. End with a square lattice built from that same gadget.

Each station has a shared understanding target and one practice question. Open the feedback after choosing one of the four answers. Earlier milestones establish the route's conceptual dependencies. The Revise and Learn paragraphs also give enough information to reason through each question on its own.

[Anchor bridge](BRS_BRIDGE.md) · [Scientific account](../science/README.md)

## Phase I · Background and preliminaries

### M01 An excitation on one link

**Understanding target.** Relate one elementary link to the occupation patterns at its two ends.

**Revise.** A mode is a place that can hold an excitation. A supplied link puts exactly one excitation in two modes, one at each endpoint.

**Learn.** In a coherent superposition, the two occupation patterns can still interfere. Counting both modes separately reveals where the excitation is. A count of their sum only tells how many excitations they hold.

**Test.** What can a joint count of Alice's mode and the first helper's mode tell you about their raw link?

- **A.** It must give one and does not distinguish the two placements.
- **B.** It gives zero or two with equal probabilities.
- **C.** It must give two because the link has two modes.
- **D.** It gives one only when Alice's mode is occupied.

<details>
<summary>Check your answer</summary>

**A.** Either occupation pattern contains exactly one excitation.

</details>

[Source · Network model](../science/model.md)

### M02 A common phase at the helper

**Understanding target.** Identify which occupation patterns acquire identical phases.

**Revise.** The first helper holds two modes, one for each incident link. A phase at this laboratory multiplies a pattern with $`n`$ occupied modes by $`e^{in\theta}`$. Only relative phases between patterns affect their interference.

**Learn.** The two patterns in which just one mode is occupied both pick up the factor $`e^{i\theta}`$. The patterns with zero and two excitations pick up factors $`1`$ and $`e^{2i\theta}`$.

**Test.** The helper prepares a superposition of two patterns. Which pair keeps exactly its original relative phase for every $`\theta`$?

- **A.** Neither mode occupied and just the left mode occupied.
- **B.** Both modes occupied and just the right mode occupied.
- **C.** Just the left mode occupied and just the right mode occupied.
- **D.** Neither mode occupied and both modes occupied.

<details>
<summary>Check your answer</summary>

**C.** The two one-excitation patterns acquire the same factor for every angle.

</details>

[Source · Network model](../science/model.md) · [Builds on M01](#m01-an-excitation-on-one-link)

### M03 Averaging an unavailable angle

**Understanding target.** Predict whether a coherence survives when one phase record is unavailable.

**Revise.** To predict an experiment with an unavailable angle, average over its possible values. A coherence is the interference term between two occupation patterns.

**Learn.** For a uniformly random angle, the average of $`e^{im\theta}`$ is zero for every nonzero integer $`m`$. For $`m=0`$ it is one. For two patterns, $`m`$ is their difference in excitation count at the laboratory whose angle is averaged.

**Test.** Take two network patterns that differ by one excitation at Alice and also by one at Bob in the opposite direction. The two laboratories have independent uniform angles. What happens to the interference term?

- **A.** It survives because the differences sum to zero.
- **B.** It vanishes because an independent average already has a nonzero count difference to remove.
- **C.** It survives whenever both endpoint counts can be measured.
- **D.** It vanishes only if the link itself is physically removed.

<details>
<summary>Check your answer</summary>

**B.** Each endpoint has its own phase average. Their opposite count changes cannot cancel independent angles.

</details>

[Source · Network model](../science/model.md) · [Builds on M02](#m02-a-common-phase-at-the-helper)

### M04 Reading a sector without reading a pattern

**Understanding target.** Distinguish a total-count measurement from a measurement of individual occupancies.

**Revise.** A charge sector is the set of occupation patterns giving one fixed total count. A helper's two incident modes can hold occupations 00, 01, 10 or 11.

**Learn.** A measurement that reads just the total count can keep the 01 and 10 patterns coherent. A procedure reading both modes and adding the answers leaves separate records of the two patterns.

**Test.** A device reports a single total count to Alice. Which internal procedure preserves coherence between 01 and 10 when it reports one?

- **A.** Read both modes, add the reported values and disclose only their sum.
- **B.** Read one mode, then use its value to decide which other mode to read.
- **C.** Read both modes and ask Alice to erase the text of the two records.
- **D.** Measure the total count directly, with no record of the individual occupancies.

<details>
<summary>Check your answer</summary>

**D.** Only the final procedure measures exactly the quantity shared by both patterns without obtaining which-mode information.

</details>

[Source · Network model](../science/model.md) · [Builds on M03](#m03-averaging-an-unavailable-angle)

### M05 An encoded qubit

**Understanding target.** Connect a fixed-count pair of modes to a qubit that can be used locally.

**Revise.** Alice can encode two logical alternatives in two physical modes by placing a single excitation in the first mode or in the second. A common local phase depends only on the total count.

**Learn.** Charge-preserving local operations can mix two alternatives of the same count. Both receive the same phase, so their relative phase stays available.

**Test.** Which proposed pair of logical alternatives can Alice mix by these operations while retaining protection against a common unknown phase?

- **A.** 00 and 11.
- **B.** 10 and 11.
- **C.** 01 and 10.
- **D.** 00 and 01.

<details>
<summary>Check your answer</summary>

**C.** Both dual-rail alternatives have count one. Every other pair compares different total counts.

</details>

[Source · Network model](../science/model.md) · [Builds on M04](#m04-reading-a-sector-without-reading-a-pattern)

### M06 One raw link after averaging

**Understanding target.** Recognize the operational difference between one isolated link and a pooled resource.

**Revise.** A raw link begins with a coherent superposition of the excitation at Alice and at the helper. Independent phase averaging at the two ends removes coherence between terms with different local counts.

**Learn.** When their coherence is gone, the remaining state is a classical mixture of two product occupations. Local quantum operations and classical messages cannot extract entanglement from such a mixture.

**Test.** Alice and the helper discard all other modes and keep only their raw link after averaging. What is available?

- **A.** A shared random placement of one excitation.
- **B.** A locally encoded Bell pair with an unknown sign.
- **C.** Two coherent alternatives protected by their equal global count.
- **D.** A phase estimate that permits exact Bell correction.

<details>
<summary>Check your answer</summary>

**A.** The same global count is insufficient. The two placements have different local counts, so they form a mixture after independent endpoint averaging.

</details>

[Source · Network model](../science/model.md) · [Builds on M05](#m05-an-encoded-qubit)

### M07 Local operations and the success flag

**Understanding target.** Read the protocol's separation and output requirements.

**Revise.** Each laboratory may operate on all its own modes and send classical records. The desired output is an encoded Bell pair physically held at Alice and Bob. A success flag tells them which runs supplied that state.

**Learn.** A classical message can name a mode or a correction. It cannot move a coherent quantum state into another laboratory by itself.

**Test.** Which proposed implementation meets the operation and output contract?

- **A.** An encoded Bell pair is inferred from classical endpoint statistics after all modes were measured.
- **B.** A helper applies a joint quantum gate directly to one Alice mode and one Bob mode.
- **C.** Alice and Bob receive a common parity value with no retained quantum systems.
- **D.** A helper sends its outcome as a bit so Alice can correct the encoded state retained at the endpoints.

<details>
<summary>Check your answer</summary>

**D.** The final proposal keeps the Bell output at the endpoints and uses the helper's classical record for a local correction.

</details>

[Source · Network model](../science/model.md) · [Builds on M06](#m06-one-raw-link-after-averaging)

### M08 An arrow represents an occupation

**Understanding target.** Translate an occupation record into an orientation and back.

**Revise.** Every edge has one excitation at one of its ends. Put an arrow on the edge pointing toward the occupied end. The number of arrows pointing into a vertex is its indegree.

**Learn.** Each pattern of oriented edges represents a possible full occupation pattern. A laboratory's total count is the number of occupied ends at that vertex.

**Test.** On Alice–helper–Bob, the arrows run from Alice to the helper and then from the helper to Bob. What are their respective counts?

- **A.** One, one, zero.
- **B.** Zero, one, one.
- **C.** Zero, two, zero.
- **D.** One, zero, one.

<details>
<summary>Check your answer</summary>

**B.** The first arrow contributes one at the helper. The second contributes one at Bob.

</details>

[Source · Graph and charge-sector proofs](../science/graph.md) · [Builds on M07](#m07-local-operations-and-the-success-flag)

### M09 How likely is a charge record?

**Understanding target.** Translate the number of compatible orientations into a probability.

**Revise.** With balanced independent links, either arrow direction has squared amplitude one half for one edge. Every full orientation of two edges has the same probability, one quarter.

**Learn.** A total-count measurement keeps the orientation patterns that match the record. Its outcome probability is the sum of their probabilities, since the full patterns are distinct, orthogonal occupation configurations.

**Test.** For two edges meeting at a helper, two full orientations put exactly one excitation at the helper. How often does the helper report one?

- **A.** One eighth.
- **B.** One quarter.
- **C.** Three quarters.
- **D.** One half.

<details>
<summary>Check your answer</summary>

**D.** Add the probabilities of the two compatible orientations, giving two quarters.

</details>

[Source · Graph and charge-sector proofs](../science/graph.md) · [Builds on M08](#m08-an-arrow-represents-an-occupation)

### M10 What a directed cycle can hide

**Understanding target.** See how reversing a directed cycle changes an orientation while retaining the charge record.

**Revise.** A directed cycle follows the arrows and eventually returns to its starting vertex. Each vertex visited once along that cycle has one cycle arrow entering and one leaving.

**Learn.** Reversing every arrow on such a cycle exchanges the entering and leaving arrows at those vertices. Any edges outside the cycle keep their orientations.

**Test.** Use two of the worked example's two-hop paths as a four-edge loop. If the arrows circulate consistently, which operation creates a different orientation with unchanged counts at every vertex?

- **A.** Reverse one edge of the loop.
- **B.** Reverse just the first path from Alice to Bob.
- **C.** Reverse all four edges of the loop.
- **D.** Reverse two opposite edges of the loop.

<details>
<summary>Check your answer</summary>

**C.** A full reversal leaves one arrow entering and one leaving each loop vertex. A proper nonempty part of this loop has an endpoint where the count changes.

</details>

[Source · Graph and charge-sector proofs](../science/graph.md) · [Builds on M09](#m09-how-likely-is-a-charge-record)

### M11 A partition with just one crossing edge

**Understanding target.** Infer whether a one-edge cut has any quantum ambiguity after the counts are known.

**Revise.** A cut partitions laboratories into two sides. Summing the counts on either side counts one for every edge internal to that side, plus the excitations placed there by crossing edges.

**Learn.** With one crossing edge, the excess over the count of internal edges determines whether its excitation is on the chosen side. Once that occupation is fixed, the remaining compatibility conditions concern either side separately.

**Test.** Suppose removing four two-hop paths leaves Alice's first edge as the only edge crossing a cut near Alice. The count sum on Alice's side exceeds the number of internal edges by one. What does the record say about the crossing edge?

- **A.** Its two directions remain coherent because the entire graph contains one excitation per edge.
- **B.** Its excitation is on Alice's side and the count sector gives no crossing-edge coherence.
- **C.** Its excitation is on Bob's side and the edge has two allowed orientations.
- **D.** The edge is missing because the sum subtracts the internal edges.

<details>
<summary>Check your answer</summary>

**B.** The excess is the contribution of the crossing excitation, and an excess of one places it on Alice's side.

</details>

[Source · Graph and charge-sector proofs](../science/graph.md) · [Builds on M10](#m10-what-a-directed-cycle-can-hide)

### M12 The full problem for one batch

**Understanding target.** Combine the noise model, operation scope and performance measure.

**Revise.** One batch supplies one state per elementary edge of the five-path bond. The unknown phase at each vertex is common to that vertex's modes. Each protocol uses separated laboratory operations and classical communication.

**Learn.** The score is the probability that a batch heralds an exact encoded Bell pair between the specified endpoints. Rejected batches consume their input resources, so they count in the probability.

**Test.** Which benchmark matches this question?

- **A.** Across 100 deposited batches, count how many produce the announced exact pair at Alice and Bob using only the allowed operations.
- **B.** Among successful trials, report the number with any entanglement across any graph cut.
- **C.** Count exact pairs only after allowing arbitrary joint gates between the intermediate laboratories.
- **D.** Report how often five supplied paths have any detected excitation at both endpoints.

<details>
<summary>Check your answer</summary>

**A.** The numerator counts the specified heralded output and the denominator includes all independently supplied batches.

</details>

[Source · Network model](../science/model.md) · [Builds on M11](#m11-a-partition-with-just-one-crossing-edge)

## Phase II · Mechanism and innovation

### M13 Activate one two-hop path

**Understanding target.** Identify the intermediate charge record that leaves two coherent path orientations.

**Revise.** On a two-hop path there are two edges, each with an excitation at one end. The helper sits where the edges meet and measures only its total.

**Learn.** A helper with zero excitations has both particles at the remote ends. A helper with two has both there at the helper. If it holds one excitation, either of the two incident modes can hold it and the other particle is at an endpoint.

**Test.** Which helper outcome should the receiver keep for pooling?

- **A.** Zero only, because the endpoints each hold something.
- **B.** Zero or two, depending on which link was first.
- **C.** Two only, because concentration means success.
- **D.** One, because it leaves two endpoint placements compatible with the same record.

<details>
<summary>Check your answer</summary>

**D.** The one-count sector contains the two opposite uniformly directed orientations. The other sectors specify one orientation each.

</details>

[Source · Parallel-path proof](../science/parallel-paths.md) · [Builds on M12](#m12-the-full-problem-for-one-batch)

### M14 Where the helper's sign goes

**Understanding target.** Connect the helper's phase-preserving measurement to endpoint feed-forward.

**Revise.** In an active path, the two endpoint configurations are correlated with the helper's two one-excitation occupancies. A measurement in their sum-and-difference basis removes that occupation label without disclosing which one occurred.

**Learn.** The sum outcome gives the plus superposition of endpoint placements and the difference outcome gives the minus superposition. A sign change on one occupied endpoint mode transforms the latter to the former without altering its count.

**Test.** The helper announces the difference outcome. What can Alice do while preserving charge and preparing the path for pooling?

- **A.** Apply a relative sign through a local phase flip on her path mode.
- **B.** Measure her path mode to learn the higher-amplitude endpoint.
- **C.** Request Bob's phase reference as a classical number before computing any correction.
- **D.** Discard her mode, since both endpoint alternatives then have the same probability.

<details>
<summary>Check your answer</summary>

**A.** The known minus sign comes from the measurement result. A local diagonal phase flip corrects it.

</details>

[Source · Parallel-path proof](../science/parallel-paths.md) · [Builds on M13](#m13-activate-one-two-hop-path)

### M15 Pool the active paths before reading endpoints

**Understanding target.** Identify the output record that can yield a fixed-charge Bell pair.

**Revise.** After helper processing, each active path has one coherent endpoint excitation. Suppose there are three active paths. A total count of two at Alice means her occupied pair of path modes might be any two of the three, with Bob holding the complementary mode.

**Learn.** In a sector where Alice has every active excitation or none of them, there is only one allocation. A sector with a nontrivial subset keeps several distinct allocations.

**Test.** Which set of Alice's total-count outcomes can retain endpoint entanglement for these three active paths?

- **A.** Only zero and three.
- **B.** Only three, because all paths were active.
- **C.** One and two.
- **D.** All four, because the helper flags already heralded the final pair.

<details>
<summary>Check your answer</summary>

**C.** Either intermediate value leaves several coherent complementary placements. The extreme values each identify one placement.

</details>

[Source · Parallel-path proof](../science/parallel-paths.md) · [Builds on M14](#m14-where-the-helpers-sign-goes)

### M16 Count compatible endpoint placements

**Understanding target.** Connect occupation multiplicity to the number of equal-weight correlated terms.

**Revise.** Alice's recorded count fixes how many of the active path modes she occupies. Bob's occupied path modes are the complement. Distinct choices on Alice's side give distinct, orthogonal occupation choices on Bob's side.

**Learn.** When all active raw links are balanced, each allowed choice has the same weight after the known signs are corrected. The Schmidt rank counts the orthogonal correlated terms in this form.

**Test.** Three paths activate and Alice finds count one. What is the Schmidt rank?

- **A.** One, because Alice saw one excitation.
- **B.** Two, because there are two laboratories.
- **C.** Three, because Alice can occupy any of the three paths.
- **D.** Six, because Alice's choice and Bob's choice can vary independently.

<details>
<summary>Check your answer</summary>

**C.** Each of Alice's three choices fixes Bob's complementary choice and contributes one equal-weight term.

</details>

[Source · Parallel-path proof](../science/parallel-paths.md) · [Builds on M15](#m15-pool-the-active-paths-before-reading-endpoints)

### M17 Extract one pair from a larger sector

**Understanding target.** Explain how a charge-preserving filter converts a nontrivial sector to one exact Bell pair.

**Revise.** In the example with three active paths and Alice count one, her three possible occupation labels have equal amplitudes and complementary partners at Bob. A filter can keep two labels without distinguishing them.

**Learn.** Alice uses three possible unordered pairs of labels as filter outcomes. Each label belongs to two outcomes. Giving the same squared weight one half on each of those outcomes makes the total weight one for each label.

**Test.** What should Alice communicate after the filter?

- **A.** Which of the two retained labels really occurred.
- **B.** Nothing, because Bob can always identify the chosen pair from his total count.
- **C.** Each label discarded at the helpers before the endpoint counts were measured.
- **D.** The pair of labels retained, so both can decode those coherent alternatives.

<details>
<summary>Check your answer</summary>

**D.** The outcome records only the selected pair. The two alternatives stay coherent and equally weighted.

</details>

[Source · Parallel-path proof](../science/parallel-paths.md) · [Builds on M16](#m16-count-compatible-endpoint-placements)

### M18 Two directions across the active bundle

**Understanding target.** Translate endpoint success into a joint event for the path orientations.

**Revise.** A path that is coherently active can have its arrows pointing consistently either from Alice to Bob or from Bob to Alice in an occupation sample. These place its remaining excitation at Bob or at Alice, respectively.

**Learn.** A Bell pair is extractable exactly when the active paths leave at least one excitation at each endpoint. Inactive paths add only fixed, removable occupations.

**Test.** An occupation sample has paths 1 and 2 pointing toward Bob, 3 and 4 inactive, and 5 pointing toward Alice. What follows for the charge record corresponding to that sample?

- **A.** The run has an eligible sector because both path directions are represented.
- **B.** The run fails because any inactive path spoils pooling.
- **C.** The run fails because the endpoint counts differ.
- **D.** The run requires a second batch because there are three active paths.

<details>
<summary>Check your answer</summary>

**A.** Alice's active count is one and Bob's is two. These counts permit multiple coherent placements, even with the two inactive paths.

</details>

[Source · Parallel-path proof](../science/parallel-paths.md) · [Builds on M17](#m17-extract-one-pair-from-a-larger-sector)

### M19 Calculate one-shot reliability

**Understanding target.** Use inclusion–exclusion with independent path records to recover the exact five-path rate.

**Revise.** For each two-hop path, a uniform orientation sample yields Alice-to-Bob with probability one quarter, Bob-to-Alice with one quarter and inactive with one half. The five samples are independent.

**Learn.** A route needs both directions. The probability of seeing no path in either specified direction is $`(3/4)^5`$. Adding the two missing-direction probabilities counts the all-inactive case twice.

**Test.** Which expression gives the five-path chance of heralding a pair?

- **A.** $`1-(1/2)^5`$.
- **B.** $`1-2(3/4)^5+(1/2)^5`$.
- **C.** $`(3/4)^5-(1/2)^5`$.
- **D.** $`1-2(3/4)^5`$.

<details>
<summary>Check your answer</summary>

**B.** Subtract both missing-direction events and add back their intersection. The result is $`285/512`$.

</details>

[Source · Parallel-path proof](../science/parallel-paths.md) · [Builds on M18](#m18-two-directions-across-the-active-bundle)

### M20 Why these success flags can be optimal

**Understanding target.** Connect the zero-success obstruction to an attained upper bound.

**Revise.** Condition on a full charge record. If the two endpoints belong to different strongly connected components, the sector factors across those components. Local operations and classical messages cannot turn a product across a separating partition into an exact Bell pair.

**Learn.** For internally disjoint paths, the two endpoints are in one strongly connected component exactly when there is a consistently directed path each way in a compatible orientation. The pooling protocol succeeds with certainty in each such charge sector.

**Test.** What status should the resulting five-path success probability have?

- **A.** A lower bound because the protocol was only tested on short paths.
- **B.** An upper bound that may fail to be attainable due to endpoint decoding.
- **C.** The optimum within the stated input and separated-operation model.
- **D.** An optimum only among protocols measuring Alice first.

<details>
<summary>Check your answer</summary>

**C.** The impossibility bound and the attained probability count exactly the same sectors.

</details>

[Source · Parallel-path proof](../science/parallel-paths.md) · [Builds on M19](#m19-calculate-one-shot-reliability)

### M21 Different path lengths

**Understanding target.** Understand how extra intermediate stations change the balance of reliable pooling.

**Revise.** An active path of length $`\ell`$ has exactly two consistent orientations out of $`2^\ell`$ equally likely ones. The probability for each specified direction is $`2^{-\ell}`$.

**Learn.** Independent paths contribute through their own available-direction probabilities. Replacing an existing path with a longer route lowers the probability it supplies either missing direction, all else equal.

**Test.** One of the five two-hop paths is replaced by a three-hop path. How does its single-path activation probability change?

- **A.** It increases from one half to three quarters.
- **B.** It stays one half because there are still two possible directions.
- **C.** It increases from one quarter to one half.
- **D.** It drops from one half to one quarter.

<details>
<summary>Check your answer</summary>

**D.** The two consistent orientations are now two of eight rather than two of four.

</details>

[Source · Parallel-path proof](../science/parallel-paths.md) · [Builds on M20](#m20-why-these-success-flags-can-be-optimal)

### M22 Pooling versus reserving pairs in advance

**Understanding target.** Explain why retaining a choice of trails can outperform predetermined cycle attempts.

**Revise.** A fixed pair of paths succeeds only when its two members point in opposite directions. A receiver which pools every active path can use any two opposite directions while leaving other paths available.

**Learn.** Suppose two predetermined pairs are {1,2} and {3,4}, with path 5 unpaired. A single orientation example can show strict improvement if the fixed pairs fail while the pooled record is eligible.

**Test.** What example demonstrates this improvement?

- **A.** Paths 1 and 3 point in opposite directions, while 2, 4 and 5 are inactive.
- **B.** Paths 1 and 2 point in opposite directions, while 3, 4 and 5 are inactive.
- **C.** Paths 1 and 3 point toward Bob and the others are inactive.
- **D.** All five paths are inactive.

<details>
<summary>Check your answer</summary>

**A.** Neither fixed pair has two active members. Pooling can use the two active paths across those pairs.

</details>

[Source · Parallel-path proof](../science/parallel-paths.md) · [Builds on M21](#m21-different-path-lengths)

### M23 Shared components and the wider graph question

**Understanding target.** Use the orientation criterion as a probabilistic upper bound and distinguish it from attainability.

**Revise.** A strongly connected component groups vertices that can reach one another following directed edges both ways. On a general graph, compatible orientations of the same charge sector have the same components.

**Learn.** When the endpoints are in different components, the fixed-charge state factors over those components and they cannot share an exact Bell output. Being in the same component allows a positive-probability extraction, while the probability within that sector can depend on its amplitudes and local filters.

**Test.** The designer attaches new paths that overlap in their intermediate vertices. What can be stated if Alice and Bob share a component for 60% of sectors by probability?

- **A.** The upper bound is 60%, and the parallel-path equality needs a separate attainability argument.
- **B.** The exact success probability is 60% because every connected sector gives a pair with certainty.
- **C.** The protocol is impossible because there is a shared intermediate vertex.
- **D.** The success probability must exceed 60% if enough local filters are allowed.

<details>
<summary>Check your answer</summary>

**A.** Sectors with separated endpoints cannot contribute to success. Shared-component sectors may contribute less than their full probability.

</details>

[Source · Graph and charge-sector proofs](../science/graph.md) · [Builds on M22](#m22-pooling-versus-reserving-pairs-in-advance)

### M24 Why a bridge still blocks routing

**Understanding target.** Apply the graph criterion to a network with ample entanglement on both sides of a weak connection.

**Revise.** A bridge is an edge whose removal disconnects the graph. If it is the only connection between two pieces, the total charge on one side fixes its orientation in each sector.

**Learn.** Local operations and classical messages cannot bridge a product cut. Cyclic structures within a piece can still activate entanglement among labs in that piece.

**Test.** Two five-path bonds are installed in separate regions and joined by one raw edge. Alice is in the first and Bob in the second. What changes if the designer doubles the number of local paths in each region but leaves the single connecting edge?

- **A.** The exact Bell probability is at least the smaller side's internal probability.
- **B.** The two doubled regions supply an extra phase reference across the bridge automatically.
- **C.** The bridge starts behaving like an encoded link because both sides now have many excitations.
- **D.** Exact Alice–Bob routing remains impossible in this one-shot model.

<details>
<summary>Check your answer</summary>

**D.** The crossing occupation still factors by side after the charge is fixed. Extra internal cycles do not create a second crossing edge.

</details>

[Source · Graph and charge-sector proofs](../science/graph.md) · [Builds on M23](#m23-shared-components-and-the-wider-graph-question)

### M25 Turn one gadget into a lattice bond

**Understanding target.** Connect per-bond reliability to a macroscopic routing opportunity.

**Revise.** A square-lattice bond is open when its gadget heralds an encoded Bell pair. Independent open bonds on the square lattice have a percolation threshold of one half. For occupation probability above that value, long-range connections can have a probability bounded away from zero in the large-lattice limit.

**Learn.** Use separate raw states for every physical bond gadget. Their flag distributions are unchanged by each vertex's common phase, including at vertices shared by several gadgets.

**Test.** Four two-hop paths give probability $`55/128`$ and five give $`285/512`$. Which choice supports the supercritical bond argument?

- **A.** Both, because each uses more than two paths.
- **B.** Only the five-path gadget, because four paths lie below one half.
- **C.** Only the four-path gadget, because a vertex has four lattice neighbors.
- **D.** Neither, because any shared lattice vertex makes its incident gadget flags dependent.

<details>
<summary>Check your answer</summary>

**B.** The five-path probability exceeds one half. The common phase cannot correlate flag probabilities that are independent for every fixed phase assignment.

</details>

[Source · Scale and robustness](../science/scale-and-robustness.md) · [Builds on M24](#m24-why-a-bridge-still-blocks-routing)

### M26 Connect two successful bonds

**Understanding target.** Explain how a classical route can produce a quantum endpoint pair.

**Revise.** Suppose one heralded encoded pair connects Alice to an intermediate lattice vertex, and a second connects that vertex to Bob. The intermediate vertex holds one logical qubit from each pair, each encoded within fixed local charge.

**Learn.** An encoded Bell measurement at that vertex acts within the joint fixed-charge space. The outcome names a local correction on an endpoint. This operation, entanglement swapping, leaves Alice and Bob with the output pair.

**Test.** Once classical flags reveal an open path, what does its routing controller still need to arrange?

- **A.** Independent random measurement of each mode to identify the physical excitation positions.
- **B.** Nothing, because connectivity of the flags is itself the final Bell pair.
- **C.** Encoded Bell measurements at the intermediate vertices and communication of the outcomes.
- **D.** A phase reference broadcast to every intermediate vertex before any local action.

<details>
<summary>Check your answer</summary>

**C.** The flags locate available pairs. The encoded Bell measurements and corrections join them into the requested pair.

</details>

[Source · Scale and robustness](../science/scale-and-robustness.md) · [Builds on M25](#m25-turn-one-gadget-into-a-lattice-bond)

### M27 Budget the supplied modes

**Understanding target.** Count resources of the square-lattice architecture and interpret what the count measures.

**Revise.** A square-lattice vertex meets four bond gadgets in the bulk. Each gadget routes five two-hop paths, each using one raw edge mode at that vertex and another at its remote helper on that first hop.

**Learn.** The local degree counts raw half-link modes held at a lattice vertex in one batch. An intermediate path helper has just two incident raw modes.

**Test.** How many raw half-link modes does a bulk lattice vertex hold for its four adjacent gadgets?

- **A.** Five, because the same five modes can be shared across all incident gadgets.
- **B.** Ten, because each gadget uses ten elementary links globally.
- **C.** Forty, because the other endpoint of each incident raw edge must also be stored locally.
- **D.** Twenty, because each of the four gadgets contributes five incident half-links.

<details>
<summary>Check your answer</summary>

**D.** Four independent gadgets each supply five raw local modes. The number does not price auxiliary gates or extra buffers.

</details>

[Source · Scale and robustness](../science/scale-and-robustness.md) · [Builds on M26](#m26-connect-two-successful-bonds)

### M28 Add reported edge loss

**Understanding target.** Distinguish flagged missing links from imperfect but unflagged output states.

**Revise.** A flag can tell the controller that an elementary link was lost. Independent survival with probability $`s`$ gives survival probability $`s^2`$ for a two-hop path, because both raw links are needed.

**Learn.** Conditional on survival, the original active-path probability is one half. Discard a path with any loss flag before pooling.

**Test.** If $`s=1/2`$, what active-path probability enters the pooling formula for a given two-hop path?

- **A.** One eighth.
- **B.** One quarter.
- **C.** One half.
- **D.** Three quarters.

<details>
<summary>Check your answer</summary>

**A.** The two-hop path survives with probability one quarter and then activates half of the time.

</details>

[Source · Scale and robustness](../science/scale-and-robustness.md) · [Builds on M27](#m27-budget-the-supplied-modes)

### M29 Common phase and differential phase

**Understanding target.** Distinguish the noise that a fixed charge removes from the noise that can spoil the pair.

**Revise.** Two endpoint codewords in the same local charge sector receive the same factor under each common node rotation. A differential phase on one elementary edge can multiply just one of the two retained alternatives.

**Learn.** Suppose a selected loop has two retained alternatives with equal amplitude. Relative phase zero gives the desired plus Bell state. Relative phase pi gives the orthogonal minus Bell state. An unavailable fair choice between these signs removes their coherence when averaged.

**Test.** The hardware adds an independent, unrecorded random sign to just one edge of the selected loop. What can happen?

- **A.** The Bell fidelity stays one because every phase error respects total excitation count.
- **B.** The success flags can still look the same while Bell fidelity drops.
- **C.** The protocol necessarily sees additional missing-edge flags.
- **D.** Alice's total-count measurement reveals the unknown sign.

<details>
<summary>Check your answer</summary>

**B.** The sign affects coherence between equally likely occupations, without changing their probabilities or total counts.

</details>

[Source · Scale and robustness](../science/scale-and-robustness.md) · [Builds on M28](#m28-add-reported-edge-loss)

### M30 Read the whole routing guarantee

**Understanding target.** Connect ideal one-batch routing to the distinct fixed-fidelity guarantee with repeated acquisition.

**Revise.** The quarter-direction records of ideal two-hop paths give a five-path Bell herald with probability $`285/512`$. The lattice then uses classical connectivity and local encoded swaps. The input gives one single-excitation state per edge, with a common unknown phase at each node.

**Learn.** Independent differential phase errors can leave the flags unchanged while reducing the fidelity after a long sequence of swaps. With ideal encoded operations and storage, a separate protocol collects several independent copies per bond and removes most phase errors before swapping. Repeating batches and storing accepted copies cost extra resources.

**Test.** Which scientific claim is supported by the complete worked example?

- **A.** The one-batch flags certify long-range fidelity on a mesh with arbitrary differential drift.
- **B.** The repeated protocol attains fixed fidelity without charging any failed acquisitions or added storage.
- **C.** The ideal layout supports long-range one-batch success, and charged repetition gives a separate fidelity guarantee under its independent-noise model.
- **D.** The two guarantees both require learning and communicating the phase angle at every laboratory.

<details>
<summary>Check your answer</summary>

**C.** The one-batch guarantee counts open routes, while the fidelity guarantee pays for preparing and storing multiple pairs per route bond. Both use fixed-charge operations.

</details>

[Source · Scale and robustness](../science/scale-and-robustness.md) · [Builds on M29](#m29-common-phase-and-differential-phase)

[Return to the learning route](README.md)
