# Language and Structure
### Prerequisites

### Introduction
In this note, we give the [[#Definition of Language|definition of language]], as well as the [[#Definition of Structure|definition of a structure]].

### Definition of Language
**Def(Language):** A language $\mathcal{L}$ is a set that consists of 
	1) A set $\mathcal{L}_\mathcal{F}$ of function symbols $f$ with arities $n_f$
	2) A set $\mathcal{L}_\mathcal{R}$ of relation symbols $R$ with arities $n_r$
	3) A set $\mathcal{L}_\mathcal{C}$  of constant symbols $c$  

### Definition of Structure
**Def(Structure):** An $\mathcal{L}$ structure $\mathcal{M}$ consists of:
	0) A nonempty set $M$ called the domain/universe
	1) For each $f\in\mathcal{L}_\mathcal{F}$, a function $f^{\mathcal{M}}:M^{n_f}\to M$
	2) For each $R \in \mathcal{L}_\mathcal{R}$, a relation $R^M \subseteq M^{n_r}$ 
	3) For each $c\in \mathcal{L}_\mathcal{C}$, an element $c^\mathcal{M} \in M$
	We call such $f,R,c$ interpretations of symbols $f,R,c$.


