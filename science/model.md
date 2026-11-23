# The resource and the routing task

Let $`G=(V,E)`$ be a finite loopless undirected graph with specified, distinct terminals $`A,B`$. Parallel edges, when used, have distinct modes. Each edge $`e=\{u,v\}`$ supplies one excitation in a pair of labeled modes, one at each endpoint. The modes are bosonic or distinguishable qubit memories with the specified tensor product. We use only zero and one occupation in an input mode.

```math
|\psi_e\rangle=\frac{|1\rangle_{u,e}|0\rangle_{v,e}+|0\rangle_{u,e}|1\rangle_{v,e}}{\sqrt2},
\qquad |\Psi_G\rangle=\bigotimes_{e\in E}|\psi_e\rangle.
```

At a node $`v`$, the same angle multiplies all its incident modes via $`e^{i\theta_v N_v}`$, where $`N_v=\sum_{e\ni v}n_{v,e}`$. The angles are unknown. Our converse uses the average over independent uniform angles at different nodes. The fixed-number protocol has the same outcome probabilities and encoded outputs for every fixed set of angles. Thus it also applies to independently twirled batches. Preparation or distribution of the supplied links is an input cost separate from the routing step.

## Why the charge record is useful

Direct an edge toward its occupied mode and write $`q_v(x)`$ for the indegree of vertex $`v`$ in orientation $`x`$. Let $`\mathcal{F}_q`$ be the set of orientations with indegree vector $`q`$. Twirling deletes a matrix element exactly when a node's charge differs between its two orientations. The twirled state has the form

```math
\rho_G=\sum_{q:\,|\mathcal{F}_q|>0}
\frac{|\mathcal{F}_q|}{2^{|E|}}
|\mathcal{F}_q\rangle\langle\mathcal{F}_q|,
\qquad
|\mathcal{F}_q\rangle
=\frac{1}{\sqrt{|\mathcal{F}_q|}}\sum_{x\in\mathcal{F}_q}|x\rangle.
```

Here $`|x\rangle`$ lists the occupations in all labeled modes. The charges can be read locally with projectors that keep alternatives within each charge sector coherent. Before averaging, all alternatives in a sector acquire the same phase. Consequently the charge record has the distribution of the indegrees of a fair independent orientation of all edges.

The state of an isolated edge after twirling is an equal mixture of two product occupations. In a network, orientations can differ while producing the same charge at every node. Such alternatives carry the coherence the routing protocol uses.

## Operations, output and accounting

Operations couple only modes held at the same node. We permit local classical records, classical messages and local fixed-number ancillary systems. In each number sector, local operations act on the degrees of freedom that specify the occupied modes. An encoded qubit can be stored in two modes with exactly one excitation, using $`|0_{\rm L}\rangle=|10\rangle`$ and $`|1_{\rm L}\rangle=|01\rangle`$. A success flag certifies that the specified endpoints hold one exact encoded Bell pair after stated corrections. An unsuccessful batch produces a failure flag. We count both outcomes in the one-batch probability.

Quantum operations between distinct laboratories, external phase reference states and extra shared entanglement are absent. The ideal graph results use perfect reports, ideal storage and arbitrary number-preserving local gates. The converse also permits unrestricted local gates on the **already twirled** resource. The architecture uses $`|E|`$ raw states and $`2|E|`$ supplied endpoint modes per batch. Local readout, work registers, storage and communication enter any implementation estimate separately.

This model inherits the source resource and orientation representation of [Entanglement Valence Threshold](https://github.com/GoGoKo699/Entanglement-Valence-Threshold/blob/e3217a7babf8448c77799747623294c3c05d8357/science/model.md). That work measures entanglement across entire vertex-color coalitions and allows quantum operations within each coalition. The task here specifies two individual terminals under separated node operations. The [four-regular comparison](degree-four-routing.md#a-separation-from-color-coalition-entanglement) gives a graph family where the two operational quantities scale differently.
