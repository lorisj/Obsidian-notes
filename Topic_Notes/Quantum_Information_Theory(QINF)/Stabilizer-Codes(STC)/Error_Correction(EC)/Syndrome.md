# Syndrome
### Metadata
Path: #pathQINF, #pathQINF/STC, #pathQINF/STC/EC 
Tags:

### Prerequisites:


### Introduction
Suppose we have a stabilizer $S = <g_1,...g_{n-k}>$
In this note we cover how we do error correction using stabilizer codes, namely syndrome decoding. We provide the [[#Syndrome Definition|definition]], say [[#Stabilizer measurement classical Theorem|how to obtain the syndrome]], (by measuring over generators of $S$) and [[#Stabilizer Measurement Quantum Theorem|show]] that this measurement does not change a coded state $|\psi\rangle \in V_S$. We then show [[#Logical Error Syndrome Lemma|any logical error has syndrome]] $(1,1,1...1)$, and lastly prove the [[#Same Syndrome Theorem|same syndrome theorem]]. 


### Syndrome Definition
**Def(Syndrome):** Given error $E$, the syndrome of E is a $l$ tuple, where each number corresponds to $\pm 1$, the eigenvalue of the ith generator of S. 
$$\text{Syndrome}(E)=(\lambda_i)_i, \text{ where } \lambda_i=\begin{cases}+1 & \text{if }E \text{ commutes with }g_i\\ -1& \text{ if } E \text{ anticommutes with } g_i\end{cases} $$
Equivalently:
$$\text{Syndrome}(E)=(Eg_iE g_i)_i$$
	These are equivalent, because $Eg_iEg_i=E(g_iE)g_i=E(\lambda_i*E g_i)g_i=\lambda_i*EEg_ig_i=\lambda_i*I =\lambda_i$	 


### Stabilizer measurement (classical) Theorem
**Thm(Classical output of  generator measurement yields syndrome):** Measuring the error state $E|\psi\rangle$ across generator $g_i$ yields classical output = $\lambda_i$ (ith syndrome of $E$) with probability = 1:
	Proof:
		Let $E|\psi\rangle$ be the error state ($|\psi\rangle \in V_S$). Consider a measurement by observable $g_i$. To find the classical output $c_i$ of the measurement, notice that 
		$\mathbb{E}(g_i) = \langle \psi | E^\dagger g_i E|\psi\rangle$	
			     $=\langle \psi | E^\dagger(g_iE)|\psi\rangle$
			     $=\langle \psi | E^\dagger (\lambda_i Eg_i)|\psi\rangle$
			     $=\langle \psi | E^\dagger \lambda_i E*(g_i|\psi\rangle)$
			     $=\langle \psi | E^\dagger \lambda_i E|\psi\rangle$
			     $=\lambda_i\langle \psi | E^\dagger  E|\psi\rangle$
			     $=\lambda_i\langle \psi | I|\psi\rangle=\lambda_i\langle \psi | \psi\rangle=\lambda_i$
				Because note that $g_iE=\lambda_i*Eg_i$, and $g_i|\psi\rangle = |\psi\rangle$
			     $=Pr(\lambda_i)(\lambda_i) +Pr(-\lambda_i)(-\lambda_i)\implies Pr(-\lambda_i) = 0,Pr(\lambda_i)=1$
		 So we get $\lambda_i$ as a measurement result with probability 1.


### Stabilizer Measurement (Quantum) Theorem
This theorem tells us that measuring across the stabilizer (particularly the generators of the stabilizer) will not affect any vectors in the code space:
**Thm(Quantum Measurement by Elements of S):** Measuring with observables given by any subset $M\subseteq S$, will fix $V_S$ pointwise:
	Proof:
		If we measure $|\psi\rangle \in V_S$ with $M=\{s_1,s_2,...s_{|M|}\}$, first note that $V_S \subseteq \text{+1 eigenspace}(s_i)$, and so will measure to $|\psi\rangle$ with probability 1. Repeated measurements just fix it pointwise again, so measuring all observables in $M\subset S$ in any order yields $|\psi\rangle$ unchanged. 


### Logical Error Syndrome Lemma
**Lemma(Syndrome of an Error in the Normalizer):** Note that any operator $E\in \mathcal{N}(S)$ has syndrome $(1,1,...1)$
	Proof:
		This follows directly from the definition of $\mathcal{N}(S)$, any element in the normalizer commutes with all generators of $S$, and thus has syndrome $(1,1,...1)$.


### Same Syndrome Theorem
**Thm(Same Syndrome):** Two errors $E,F$ have the same syndrome if and only if $E^\dagger F \in \mathcal{N}(S)$:
	Proof:
		$\text{Syndrome}(E)=\text{Syndrome}(F)$
		By the second version of the definition of syndrome:
		$\iff \forall_{g_i \in S} Eg_iE g_i = Fg_iF g_i$
		Apply $g_i$ on the right of both sides, and note $(g_i)^2=I$
		$\iff \forall_{g_i \in S} Eg_iE= Fg_iF$
		Apply $E$ on left and right of both sides:
		$\iff \forall_{g_i \in S} EEg_iE E = EFg_iF E$
		Note  $E^2 = I$
		$\iff \forall_{g_i \in S} g_i= EFg_iFE$
		Note $E^\dagger = E$, $F^\dagger = F$
	    $\iff \forall_{g_i \in S} g_i= E^{\dagger}Fg_iF^{\dagger}E$
	    Note for any operators $(AB)^\dagger = B^\dagger A^\dagger$
	    $\iff \forall_{g_i \in S} g_i= E^{\dagger}Fg_i(E^{\dagger}F)^\dagger$ 
	    By [[Normalizer_and_Centralizer#Normalizer Definition|definition of normalizer]]
		$\iff E^\dagger F \in \mathcal{N}(S)$

