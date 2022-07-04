# Normalizer and Centralizer
#### Prerequisites:
[[STC-BP-Coding_Space_Definition_and_Properties]]

### Introduction
This note talks about the definitions of [[#Normalizer Definition|normalizer]] and [[#Centralizer Definition|centralizer]] of a stabilizer, and gives a [[#Pauli Normalizer Centralizer theorem|theorem]] that shows that they are in fact the same thing. So you can think of commuting with the generators as being the same thing as fixing S setwise under conjugation.

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

### Normalizer Size Theorem
**Thm(Normalizer Size):** $|\mathcal{N}(S)|=2^{n-k}$
	Proof: $|S|=2^{n-k}$ #wip