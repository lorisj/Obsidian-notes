### Prerequisites

### Introduction
- #wip

### Span Definition
**Def(Span):** Given a [[FUN-Vector_Spaces#Vector Space Definition Axioms|vector space]] $\mathcal V$ over field $\mathbb F$, and $A\subseteq V$, define $\text{Span}(A)= \bigcap_{\mathcal S < \mathcal V : A \subseteq S}\mathcal S$ , i.e the intersection of all subspaces of $\mathcal V$  whose domain contains $A$.


### Span is a Subspace Lemma
**Lem(Span is a Subspace):** For vectorspace $\mathcal V$,  and $A \subseteq V$, $\text{span}(A)$ is a vectorspace. 
	Proof:
		Because $\text{dom}(\text{Span}(A)) \subseteq V$, (as $\text{dom}(\mathcal S) \subseteq V$ for all such $\mathcal S$ listed above) using the fact that [[Vector_Spaces#Substructure of a Vector Space is a Vector Space Lemma|any substructure of a vector space is a vector space]], it must be that $\text{Span}(A)$ is a substructure of $\mathcal V$, and so a subspace.
