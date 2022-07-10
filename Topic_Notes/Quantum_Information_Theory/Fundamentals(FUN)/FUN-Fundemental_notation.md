# Notation used in quantum information theory
### Prerequisites

### Introduction
In this section we define the terms:
- $\mathbb{N}$ and $\mathbb{Z}_+$ in the [[#Basic Math notation assumptions|basic math notation section]]
- $\mathcal{H}$, $\mathcal{U}$ in the [[#Quantum Fundamentals|quantum fundamentals section]] 
-  $\sigma_X, X, \sigma_Y, Y \sigma_Z, Z, \text{CNOT}, \text{CCNOT}$ in the [[#Basic gates|basic gates section]] 

### Basic Math notation/assumptions
$$\mathbb{N}=\{0,1,2,...\}$$
$$\mathbb{Z_+}=\{1,2,...\}$$
### Quantum Fundamentals

**Def($\mathcal H$):** $\mathcal{H} =$ state space **(from axiom 1)**
**Def($\mathcal U$):** $\mathcal U =$ set of all unitary operators on $\mathcal{H}$ **(from axiom 2)** 

### Basic gates
#### Single Qubit
$$ \sigma_X=X=\left[\begin{matrix}
0&1\\1&0
\end{matrix}\right]$$
$$ \sigma_Z=Z=\left[\begin{matrix}
1&0\\0&-1
\end{matrix}\right]$$
$$\sigma_Y=Y = i*XZ =\left[\begin{matrix}0&-i\\i&0\end{matrix}\right]$$
#### Multi Qubit
$$CNOT=\left[\begin{matrix}I_{2\times2}&0_{2\times2}\\0_{2\times2}&X\end{matrix}\right]$$
$$TOFFOLL(CCNOT) = \left[\begin{matrix}I_{2\times2}&0_{2\times4}\\0_{4\times2}&CNOT\end{matrix}\right]$$

