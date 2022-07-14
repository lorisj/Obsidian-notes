# Stabilizer definition and properties
#### Prerequisites:

### Introduction
This note gives the [[#Stabilizer Definition|definition]] and some [[#Stabilizer Properties|properties]] for stabilizers as well as the [[#Stabilizer Size Theorem|stabilizer size theorem]].

### Stabilizer Definition
- **Def (Stabilizer):** A stabilizer $S\subseteq \mathcal{G^n}$ is a finite abelian subgroup of $\mathcal{G^n}$

### Stabilizer Properties
- $-I \notin S$ 
Why is $-I\notin S$?
	This is because $-I\in S \implies$ $V_S = \{ \vec{0} \}$, as $-I*\vec{v} = \vec{v} \implies \vec{v} = \vec{0}$ 

- $S$ has $l=n-k$ commuting and independent generators
	(Follows from the fact that by [[#Stabilizer Definition|definition]] $S$ is an abelian group)

### Stabilizer Size Theorem
**Thm(Stabilizer Size):** Given stabilizer $S=<g_1, \ldots g_{n-k}>$, $|S/\{\pm I, \pm i\}|=2^{n-k}$.
	Proof:
		We assume familiarity with the [[STC-BP-Check_Matrix#Introduction|check matrix]]. 
		Let $B=\{r(g_1),\ldots r(g_{n-k})\}$ (rows of $H(S)$) ,$\mathcal V=\text{rowspace}(H(S))$.
		This means $\mathcal V$ is $\text{span}(B)$. Because $\{g_1, \ldots g_{n-k}\}$ is a a set of linearly independent group generators, this means $B$ is a set of linearly independent vectors by the [[STC-BP-Check_Matrix#Linear Independence is Group Independence Corollary|linear independence is group independence corollary]], and so $B$ is a basis for $V$. Using the [[FUN-Basis#Unique Decomposition Theorem|unique decomposition theorem]], each vector $\in V$ corresponds to a unique linear combination of basis vectors $B$. So $|V|=\# \text{linear combinations of }\{h(g_1),\ldots h(g_{n-k})\}=|2^{n-k}|$ by the [[COM-Mod_2_Vector_Space#Mod 2 Vector Space Size Theorem|mod 2 vector space size theorem]]. Note $|V|=|S/\{\pm I, \pm i\}|$ because you can make an $\mathcal L_{\text{vspace}}$ sentence $\psi_{p}$ that is equivalent to saying the size of the current model is $p \in \mathbb N$, we know that $\mathcal V \models \psi_{2^{n-k}}$. Because $\mathcal V \simeq S/\{\pm I, \pm i\}$ by the [[STC-BP-Check_Matrix#Pauli Group is a mod 2 Vector Space Lemma|check matrix isomorphism theorem]], and we know that  [[isomorphism is elementary embedding thm|every isomorphism is an elementary embedding]], we can conclude that  $S/\{\pm I, \pm i\}\models \psi_{2^{n-k}}$  and so $|S/\{ \pm I, \pm i \}|=2^{n-k}$.
