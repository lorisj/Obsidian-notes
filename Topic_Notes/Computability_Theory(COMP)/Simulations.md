# Simulations
### Metadata
Path: #pathCOMP
Tags:

### Prerequisites

### Introduction


### Simulation Lemma
**Lem(Simulation):** Given input $n \in \omega$ and $P_e$, you can effectively simulate the computation of $P_e$ on input $n$.
	Proof:
		Make initial configuration $q_1, \bar{l},\bar{r},s=input[0]$, then we can find the second configuration through [[Turing_Machines#Running a Turing Program|running a Turing Program]]. 

### Universal Machine Theorem
**Thm(Universal Machine):** There is a partial computable function $\psi(e,n)$ such that $\psi(e,n)=\varphi_e(n)$.
	*$\implies$ for some i, $\psi=\varphi_i$.*
	Proof:
		On input $(e,n)$ $\psi$ [[#Simulation Lemma|simulates]] the act of $P_e$ on input $n$, and just outputs the same result if the computation stops.

 *$\psi$ essentially is just a function that runs a Turing machine that you give "code" $e$ to and "input" $n$.* 

 