# Von Neumann Entropy
### Prerequisites

### Introduction
In this note, we give the [[#Definition|definition]] of Von Neumann Entropy, which is the generalization of the concept of [[FUN-Shannon Entropy|shannon entropy]]


### Entropy
**Def(Von Neumann Entropy):** The Von Neumann entropy of a density operator $\rho$ is written as $S(\rho)$, and is defined as the Shannon entropy $H(p_Y)$ of the distribution $p_Y(y)=(\lambda_y)_y$, where $p_Y(y)$ are the eigenvalues of $\rho$ which are found from the spectral decomposition of $\rho=\sum_y{\lambda_y |\psi_y\rangle\langle\psi_y|}$. 

### Von Neumann Entropy is Minimal Theorem
**Thm(Von Neumann Entropy is Minimal):** Let $\rho$ be a density operator. $S(\rho)$ is minimal in the sense that for any other ensemble corresponding to $\rho$ with probabilities $p_X$, $H(p_y)\le H(p_x)$.
	Proof:
	#wip use concavity of entropy? + recursivity if needed
	