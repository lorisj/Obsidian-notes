# Coding space ($V_S$) definition and properties
### Metadata
Path: #pathQINF, #pathQINF/STC, #pathQINF/STC/BP 
Tags:

### Prerequisites:
[[Stabilizer_Definition_and_Properties]]

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
	
	Since $S$ is abelian, [[Stabilizer_Definition_and_Properties#Stabilizer Definition|by definition]] this make $S$ a stabilizer.
	Note these properties are [[Stabilizer_Definition_and_Properties#Stabilizer Properties|the same]] as the ones for a non empty stabilizer.


### Coding space ($V_S$) properties
- $V_S$ is not empty
	$-I \notin S$, so by  [[Stabilizer_Definition_and_Properties#Stabilizer Properties|these properties]]
- $dim(V_S)= 2^{k} = \text{Means we have k error corrected/logical qubits}$
	[[#Coding space size theorem]]


### Projector Lemma
- **Lem(Stabilizer Projector):** $\Pi_{V_S}=\frac{1}{|S|}\sum_{g\in S}g$ is the projector onto $V_S$.
	Proof:
		$\Pi_{V_S}$ is a weighted sum of hermitian operators so it is hermitian.
		Claim: $\Pi_{V_S}^\dagger \Pi_{V_S}=\Pi_{V_S}$ therefore $\Pi_{V_S}$ is a projector:
			$\Pi_{V_S}^\dagger \Pi_{V_S}=\frac{1}{|S|^2}\sum_{g\in S}\sum_{h\in S}g^\dagger h$
						 $=\frac{1}{|S|^2}\left [g_1(\sum_{h\in S}h)+\ldots+g_{|S|}(\sum_{h\in S}h)\right ]$
						 $=\frac{1}{|S|^2}\left [(\sum_{h\in S}g_1h)+\ldots(\sum_{h\in S}g_{|S|}h)\right ]$
						 $=\frac{1}{|S|^2}\left [(\sum_{h'\in g_1S}h')+\ldots(\sum_{h'\in g_{|S|}S}h')\right ]$
						 $=\frac{1}{|S|^2}\left [(\sum_{h'\in S}h')+\ldots(\sum_{h'\in S}h')\right ]$
							 Note $g_i S=S$ because [[acting on a group by a group element is an automorphism]].
						 $=\frac{1}{|S|}\sum_{h\in S}h=\Pi_{V_S}$
		Claim: $\text{im}(\Pi_{V_S})\subseteq V_S$:
			For arbitrary $|\psi\rangle$: $\Pi_{V_S}|\psi\rangle=\frac{1}{|S|}\sum_{g\in S}{g|\psi\rangle}$. If we take any $h\in S$, $h(\Pi_{V_S}|\psi\rangle)=(h\Pi_{V_S})|\psi\rangle=\Pi_{V_S}|\psi\rangle$. Thus $\text{im}(\Pi_{V_S})\subseteq V_S$.
		Claim: $V_S \subseteq \text{im}(\Pi_{V_S})$
			Take $|\psi\rangle \in V_S$. Note $\Pi_{V_S}|\psi\rangle=\frac{1}{|S|}\sum_{g\in S}g|\psi\rangle=\frac{1}{|S|}\sum_{g\in S}|\psi\rangle=|\psi\rangle$. Thus $V_S\subseteq \text{im}(\Pi_{V_S}).$
		Thus $\Pi_{V_S}$ is hermitian, and its square is $I$, so it is a projector with image $V_S.$


### Coding space size theorem
- **Thm(Coding space size):** $\text{dim}(V_S) = 2^k$ for nontrivial stabilizer $S=<g_1, \ldots g_{}>$.
	Proof:
		Consider a stabilizer $S=<g_1,\ldots g_{n-k}>$. We know $\Pi_{V_S}$ is the projector onto $V_S$, so $\text{rank}(\Pi_{V_S})=\text{dim}(V_S)$. Note that $\text{dim}(V_S)=\text{Tr}(\Pi_{V_S})$ because the [[trace of a projector is is the dimension of it's image]]. $\implies \text{dim}(V_S)=\frac{1}{|S|}\sum_{g\in S}\text{Tr}(g)=\frac{1}{|S|}\sum_{g\in S}2^n \delta_{g,I}$ because note [[trace is the sum of eigenvalues]], and the [[F-ST-Pauli_Group#Eigenvalues|eigenvalues of elements in the Pauli group]] are $\pm 1$ unless they are $I$

- #wip

