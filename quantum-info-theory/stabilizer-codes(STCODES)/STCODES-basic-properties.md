# Basic properties of stabilizer codes and related concepts

## Notation:
$$\mathcal{G^n}=(G^n,*,*^{-1})=  \text{Arbitrary subgroup of } \mathcal{P^n}$$
## Stabilizer
- **Def (Stabilizer):** A stabilizer $S\subseteq \mathcal{G^n}$ is an ablean subgroup of $\mathcal{G^n}$ 


- **Def (Coding space):** $V_S$ is the vector space stabilized by $S$:
	- $V_s$ is the +1 eigensubspace of $S$: $$\{V_S =|v\rangle \in \mathcal{H} : S_i |v\rangle = |v\rangle \text{ for all } S_i \in S\}$$
- **Def(Stabilizer code):** a $[n,k]$ stabilizer code is the vectorspace $V_S$ stabilized by S such that:
	- $-I \notin S$
	 Why is $-I\notin S$?
		 This is because $-I\in S \implies$ $V_S = \left\{\vec{0}\right\}$, as $-I*\vec{v} = \vec{v} \implies \vec{v} = \vec{0}$ 

	- $S$ has $l=n-k$ commuting independent generators, $S = <g_1, ... g_l>$
	(so S is abelean)


<<<<<<< HEAD
=======
#### Properties of S:
- $-I \notin S$ 
Why is $-I\notin S$?
	This is because $-I\in S \implies$ $V_S = \{ \vec{0} \}$, as $-I*\vec{v} = \vec{v} \implies \vec{v} = \vec{0}$ 

- $S$ has $l=n-k$ commuting and independent generators
		(Follows from the fact that $S$ is an abelean group)

>>>>>>> ff70a0808f99ee1a7e02408bd1550164e447070f

#### Properties of $V_S$:
- $V_S$ is not empty
- $dim(V_S)= 2^{k} = \text{Means we have k error corrected/logical qubits}$


## Normalizer/centralizer:
**Def (Normalizer):** $\mathcal{N}(S\subseteq_\text{group} G^n)=\{E\in G^n: E \text{ fixes } S \text{ setwise under conjugation}\}$ 
														$= \{E\in G^n : E SE^\dagger \in S \}$

Normalizers are important because they are equivalent to something called the centrilizer

**Def (Centralizer):**  $\mathcal{Z}(S\subseteq_\text{group} G^n)=\{E\in G^n : E\text{ commutes with every element of }S\}$  
														$= \{E\in G^n : \forall_{s\in S} {E s=sE} \}$
														$\equiv\{E\in G^n: E \text{ fixes } S \text{ pointwise under conjugation}\}$

For the pauli group, $\mathcal{Z}(S)=\mathcal{N}(S)$ if $-I \notin S$
