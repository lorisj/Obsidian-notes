# Notation

### Metadata
Path: #pathCOMP
Tags: #notation

### Prerequisites
[[Turing_Machines#Introduction|Turing Machines]]

### Introduction


### Basic Math Notation
$\omega = \mathbb N = \{0,1,\ldots\}$
$2 = \{0,1\}$
$2^{<\omega} = \{\text{finite binary sequences}\}=\{0,1\}^*$
$A^B = \{\text{functions }f:B\to A\}$
$2^\omega = \{\text{infinite binary sequences}\} \leftrightarrow \mathcal P(\omega)$ (power set)

### Characteristic Function Definition
**Def(Characteristic Function):** If $(A\subseteq \omega)$, the characteristic function on $A$ is $\chi_A(n)$ (\chi) which is defined as $\chi_A(n)= \begin{cases} 0 :& n \notin A\\ 1:&n\in A\end{cases}$ 
Often we write $A(n)$ for $\chi_A(n)$, such that $A(n) = 1\iff n\in A$.

### Computability
**Def($\varphi_e(x)\downarrow$ and $\varphi_e(x)\uparrow$):** These are defined as follows:
- If $\varphi_e(x)$ halts with output $y$, then we write $\varphi_e(x)\downarrow = y$
- If $\varphi_e(x)$ doesn't halt, then it diverges and we say $\varphi_e(x)\uparrow$
