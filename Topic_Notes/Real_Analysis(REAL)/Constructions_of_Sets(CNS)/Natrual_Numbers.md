# Natural Numbers
### Metadata
Path: #pathREAL , #pathREAL/CNS 
Tags: 

### Prerequisites

### Introduction
This note contains information on the construction of the set of natural numbers.

### Informal Definition of Natural Numbers
Informally $\mathbb N = \{0,1,\ldots\}$

### Inductive Set Construction Theorem
**Thm(Inductive Set Construction):** If you want to construct a family $(s_n)_{n \in \mathbb N}$ of sets, it is enough to simply:
1) Construct $s_0$
2) Given $s_n$ construct $s_{n+1}$
Then the resulting $(s_n)_{n\in \mathbb N}$ is unique.
	Proof:
		First part:
			We use induction on $P(n) =$"The set $s_n$ exists"  
		Second part:
			Let $s_n$ and $s'_n$ be two sets constructed this way.
			We use induction on $P(n)=$"The set $s_n$ = $s'_n$"
			Thus inductive constructions are unique.


### Inductive Function Construction Corollary
**Cor(Inductive Function Construction):** If you want to construct a family $(f_n)_{n \in \mathbb N}$ of functions, it is enough to simply:
1) Construct $f_0$
2) Given $f_n$ construct $f_{n+1}$
Then the resulting $(f_n)_{n \in \mathbb N}$ is unique.
	Proof:
		Simply use the fact that [[#Inductive Set Construction Theorem|you could construct]] the [[graph of a function]] this way, and that [[functions are defined via graphs in model theory]].


### Peano Triple Definition
**Def(Peano Triple):** Let $\mathcal L_p = \{e, s\}$ be the language where $e$ is a constant and $s$ is a function with arity 1. A Peano Triple is a $\mathcal L_p$ structure $\mathcal P= (P,e^\mathcal P, s^{\mathcal P})$ that satisfies:
1) $s$ is injective:
	$\forall_x\forall_y s(x)=s(y)\implies x=y$
2) $e$ is never a successor: 
	$\forall_{x} e^{\mathcal P} \ne s^{\mathcal P}(x)$
3) Substructures are the original structure:
	If $X \subseteq P$ is such $e\in X$ and $\forall_{x \in X} s(x) \in X$ then $X=P$
	Or if $\mathcal M \le_{\mathcal L_p} \mathcal P$ then $\mathcal M = \mathcal P$ 


### Natural Numbers are a Peano Triple Lemma
**Lem(Natural Numbers are a Peano Triple):** $(\mathbb N, 0^\mathcal N, (1+)^{\mathcal N})$ is a [[#Peano Triple Definition|Peano triple]].
	Proof:
		We just have to show it satisfies the axioms:
		- Clearly $s^\mathcal N$ is injective, as $1+n = 1+m \implies n=m$
		- $0^\mathcal N$ is not the successor of any other number in $\mathbb N$.
		- Take any substructure $\mathcal M \le_{\mathcal L_p} \mathcal N$. We will show that any $\mathcal L_p$ embedding is an isomorphism, which implies $M=\mathbb N$, and thus $\mathcal M = \mathcal N$. Suppose we have an $\mathcal L_p$ embedding $\phi : M \to \mathbb N$. We just need to show that $\phi$ is surjective. Take $q \in \mathbb N$. By properties on $\mathbb N$ we know that the $\mathcal L_p$ term $t =\circ_{i=1}^{q}(s)(e)$ (which is $s$ applied $q$ times to $e$ or just $e$ if $q = 0$) has interpretation $t^\mathcal N = q$ in $\mathcal N$. Note that it also has some interpretation $t^\mathcal M$ in $\mathcal M$, and if you apply $\phi$ to this interpretation, you get $t^\mathcal N = q \in \mathbb N$ as $\phi$ is an $\mathcal L_p$ embedding. In short, we assume every element $q\in \mathbb N$ has some term that consists of finite applications of $s$ onto $e$. There must be some corresponding term in $\mathcal M$, and this term $t^\mathcal M$ gets mapped to $t^\mathcal N = q\in \mathbb N$ as $\phi$ maps the term from it's interpretation in $\mathcal M$ to its corresponding interpretation in $\mathcal N$, which we already said was just $q$. Thus $\phi$ is surjective, and so is an isomorphism. Thus $\mathcal M = \mathcal N$. 


### Domain of Peano Triple is the Set of No Variable Terms Theorem
**Thm(Domain of Peano Triple is the Set of No Variable Terms):** Let $\mathcal P = (P,e^\mathcal P, s^\mathcal P)$ be a Peano Triple. We can show that  $P =\{t^\mathcal P : t \text{ is a }\mathcal L_p \text{ term without variables}\}$=$\{ t^\mathcal P : t^\mathcal P = \circ_{i=1}^n(s^\mathcal P)(e^\mathcal P) : n \in \mathcal N \}$. So every element in $P$ corresponds to a unique interpretation $t^\mathcal P$ of a no variable term $t$.
	Proof:
		Take the alleged substructure $\mathcal M=(M,e^\mathcal P, s^\mathcal P)$ where we define the domain $M = \{t^\mathcal P : t \text{ is a }\mathcal L_p \text{ term without variables}\}=\{ t^\mathcal P : t^\mathcal P = \circ_{i=1}^n(s^\mathcal P)(e^\mathcal P) : n \in \mathbb N \}$ (when $n  = 0$ by convention we say that this composition acts as the identity. This means $s^\mathcal P$ applied to $e^\mathcal P$ 0 times evaluates to $e^\mathcal P \in M$). Informally this means that $M=\{e^\mathcal P, s^\mathcal P(e^\mathcal P), s^\mathcal P(s^\mathcal P(e^\mathcal P)), \ldots\}$. This is a substructure of $\mathcal P$, as 1) $M$ contains constant symbol $e^\mathcal P \in M$, and 2) $M$ is closed under $s$: Given any $q\in M$, that means that for some finite $n$, it must be that $q = \circ_{i=0}^n(s^\mathcal P)(e^\mathcal P)$, and so $s^\mathcal P(q) = \circ_{i=1}^{n+1}(s^\mathcal P)(e^\mathcal P)$, which is in $q$. Thus by induction, for every element $q \in M$ there must exist a corresponding element $s(q) \in M.$ Thus $\mathcal M$ is a substructure, and therefore by the third [[#Peano Triple Definition|Peano axiom]], $M=P$. Thus any Peano triple has domain equal to the set of all interpretations of no variable terms.


### Peano Triples are Isomorphic Theorem
**Thm(Peano Triples are Isomorphic):** Any Peano triple $\mathcal P = (P,e^\mathcal P, s^\mathcal P)$ is $\mathcal L_{p}$ isomorphic to $\mathcal Q = (Q, e^{\mathcal Q}, s^\mathcal Q)$, and the isomorphism is unique.
	Proof:
		Note $P = \{t^\mathcal P : t \text{ is an }\mathcal L_p \text{ term without variables}\}$ by [[#Domain of Peano Triple is the Set of No Variable Terms Theorem|the previous theorem]]. Likewise, $Q = \{t^\mathcal N : t \text{ is an }\mathcal L_p \text{ term without variables}\}$. Define the map $\phi:P \to Q$  (inductively on n) that takes $\circ_{i=1}^n(s^\mathcal P)(e^\mathcal P) \to \circ_{i=1}^n(s^\mathcal Q)(e^\mathcal Q)$ . We can simplify this as $\phi(t^\mathcal P) = t^\mathcal Q$. Note that $\phi$ preserves $e$ as when $n=0$, $e^\mathcal P\to e^\mathcal Q$, and by induction, if we preserve the $n$th term, we also preserve the $n+1$th term, and therefore all terms, which is the domain of $P$, and also the domain of $Q$. Thus $s$ is preserved through $\phi$, and so it is an isomorphism. Because we defined $\phi$ inductively, it must be unique by the [[#Inductive Function Construction Corollary|inductive function construction corollary]].

### Review
1) Show that inductive construction of sets and functions imply uniqueness.
	[[#Inductive Set Construction Theorem|Sets]], [[#Inductive Function Construction Corollary|Functions]].
2) What is a Peano Triple?
	[[#Peano Triple Definition|Peano Triple Definition]].
3) Show the Natural Numbers are a Peano Triple.
	[[#Natural Numbers are a Peano Triple Lemma|Natural numbers are a Peano triple]].
4) Show that the domain of any Peano Triple is the set of No variable $\mathcal L_{\text{peano}}$ terms
	[[#Domain of Peano Triple is the Set of No Variable Terms Theorem|Domain is terms]].
5) Show that Peano triples force all structures to be isomorphic, and that the isomorphism is unique.
	[[#Peano Triples are Isomorphic Theorem|Peano Triples are isomorphic, and the isomorphism is unique]].