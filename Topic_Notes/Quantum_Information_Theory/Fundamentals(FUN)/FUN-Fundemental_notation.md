# Notation used in quantum information theory
[[Quantum_Information_Theory/Fundamentals(FUN)/Fundamentals]]
## Basic Math notation/assumptions
$$\mathbb{N}=\{0,1,2,...\}$$
$$\mathbb{Z_+}=\{1,2,...\}$$
## Fundamentals:

**Def:** $\mathcal{H} =$ state space **(from axiom 1)**
**Def:** $U =$ Arbitrary unitary evolution **(from axiom 2)** 

### Basic gates:
#### Single Qubit:
$$ \sigma_X=X=\left[\begin{matrix}
0&1\\1&0
\end{matrix}\right]$$
$$ \sigma_Z=Z=\left[\begin{matrix}
1&0\\0&-1
\end{matrix}\right]$$
$$\sigma_Y=Y = i*XZ =\left[\begin{matrix}0&-i\\i&0\end{matrix}\right]$$
#### Multi Qubit:
$$CNOT=\left[\begin{matrix}I_{2\times2}&0_{2\times2}\\0_{2\times2}&X\end{matrix}\right]$$
$$TOFFOLL(CCNOT) = \left[\begin{matrix}I_{2\times2}&0_{2\times4}\\0_{4\times2}&CNOT\end{matrix}\right]$$

