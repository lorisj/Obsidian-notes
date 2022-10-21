# Check Matrix for Stabilizer Codes
### Metadata
Path: #pathQINF, #pathQINF/STC, #pathQINF/STC/BP 
Tags:

### Prerequisites
[[Stabilizer_Definition_and_Properties#Introduction|Stabilizer Definition]] 

### Introduction
In this note, we give the [[#Check Matrix Definition|definition]] of the check matrix, and some [[#Examples|examples]]. We show the [[#Isometry with mathcal G n|isometry]] that $\mathcal G^n$ has with the check matrix. By adding [[#Scalar Multiplication|scalar multiplication]], we then get a result that the [[#Pauli Group is a mod 2 Vector Space Lemma|Pauli group is a mod 2 vector space]]. From here we can get the result that [[#Linear Independence is Group Independence Corollary|linear independence is group independence]].

### Check Matrix Definition
**Def(Check Matrix):** The check matrix for stabilizer $S=<s_1, s_2, ... s_{|S|}>$ is $H(S)$, a matrix
	$H(S)=\left[\begin{matrix}r(s_1)\\ r(s_2)\\ \ldots \\ r(s_{|S|}) \end{matrix}\right]$ where the row vectors are defined by a function:  $r(g\in \mathcal{G^n})=\left[x_1, x_2, ... x_n  |z_1, z_2, ... z_n  \right]$, where $x_i$ is 0/1 corresponding to if there is an $X$ or $Y$ in the $i$th space, and $y_i$ is 0/1 corresponding to if there is a $Z$ or $Y$ in the $i$th space.

### Examples
**Exp(n=2):** Let $S=<s_1, s_2>=<I\otimes X, Z \otimes Y>$: 
	$r(s_1)=[\begin{matrix}0&1&0&0\end{matrix}]$
	$r(s_2)=[\begin{matrix}0&1&1&1\end{matrix}]$
	$H(S)=\left[\begin{matrix}0&1&|&0&0\\0&1&|&1&1	\end{matrix}\right]$

### Isometry with $\mathcal{G}^n$: 
Recall that $\mathcal{G}^n=\{G^n,*,I\}$ is the $n$-fold [[F-ST-Pauli_Group#Introduction|Pauli Group]]. To show that it has a similar structure to $\mathcal{R}=(R,\bar{\oplus},\vec{0})$ (where $R=\{r(g):g\in G^n\}$, where [[#Check Matrix Definition|r is defined above]] and $\bar{\oplus}$ is vector addition mod 2) simply note that $r(g_1*g_2)=r(g_1)\bar{\oplus} r(g_2)$:
	Consider $n=1$. If we let the identity $I$ map to $\vec{0}$, we can see that the identity $\vec{0}$ behaves properly with everything else. Next consider $X$ acting on $Z$: This should map to the same thing that $Y$ does, and in fact $r(X)\oplus r(Z)=r(XZ)=r(Y)$. Any element squared is the identity in the Pauli group, and any element $\oplus$ itself in $\mathcal{R}$ is also the identity. This generalizes to any n, and so $\oplus$ "plays nice" with $r$. 
Thus $r$ is an $\mathcal{L}_{\text{group}}$ embedding, and $\mathcal{G^n} \simeq \mathcal{R}$. However note that in this case $r$ is not invertible, as addition is commutative. For instance in $\mathcal{G^1}:r(X)\oplus r(Z)=r(Z)\oplus(X)$, however $X*Z\ne Z*X$. If we consider the quotient group $\mathcal{G^n}/\mathcal{Z}$, where $\mathcal{Z}=\{\{\pm I, \pm i\},*,I\}$, then we can ignore any sign differences that occur. Then $r$ becomes invertible, and therefore an $\mathcal{L}_{\text{group}}$ isomorphism.

### Scalar Multiplication
Note scalar multiplication in the expanded vector space is just $0/1$ so $c*r(g_i)=r(I)$ or $=r(g_i)$ for $c=(0/1)$. Note $c=1$ just is the identity operation, but in the Pauli group we have no similar interpretation of multiplying by $c=0$. So you can add a sort of exponent operation where $0*r(g_i)=\text{all zero vector}=r(I)$ is equivalent to $(g_i)^0$
$1*r(g_i)=r(g_i)$ is equivalent to $(g_i)^1$.
So we write these exponents as function interpretations of scalar multiplication as $\{exp0, exp1\}$. 
### Pauli Group is a mod 2 Vector Space Lemma
**Lemma(Pauli group is a mod 2 VSpace)** The structure $(\mathcal{G^n}\cup\{exp0,exp1\})/\{\pm I, \pm i\}$ is  isomorphic to $\mathcal{R}\cup\{0*,1*\}$ as a $\mathbb{Z}_2$ vector space:
	Proof: 
	Vector addition: $\oplus$ should be equivalent to $*$
		$r(g_i)\oplus r(g_j)=$$r(g_i * g_j)$ , already shown [[#Isometry with mathcal G n|here]]. 
	Scalar multiplication: $0*, 1*$ should be equivalent to $exp0, exp1$:
		$1*r(g_i)=r(g_1)=r(exp1(g_i))$
		$0*r(g_i)=r(I)=r(exp0(g_i))$
	Identity maps to identity
	Note that $r$ is  
		#wipImp ADD stuff talking about $P^n/\{\pm I, \pm i\}$ and its size in Pauli algebra notes, use that fact here.
With this fact we can prove the [[#Linear Independence is Group Independence Corollary|following corollary]]:

### Linear Independence is Group Independence Corollary
**Cor(Linear independence is group independence):** Saying $g_1,...g_m \in  \mathcal{S_G}=(\mathcal{G^n}\cup\{exp0,exp1\})/\{\pm I, \pm i\}$ are independent group generators is equivalent to saying that $r(g_1), r(g_2), \ldots r(g_m)$ are linearly independent basis vectors in $\mathcal{S_R}=\mathcal{R}\cup\{0*,1*\}$.
	Proof: 
	Since $\mathcal{S_R}\simeq\mathcal{S_G}$ and they are finite structures, $r$ is an $\mathcal{L}_{\text{vspace}}-$ elementary embedding by the [[isomorphism is elementary embedding thm]]. 
	$(\implies)$
		Note the $\mathcal{L}_{\text{vspace}}$ formula that says that $(a_i)_{i \in I}$ are independent is $\varphi(\bar a)=$
- #wip

### Check Matrix Inner Product Lemma
**Lem(Check Matrix Inner Product):** Given two operators $v,w \in \mathcal G^n$, $v$ and $w$ commute if and only if the twisted inner product $r(v)\Lambda r^T(w)=0$, where $\Lambda = \left[\begin{matrix}0_{n\times n} & I_{n\times n} \\ I_{n \times n} & 0_{n\times n} \end{matrix}\right]$.
	Proof:
		Suppose
- #wip