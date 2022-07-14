# Homomorphisms, Embeddings, and Isomorphisms
### Prerequisites
[[FUN-Language_and_Structure#Introduction|Languages/Structures]] 

### Introduction
In this note, we write about structure preserving maps between structures. This includes the definitions of [[#Homomorphisms Embeddings and Isomorphisms|homomorphism]], [[#mathcal L Embedding Definition|embedding]], and [[#mathcal L Isomorphism Definition|isomorphism]].

### $\mathcal{L}$ Homomorphism Definition
**Def($\mathcal{L}$ Homomorphism):** An $\mathcal{L}$ Homomorphism $\eta$ is a function between two $\mathcal{L}$ structures $\eta : \mathcal{M}\to\mathcal{N}$ such that $\eta$  preserves all interpretations of symbols in $\mathcal{L}$. Formally:
	1) For each function symbol $f$ of arity n, and each $a_1,\ldots a_n \in M$:
			$\eta(f^\mathcal{M}(a_1,\ldots a_n))=f^\mathcal{N}(\eta(a_1),\ldots\eta(a_n))$ 
	2) For each relation symbol $R$ of arity n, and each $a_1,\ldots a_n \in M$:
			$(a_1,\ldots a_n)\in R^\mathcal{M}\iff (\eta(a_1),\ldots\eta(a_n)) \in R^\mathcal{N}$ 
	3) For each constant symbol $c$ :
			$c^\mathcal{M} =c^\mathcal{N}$


### $\mathcal{L}$ Embedding Definition
**Def($\mathcal{L}$ Embedding):** An $\mathcal{L}$ embedding $\eta$ is a one to one $\mathcal{L}$ [[#mathcal L Homomorphism Definition|homomorphism]].

### $\mathcal{L}$ Isomorphism Definition
**Def($\mathcal{L}$ Isomorphism):** An $\mathcal{L}$ isomorphism $\eta$ is a bijective $\mathcal{L}$ [[#mathcal L Homomorphism Definition|homomorphism]].


