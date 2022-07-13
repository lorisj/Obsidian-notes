# Basis
### Prerequisites
#wip
### Introduction
#wip
### Definition of Basis
#wip

### Unique Decomposition Theorem
**Thm(Unique Decomposition):** Given a basis $\{v_i\}_{i\in I}$  with index set $I$, and  $\mathbb{F}$-[[FUN-Vectorspaces#Introduction|vectorspace]] $\mathcal{V}$, for every vector $v \in V$ there is a unique subset of scalars $\{c_j\}_{j\in J}$ where $J$ is a finite subset of $I$ such that $v=\sum_{j\in J}c_j v_j$.
	Proof: $\{v_i\}_{i \in I}$ is a basis, so $\text{span}(\{v_i\}_{i\in I})=V$. Thus $v \in V \implies v = \sum_{j \in J} c_j v_j$ for some index set $J$, because of the [[Definition of span|definition of span]]. Now all we have to do is prove that this decomposition is unique:
		Suppose $v$ has two decompositions: $v=\sum_{j\in J} c_j *v_j$ and $v=\sum_{k\in K} d_k *v_k$  for finite $J$ and $K$. Assume $K = J$ as otherwise you can expand both to have the same elements by adding zeros where needed.
		$\implies v-v=\sum_{j\in J}(c_j-d_j)v_j$
		$\implies 0=\sum_{j\in J}{(c_j-d_j)}v_j$
		$\implies \forall_{j \in J} c_j-d_j =0$ by [[Linear Independence|definition of linear independence applied to a basis]]
		$\implies \forall_{j\in J} c_j=d_j$ 
		Thus the decomposition is unique for a given basis.   
