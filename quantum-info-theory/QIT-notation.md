# Notation used in quantum information theory
### Fundementals:

**Def:** $\mathcal{H} =$ state space **(from axiom 1)**
**Def:** $U =$ Arbitrary unitary evolution **(from axiom 2)** 

### Basic gates:
$$ X=\left[\begin{matrix}
0&1\\1&0
\end{matrix}\right]$$
$$ Z=\left[\begin{matrix}
1&0\\0&-1
\end{matrix}\right]$$
$$Y = i*XZ =\left[\begin{matrix}0&-i\\i&0\end{matrix}\right]$$
### Groups:

**Def:** $\mathcal{P} =(P,*,*^{-1})=(\{cI,cX,cY,cZ : c\in \{\pm1,\pm i\}\},*,*^{-1})$ be the 1 pauli group

You can check that this does in fact form a group. 
We can generalize this to nfold tensor products:

**Def:** $\mathcal{P^n}=\otimes_{i=1}^n{A_i} \hspace{10mm}\text{where } A_i\in P$


### Properties of $\mathcal{P^n}$:
- Every element is its own inverse
- Every element either commutes/anticomutes


