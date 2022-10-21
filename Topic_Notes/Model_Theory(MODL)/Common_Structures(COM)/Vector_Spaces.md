# Vector Spaces
### Metadata
Path: #pathMODL, #pathMODL/COM
Tags: 

### Prerequisites

### Introduction
Let $F$ be some field
$\mathcal{L}=\{0,+,-,\cdot_r : r\in F\}$
This note states the [[#Axioms]],(the definition of a vector space) as well as a few results and interpretations:
[[#Substructure of a Vector Space is a Vector Space Lemma|Any substructure of a vector space is also a vector space]]
[[#Incompleteness of Finite Field Vector Spaces Thm|Finite field vector spaces are incomplete]]
[[#Terms Interpretation|The interpretation of terms]]
[[#Formulas Interpretation|The interpretation of formulas]]
[[#Algebraic Closure for Vector Spaces|The meaning of algebraic closure for vector spaces]]

### Axioms
Let $T_v$ be the theory of vector spaces, axiomatized by: 
[[Abelian_Group#Axioms|Abelian group axioms]] on $+$:
- Associativity: $\forall_x \forall_y \forall_z x+(y+z)=(x+y)+z$
- Commutativity: $\forall_x\forall_y x+y=y+x$
- Identity: $\forall_x x +0=x$
- Inverse: $\forall_x x +(-x)=0$
Scalar Multiplication axioms:
- $\{\forall_x \cdot_r(\cdot_v(x))=\cdot_{rv}(x): \text{ for all } r,v \in F\}$
- $\{\forall_x \cdot_r(x)+\cdot_v(x)=\cdot_{r+v}(x): \text{ for all }r,v \in F\}$
- $\{\forall_x\forall_y \cdot_r(x+y)=\cdot_r(x)+\cdot_r(y): \text{ for all } r \in F \}$
- $\{\forall_x s_1(x)=x\}$
Non-Trivial Axiom:
- $\exists_x x\ne 0$

### Substructure of a Vector Space is a Vector Space Lemma
**Lem(Substructure of Vector Space is a Vector space):** Given structure $\mathcal{M}$ that satisfies the axioms, it must also be the case that $\mathcal S < \mathcal B$ also satisfies the axioms.
	Proof:
	Easy to see, just note that all formulas are universal, so applying the [[Substructure_Results#Substructures with Quantified Formulas Theorem|substructures with quantified formulas theorem part 2]], we can see that for axiom $\phi$, because each axiom is a universal sentence,  $\mathcal{B} \models \phi$ implies that $\mathcal{S} \models \phi$. If we count the nontrivial axiom, we can change the lemma to say any nontrivial substructure is a vector space, as that axiom would also be true in both cases.


### Terms Interpretation
Consider the language of $\mathbb{F}$ vector spaces in $\mathcal{L}_\text{vspace}=\{0,+,-,\cdot_r : r\in \mathbb F\}$ with structure $\mathcal M$. 
Recall the [[Terms_Formulas_and_Sentences#Terms Definition|definition of terms]].
Note that the set of $\mathcal L_{\text{vspace}}$ terms is the set of weighted sums/subtractions of variable symbols $x_1, \ldots x_n$, and $0$. We can interpret terms as linear combinations of vectors, as we can easily change any $-(t(\bar a))$ for any term $t$ as $\cdot_{-1}(t(\bar a))$ remove any $+(\cdot_r(0))$, and then all we are left with is just terms containing variables, $+$, and scalar multiplications of variables. Thus terms are simply linear combinations of their variables.

### Formulas Interpretation
Consider the language of $\mathbb{F}$ vector spaces in $\mathcal{L}_\text{vspace}=\{0,+,-,\cdot_r : r\in \mathbb F\}$ with structure $\mathcal M$. 
Recall the [[Terms_Formulas_and_Sentences#Formulas Definition|definition of formulas]], and the fact that  [[#Terms Interpretation|terms are linear combinations]]. We now consider what the set of terms can be:

- Point 1) This means that a formula can say if two linear combinations evaluate to the same vector.
- Point 2) No relation symbols, so we do not need to consider point 2.
- Points 3,4) any logical combination of formulas saying that if two linear combinations evaluate to the same vector.
- Point 5) Quantified statements of above.

So we see that formulas can only tell us boolean combinations and quantified extensions of formulas that just say if two linear combinations of variable terms evaluate to be equal.

### Algebraic Closure for Vector Spaces
Consider the language of $\mathbb{F}$ vector spaces in $\mathcal{L}_\text{vspace}=\{0,+,-,\cdot_r : r\in \mathbb F\}$ with structure $\mathcal M$.
Recall the [[Algebraic_Closure_and_Independence#Algebraic Closure Definition|definition of algebraic closure]].

Consider some set $A\subseteq M$. We know that [[#Formulas Interpretation|from the interpretation above]], formulas can only say some quantified/logical extension of if two linear combinations of variables are equal. We claim the following lemma:
**Lem(Algebraic Closure for Vector Spaces):** $\text{acl}(A)=\text{span}(A)$ for *infinite* $\mathcal{L}_{\text{vspace}}$ structure $\mathcal M$ that satisfies the axioms, and for any $A\subseteq M$.
	Proof:
		($\text{acl}(A)\subseteq \text{span}(A)$):
			Suppose $x\in \text{acl}(A)$. This means that there must be some $\mathcal L_{\text{vspace}}$ formula $\varphi(k,\bar a)$ that defines a finite set $K$ (i.e $K=\{k \in M : \varphi(k,\bar a)\text{ with } \bar a \in A^m\}$ by the [[Definable_Sets#Definable Set Definition|definition of definable sets]] and $K$ is finite) with $x \in K$. To show that any finite definable set $\subseteq \text{span}(A)$, we use induction on [[Terms_Formulas_and_Sentences#Formulas Definition|formulas]]:
				points 1,2) $\varphi(\bar x, \bar a)$ is atomic $\implies$ $\varphi$ is $x=\sum_{j}\cdot_{d_j}(a_j)$ 
					We see that clearly $x\in \text{span}(A)$, and $\varphi$ defines $\{x\}$ which is finite.
				points 3) $\varphi$ can be $x\ne \sum_{j}\cdot_{d_j}(a_j)$
					If $x$ is not a particular linear combination of $a_j$, then it could be anything but $y=\sum_{j}\cdot_{d_j}(a_j)$. So the set it defines must include infinitely many vectors, because $M-\{y\}$ is still infinite.
				point 4) $\varphi$ can be some logical combination of above points
					Up until now, a formula either defines a finite set in $\text{span}(A)$, or an infinite set $\notin \text{span}(A)$. Using $\land$ and $\lor$ on two formulas, we would only have a problem if the new formula defines a finite set with something $\notin \text{span}(A)$. #wipImp 
		($\text{span}(A)\subseteq \text{acl}(A)$):
			Suppose $x \in \text{span}(A)$. Let $c_1, \ldots c_m$ correspond to scalars and $a_1, \ldots a_m$ correspond to vectors $\in A$ that make $x=\sum_{i}c_i * a_i$, [[span implies linear combination|which must exist, since]] $x \in \text{span(A)}$. To show $x \in \text{acl}(A)$, we must find some formula $\varphi(z, \bar y)$, and some parameters $\bar a$ with $a_i \in A$ such that $\mathcal M \models \varphi(z, \bar a)$ if and only if $z = x$. Let $\varphi(z,\bar y)$ be the formula "$z=\sum_{i}\cdot_{c_i}(y_i)$". Note $\varphi(z,\bar a)$ with $\bar a =(a_1, \ldots a_m)$ as defined above will only be satisfied with $z=x$, completing our proof.


### Incompleteness of Finite Field Vector Spaces Thm
**Thm(Finite Field Vector Spaces are not Complete):** Suppose $F$ is a finite field. Then, the axioms do not form a complete theory. Namely there is some sentence $\phi$, models $\mathcal M, \mathcal N$ such that $\mathcal{M},\mathcal{N}\models T_v$ however $\mathcal{M} \models \phi$, and $\mathcal{N}\models \neg \phi$.
	Proof:
	Consider the fields $\mathbb F_p$ and $\mathbb F_q$ for $q > p$ (not equal). Consider $\mathcal M =\{ \mathbb F_p,0,+,-,\cdot_r:r\in \mathbb F_p\}$, $\mathcal N=\{\mathbb F_q, 0,+,-,\cdot_r : r\in \mathbb F_q\}$ . Note that these both satisfy the [[#Axioms|vector space axioms]], however the sentence $\phi$ which is "$\forall_x \sum_{i=1}^p x= 0$" is true in $\mathcal M$, but not in $\mathcal N$. 

