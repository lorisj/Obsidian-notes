# Theories,  Elementary Classes and Equivalence
### Prerequisites

### Introduction
#wip 

### Theories and Satisfiability Definition
**Def(Theory):** An $\mathcal L$ theory $T$ is a set of $\mathcal{L}$ [[FUN-Terms_Formulas_and_Sentences#Sentence Definition|sentences]]. We say that $\mathcal{M}$ is a model of $T$ (i.e $\mathcal M \models T$) if $\mathcal M \models \phi$ for every $\phi \in T$.

**Def(Satisfiability):** An $\mathcal L$ theory $T$ is said to be satisfiable iff $T$ has a model $\mathcal M$, i.e there is some $\mathcal M$ such that $\mathcal M\models T$.

### Full Theory Definition
**Def(Full Theory):** The full theory of $\mathcal L$ structure $\mathcal M$, denoted $\text{Th}(\mathcal M)$, is the complete set of sentences that $\mathcal M$ satisfies. $\text{Th}(\mathcal M)=\{\mathcal{L} \text{ sentences }\phi : \mathcal M \models \phi\}$ 

### Elementary Classes Definition and Intuition
**Def(Elementary Class):** A class $\mathcal{K}$ of $\mathcal L$ structures is called an elementary class if there is an $\mathcal L$ theory $T$ such that $\mathcal{K}=\{\mathcal M : \mathcal M \models T\}$.

Note that to get an elementary class is to consider $T=\text{Th}(\mathcal M)$ and this guarantees that the elementary class $\mathcal K = \{\mathcal{N}:\mathcal N \models T\}$ contains at least one element, namely $\mathcal{M}$.

### Equivalence Definition
**Def(Elementary Equivalence):** Two $\mathcal L$ structures $\mathcal M,\mathcal N$ are elementary  equivalent if they satisfy the same set of $\mathcal{L}$ sentences. More formally, $\mathcal{M}\equiv \mathcal{N}$ if and only if $\text{Th}(\mathcal{M})=\text{Th}(\mathcal N)$

### Complete Theory Definition
**Def(Complete Theory):** A theory $T$ is called a complete theory if for every $\mathcal L$ sentence $\varphi$, either $T\models \varphi$ or $T \models \neg \varphi$.


### Full theory is Complete Theorem
**Thm(Full Theory is Complete):** Note that the full theory of any model $\text{Th}(\mathcal M)$ is always complete
	Proof:
	Recall the [[#Full Theory Definition|definition of the full model of a theory]]. 