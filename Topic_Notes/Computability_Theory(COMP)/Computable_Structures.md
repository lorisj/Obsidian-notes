# Computable Structures
### Metadata
Path: #pathCOMP
Tags:

### Prerequisites
[[Turing_Machines#Introduction|Turing Machines]]

### Introduction

### Computable Function Definition
**Def(Computable Function):** Let $f: \mathbb N \to \mathbb N$ be a partial function. A Turing machine $\mathcal M$ computes $f$ if and only if for all $x \in \mathbb N$:
1) If $f(x) = y$, then $\mathcal M$ halts on input $x$ with output $y$.
2) If $f(x)$ is not defined, then $\mathcal M$ should not halt on input $x$. In this case, we say $f$ is a partial computable function.

If $f$ is total and partial computable, then it is computable.


### Computable Function Examples
**Exp($f(x) = 2x + 2$ is computable):** Let $f(x) = 2x+2$. Consider the following $\delta:$
$\left[\begin{matrix}(q_1, 1) \to (q_1, 1, R)&(q_1, b)\to (q_2, 1, R)\\&(q_2,b)\to (q_0,1,R)\end{matrix}\right]$

Start: 
$(q_1,1)\to (q_1,1,R)$
$[\ldots b|b|(1)|1|1|\ldots |1| b \ldots] \to [\ldots b|b|1|(1)|1|\ldots |1| b \ldots]$
This keeps going until we reach the first b after the ones:
$(q_1,b)\to (q_2,1,R)$
$[\ldots b|b|1|1|1|\ldots |1| (b)|b|b|b \ldots] \to [\ldots b|b|1|1|1|\ldots |1| 1|(b)|b|b \ldots]$
$(q_2,b) \to (q_0,1,R)$
$[\ldots b|b|1|1|1|\ldots |1| 1|(b)|b|b \ldots] \to [\ldots b|b|1|1|1|\ldots |1| 1|1|(b)|b \ldots]$
Then since we are in state $q_0$, the computation halts, and because we have written two ones, we have successfully computed $f$.

### Computable Set Definition
**Def(Computable Set):** A set $A \subseteq \omega$ is computable iff $A(.)$ is computable.


