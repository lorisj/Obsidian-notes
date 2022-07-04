# Optimal Random Coding
### Prerequisites
[[STC-EC-Correctability_of_errors]]

### Introduction

### Pauli Channel
**Def(Pauli Channel):** The Pauli channel is a CPTP map $\mathcal{K}$ where:
	$$\rho\to p_I\rho+p_XX\rho X+p_Y Y\rho Y + p_Z Z \rho Z$$
	For probability vector $\vec{p}=(p_I,p_X,p_Y,p_Z)$.

The capacity of the Pauli Channel is $I_C= 1-H(\vec{p})$ , where $\vec{p}$ is the probability vector mentioned above, and maximizing density operator is $I/2$.
#wip Add notes on pauli channel

### Typical error set
**Def(Typical Error Set):** $T_\delta=\{a^n : |\frac{1}{n}\log{(Pr(E_{a^n})-H(\vec{p}))}|\le \delta \}$ , where $P(E_{a^n})$ is the probability that an IID Pauli channel issues tensor-product error $E_{a^n}=\bigotimes_{i=1}^{n}E_{a_i}$.

Note $\sum_{a\in T_\delta}{P(E_{a_n})} \le1-\delta$ , argument is just applying the [[GEN-Typical_Set#Probability of Error|error probability of the typical set]]

If we correct all the errors in the typical error set, then we have satisfied the [[EC-Definition_and_Requirements#Error Property|error correcting probability]] property of error correcting codes. If our code then achieves capacity $I_C$, then it is an optimal code.

### Stabilizer Codes Achieve Pauli Channel Capacity Theorem 
To satisfy the [[EC-Definition_and_Requirements#Error Property|error correcting probability]] of error correcting codes, we want for all $E_a, E_b \in T_\delta: E_a E_b \notin \mathcal{N}(S)-S$ ([[STC-EC-Correctability_of_errors#Correctable errors theorem|Error correction thm for Stabilizer Codes]]) i.e all typical errors are correctable.

**Thm(Stabilizer Codes Achieve Pauli Channel Capacity):** Stabilizer codes can achieve capacity for the Pauli channel.
	Proof: Construct a random stabilizer code $(V_S)\cup S$ such that $E_a E_b \notin T_\delta$. This means that all typical errors can be corrected, and so we only have to look at $p_{error}$ to prove the theorem. We consider $\mathbb{E}[p_{error}]$ under the distribution of uniform random stabilizer codes:
	$\mathbb{E}(p_{error})$
		$=\sum_{a^n \in T_\delta}{[P(E_{a^n})P_S(E_{a_n} \text{ is not correctable under } S)}]+\epsilon$ 
			This is just using the [[Law_of_Total_Probability]], and adding the $\epsilon$ corresponds to the probability of error due to an error outside the typical set.
		$=\sum_{a^n\in T_\delta}P(E_{a^n})P_S(\exists_{E_{a^n}} : b^n \ne a^n, b^n \in T_\delta \text{ and } E_{a^n}E_{b^n} \notin \mathcal{N}(S)-S )$ 
		$\le \sum_{a^n \in T_\delta, b^n \ne a^n} P(E_{a^n})P_S( E_{a^n}E_{b^n} \notin \mathcal{N}(S)-S )$
			This is just assuming that there always exists such a $b_n$. So you're summing over all $a_n \in T_\delta$, and assume that there is some fixed $b^n \ne a^n$
		$\le 2^{nH(\vec{p})}$
			The number of non identity elements in $\mathcal{P}^n$ is $2^{2n}-1$. 
			The number of non identity elements in $\mathcal{N}(S)$ is $2^{n+k}-1$
			