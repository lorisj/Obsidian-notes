# Normalizer and Centralizer
### Metadata
Path: #pathQINF, #pathQINF/STC, #pathQINF/STC/BP 
Tags:

### Prerequisites:
[[Coding_Space_Definition_and_Properties#Introduction|Coding space definition and properties]]
[[Stabilizer_Definition_and_Properties#Introduction|Stabilizer definition and properties]]

### Introduction
In this note, we talk about the definitions of [[#Normalizer Definition|normalizer]] and [[#Centralizer Definition|centralizer]] of a stabilizer, and give a [[#Pauli Normalizer Centralizer theorem|theorem]] that shows that they are in fact the same thing. We then find [[#Normalizer Size Theorem|size of the nomalizer]].

### Normalizer Definition
**Def (Normalizer):** $\mathcal{N}(S\subseteq_\text{group} G^n)=\{E\in G^n: E \text{ fixes } S \text{ setwise under conjugation}\}$ 
														 $= \{E\in G^n : E SE^\dagger \in S \}$

Normalizers are important because they are equivalent to something called the centralizer

### Centralizer Definition:
**Def (Centralizer):**  $\mathcal{Z}(S\subseteq_\text{group} G^n)=\{E\in G^n : E\text{ commutes with every element of }S\}$  
														 $= \{E\in G^n : \forall_{s\in S} {E s=sE} \}$
														 $\equiv\{E\in G^n: E \text{ fixes } S \text{ pointwise under conjugation}\}$



### Pauli Normalizer/Centralizer theorem
**Thm(Pauli Normalizer/Centralizer)** For the Pauli group, $\mathcal{Z}(S)=\mathcal{N}(S)$ if $-I \notin S$
	Proof:

- #wip
### Normalizer Size Theorem
**Thm(Normalizer Size):** Let $S=<g_1,\ldots g_{n-k}>$ be a stabilizer. $|\mathcal{N}(S/\{\pm I, \pm i\})|=2^{n+k}$
	Proof: 
		We know that $v$ commutes with $g_i$ if and only if $h(g_i) \Lambda h^T(v)=0$ from the [[Check_Matrix#Check Matrix Inner Product Lemma|check matrix inner product]]. So $v$ commutes with all $g_i$ if $\left[\begin{matrix}r(g_1)\\ \ldots \\ r(g_{n-k})\end{matrix}\right]\Lambda r^T(v)=H \Lambda r^T(v)$ is equal to $\left[\begin{matrix}0\\ \ldots \\ 0\end{matrix}\right]$. We wish to count the number of such possible $v$, which would give us $|\mathcal{N}(S/\{\pm I, \pm i\})|$ because of the [[isomorphism is elementary embedding thm]], and we can make an $\mathcal L_{\text{vspace}}$ sentence $\psi_p$ that says the size of the model is $p\in\mathbb N$. So $|\mathcal N(S/\{\pm I, \pm i\})|=|\text{ker}(H\Lambda)|$, and this is $=2^{\text{nullity}(H\Lambda)}$ by the [[Mod_2_Vector_Space#Mod 2 Vector Space Size Theorem|mod 2 vector space size  theorem]]. Because the rows of $H$ are linearly independent ([[Check_Matrix#Linear Independence is Group Independence Corollary|independent generators implies linear independence]]) that means the $\text{RREF}(H)$ has maximal rank, and so $\text{rank}(H\Lambda)=\text{rowrank}(H)=l=n-k$ as right multiplication by $\Lambda$ is invertible. By the [[rank nullity theorem]]:
		$\implies 2n=l+\text{nullity}(H\Lambda)$
		$\implies 2n=n-k+\text{nullity}(H\Lambda)$
		$\implies n+k=\text{nullity}(H \Lambda )$
		$\implies 2^{n+k}=|\mathcal N(S)|$

