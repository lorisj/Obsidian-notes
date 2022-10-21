# Typical Subspace
### Metadata
Path: #pathQINF, #pathQINF/SRC
Tags:

### Prerequisites
[[Typical_Set#Introduction|Classical typical set]]
[[Quantum_Source#Introduction|Quantum source]]

### Introduction
- #wip
### Typical Subspace Definition
**Def(Typical Subspace):** Suppose we have a [[Quantum_Source#Quantum Random Process|quantum random process]] $\rho^{X^n}=\sum_{x^n \in \mathcal X ^n} p_{X^n}(x^n)|x^n\rangle \langle x^n|$. Define the $\delta-$typical subspace: 
$T_{\delta}^{X^n}=\text{span}\{|x^n\rangle : |-\log(P_{X^n}(x^n))/n-H(X)|\le \delta\}=\text{span}\{|x^n\rangle : x^n \text{ is }A_{\delta}^{X^n} \text{ typical}\}$ 
where $A_{\delta}^{X^n}$ is the [[Typical_Set#Introduction|classical typical set]].

### Typical Projector Definition
**Def(Typical Projector):** Let $T_{\delta}^{X^n}$ be the [[#Typical Subspace Definition|typical subspace]]. We define the typical projector as $\Pi_{\delta}^{X^n}=\sum_{|x^n\rangle \in T_{\delta}^{X^n}}|x^n\rangle \langle x^n|$.
	Note this is a projector as it has orthogonal eigenvectors ($\langle y^n|x^n\rangle=\delta_{xy}$) and eigenvalues are all 1.

### Sliced Density Operator Definition
**Def(Sliced Density Operator):** Given some density operator $\rho^{X^n}$, let $T_\delta^{X^n}$ be the typical subspace with projector $\Pi_{\delta}^{X^n}$. Define the sliced density operator $\tilde{\rho}_{\delta}^{X^n}=\Pi_{\delta}^{X^n}\rho^{X^n}\Pi_{\delta}^{X^n}$. 
	This turns the density operator into another operator that only has components in the typical subspace.

### Unit Probability of Typical Subspace Lemma
**Lem(Unit Probability of Typical Subspace):** $\forall_{\epsilon > 0} \text{Tr}(\Pi_\delta^{X^n} \rho^{X^n})\ge 1-\delta$ for sufficiently large $n$.
	Proof:
		Note $\text{Tr}(\Pi_{\delta}^{X^n}\rho^{X^n})=\sum_{x^n\in A_{\delta}^{X^n}}p_{X^n}(x^n)$ because the trace is the sum of the eigenvalues (probabilities) of all elements that are in the typical set, which is $P(A_{\delta}^{X^n})\ge 1-\delta$ for sufficiently large n by the [[Typical_Set#Unit Probability Theorem|classical typical set unit probability theorem]]
		

### Exponentially Small Distribution Lemma
**Lem(Exponentially Small Distribution):** $\text{Tr}(\Pi_{\delta}^{X^n})\le 2^{n(H(X)+c*\delta)}$ 
	Proof:
		Note $\text{Tr}(\Pi_{\delta}^{X^n})=\sum_{x\in A_{\delta}^{X^n}}1=|A_{\delta}^{X^n}|$, which is $\le 2^{n(H(X)+c*\delta)}$ by the [[Typical_Set#Typical Set Size Theorem|classical typical set size theorem]].
		 

### Equipartition Property Lemma
**Lem(Equipartition Property):** For each eigenvalue $\lambda_i$ of [[#Sliced Density Operator Definition|sliced density operator]] $\tilde{\rho}_{\delta }^{X^n}$, $2^{-n(H(X)+c\delta)}\le \lambda_i \le 2^{-n(H(X)-c\delta)}$ 
	Proof:
		Note $\lambda_i=p_{X^n}(x^n)$ for some $x^n \in A_{\delta}^{X^n}$, and then the lemma follows directly from the [[Typical_Set#Equipartition Property Theorem|classical typical set equipartition theorem]].