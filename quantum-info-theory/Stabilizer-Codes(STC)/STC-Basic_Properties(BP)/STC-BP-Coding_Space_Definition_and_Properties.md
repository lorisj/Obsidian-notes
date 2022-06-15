# Coding space ($V_S$) definition and properties
[[Basic_Properties]]
## Coding space ($V_S$) definition and properties:
- $V_S$ is not empty
- $dim(V_S)= 2^{k} = \text{Means we have k error corrected/logical qubits}$

- **Def (Coding space):** $V_S$ is the vector space stabilized by $S$:
	- $V_s$ is the +1 eigenspace of $S$: $$\{V_S =|v\rangle \in \mathcal{H} : S_i |v\rangle = |v\rangle \text{ for all } S_i \in S\}$$
- **Def(Stabilizer code):** a $[n,k]$ stabilizer code is the vector-space $V_S$ stabilized by S such that:
	- $-I \notin S$
	 Why is $-I\notin S$?
		 This is because $-I\in S \implies$ $V_S = \left\{\vec{0}\right\}$, as $-I*\vec{v} = \vec{v} \implies \vec{v} = \vec{0}$ 

	- $S$ has $l=n-k$ commuting independent generators, $S = <g_1, ... g_l>$
	(so S is abelian)


