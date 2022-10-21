# Weak Law of Large Numbers
### Metadata
Path: #pathPROB, #pathPROB/CON
Tags:

### Prerequisites
- [[Random process]]
- [[Weak_Law_of_Large_Numbers#Introduction|WLLN]]
- [[Convergence_in_Probability#Introduction|Convergence in probability]]
### Introduction

### Weak Law of Large Numbers Theorem
**Thm(Weak Law of Large Numbers):** Let $X_1,\ldots X_n,\ldots$ be an [[iid random process|IID random process]] random process with finite mean $E[X_i]=\mu$ and finite variance $Var[X_i]=\sigma^2$, then if we define $Z_n := \frac{1}{n}\sum_{i=1}^{n}X_i$ , then $Z_n$ [[Convergence_in_Probability#Convergence in Probability Definition|converges to]]  $\mu$ [[Convergence_in_Probability#Convergence in Probability Definition|in probability]].
	Proof:
		Note $E[Z_n]=\frac{n\mu}{n}=\mu$
		$P(|Z_n-\mu|>\epsilon)\le \frac{Var(Z_n)}{\epsilon^2}$
			By [[Mean_Distance_Inequalities#Chebyshev's Inequality Definition|Chebyshev's Inequality]].
		$=\frac{1}{n\epsilon^2}$
			$Var(Z_n)=\frac{1}{n^2}(n\sigma^2)\to 0$ in probability as $n\to \infty$.
		$\to 0$ as $n\to \infty$

