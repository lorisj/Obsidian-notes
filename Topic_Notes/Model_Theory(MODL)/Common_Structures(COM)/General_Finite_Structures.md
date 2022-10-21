# General Finite Structures
### Metadata
Path: #pathMODL, #pathMODL/COM
Tags: 

### Prerequisites
- #wip
### Introduction
- #wip
### Finite Structures Have Quantifier Elimination Lemma
**Lem(QE for Finite Structures):** Let $\mathcal{M}$ be a finite $\mathcal{L}$ structure. Then $\mathcal{M}$ admits quantifier elimination.
	Proof: Because $\mathcal{M}$ is finite, we can turn any $\mathcal{L}$ formula $\phi$ into a quantifier free equivalent $\phi_{\text{QE}}$, by replacing any instance of $\forall_x\psi(\bar{a},x)$ with $\bigwedge_{x\in M}\psi(\bar{a},x)$ , and any instance of $\exists_x \psi(\bar{a},x)$ with $\bigvee_{x\in M} \psi(\bar{a},x)$. These yield finite formulas with the same truth value as their quantified counterparts. 


### Finite Isomorphism Corollary
**Cor(Finite Isomorphism):** Let $\mathcal{M,N}$ be finite $\mathcal{L}$ structures, and $\mathcal{M}\cong \mathcal{N}$ with isomorphism $\mathcal{E}$. Then $\mathcal{E}$ is an elementary embedding.
	Proof: 
		Using the [[#Finite Structures Have Quantifier Elimination Lemma|Finite Structures Have QE Lemma]], any $\mathcal{L}$ formula $\phi$ can be turned into an equivalent $\phi_{qe}$ that has no quantifiers. #wip use the lemma that any quantifier free formula is true in all isomorphic structures.