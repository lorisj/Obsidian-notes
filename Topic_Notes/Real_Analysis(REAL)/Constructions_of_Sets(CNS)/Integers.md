# Natural Numbers
### Metadata
Path: #pathREAL , #pathREAL/CNS 
Tags: 

### Prerequisites
- [[Natrual_Numbers#Introduction|Natural Numbers]]

### Introduction

### Integers Definition
**Def(Integers):** The integers $\mathcal Z = (\mathbb Z, 0, +(\cdot, \cdot), -(\cdot))$ with domain $\mathbb Z = \mathbb N \times \mathbb N$ quotient [[equivalence relation]] $(x_1,y_1)\equiv(x_2,y_2) \iff  x_1+y_2=y_1+x_2$. It turns out this makes it an [[Abelian Groups#Abelian Group Definition|abelian group.]]


### Homomorphism from Integers to Abelian Group
**Lem(Homomorphism from Integers to Abelian Group):** Let $\mathcal G=(G,e, \oplus, -^\mathcal G)$ be an abelian group, and $g \in G$. There exists a unique map $f : \mathbb Z \to G$ such that $f$ is a homomorphism and $f(1) = g$.
	Proof:
		Construct $f$ by induction
			Since $f$ must be a homomorphism:
				Let $f(0) = e$ 
				Let $f(1) = g$
				Let $\forall_{z_1, z_2}f(z_1 + z_2) = f(z_1) \oplus f(z_2)$
				Let $\forall_{z_1} f(-^\mathbb Z z_1) = -^\mathcal G f(z_1)$
				Note that  $\forall_{z \in \mathbb Z_+}: z= \sum_{i=1}^z{1}\implies f(z)=\oplus_{i=1}^z{g}$.
				Note that  $\forall_{z \in \mathbb Z_-}:-^\mathbb Z z=\sum_{i=1}^{-\mathbb Z z}1\implies f(z)=-^\mathcal Gf(-^\mathbb Z z)=-^\mathcal G \oplus_{i=1}^{-z}g$
				Thus the function is well defined, and so exists.
			We show uniqueness by showing homomorphism $h:\mathbb Z \to G$ that has $h(1)=g$ acts the same way on all $\mathbb Z$ by induction:
			Base cases:
				$h(0) = e=f(0)$.
				$h(1)= g = f(1)$
			If $n \in \mathbb Z_+:$ Assume $g(n)=f(n)$:
				$g(n+1) = g(n)\oplus g(1)=g(n)\oplus g=f(n)\oplus g=f(n)\oplus f(1)=f(n+1)$
			If $n \in \mathbb Z_-:$ Assume $g(n) = f(n)$, and note we proved the claim holds for $\mathbb Z_+$:
				$-^\mathbb Z n \in \mathbb Z_+\implies f(-^\mathbb Z n) = g(-^\mathbb Z n)\implies -^\mathcal G f(n)=-^\mathcal G g(n)\implies f(n)=g(n)$
					(just add $g(n)$ and $f(n)$ on both sides)
			Thus $f$ is unique given the conditions above.

### Free Generator Theorem
**Thm(Free Generator):** $\mathcal Z$ is the unique group with a [[free_element (group) |free]] [[group generator|generator]] up to isomorphism.
	


### Review
1) How do you build the integers?
	[[#Integers Definition|Check Definition]]
2) Let $\mathcal G=(G,e,\oplus,-^\mathcal G)$ be some abelian group, and fix some element $g \in G$. Show that there is a unique $\mathcal L = \{e,+(\cdot, \cdot),-(\cdot)\}$ homomorphism from $\mathbb Z$   if you force $f(1)=g$.
	[[#Homomorphism from Integers to Abelian Group|Homomorphism from Integers to Abelian Group]] 

3) What is a free element in a group? What is a group generator? What can you say about a group with a free generator?
	[[free_element (group)|Free]] ,[[group generator]] . If both $\implies$ group is isomorphic to $\mathbb Z$: [[#Free Generator Theorem|free generator theorem]].