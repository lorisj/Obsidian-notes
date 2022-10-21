# Ring Definition and Properties
#### Prerequisites
[[RGT-Notation|Notation]]
### Introduction
In this note we give the [[#Ring Axioms]], as well as some [[#Examples]] and [[#Properties]]. 
### Ring Axioms
**Def(Ring):** A Ring $\mathcal{R}=(R,0_R,1_R,+_R,*_R)$ is an $\mathcal{L}_\text{ring}$ structure that satisfies:
1) $(R,+_R,0_R)$ under $\mathcal{L}_{\text{group}}$  is an abelian group
2) $*$ is associative: $\mathcal{R}\models \forall_{r,s,t} [r*(s*t)=(r*s)*t]$
3) $*$ is L/R distributive: $\mathcal{R}\models \forall_{r,s,t} [r*(s+t)=r*s+r*t \land (s+t)*r=s*r+t*r]$
4) $1$ is identity: $\forall_r1*r=r$

### Examples
$\mathcal{M}=(\text{Mat}_{n\times n},0_{n\times n}, I_{n \times n}, *_\text{Mat})$ is a ring:
$\mathcal{R}=(\mathbb{R},0_{\mathbb{R}},1_{\mathbb{R}}, +_{\mathbb{R}},*_{\mathbb{R}})$
[[RGT-PR-Endomorphism_Ring_Definition_and_Properties#Introduction|Endomorphism Ring of an abelian group]]
[[RGT-PR-Group_Ring_Definition_and_Properties#Introduction|Group ring]]


### Properties
#### Additive Identity Annihilation Lemma 
**Lem(Additive Identity Annihilation):** For ring $\mathcal{R}$: $\forall_x x0_R=0_Rx=0_R$.
	Proof:
		For all $x\in R$:
		   $x=(1_R)x=(0_R+1_R)x=0_Rx+1_Rx=0_Rx+x$
		$-x$                                                                    $-x$
		$\implies 0_R=0_Rx$
		   $x=x(1_R)=x(0_R+1_R)=x0_R+x1_R=x0_R+x$
		$-x$                                                                    $-x$
		$\implies 0_R=x0_R$
