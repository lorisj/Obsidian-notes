# Vector Spaces
### Prerequisites
### Introduction
Let $F$ be some field
$\mathcal{L}=\{0,+,-,\cdot_r : r\in F\}$
This note states the [[#Axioms]],(the definition of a vector space) as well as a few results:
[[#Substructure of a Vector Space is a Vector Space Lemma|Any substructure of a vector space is also a vector space]]
[[#Incompleteness of Finite Field Vector Spaces Thm|Finite field vector spaces are incomplete]]
### Axioms
Let $T_v$ be the theory of vector spaces, axiomatized by: 
[[COM-Abelean_Group#Axioms|Abelian group axioms]] on $+$:
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
**Lem(Substructure of Vector space is a Vector space):** Given structure $\mathcal{M}$ that satisfies the axioms, it must also be the case that $\mathcal S < \mathcal B$ also satisfies the axioms.
	Proof:
	Easy to see, just note that all formulas are universal, so applying the [[FUN-Substructure_Results#Substructures with Quantified Formulas Theorem|substructures with quantified formulas theorem part 2]], we can see that for axiom $\phi$, because each axiom is a universal sentence,  $\mathcal{B} \models \phi$ implies that $\mathcal{S} \models \phi$. If we count the nontrivial axiom, we can change the lemma to say any nontrivial substructure is a vector space, as that axiom would also be true in both cases.


### Terms Interpretation
Consider the language of $\mathbb{F}$ vector spaces in $\mathcal{L}_\text{vspace}=\{0,+,-,\cdot_r : r\in \mathbb F\}$ with structure $\mathcal M$. 
Recall the [[FUN-Terms_Formulas_and_Sentences#Terms Definition|definition of terms]].
Note that the set of $\mathcal L_{\text{vspace}}$ terms is the set of weighted sums/subtractions of variable symbols $x_1, \ldots x_n$, and $0$. We can interpret terms as linear combinations of vectors, as we can easily change any $-(t(\bar a))$ for any term $t$ as $\cdot_{-1}(t(\bar a))$ remove any $+(\cdot_r(0))$, and then all we are left with is just terms containing variables, $+$, and scalar multiplications of variables. Thus terms are simply linear combinations of their variables.

### Formulas Interpretation
Consider the language of $\mathbb{F}$ vector spaces in $\mathcal{L}_\text{vspace}=\{0,+,-,\cdot_r : r\in \mathbb F\}$ with structure $\mathcal M$. 
Recall the [[FUN-Terms_Formulas_and_Sentences#Formulas Definition|definition of formulas]], and the fact that  [[#Terms Interpretation|terms are linear combinations]]. We now consider what the set of terms can be:

- Point 1) This means that a formula can say if two linear combinations evaluate to the same vector.
- Point 2) No relation symbols, so we do not need to consider point 2.
- Points 3,4) any logical combination of formulas saying that if two linear combinations evaluate to the same vector.
- Point 5) Quantified statements of above.

So we see that formulas can only tell us boolean combinations and quantified extensions of formulas that just say if two linear combinations of variable terms evaluate to be equal.

### Algebraic Closure Interpretation
Consider the language of $\mathbb{F}$ vector spaces in $\mathcal{L}_\text{vspace}=\{0,+,-,\cdot_r : r\in \mathbb F\}$ with structure $\mathcal M$.
Recall the [[FUN-Algebraic_Closure_and_Independence#Algebraic Closure Definition|definition of algebraic closure]].

Consider some set $A\subseteq M$. We know that [[#Formulas Interpretation|from the interpretation above]], formulas can only say some quantified/logical extension of if two linear combinations of variables are equal. We claim the following lemma:
**Lem(Algebraic Closure for Vector Spaces):** $\text{acl}(A)=\text{span}(A)$ for $\mathcal{L}_{\text{vspace}}$ structure $\mathcal M$, and $A\subseteq M$.
	Proof:
		($\text{acl}(A)\subseteq \text{span}(A)$):
			Suppose $\bar x\in \text{acl}(A)$. This means that there must be some $\mathcal L_{\text{vspace}}$ formula $\varphi(\bar k,\bar a)$ that defines a finite set $K$ (i.e $K=\{\bar k \in M^n : \varphi(\bar k,\bar a)\text{ with } \bar a \in A^m\}$ by the [[FUN-Definable_Sets#Definable Set Definition|definition of definable sets]])with $\bar x \in K$
			
			

### Definable Closure Interpretation


### Incompleteness of Finite Field Vector Spaces Thm
**Thm(Finite Field Vector Spaces are not Complete):** Suppose $F$ is a finite field. Then, the axioms do not form a complete theory. Namely there is some sentence $\phi$, models $\mathcal M, \mathcal N$ such that $\mathcal{M},\mathcal{N}\models T_v$ however $\mathcal{M} \models \phi$, and $\mathcal{N}\models \neg \phi$.
	Proof:
	#wip 
