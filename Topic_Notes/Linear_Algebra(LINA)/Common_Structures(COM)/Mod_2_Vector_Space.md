# Mod 2 Vector Space
### Metadata
Path: #pathLINA , #pathLINA/COM
Tags:

### Prerequisites

### Introduction

### Mod 2 Vector Space Definition
#wip just a $\mathbb Z_2$ vector space (finite necessary?)

### Mod 2 Vector Space Size Theorem
**Thm(Mod 2 Vector Space Size):** Let $\mathcal V$ be a finite mod 2 vector space, and $\mathcal S < \mathcal V$ be a subspace. Then, $|S|=2^{\text{dim}(\mathcal S)}$ 
	Proof:
		Let $B=\{b_1, \ldots b_l\}$ be a basis for $\mathcal S$. Then note each vector in $v\in S$ has a unique decomposition with respect to $B$ by the [[FUN-Basis#Unique Decomposition Theorem|unique decomposition theorem]]. Thus $v=\sum_{i=1}^l c_i(b_i)$. Because $B$ is a basis for $\mathcal S$, we must have $\mathcal S = \text{span}(B)$, and so each linear combination of basis vectors corresponds to one vector in $S$, and every vector in $S$ corresponds to one linear combinations. So $\# \text{linear combinations}=|\mathcal S|$, and since every $c_i \in \{0,1\}$, $\#\text{linear combinations}=2^{l}$, as each $c_i$ has two options. Since we have $l$ basis vectors, $|S|=2^{\text{dim}(\mathcal S)}$.