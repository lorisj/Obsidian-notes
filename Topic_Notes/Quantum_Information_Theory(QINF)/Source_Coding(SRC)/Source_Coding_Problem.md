# Source Coding Problem
### Metadata
Path: #pathQINF, #pathQINF/SRC
Tags:

### Prerequisites
[[Quantum_Source#Introduction|Quantum source]]

### Introduction
In this note, we give a summary of the channel coding problem in the quantum setting, namely the issues of [[#State Preparation]], [[#Encoding]], [[#Transmission]], [[#Decoding]]. We also cover the [[#Source Coding Error Definition|definition of error]] for source coding.

### State Preparation
Alice has system $\mathcal A$, and a [[Quantum_Source#Quantum Source Definition|quantum source]] $\rho=\sum_{x}p_X(x)|\psi_x\rangle \langle \psi_x|$ in $A$, where $\{|\psi_x\rangle\}_x$ is a set of arbitrary quantum states, and $p_X$ is a probability mass function. We can then diagonalize $\rho$ as $\rho=\sum_y p_Y(y)|\phi_y\rangle\langle \phi_y|$, where $\{|\phi_y\rangle\}_y$ forms an orthonormal basis for some subspace of $\mathcal H$. We consider the problem of compressing the corresponding [[Quantum_Source#Quantum Random Process|quantum random process]] $\rho^{\otimes n}\in \mathcal A^{n}$ and recovering with asymptotically low probability of error.
We also consider the [[Purification|purification]] of state $\rho$ with some reference system $\mathcal R$ as $|\varphi_{\mathcal R,\rho}\rangle=\sum_{x}\sqrt{p_X(x)}|x\rangle |\psi_x\rangle$. This is useful to ensure the compression respects entanglement.

### Encoding
Alice encodes the [[Quantum_Source#Introduction|quantum source]] according to some [[Quantum Channel|CPTP]] map $\text{Enc}:\mathcal A^n\to \mathcal W$ that goes to a smaller subspace of $\mathcal H^{\otimes n}$. $\text{Enc}(\rho^{\otimes n})$ takes $\rho^{\otimes n}$ to a subspace of dimension $2^{n*R}$, where $R$ is the rate of compression, formally defined as $R=\frac{1}{n}\log(\text{dim}(\mathcal W))-\delta$, where $\delta$ is an arbitrary small number and a function of $n$.

### Transmission
Alice transmits system $\mathcal W$ to Bob using $n(R+\delta)$ noiseless qubit channels.

### Decoding
Bob applies decompression map $\text{Dec}:\mathcal W\to \hat{ \mathcal A}^{n}$. We define the error [[#Source Coding Error Definition|as follows]]:

### Source Coding Error Definition
A protocol has error $\epsilon$ if it has its output close in [[Trace Distance|trace distance]] to its input. Formally:
if $||\varphi_{\mathcal{R},\rho}\rangle \langle \varphi_{\mathcal R, \rho}| - (\text{Dec} \circ \text{Enc}) (|\varphi_{\mathcal{R},\rho}\rangle \langle \varphi_{\mathcal R, \rho}|)|_{\text{trace}}\le \epsilon$. Note $\text{Dec}$ and $\text{Enc}$ are acting on $\mathcal{R} \otimes \mathcal{A^n}$ and $\mathcal{R} \otimes \mathcal W$, so define their extensions on the composite systems as acting the same way on $\mathcal A^n$ and $\mathcal W$, but acting as the identity on system $\mathcal R$. 
