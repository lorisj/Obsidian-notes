# Terms, Formulas, and Sentences
### Metadata
Path: #pathMODL, #pathMODL/FUN
Tags: 

### Prerequisites
[[Language_and_Structure#Introduction|Languages and Structures]]

### Introduction
In this note, we give the [[#Terms Definition|definition of terms]], as well as the [[#Interpretation of Terms|interpretation of terms]], and some [[#Examples of Terms and Interpretations|examples of terms and interpretations]], as well as some [[#Intuition for terms|intuition for terms]]. 
Then we give the [[#Formulas Definition|definition of formulas]], the [[#Atomic and Quantifier Free Formulas Definition|definition of atomic and quantifier free formulas]], some [[#Intuition for formulas|intuition for formulas]], and lastly the [[#Sentence Definition|definition of sentence]].

### Terms Definition
**Def($\mathcal{L}$ Terms):** The set of $\mathcal{L}$ terms are defined inductively:
	1) Every constant symbol $c$ is a term
	2) Every variable symbol $v_i$ is a term
	3) If $t_1,\ldots t_{n_f}$ are terms and $f$ is a function symbol, then $f(t_1, \ldots t_{n_f})$ is a term

Think of these as generalizations of elements of the domain $M$:
	a) Constant symbols are interpreted as elements of $M$
	b) Variables should take values in $M$
	c) $f$ has codomain $M$, so evaluating $f(t_1,\ldots t_{n_f})$ should give something $\in M$ 
These generalizations lead to the interpretations of terms, given below.

### Interpretation of Terms
**Def(Interpretation of Terms):** Given $\mathcal{L}$ structure $\mathcal{M}$ where $t$ is a term involving variables $v_1, \ldots v_n$, $t$ has interpretation $t^\mathcal{M}$ in $\mathcal{M}$ as a function $M^n \to M$, defined as: 
	1) If $t$ is a constant symbol $c$, then $t^{\mathcal{M}}(\bar{a})=c^{\mathcal{M}}$
	2) If $t$ is a variable $v_j$, then $t^\mathcal{M}(\bar{a})=a_j$
	3) If $t$ is $f[t_1,\ldots t_{n_f}]$, then $t^\mathcal{M}(\bar{a})= f^\mathcal{M}[t_1^\mathcal{M}(\bar{a}),\ldots t_{n_f}^\mathcal{M}(\bar{a})]$

### Examples of Terms and Interpretations
**Exp(Rings):** Let $\mathcal{L}_\text{ring}$ be the language of rings. These are what $\mathcal{L}$ terms could look like:
	- $t:M\to M$ where $t(x)=x*x$ 
	- $t:M\to M$ where $t(x)=3$
	So for rings, we can think of the terms as just being polynomials of different variable symbols. 
**Exp(Real Numbers):** Let $\mathcal{L}=\{+,-,0,1\}$ be the language of rings, and $\mathcal{R}=(\mathbb{R},+^\mathbb{R},-^\mathbb{R},0^\mathbb{R},1^{\mathbb{R}})$ be the real numbers as a ring. 
	- Let $t_1$ be "$0$". 
		$t_1^\mathcal{R}(\bar{a})$ is constant symbol 0 acting on arguments $\bar{a}$ so $t_1^\mathcal{R}(\bar{a}) =0^{\mathbb{R}}(\bar{a})= 0^{\mathbb{R}}$  
	- Let $t_2$ be "$+(0,0)$" 
		$t_2^\mathcal{R}(\bar{a})$ is $+(t_1,t_1)$ which becomes $+^{\mathbb{R}}(0^\mathbb{R},0^\mathbb{R})$ 
	- Let $t_3$ be $-(v_j,+(t_0,t_0))$
		$t_3^\mathcal{R}(\bar{a})$ is $-(v_j,t_2)$, becomes $-^\mathbb{R}(a_j,+^{\mathbb{R}}(0^\mathbb{R},0^{\mathbb{R}})$
	We can see that formally these are are still polynomials. 

### Intuition for terms
We can see that terms are just generalized polynomials. They are functions that contain multiple variables, and then evaluate what that result is in different $\mathcal L$ structures. 
Think of a term $t^{\mathcal{M}}(\bar{a})$ as the evaluation of the polynomial $t$ using the structure in $\mathcal{M}$.

### Formulas Definition
**Def($\mathcal{L}$ Formulas):** The set of $\mathcal{L}$ formulas are defined inductively:
	1) If $s$ and $t$ are terms, then $s=t$ is a formula
	2) If $R \in \mathcal{L}_\mathcal{R}$ has arity $n_R$ and $t_1,\ldots t_{n_R}$ are terms, then $R(t_1,\ldots t_{n_R})$ is a formula
	3) If $\varphi$ is a formula, then so is $\neg \varphi$
	4) If $\varphi$ and $\psi$ are formulas, then so are $\varphi \land \psi$ and $\psi \lor \varphi$
	5) If $\varphi$ is a formula, then so are $\exists_{v} \varphi$ and $\forall_v \varphi$
If a formula is built only with 1 and 2, then it is atomic
If a formula is built without 5, then it is quantifier free


### Atomic and Quantifier Free Formulas Definition
**Def(Atomic Formulas):** An atomic formula is simply a formula in the set defined by only the first 2 of the [[#Formulas Definition|conditions listed in the definition of formulas]].
Think of atomic formulas as being the formulas that don't involve any additional logic, i.e anything like and, or, quantifiers, not. 

**Def(Quantifier Free Formulas):** A quantifier free formula is simply a formula in the set defined by only the first 4 of the [[#Formulas Definition|conditions listed in the definition of formulas]]. 
Quantifier free formulas can contain anything but quantifiers.


### Intuition for formulas
We can see that formulas can consist of quantified and logical statements regarding if two generalized polynomials are equal/have some other relation. So first order logic only has the power to say a quantified logical statement about if two generalized polynomials in the language are equal or have some other specified relation.

### Sentence Definition
**Def($\mathcal{L}$ sentence):** an $\mathcal{L}$ sentence is an $\mathcal{L}$ [[#Formulas Definition|formula]] without any free variables. So each variable should be bound by (i.e appear as the parameter of) some quantifier in the variable's scope.

