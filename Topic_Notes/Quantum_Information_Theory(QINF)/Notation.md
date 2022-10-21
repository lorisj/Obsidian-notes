# Notation Used in Quantum Information Theory
### Metadata
Path: #pathQINF
Tags: #notation 

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

*Delete all that follows*

The total unitary matrix for the circuit $=U = X = \left[\begin{matrix}0&1\\1&0\end{matrix}\right]$ 

Lets review how $X$ acts on the basis $|0\rangle, |1\rangle$:
 
- $X|0\rangle = \left[\begin{matrix}0&1\\1&0\end{matrix}\right]* \left[\begin{matrix}1 \\ 0\end{matrix} \right]=\left[\begin{matrix}0 \\ 1\end{matrix} \right]$

- $X|1\rangle = \left[\begin{matrix}0&1\\1&0\end{matrix}\right]* \left[\begin{matrix}0 \\ 1\end{matrix} \right]=\left[\begin{matrix}1 \\ 0\end{matrix} \right]$


For general 1 qubit input, there is some $a,b\in \mathbb C$ such that $|\text{input} \rangle = a|0\rangle + b|1\rangle$

$\implies X|\text{input}\rangle = X(a|0\rangle + b|1\rangle)$
$=a(X|0\rangle)+b(X|1\rangle)$ *(linearity of $X$)*
$= a(|1\rangle)+b(|0\rangle)$ *(we showed how $X$ acts on basis $(|0\rangle, |1\rangle)$)*



Total unitary matrix for the circuit $=U = HX = \left[\begin{matrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}\end{matrix}\right]\left[\begin{matrix}0&1\\1&0\end{matrix}\right]=\left[\begin{matrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\-\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\end{matrix}\right]$ 

$\implies U|\text{input}\rangle = a(U|0\rangle) + b(U|1\rangle)$
$=a\left(\left[\begin{matrix}\frac{1}{\sqrt 2} \\ -\frac{1} {\sqrt 2}\end{matrix}\right]\right) + b\left(\left[\begin{matrix}\frac{1}{\sqrt 2} \\ \frac{1} {\sqrt 2}\end{matrix}\right]\right)$




Total unitary matrix for the circuit $=U = I \otimes X = \left [ \begin{matrix}1&0\\0&1 \end{matrix}\right ]\otimes \left [ \begin{matrix}0&1\\1&0 \end{matrix}\right ] = \left [ \begin{matrix}X&0\\0&X \end{matrix}\right ]$ 
$=\left[\begin{matrix}0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0\end{matrix}\right]$

For general 2 qubit input, there are some $a,b,c,d\in \mathbb C$ such that $|\text{input} \rangle = a|00\rangle + b|01\rangle+c|10\rangle + d|11\rangle$ *(because these vectors are a basis for $\mathcal C^4$)*
$\implies U|\text{input}\rangle = a(U|00\rangle)  + b(U|01\rangle)+c(U|10\rangle)+d(U|11\rangle)$ *(by linearity of $U$)*



$I\otimes X(a|00\rangle + b|01\rangle+c|10\rangle + d|11\rangle)=a|01\rangle + b|00\rangle + c|11\rangle + d|10\rangle$


