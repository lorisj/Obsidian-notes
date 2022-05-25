# Basic properties of stabilizer codes and related concepts

## Notation:
$$\mathcal{G^n}=(G^n,*)=  \text{Arbitrary subgroup of } \mathcal{P^n}$$
## Stabilizer
- **Def (Stabilizer):** A stabilizer $S\subseteq \mathcal{P^n}$ is an ablean subgroup of $\mathcal{P^n}$ 




- **Def (Coding space):** $V_S$ is the vector space stabilized by $S$:
	- $V_s$ is the 1 eigensubspace of $S$: $$\{V_S =|v\rangle \in \mathcal{H} : S_i |v\rangle = |v\rangle \text{ for all } S_i \in S\}$$


#### Properties of S:
- $-I \notin S$ (Generally)
- $S$ has $l=n-k$ commuting and independent generators
		(Follows from the fact that $S$ is an abelean group)
Why is $-I\notin S$?
This is because $-I\in S \implies$ $V_S = \left\{\vec{0}\right\}$, as $-I*\vec{v} = \vec{v} \implies \vec{v} = \vec{0}$ 


#### Properties of $V_S$:
- $V_S$ is not empty
- $dim(V_S)= 2^{k}$


## Normalizer/centralizer:
**Def (Normalizer):** $\mathcal{N}(G^n)=\{\text{unitary }U \in L(\mathcal{H},\mathcal{H}) : U \text{ fixes } G^n \text{ setwise}\}$
Normalizers are important because they are equivalent to something called the centrilizer:

