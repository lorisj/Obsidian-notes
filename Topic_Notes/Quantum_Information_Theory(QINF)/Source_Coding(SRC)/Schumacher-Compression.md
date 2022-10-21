# Schumacher Compression
### Metadata
Path: #pathQINF, #pathQINF/SRC
Tags:

### Prerequisites
[[Quantum_Source#Introduction|Quantum Source]]
[[Source_Coding_Problem#Introduction|Source coding problem]]
[[Typical_Subspace#Introduction|Typical Subspace]]

### Introduction
We cover the implementation of the steps listed in the [[Source_Coding_Problem#Introduction|source coding problem]], for Alice to send quantum source to Bob using Schumacher compression. This includes [[#State Preparation|state preparation]], [[#Encoding|encoding]], [[#Transmission|transmission]], and [[#Decoding|decoding]].

### State Preparation
Suppose we have [[Quantum_Source#Quantum Source Definition|quantum source]] $\rho^X$, with corresponding [[Quantum_Source#Quantum Random Process|quantum random process]] $\rho^{X^n}$.
Without loss of generality we consider the [[Quantum_Source#Spectral Decomposition of a Quantum Source|spectral decomposition of the quantum source]] $\rho^X=\sum_{x\in \mathcal X} p_X(x)|x\rangle \langle x|$ where $\{|x\rangle : x \in \mathcal X\}$ forms an orthonormal basis for $\mathcal H$. This generalizes to the quantum random process:
$\rho^{X^n}=\sum_{x^n\in \mathcal{X}^n}p_{X^n}(x^n)|x^n\rangle\langle x^n|$ where again $\{|x^n\rangle: |x^n\rangle \in \mathcal X^n\}$ forms an orthonormal basis for $\mathcal H ^ {\otimes n}$ where $p_{X^n}(x^n)=p_{X^n}(x_1, x_2, \ldots x_n)\equiv\prod_{i=1}^n p_X(x_i)$. 


### Encoding
Alice first performs a typical subspace measurement with observable $A=\Pi_{\delta}^{X^n}$. This is equivalent to $A=0*(I-\Pi_{\delta}^{X^n}) \oplus 1*\Pi_{\delta}^{X^n}$ where $X \oplus Y$ is $Y$ acting on the typical subspace $T_{\delta}^{X^n}$, and $X$ acting on the quotient space $\mathcal H / T_{\delta}^{X^n}$. If we get classical output $0$, then we consider this an error and terminate the process. If not then we get classical output $1$, and so we proceed, with output of the measurement being the normalized [[Typical_Subspace#Sliced Density Operator Definition|sliced density operator]] $\text{Norm}_{\text{Tr}=1}(\tilde{\rho}_{\delta}^{X^n})=\frac{1}{\text{Tr}(\tilde{\rho_{\delta}^{X^n}})}\tilde{\rho}_{\delta}^{X^n}$$=\frac{1}{\text{Pr}(A_{\delta}^{X^n})}\tilde{\rho}_{\delta}^{X^n}$.

Consider the [[classical Shannon compression]] of i.i.d random process $X^n$. Suppose this has encoding map $f$ that maps elements from the typical subset to the code set.

We encode using the unitary map $U_f$ defined below:
$U_f=\sum_{x^n \in T_{\delta}^{X^n}}|f(x^n)\rangle \langle x^n|$
Note this is just the quantum analogue of the [[classical Shannon compression#endcoder|classical Shannon compression encoding map]] that takes $x^n\in A_{\delta}^{X^n}\to$ its corresponding index in the code set.

Note that the full encoding map, with measurement and $U_f$ acts as follows assuming a successful measurement result:
$\text{Enc}(\sigma)\equiv \frac{1}{\text{Pr}(A_{\delta}^{X^n})}U_f\tilde{\rho}_{\delta}^{X^n}U_{f}^{\dagger}$

### Transmission
Alice transmits all of their compressed qubits to Bob over $n(H(X)+\delta)$ uses of a noiseless [[quantum channel]].

### Decoding
Bob receives transmitted qubits and performs decompression map $U_{f^{-1}}$ defined below:
$U_{f^{-1}}=\sum_{x^n \in T_{\delta}^{X^n}}|x^n\rangle \langle f(x^n)|$
Note that for the sliced density operator $U_{f^{-1}} U_f \equiv I$, because $f$ is invertible restricted to $x^n \in A_{\delta}^{X^n}$. 
