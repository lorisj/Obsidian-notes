# Quantum Source

### Definition of Quantum Source

**Def(Quantum Source):** A quantum source $\rho$ is an ensemble of pure states with probabilities $\{|\psi_x\rangle, p_X(x)\}_x$. Equivalently it is a density operator $\rho=\sum_{x}p_X(x)|\psi_x\rangle \langle \phi_x|$.
	You can think about this as a random variable $X$ that takes values $\{|\psi_x\rangle\}_x$ with probability measure $p_X(x)$. However note that the states $|\psi_x\rangle$ <u>do not need to be orthogonal</u>, however $\rho$ [[#Spectral Decomposition of a Quantum Source|can be decomposed]] into another equivalent source that has this property.

### Spectral Decomposition of a Quantum Source
Suppose we have a quantum source $\rho=\sum_x p_X(x) |\psi_x\rangle\langle \psi_x|$. Now note because $\rho$ is hermitian, we can decompose it into $\rho = \sum_yp_Y(y)|\phi_y\rangle\langle\phi_y|$ using the [[spectral theorem]], and so $\langle \phi_i|\phi_j \rangle = \delta_{ij}$, so we have turned this quantum source into a classical one, and notably $|\text{range}(Y)|\le |\text{range}(X)|$. This becomes important when you consider the entropy of the classical random variables $X$ and $Y$. [[#Vonn Neumann entropy is minimal|As it turns out]], $H(Y)\le H(X)$.

### Entropy
**Def(Von Neumann Entropy):** The Von Neumann entropy of a quantum source $S(\rho)$ is equal to the entropy $H(p_Y)$ of the distribution $p_Y(y)=(\lambda_y)_y$, where $p_Y(y)$ are the eigenvalues of $\rho$ which are found from the spectral decomposition of $\rho=\sum_y{\lambda_y |\psi_y\rangle\langle\psi_y|}$. 

### Von Neumann Entropy is Minimal Theorem
**Thm(Von Neumann Entropy is Minimal):** Let $d$ be a quantum source. minimal in the sense that for any other ensemble with probabilities $p_X$, $H(p_y)\le H(p_x)$. #wip 
