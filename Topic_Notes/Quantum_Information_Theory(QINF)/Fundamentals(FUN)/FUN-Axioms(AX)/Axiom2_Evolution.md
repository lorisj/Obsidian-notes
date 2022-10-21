# Axiom 2: Evolution
### Metadata
Path: #pathQINF #QINF/Fun/AX
Tags:

### Prerequisites 
- #wip
### Introduction
- #wip
### Axiom 2 (Evolution):
A quantum system $\rho$ evolves through a unitary transformation $\rho \to U\rho U^\dagger$, where $U$ is a [[#Unitary Operator Definition|unitary]] operator.


### Unitary Operator Definition
**Def(Unitary):** An operator $U$ is unitary if and only if one of the following equivalent conditions are met:
1) $U^\dagger U = I_\mathcal H$.
2) $UU^\dagger = I_\mathcal H$
3) $\forall_{|\psi\rangle \in \mathcal H} \langle \psi|U^\dagger U |\psi\rangle = \langle \psi |\psi\rangle$ ($U$ preserves inner products for all vectors)


### Length Corollary
**Cor(Length):** If $U$ is unitary, the length of the vector $U|\psi\rangle$ is the length of the vector $|\psi\rangle$
	Proof:
		$\text{Len}(U|\psi\rangle)= \sqrt{(U|\psi\rangle)^\dagger (U|\psi\rangle)}=\sqrt{\langle \psi|U^\dagger U |\psi\rangle}$  
			By the [[definition of length]] and the fact that $(AB)^\dagger = B^\dagger A^\dagger$ for operators $A,B$
		$=\sqrt{\langle\psi |\psi\rangle}$
			By the 3rd version of the [[#Unitary Operator Definition|definition of unitary operators]] 
		$=\text{Len}(|\psi\rangle)$
			By the [[definition of length]]

