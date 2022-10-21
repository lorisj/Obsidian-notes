# Group Ring
#### Prerequisites:
[[RGT-Notation|Notation]]
[[RGT-PR-Ring_Axioms_and_Properties#Introduction|Ring definition]]
### Introduction
This section talks about the [[#Group Ring Definition|definition of a group ring]], shows how [[#Satisfiability of ring axioms|this definition does form a ring]], 
### Group Ring Definition
**Def(Group Ring):** Let $\mathcal{K}=(K,0_K,1_K,+_K,*_K)$ be a ring, $\mathcal{G}=(G,1_G,\circ_G)$ be a group. The group ring $\mathcal{KG}$ (or $\mathcal{K}[\mathcal{G}]$) is defined as $=(R,0_R,1_R,+_R,*_R)$ where: (sum here is unordered, grouped by group elements $g\in G$, i.e collects elements of the same 2nd item in the tuple)
$$R=\{\sum_{g\in G}{(a_g,g)}\}, \text{ where }\forall_{g\in G} a_g\in K \text{ and finite } a_g \text{ are nonzero} $$
	This is similar to the set of polynomials with the variables corresponding to the elements $g\in G$ with coefficients in $K$, as these are also unordered sums, grouped by $G=\{X,X^2,X^3,...\}$
$$+_R(\sum_{g\in G}{(a_g,g)},\sum_{g\in G}{(b_g,g)})=\sum_{g\in G}{((a_g+_Kb_g),g)}
$$
$$*_R(\sum_{g\in G}{(a_g,g)},\sum_{h\in G}{(b_h,h)})=\sum_{g\in G}\sum_{h\in G}((a_g*_Kb_h),(g\circ_G h))$$
$$0_R=\sum_{g\in G}(0_K,g)$$
	$$1_R=(1_K,1_G)$$
### Satisfiability of ring axioms
[[RGT-PR-Ring_Axioms_and_Properties#Ring Axioms|Ring Axioms]]
1) $(R,+_R)$ is an abelian group, as it is isomorphic to $K^{|G|}$, ($|G|$ tuples each of length $K$) which is a ring, and so leaves $(R,+_R)$ abelian.
2) Associativity of $*_R$ follows naturally from the fact that $\mathcal{K},*_k$ is associative, and that $\mathcal{G},\circ_G$ is associative.
3) Note $+$ leaves the second tuple unaffected, and since $*_\mathcal{K}$ is L/R distributive, so is $*_\mathcal{R}$.
4) $1_R*_R(\sum_{g\in G}(a_g,g))=\sum_{g\in G}\sum_{h\in G}((1_K*_Kb_h),(g\circ_G h))$

### Examples:
The intuition for group rings becomes clear when you consider the shorthand to be $\mathcal{K}[\mathcal{G}]$.  
The simplest example is $\mathbb{R}[X]$, the polynomials with coefficients in the real numbers, which of course [[RGT-PR-Ring_Axioms_and_Properties#Examples|are a ring]].