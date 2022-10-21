### Pauli Groups:
### Prerequisites
- #wip

### Introduction
This note covers the [[#Definition of Pauli group|definition of the Pauli Group]], as well as its [[#Properties of mathcal G n|properties]].

### Definition of Pauli group
**Def:** $\mathcal{G} =(G,*,I)=(\{cI,cX,cY,cZ : c\in \{\pm1,\pm i\}\},*,I)$ be the 1 Pauli group

You can check that this does in fact form a group. 
We can generalize this to nfold tensor products:

**Def:** $\mathcal{G^n}=\otimes_{i=1}^n{\mathcal G}$
Also forms a group because the [[tensor product preserves group structure]].

### Properties of $\mathcal{G^n}$:
- Every element is its own inverse
- Every element either commutes/anticommutes
- $\mathcal{G^n}$ forms a basis for $\mathbb{C}^{2^n\times 2^n}$
- $|\mathcal{G}^n|=4^n *4 = 4^{n+1}$ 

### Eigenvalues of Pauli Operators Lemma
**Lem(Eigenvalues of Pauli Operators):** $g\in G^n\implies \text{Eigenval}(g)\in \{\pm 1, \pm i\}.$
	Proof:
		$g \in G^n \implies$ the eigenvalues of $g$ are the products of the eigenvalues of it's component operators $g = \otimes_{i=1}^{n} g_i$ . Note the eigenvalues of $g\in G^n$ are simply the products of the eigenvalues of the $1$ Pauli group $\mathcal G$. Note that elements in $\{cI, cX,cY,cZ:c\in C=\{\pm 1, \pm i\}\}$ have eigenvalues $\in C$, and note $(C, *_{\mathbb C})$ is closed under $*$ thus eigenvalues of $g$ must be in $C$.  

### Trace of Pauli Operators Lemma
**Lem(Trace of Pauli Operators):** $g\in G^n \implies$ $\text{Tr}(g)=c*2^n*\delta_{g,cI}$
