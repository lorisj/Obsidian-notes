# Stabilizer definition and properties
#### Prerequisites:

### Introduction
This note gives the [[#Stabilizer Definition|definition]] and some [[#Stabilizer Properties|properties]] for Stabilizers.

### Stabilizer Definition
- **Def (Stabilizer):** A stabilizer $S\subseteq \mathcal{G^n}$ is a finite abelian subgroup of $\mathcal{G^n}$

### Stabilizer Properties
- $-I \notin S$ 
Why is $-I\notin S$?
	This is because $-I\in S \implies$ $V_S = \{ \vec{0} \}$, as $-I*\vec{v} = \vec{v} \implies \vec{v} = \vec{0}$ 

- $S$ has $l=n-k$ commuting and independent generators
	(Follows from the fact that by [[#Stabilizer Definition|definition]] $S$ is an abelian group)

### Stabilizer Size Theorem
**Thm(Stabilizer Size):** Given $n-k$ independent commuting generators, $-I \notin S \implies |S| = 2^{n-k}$
	Proof: For this proof, we leverage the [[STC-BP-Check_Matrix#Pauli Group is a mod 2 Vector Space Lemma|isometry between the check matrix and pauli group]]. The size of the $n-k$ generated stabilizer group is simply the size of the $$
	
#wip 