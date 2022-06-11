# Basic properties of stabilizer codes and related concepts

## Notation:
$$\mathcal{G^n}=(G^n,*,*^{-1})=  \text{Arbitrary subgroup of } \mathcal{P^n}$$
## Stabilizer
- **Def (Stabilizer):** A stabilizer $S\subseteq \mathcal{G^n}$ is an ablean subgroup of $\mathcal{G^n}$ 




	- **Def (Coding space):** $V_S$ is the vector space stabilized by $S$:
	- $V_s$ is the 1 eigensubspace of $S$: $$\{V_S =|v\rangle \in \mathcal{H} : S_i |v\rangle = |v\rangle \text{ for all } S_i \in S\}$$

- **Def(Stabilizer code):** a $[n,k]$ stabilizer code is the vectorspace $V_S$ stabilized by S such that:
	- $-I \notin S$
	- $S$ has $l=n-k$ non commuting independent generators, $S = <g_1, ... g_l>$



#### Properties of S:
- $-I \notin S$ 
Why is $-I\notin S$?
	This is because $-I\in S \implies$ $V_S = \{\vec{0}\}$, as $-I*\vec{v} = \vec{v} \implies \vec{v} = \vec{0}$ 

- $S$ has $l=n-k$ commuting and independent generators
		(Follows from the fact that $S$ is an abelean group)


#### Properties of $V_S$:
- $V_S$ is not empty
- $dim(V_S)= 2^{k} = \text{Means we have k error corrected qubits}$


## Normalizer/centralizer:
**Def (Normalizer):** $\mathcal{N}(S\subseteq_\text{group} G^n)=\{E\in G^n: E \text{ fixes } S \text{ setwise under conjugation}\}$ 
														$= \{E\in G^n : E SE^\dagger \in S \}$

Normalizers are important because they are equivalent to something called the centrilizer

**Def (Centralizer):**  $\mathcal{Z}(S\subseteq_\text{group} G^n)=\{E\in G^n : E\text{ commutes with every element of }S\}$  
														$= \{E\in G^n : \forall_{s\in S} {E s=sE} \}$
														$\equiv\{E\in G^n: E \text{ fixes } S \text{ pointwise under conjugation}\}$

For the pauli group, $\mathcal{Z}(S)=\mathcal{N}(S)$ if $-I \notin S$



## Error correction
How does error correction work?

Suppose we have a stabilizer $S = <g_1,...g_l>$
and a state $|\psi\rangle$ that has been corrupted by some error $E_j \notin \mathcal{N}(S)-S$

so we now have $|\phi\rangle=E_j|\psi\rangle$. 

If we measure $|\phi\rangle$ $l$ times with observables $g_1, g_2,...g_l$ we get the **syndrome** vector $\vec{\lambda} = (\text{eigenvalue } i)_{i=1}^{l}$

Consider 2 cases:
1) $E_j$ is the unique operator corresponding to the syndrome $\vec{\lambda}$
2) $E_j\ne E_k$, but they do give the same syndrome.

#### For case 1:
Error correction can be performed by simply applying $E_j^\dagger$ :
$|\psi '\rangle=E_j^\dagger |\phi\rangle = E_j^\dagger E_j |\psi\rangle = |\psi\rangle$
Thus the state can be corrected.

#### For case 2:
