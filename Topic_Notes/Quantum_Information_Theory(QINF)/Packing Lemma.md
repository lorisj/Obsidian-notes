 # Packing Lemma
### Metadata
Path: #pathQINF #wip
Tags:

### Prerequisites:

### Introduction


### Sending Information
Suppose we have an ensemble $\sigma = \{p_X(x), \sigma_x\}_{x\in \mathcal X}$. (Note that $\mathcal X$ is the index set for the ensemble.) We wish to examine how Alice can reliably transmit classical information by using this ensemble. Alice can pick some subset $\mathcal C\subseteq \mathcal X$, and generate some index set $\mathcal M \simeq \mathcal C\subseteq \mathcal X$ with isomorphism $c_m : M \to C$. We assume each message has equal probability, so the density operator that she sends to Bob is one of  $\sigma_{out} \sim \{\frac{1}{|M|}, \sigma_{c_m}\}$ with distribution $\frac{1}{|M|}$.


### Receiving Information
Suppose Alice sends $\sigma_{c_m}$. Bob wishes to determine which classical message that Alice sends. Bob can construct POVM $\{\Lambda_q\}_{q \in \mathcal M}$ from ($\{\Pi_x\}_{x\in \mathcal X}$, and the code space projector $\Pi$).  The probability of error of a message $m$ under code $\mathcal C$ is defined as: $p_e(m,\mathcal C)=1-\text{Tr}(\Lambda_m \sigma_{c_m})= \text{Tr}[(I-\Lambda_m)\sigma_{c_m}]$.

### Performance Measures Definition
**Def(Performance Measure):** A performance measure for this process can be one of 3:
1) Maximal probability of error of codeword (strongest):
	A code $\mathcal C$ has maximum probability of error $\epsilon = \text{max}_{m \in \mathcal M} [p_e(m, \mathcal C)]$.
2) Average probability of error of the code $\mathcal C$ (weaker):
	A code $\mathcal C$ has average probability of error $\epsilon = \frac{1}{|M|}\sum_{m=1}^{|M|} p_e(m,\mathcal C)$
3) Expectation of error of a random code (weakest):
	A random code has expected probability of error $\epsilon = \mathbb E_{\mathcal C} \left[\frac{1}{|M|} \sum_{m=1}^{|M|}p_e(m,\mathcal C) \right]$


### Statement of Packing Lemma
**Lem(Packing):** Suppose we have a $\sigma = \{p_X(x), \sigma_x\}$. Suppose a code space projector $\Pi$ and codeword projectors $\{\Pi_x\}_{x \in \mathcal X}$ exist, and these projectors and ensemble satisfy:
1) $\forall_{x\in\mathcal X}\text{Tr}(\Pi \sigma_x)\ge 1-\epsilon$
2) $\forall_{x\in\mathcal X} \text{Tr}(\Pi_x \sigma_x) \ge 1-\epsilon$
3) $\forall_{x\in\mathcal X} \text{Tr}(\Pi_x) \le d$
4) $\Pi\rho\Pi \le \frac{1}{D}\Pi$ (eigenvalues of left $\le$ eigenvalues of right)
where we have fixed $\epsilon \in (0,1), D > 0, d \in (0,D)$. 
We can generate a set $\mathcal C = \{Y_m\}_{m \in \mathcal M}$ of random variables $Y_m\in \mathcal X$ independently according to $p_X(x)$, such that each random variable $Y_m$ is independent of its particular message $m$. The set $\mathcal C$ constitutes a random code. 
	*This lemma states there exists a corresponding POVM $\{\Lambda_m\}_{m \in \mathcal M}$ that reliably distinguishes the states $\{\sigma_{Y_m}\}_{m \in \mathcal M}$ in the sense that the average probability of detecting the correct state is high:
	$\mathbb E_{\mathcal C} \left[\frac{1}{|M|} \sum_{m=1}^{|M|}\text{Tr}(\Lambda_m \sigma_{Y_m}) \right] \ge 1-2(\epsilon+2\sqrt{\epsilon})-4|M|\frac{d}{D}$
	when $D/d$ is sufficiently large, and $\epsilon$ is sufficiently small, and $|M|<<D/d$.*
 
Explanation:
1) Lemma states that the code space with projector $\Pi$ contains all messages $\sigma_x$ with high probability.
2) Lemma states that the code word with projector $\Pi_x$ contains message $\sigma_x$ with high probability.
3) Lemma states that the dimension of each code word space is less than some $d$
4) Lemma states that $\sigma$ restricted onto $\mathcal X$  is approximately maximally mixed.

Note that conditions $1,4 \implies Tr(\Pi)\ge D(1-\epsilon)$

The idea of the lemma is that we can pack $|M|$ classical messages into $\text{im}(\Pi)$. You are trying to pack as many subspaces of size $d$ into the larger space of size $D$.

#### Proof of Packing Lemma:
##### Random Code
Given a message set $\mathcal M$, and ensemble $\sigma = \{p_X(x), \sigma_x\}_{x\in \mathcal X}$ bundled with random variable $X \sim p_X$.
We construct a code $\mathcal C\subseteq \mathcal X$ at random by independently generating $|\mathcal M|$ codewords according to $p_X(\cdot)$, and index them by $m \in \mathcal M$. Let $C_m$ be a random variable which takes value $c_m \in \mathcal X$ with probability $p_X(c_m)$, and so note the realizations of these random variables forms the code: i.e $\{c_m\}_{m \in \mathcal M} = \mathcal C.$  Note it turns out the probability of generating a fixed code $\mathcal C$ is: $P(\mathcal C) = \prod_{i=1}^{|\mathcal M|}p_X(c_m)$. 
One reason we do this is because if we have two functions $f,g$, and two different random codewords $C_m,C_{m'}$, then 
	$E_{\mathcal C}\left [ f(C_m) g(C_{m'})\right] =\sum_{C\in \{\mathcal C\}}p(C)f(c_m)g(c_{m'})$
	$=\sum_{c_1 \in \mathcal X}\sum_{c_2 \in \mathcal X}\ldots \sum_{c_{|\mathcal M|} \in \mathcal X} \left[\left(\prod_{i=1}^{|\mathcal M|}p_X(c_i)\right) f(c_m) g(c_{m'})\right]$
	$=\sum_{c_m \in \mathcal X}p_X(c_m)f(c_m)\sum_{c_{m'} \in \mathcal X} p_X(c_{m'})g(c_{m'})$
	$=E_{X}\left[f(X)\right]E\left[g(X)\right]$

##### Code Construction
**Def(Packing Code):** 
Given a message set $\mathcal M$, and ensemble $\sigma = \{p_X(x), \sigma_x\}_{x\in \mathcal X}$ bundled with random variable $X \sim p_X$.
1) We choose a random code $\mathcal C = \{c_m : \mathcal M \to \mathcal X\}_{m \in \mathcal M}$ as described [[#Random Code|above]] where $c_m$ takes $m$ to some value in $\mathcal X$.
2) We reveal the code $\mathcal C$ to both the sender and receiver.
3) The sender chooses a message $m \in \mathcal M$ by r.v. $M\sim Uni(\mathcal M)$, and encodes it into codeword using $c_m$.
4) The receiver performs [[POVM#Introduction|POVM]] $\{\Lambda_m\}_{m \in \mathcal M}$  to determine the message that the sender transmits, and each POVM element $\Lambda_m$ corresponds to a message $m$. The receiver obtains a classical result from the measurement, and we model it with the random variable $M^{'}$. The conditional probability $Pr\left[M^{'}=m | M = m\right] = Tr\left(\Lambda_m \sigma_m\right)$. 
5) The receiver decodes correctly iff $M^{'}= M$.

##### POVM Construction
Note that we cannot necessarily use projectors $\{\Pi_x\}_{x \in \mathcal X}$ because these may not constitute a [[POVM#Introduction|POVM]], as it could be that $\sum_{x \in \mathcal X}\Pi_x \ne I$ . Also it is possible for $im(\Pi_x)$ to have some element not in $\Pi$, so to fix this, define:

**Def($\Upsilon_x$):** Let $\Upsilon_x = \Pi \Pi_x \Pi$, so that $im(\Upsilon) \subseteq im(\Pi)$.

Note $\Upsilon_x$ is [[positive semi definite]]. 

So construct the POVM as:
$$\Lambda_m = \left(\sum_{m'=1}^{|\mathcal M|}\Upsilon_{c_{m'}}\right)^{-1/2}\Upsilon_{m}\left(\sum_{m'=1}^{|\mathcal M|}\Upsilon_{c_{m'}}\right)^{-1/2}$$

(Note this is a similar argument as from [[E598_HW4_Q5_a]], note all $\Lambda_m$ are [[positive semi definite]])

This doesn't necessarily constitute a valid POVM, because $\sum_{m'=1}^{|\mathcal M|}\Lambda_{m} \le I$, but we could add a $\Lambda_0 = I-\sum_{m'=1}^{|\mathcal M|}\Lambda_m$ to complete the measurement. 
Claim: $\sum_{m'=1}^{|\mathcal M|}\Lambda_{m} \le I$: ($\iff I-\sum_{m'=1}^{|\mathcal M|}\Lambda_{m}$ is positive semi definite)
	Proof:
			Note each $\Lambda_m$ is [[positive semi definite]], $I-\Lambda_m$ is positive semi definite because: 
			$\left[I-\left(\sum_{m'=1}^{|\mathcal M|}\Upsilon_{c_{m'}}\right)^{-1/2}\Upsilon_{m}\left(\sum_{m'=1}^{|\mathcal M|}\Upsilon_{c_{m'}}\right)^{-1/2}\right]|\psi\rangle$ 
			$=\left[I-\left(\Pi\sum_{m'=1}^{|\mathcal M|}\Pi_{c_{m'}}\Pi\right)^{-1/2}\Upsilon_{m}\left(\Pi\sum_{m'=1}^{|\mathcal M|}\Pi_{c_{m'}}\Pi\right)^{-1/2}\right]|\psi\rangle$ 
			diagonalize $Gamma_{c_M'}$
			