# Coding space ($V_S$) definition and properties
[[Basic_Properties]]
## Normalizer/centralizer:
**Def (Normalizer):** $\mathcal{N}(S\subseteq_\text{group} G^n)=\{E\in G^n: E \text{ fixes } S \text{ setwise under conjugation}\}$ 
														$= \{E\in G^n : E SE^\dagger \in S \}$

Normalizers are important because they are equivalent to something called the centralizer

**Def (Centralizer):**  $\mathcal{Z}(S\subseteq_\text{group} G^n)=\{E\in G^n : E\text{ commutes with every element of }S\}$  
														$= \{E\in G^n : \forall_{s\in S} {E s=sE} \}$
														$\equiv\{E\in G^n: E \text{ fixes } S \text{ pointwise under conjugation}\}$

For the Pauli group, $\mathcal{Z}(S)=\mathcal{N}(S)$ if $-I \notin S$

