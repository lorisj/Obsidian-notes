# Truth

### Prerequisites
[[FUN-Language_and_Structure#Introduction|Languages and Structures]], [[FUN-Terms_Formulas_and_Sentences#Introduction|terms, formulas, sentences]]

### Introduction
In this note we give [[#Truth Definition|definition of truth]], as well as a [[#Everything in a Structure is True or False Lemma|result that states everything in a structure is either true or false]].

### Truth Definition
**Def(Truth):** Let $\mathcal{M}$ be an $\mathcal{L}$ structure, and $\varphi(x_1, \ldots x_n)$ be an $\mathcal{L}$ formula, and let $a_1, \ldots a_n \in M$. We define $\mathcal{M}\models\varphi(a_1, \ldots a_n)$ through the following cases:
	1) Case $\varphi$ is $s=t$: 
		iff $s^\mathcal{M}=t^\mathcal{M}$, then $\mathcal{M} \models \varphi(\bar{a})$   
	2) Case $\varphi$ is $R(t_1, \ldots t_n)$: 
		iff $(t_1^\mathcal{M}(\bar{a}),\ldots t_n^\mathcal{M}(\bar{a}))\in R^\mathcal{M}$ then  $\mathcal{M} \models \varphi(\bar{a})$  
	3) Case $\varphi$ is $\neg \psi$:
		iff $\mathcal{M} \not \models \psi(\bar{a})$ then $\mathcal{M} \models \varphi(\bar{a})$ 
	4) Case $\varphi$ is $\psi_1 \land \psi_2$:
		iff $\mathcal{M}\models \psi_1(\bar{a})$ and $\mathcal{M} \models \psi_2(\bar{a})$ then $\mathcal{M} \models \varphi(\bar{a})$
	5) Case $\varphi$ is $\psi_1 \lor \psi_2$:
		iff $\mathcal{M} \models \psi_1(\bar{a})$ or $\mathcal{M} \models \phi_2(\bar{a})$ then $\mathcal{M}\models \varphi$
	6) Case $\varphi$ is $\exists_y \psi(\bar{x},y)$: 
		iff there is a $b \in M$ such that $\mathcal{M}\models \psi(\bar{a},b)$ then $\mathcal{M}\models \varphi(\bar{a})$
	7) Case $\varphi$ is $\forall_y \psi(\bar{x},y)$:
		iff for every $b \in M$, $\mathcal{M}\models \psi(\bar{a},b)$ then $\mathcal{M}\models \varphi(\bar{a})$ 

If $\mathcal{M}\models \varphi(\bar a)$, then we say $\mathcal{M}$ satisfies $\varphi(\bar a)$, or that $\varphi(\bar a)$ is true in $\mathcal{M}$.


### Everything in a Structure is True or False Lemma
**Lem(Everything in a structure is True or False):** Fix arbitrary $\mathcal{L}$ structure $\mathcal{M}$. For any $\mathcal{L}$ sentence $\varphi(\bar{x})$, and any tuple $\bar{a} \in M$, it is either the case that $\mathcal{M}\models \varphi(\bar{a})$ xor that $\mathcal{M}\models \neg \varphi(\bar a)$.
	Proof: This follows mostly from [[#Truth Definition|case 3]]. It must be the case that either $\mathcal{M}\models \varphi(\bar{a})$ xor $\mathcal M \not \models \varphi(\bar a)$. This can be shown because any formula $\varphi(\bar{a})$ by induction using the steps [[#Truth Definition|listed here]] will either be $\mathcal M \models \varphi(\bar{a})$ or not, in which case we can by definition say $\mathcal{M} \not \models \varphi(\bar{a})$. Thus using [[#Truth Definition|case 3]], we can see that either $\mathcal{M} \models \varphi(\bar a)$ xor $\mathcal{M} \models \neg \varphi(\bar a)$.

