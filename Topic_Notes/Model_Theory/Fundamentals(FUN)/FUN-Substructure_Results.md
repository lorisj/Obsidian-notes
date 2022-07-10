# Substructure results
### Prerequisites

### Introduction

### Substructure definition
**Def(Substructure):** If $\mathcal{M,N}$ are $\mathcal{L}$ structures with $M\subseteq N$ and the inclusion map $\eta:M\to N$ acts as the identity on $M$ is an $\mathcal{L}$ embedding, then $\mathcal{M}$ is a substructure of $\mathcal{N}$. (sometimes written as either $\mathcal{M}\le \mathcal{N}$ or simply $\mathcal{M}\subseteq \mathcal{N}$)

### Examples
**Ex(Substructures of groups):** Note that the notion of substructure is sensitive to the language $\mathcal{L}$. So for instance if $\mathcal{L_{\text{group}}}=\{e,\cdot\}$, then a substructure does not preserve inverses and therefore is not a group, however if $\mathcal{L_{\text{group}}}=\{e,\cdot,\cdot^{-1}\}$ then a substructure must preserve inverses and therefore would be a group.

### Substructures Respect Quantifier Free Formulas Theorem
**Thm(Substructures Respect Quantifier Free Formulas):** Suppose $\mathcal S\le \mathcal B$. $\bar{s} \in S$, and $\varphi$ a quantifier free formula. Then $\mathcal{S} \models \varphi (\bar{s})$ if and only if $\mathcal B \models \varphi (\bar{s})$. (note S is smaller, B is bigger)
	Proof: We argue this result working backwards, first using induction on [[FUN-Terms_Formulas_and_Sentences#Terms Definition|terms]] and [[FUN-Terms_Formulas_and_Sentences#Interpretation of Terms Definition|their interpretations]], and then on [[FUN-Terms_Formulas_and_Sentences#Formulas Definition|formulas]].
		Claim: If $t(\bar{x})$ is a term, and $\bar s \in S$, then $t^\mathcal{S}(\bar s)=t^\mathcal B (\bar s)$
			Proof: (inductive hypothesis: Assume claim is true for subterms $k_i(\bar s)$)
				1) If $t$ is a constant symbol $c$, then $t^\mathcal S(\bar s) = c^\mathcal S = c^\mathcal B = t^\mathcal B (\bar s)$.
				2) If $t$ is a variable symbol $v_i$, then $t^\mathcal S(\bar s) =s_i=t^\mathcal B (\bar s)$.
				3) If t is $f(k_1,\ldots k_n)$ where $k_1, \ldots k_n$ are terms, then by the inductive hypothesis, for each $i$ $k_i^\mathcal S(\bar s)=k_i^\mathcal B(\bar s)$, so $t^\mathcal{S}(\bar s)=f^\mathcal{S}(k_1^\mathcal S(\bar s)\ldots k_n^\mathcal S(\bar s))=f^\mathcal{B}(k_1^\mathcal B(\bar s)\ldots k_n^\mathcal B(\bar s))$, because $f^\mathcal{B}$ acting on elements in $S$ is the same thing as $f^\mathcal S$ acting on the same elements by the [[#Substructure definition|definition of substructure]] as the function $f^\mathcal S$ is the restriction of $f^\mathcal B$.
		Claim: $\mathcal S \models \varphi(\bar s)$ if and only if $\mathcal B \models \varphi(\bar s)$ 
			Proof: (inductive hypothesis: Assume claim is true for subformulas $\psi(\bar a)$)
				1) If $\varphi (\bar x)$ is $t=v$ for terms $t,v$, then
					$\mathcal{S}\models \varphi(\bar s)\iff t^\mathcal S (\bar s)=v^\mathcal S (\bar s) \iff t^\mathcal B (\bar s)=v^\mathcal B (\bar s)\iff \mathcal{B} \models \varphi(\bar s)$ 
					The second $\iff$ is precisely the claim that we proved just above.
				2) If $\varphi(\bar x)$ is $R(t_1, \ldots t_n)$, then 
					$\mathcal{S}\models \varphi(\bar s)\iff (t_1^\mathcal S (\bar s),\ldots t_n^\mathcal S (\bar s)) \in R^\mathcal S \iff (t_1^\mathcal B (\bar s),\ldots t_n^\mathcal B (\bar s)) \in R^\mathcal B \iff \mathcal{B} \models \varphi(\bar s)$ 
					where the second $\iff$ is due to the fact that the restricted relation $R^\mathcal S$ is equivalent to $R^\mathcal B$ when acting on elements in $S$, and that $t_i ^\mathcal B(\bar s) \in S$.
				3) If $\varphi (\bar x)$ is $\neg \psi(\bar x)$, then 
					$\mathcal S \models \varphi(\bar s)\iff \mathcal S \not \models \psi(\bar s)\iff \mathcal B \not \models \psi(\bar s)\iff \mathcal B \models \varphi(\bar s)$ 
					where the second $\iff$ is due to the inductive hypothesis
				4) If $\varphi (\bar x)$ is $\psi_1(\bar x) \land \psi_2 (\bar x)$, then				
					$\mathcal S \models \varphi(\bar s)\iff \mathcal S  \models \psi_1(\bar s) \text{ and }\mathcal S  \models \psi_2(\bar s)$  
					$\iff \mathcal B  \models \psi_1(\bar s) \text{ and }\mathcal B \models \psi_2(\bar s)\iff \mathcal B \models \varphi(\bar s)$
				where the second $\iff$ is due to the inductive hypothesis
			From and we can get or, so that proves the claim.

### Substructures with Quantified Formulas Theorem
**Thm(Substructures with Quantified Formulas):** Suppose $\mathcal{S} \le \mathcal B$, $\bar s \in S$, and $\varphi(\bar x, \bar y)$ is a quantifier free formula. Then:
	1) if $\mathcal S \models \exists_{\bar y} \varphi(\bar s, \bar y)$, then $\mathcal B \models \exists_{\bar y} \varphi(\bar s, \bar y)$
	2) if $\mathcal B \models \forall_{\bar y} \varphi(\bar s, \bar y)$, then $\mathcal S \models \forall_{\bar y} \varphi(\bar s, \bar y)$
	Proof for 1):
		Recall the [[FUN-Truth#Truth Definition|definition of truth in structures]], namely point 6. If $\mathcal S \models \exists_{\bar y} \varphi(\bar s, \bar y)$, then there is some $\bar k$ in $S^n$ such that $\mathcal{S}\models\varphi(\bar{s},\bar{k })$ since $\bar k \in S^n$, it must also be in $B^n$ as $S\subseteq B$, and thus by the [[#Substructures Respect Quantifier Free Formulas Theorem|previous theorem]] and noting again $\varphi$ is quantifier free by assumption, $\mathcal{B}\models \varphi(\bar s, \bar k)$. Thus by [[FUN-Truth#Truth Definition|point 6 of the definition of truth in structures]], $\mathcal B \models \exists_{\bar y} \varphi(\bar s, \bar y)$.
	Proof for 2):
		Recall the [[FUN-Truth#Truth Definition|definition of truth in structures]], namely point 7. If $\mathcal B \models \forall_{\bar y} \varphi(\bar s, \bar y)$, then for every $\bar k$ in $B^n$ it must be the case that $\mathcal{B}\models\varphi(\bar{s},\bar{k })$. Note that $\mathcal S \models \forall_{\bar y} \varphi(\bar s, \bar y)$ by definition is true if and only if $\mathcal S \models  \varphi(\bar s, \bar k)$ for every $\bar k\in S^n$. Note that this condition is satisfied, because for every $\bar{k} \in S^n$ $\mathcal{B}\models \varphi(\bar s, \bar k)$ , and so by the [[#Substructures Respect Quantifier Free Formulas Theorem|previous theorem]] for every $\bar k \in S^n$:  $\mathcal S \models  \varphi(\bar s, \bar k)$ . Thus $\mathcal{S}\models \forall_{\bar y} \varphi(\bar s, \bar y)$.

