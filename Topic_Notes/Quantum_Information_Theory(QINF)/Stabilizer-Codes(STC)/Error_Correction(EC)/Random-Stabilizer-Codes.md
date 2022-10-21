# Random Stabilizer Codes
### Metadata
Path: #pathQINF, #pathQINF/STC, #pathQINF/STC/EC 
Tags:

### Prerequisites
[[Correctability_of_errors#Introduction|Correctability of errors]]
[[Typical_Set|Classical Typical Set]]

### Introduction
- #wip
### Pauli Channel
**Def(Pauli Channel):** The Pauli channel is a [[Quantum Channel|CPTP map]] $\mathcal{K}$ where:
	$\rho\to p_I\rho+p_XX\rho X+p_Y Y\rho Y + p_Z Z \rho Z$
	For probability vector $\vec{p}=(p_I,p_X,p_Y,p_Z)$.

The capacity of the Pauli Channel is $I_C= 1-H(\vec{p})$ , where $\vec{p}$ is the probability vector mentioned above, and maximizing density operator is $I/2$.
- #wip 
 
Add notes section on Pauli channel


### Typical error set
**Def(Typical Error Set):** $T_\delta=\{a^n : |\frac{1}{n}\log{(Pr(E_{a^n})-H(\vec{p}))}|\le \delta \}$ , where $P(E_{a^n})$ is the probability that an IID Pauli channel issues tensor-product error $E_{a^n}=\bigotimes_{i=1}^{n}E_{a_i}$.

Note $\sum_{a\in T_\delta}{P(E_{a_n})} \le1-\delta$ , argument is just applying the [[Typical_Set#Unit Probability|unit probability of the typical set]]

If we correct all the errors in the typical error set, then we have satisfied the [[Definition_and_Requirements#Error Property|error correcting probability]] property of error correcting codes. If our code then achieves capacity $I_C$, then it is an optimal code.


### Stabilizer Codes Achieve Pauli Channel Capacity Theorem 
To satisfy the [[Definition_and_Requirements#Error Property|error correcting probability]] of error correcting codes, we want for all $E_a, E_b \in T_\delta: E_a E_b \notin \mathcal{N}(S)-S$ ([[Correctability_of_errors#Correctable errors theorem|error correction theorem for stabilizer codes]]) i.e all typical errors are correctable.


**Thm(Stabilizer Codes Achieve Pauli Channel Capacity):** Stabilizer codes can achieve capacity for the Pauli channel.
	Proof: 
		Construct a random stabilizer code $(V_S)\cup S$ such that $E_a E_b \notin T_\delta$. This means that all typical errors can be corrected, and so we only have to look at $p_{error}$ to prove the theorem. We consider $\mathbb{E}[p_{error}]$ under the distribution of uniform random stabilizer codes:
		$\mathbb{E}_S(p_{error})$
		$=\sum_{a^n \in T_\delta}{[P(E_{a^n})P_S(E_{a_n} \text{ is not correctable under } S)}]+\epsilon$ 
			This is just using the [[Law_of_Total_Probability|law of total probability]], and adding the $\epsilon$ corresponds to the probability of error due to an error outside the typical set.
		$=\sum_{a^n\in T_\delta}[P(E_{a^n})P_S(\exists_{E_{b^n}} : b^n \ne a^n, b^n \in T_\delta \text{ and } E_{a^n}E_{b^n} \notin \mathcal{N}(S)-S )] + \epsilon$ 
			[[Correctability_of_errors#Correctable errors theorem|Correctable errors theorem]] applied to $\mathcal{E}=T_\delta$.
		$=\sum_{a^n\in T_\delta}[P(E_{a^n})P_S(\bigcup_{b^n \in T_\delta, b^n\ne a^n}  E_{a^n}E_{b^n} \notin \mathcal{N}(S)-S )] + \epsilon$
			 $Pr(\exists_{x\in A} \varphi(x))$ is the same as $Pr(\bigcup_{x\in A} \varphi(x))$ for condition $\varphi$.
		$\le \sum_{a^n,b^n \in T_\delta, b^n \ne a^n} [P(E_{a^n})P_S( E_{a^n}E_{b^n} \notin \mathcal{N}(S)-S )] + \epsilon$
			This is just [[union bound]].
		$\le \sum_{a^n,b^n \in T_\delta, b^n \ne a^n} [P(E_{a^n})P_S( E_{a^n}E_{b^n} \notin \mathcal{N}(S))] + \epsilon$
			The size of the set that $E_{a^n} E_{b^n}$ could be in either stays the same or increases when removing the $-S$.
		$= \sum_{a^n,b^n \in T_\delta, b^n \ne a^n} [P(E_{a^n})P_S( E_{b^n} \notin E_{a^n}\mathcal{N}(S))] + \epsilon$
			Apply $E_{a^n}$ on both sides, noting that $E_{a^n}\mathcal{N}(S)=\{E_{a^n} * s : s \in \mathcal{N}(S)\}$.
		$\le \sum_{a^n,b^n \in T_\delta, b^n \ne a_n} [P(E_{a^n})*2^{-(n-k)} ]+\epsilon$
			The [[F-ST-Pauli_Group#Pauli Group Size|size of]] $\mathcal{P}^n$ is $2^{2n}$. 
			The [[Normalizer_and_Centralizer#Normalizer Size Theorem|size of]] $\mathcal{N}(S)$ is $2^{n+k}$.
			Note that the size of $E_{a^n}\mathcal{N}(S)$ is also $2^{n+k}$, because group actions are invertible, and so there must be some bijection between $E_{a^n}\mathcal{N}(S)$ and $\mathcal{N}(S)$, namely $E_{a_n}$.
			Thus we can simply calculate the probability that a given $b^n\in T_\delta-\{a^n\}$ is in $E_{a^n}\mathcal{N}(S)$ as $\frac{|E_{a^n}\mathcal{N}(S)-\{a^n\}|}{|T_\delta-\{a^n\}|}\le \frac{|E_{a^n}\mathcal{N}(S)-\{a^n\}|}{|\mathcal{P}^n-\{a^n\}|}=\frac{|E_{a^n}\mathcal{N}(S)|-1}{|\mathcal{P}^n|-1}=\frac{2^{n+k}-1}{2^{2n}-1}\le \frac{2^{n+k}}{2^{2n}}$ .
		$\le \sum_{a^n,b^n \in T_\delta, b^n \ne a_n} [2^{-n[H(\vec p)+\delta]}*2^{-(n-k)} ]+\epsilon$
			Because $\forall_{a^n} \in T_\delta$, $Pr(E_{a^n})\le 2^{n[H(\vec p)+\delta]}$ due to the [[Typical_Set#Probability of Picking a Specific Element of the Typical Set Lemma|Probability of Picking a Specific Element of the Typical Set Lemma]]
		$= |T_\delta|^2 2^{-n[H(\vec p)+\delta]} * 2^{n-k}+\epsilon$
			Double sum over $T_\delta$
		$\le 2^{2n[H(\vec p)+\delta]} 2^{-n[H(\vec p)+\delta]}2^{n-k} + \epsilon$ 
			$|T_\delta| \le 2^{n[H(\vec p)+\delta]}$ due to the [[Typical_Set#Size of Typical Set Lemma|Size of Typical Set Lemma]]
		$=2^{n[H(\vec p)+\delta + 1 - k/n]}$ 
- #wip 

check deltas here on the last 4 steps. might need to fix a +/- somewhere, then find the relation between k/n and H(p)

