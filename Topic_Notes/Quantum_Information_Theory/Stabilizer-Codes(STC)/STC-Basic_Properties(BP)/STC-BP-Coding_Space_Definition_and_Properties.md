# Coding space ($V_S$) definition and properties
#### Prerequisites:
[[STC-BP-Stabilizer_Definition_and_Properties]]

### Introduction
Let $S = <g_1, ... g_{n-k}>$ be a stabilizer.
This note gives the [[#Coding space V_S definition|definition]] of the coding space $V_S$/$[n,k]$ stabilizer code, as well as [[#Coding space V_S properties|its properties]]. It also includes a [[#Coding space size theorem|theorem]] that says the coding space has dimension $2^k$ .

### Coding space ($V_S$) definition
- **Def (Coding space):** $V_S$ is the vector space stabilized by $S$:
	- $V_s$ is the +1 eigenspace of $S$: $$\{V_S =|v\rangle \in \mathcal{H} : S_i |v\rangle = |v\rangle \text{ for all } S_i \in S\}$$
- **Def(Stabilizer code):** a $[n,k]$ stabilizer code is the vector-space $V_S$ stabilized by S such that:
	- $-I \notin S$
	 Why is $-I\notin S$?
		 This is because $-I\in S \implies$ $V_S = \left\{\vec{0}\right\}$, as $-I*\vec{v} = \vec{v} \implies \vec{v} = \vec{0}$ 
	- $S$ has $l=n-k$ commuting independent generators, $S = <g_1, ... g_l>$
	(so S is abelian)
	
	Since $S$ is abelian, [[STC-BP-Stabilizer_Definition_and_Properties#Stabilizer Definition|by definition]] this make $S$ a stabilizer.
	Note these properties are [[STC-BP-Stabilizer_Definition_and_Properties#Stabilizer Properties|the same]] as the ones for a non empty stabilizer.



### Coding space ($V_S$) properties
- $V_S$ is not empty
	$-I \notin S$, so by  [[STC-BP-Stabilizer_Definition_and_Properties#Stabilizer Properties|these properties]]
- $dim(V_S)= 2^{k} = \text{Means we have k error corrected/logical qubits}$
	[[#Coding space size theorem]]

### Coding space size theorem
**Thm(Coding space size):** $dim(V_S) = 2^k$
	This