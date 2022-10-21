	+# Numbering the Turing Programs
### Metadata
Path: #pathCOMP
Tags:

### Prerequisites

### Introduction

### Numbering the Turing Programs Theorem
**Thm(You Can Number the Turing Programs):** A [[Turing_Machines#Turing Machine Definition|Turing program]] is a finite sequence of 5 tuples from $T_5 = (Q\times S )\times(Q\times S\times \{L,R\})$ 
	*This comes from just writing down $\delta$ as a list*
We can identify each of these $\bar t\in T_5$ with 5 tuples from $\omega^5$
We can identify each of these $\bar n \in \omega^5$ with a single number from $\omega$
	*This is just from the [[Pairing#Pairing Function Definition|pairing function]]* 
*So, $\delta$ is a finite sequence of natural numbers, and we can identify the entire $\delta$ with one natural number.*

### Gödel numbers, Index Definition 
**Def(Gödel numbers, index, $P_e$, $\varphi_e$):** 
1) Let $P_e$ be the $e$th Turing program that comes from [[#Numbering the Turing Programs Theorem|listing out the Turing programs]].
2) Let $\varphi_e$ be the partial computable function for $P_e$
We say that $e$ is the index of program $P_e$ and of partial computable function $\varphi_e$.
Note that it is possible to have $P_e \ne P_i$ but $\varphi_e = \varphi_i$.

**Cor(You Can Number All Partial Computable Functions):** Just list out the indexes, and since the $e$th Turing program $P_e$ computes the partial function $\varphi_e$, you will eventually get to the index of any computable function.

### Padding Lemma
**Lem(Padding):** For each Turing program $P_e$, there are infinitely many $P_i$ such that $P_e \ne P_i$ but $\varphi_e = \varphi_i$.
	Proof:
		Fix $P_e$. Add states $q_n, q_{n+1}, \ldots$ (1 new state for each $n \in \mathbb N$) one at a time to make new programs $P_{e,n}, P_{e, n+1}, \ldots$, with random instructions for $\delta$ acting on those states. Then we have an infinite amount of Turing machines that compute the same function, because these states will never be reached.
*We will show that $\{<e,i> : \varphi_e = \varphi_i\}$ is uncomputable*


