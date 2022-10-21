# Endomorphism Ring Definition and Properties
#### Prerequisites
[[RGT-Notation|Notation]]
### Introduction
In this note we give the [[#Definition of Ring]], as well as some [[#Examples]] and [[#Properties]].  #wip
### Definition of Endomorphism Ring
Let $\mathcal{A}=(A,\circ_A)$ be an [[abelian group|abelian group]].
The endomorphism ring of A is $\mathcal{E}(A)=(\text{End}(A),0_E,1_E,+_E,*_E)$
	- $\text{End}(A)$ is the set of $\mathcal{L}_{\text{group}}$ homomorphisms of $A$
	- $\forall_{a\in A}(r_1 +_E r_2)(a)=r_1(a)\circ_A r_2(a)$
	- $\forall_{a\in A}(r_1 *_E r_2)(a)=r_1(r_2(a))$


### Satisfiability of Ring Axioms
[[RGT-PR-Ring_Axioms_and_Properties#Ring Axioms|Ring axioms]]
1) $(R,+_R,0_R)$ under $\mathcal{L}_{\text{group}}$  is an abelian group
2) $*$ is associative: $\mathcal{R}\models \forall_{r,s,t} [r*(s*t)=(r*s)*t]$
3) $*$ is L/R distributive: $\mathcal{R}\models \forall_{r,s,t} [r*(s+t)=r*s+r*t \land (s+t)*r=s*r+t*r]$
4) $1$ is identity: $\forall_r1*r=r$

### Examples


### Properties
