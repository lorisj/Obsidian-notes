# Truth

### Prerequisites

### Introduction
#wip
### Truth Definition
**Def(Truth):** Let $\mathcal{M}$ be an $\mathcal{L}$ structure, and $\varphi(x_1, \ldots x_n)$ be an $\mathcal{L}$ formula, and let $a_1, \ldots a_n \in M$. We define $\mathcal{M}\models\varphi(a_1, \ldots a_n)$ through the following cases:
	1) Case $\varphi$ is $s=t$: 
		if $s^\mathcal{M}=t^\mathcal{M}$, then $\mathcal{M} \models \varphi(\bar{a})$   
	2) Case $\varphi$ is $R(t_1, \ldots t_n)$: 
		if $(t_1^\mathcal{M}(\bar{a}),\ldots t_n^\mathcal{M}(\bar{a}))\in R^\mathcal{M}$ then  $\mathcal{M} \models \varphi(\bar{a})$  
	3) Case $\varphi$ is $\neg \psi$:
		if $\mathcal{M} \not \models \psi(\bar{a})$ then $\mathcal{M} \models \varphi(\bar{a})$ 
	4) Case $\varphi$ is $\psi_1 \land \psi_2$:
		if $\mathcal{M}\models \psi_1(\bar{a})$ and $\mathcal{M} \models \psi_2(\bar{a})$ then $\mathcal{M} \models \varphi(\bar{a})$
	5) Case $\varphi$ is $\psi_1 \lor \psi_2$:
		if $\mathcal{M} \models \psi_1(\bar{a})$ or $\mathcal{M} \models \phi_2(\bar{a})$ then $\mathcal{M}\models \varphi$
	6) Case $\varphi$ is $\exists_y \psi(\bar{x},y)$: 
		if there is a $b \in M$ such that $\mathcal{M}\models \psi(\bar{a},b)$ then $\mathcal{M}\models \varphi(\bar{a})$
	7) Case $\varphi$ is $\forall_y \psi(\bar{x},y)$:
		if for every $b \in M$, $\mathcal{M}\models \psi(\bar{a},b)$ then $\mathcal{M}\models \varphi(\bar{a})$ 

If $\mathcal{M}\models \varphi(\bar a)$, then we say $\mathcal{M}$ satisfies $\varphi(\bar a)$, or that $\varphi(\bar a)$ is true in $\mathcal{M}$.


### Everything is True or False Lemma
**Lem(Everything is True or False):** Fix arbitrary $\mathcal{L}$ structure $\mathcal{M}$. For any $\mathcal{L}$ sentence $\varphi(\bar{x})$, and any tuple $\bar{a} \in M$, it is either the case that $\mathcal{M}\models \varphi(\bar{a})$ xor that $\mathcal{M}\models \neg \varphi(\bar a)$.
	Proof: This follows immediately from case $3$. If $\mathcal{M}\not \models \varphi(\bar a)$ then it must be the case that $\mathcal M \models \neg \phi(\bar a)$. Likewise if $\mathcal{M} \not \models \neg \varphi(\bar{a})$ then 